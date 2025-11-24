import os
import subprocess
from datetime import datetime

from flask import Flask, request, render_template_string, redirect, url_for


app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


EXERCISES = [
    "1_1",
    "1_2",
    "1_3",
    "1_4",
    "1_5",
    "2_1",
    "2_2",
    "2_3",
    "2_4",
    "2_5",
    "3_1",
    "3_2",
    "3_3",
    "3_4",
    "3_5",
    "4_1",
    "4_2",
    "4_3",
    "4_4",
    "4_5",
    "5_1",
    "5_2",
    "5_3",
    "5_4",
    "5_5",
    "6_1",
    "6_2",
    "6_3",
    "6_4",
    "6_5",
    "7_1",
    "7_2",
    "7_3",
    "7_4",
    "7_5",
    "8_1",
    "8_2",
    "8_3",
    "8_4",
    "8_5",
    "9_1",
    "9_2",
    "9_3",
    "9_4",
    "9_5",
    "10_1",
    "10_2",
    "10_3",
    "10_4",
    "10_5",
]


def load_exercise_statements():
    """Carga los enunciados de README_EJERCICIOS.md por id (1_1, 1_2, ...)."""
    mapping = {}
    readme_path = os.path.join(BASE_DIR, "README_EJERCICIOS.md")
    if not os.path.exists(readme_path):
        return mapping

    current_id = None
    current_lines = []

    with open(readme_path, "r", encoding="utf-8") as f:
        for raw_line in f:
            line = raw_line.rstrip("\n")

            if line.startswith("**Ejercicio "):
                # Guardar el enunciado anterior si existe
                if current_id and current_lines:
                    mapping[current_id] = "\n".join(current_lines).strip()
                current_lines = []

                # Formato esperado: **Ejercicio X.Y**
                parts = line.strip("* ").split()
                if len(parts) >= 2:
                    num = parts[1]  # "1.1"
                    ex_id = num.replace(".", "_")
                    current_id = ex_id
                else:
                    current_id = None
            elif current_id:
                # Fin del enunciado ante una línea vacía o nuevo bloque/separador
                if line.strip() == "" or line.startswith("---") or line.startswith("## "):
                    if current_lines:
                        mapping[current_id] = "\n".join(current_lines).strip()
                        current_lines = []
                        current_id = None
                else:
                    current_lines.append(line)

    # Guardar el último enunciado si no se volcó
    if current_id and current_lines:
        mapping[current_id] = "\n".join(current_lines).strip()

    return mapping


EXERCISE_STATEMENTS = load_exercise_statements()


INDEX_TEMPLATE = """
<!doctype html>
<html lang="es">
  <head>
    <meta charset="utf-8">
    <title>Plataforma de ejercicios y QA</title>
    <style>
      body { font-family: Arial, sans-serif; margin: 2rem; }
      h1 { color: #333; }
      form { margin-bottom: 2rem; padding: 1rem; border: 1px solid #ccc; }
      label { display: block; margin-top: 0.5rem; }
      select, input[type="file"], button { margin-top: 0.3rem; }
      pre { background: #f5f5f5; padding: 1rem; white-space: pre-wrap; }
      .ok { color: green; }
      .fail { color: red; }
      .statement { margin: 1rem 0; padding: 1rem; border-left: 4px solid #007acc; background: #f0f7ff; }
    </style>
  </head>
  <body>
    <h1>Subida de respuestas y QA automático</h1>
    <p>
      Selecciona un ejercicio, escribe tu solución en Python en el cuadro de texto
      y presiona <strong>"Ejecutar QA"</strong>. El sistema ejecutará la batería
      de tests unitarios sobre tu código.
    </p>

    <form method="post" action="{{ url_for('qa') }}">
      <label for="exercise_id">Ejercicio:</label>
      <select id="exercise_id" name="exercise_id" required>
        <option value="">-- Selecciona un ejercicio --</option>
        {% for ex in exercises %}
          <option value="{{ ex }}"
            {% if ex == selected_exercise %}selected{% endif %}>
            Ejercicio {{ ex.replace('_', '.') }}
          </option>
        {% endfor %}
      </select>

      <label for="code_text">Código de respuesta (Python):</label>
      <textarea id="code_text" name="code_text" rows="18" cols="80" required>{{ code_text or "" }}</textarea>

      <button type="submit">Ejecutar QA</button>
    </form>

    {% if exercise_statement %}
      <div class="statement">
        <h2>Enunciado del ejercicio {{ selected_exercise.replace('_', '.') }}</h2>
        <pre>{{ exercise_statement }}</pre>
      </div>
    {% endif %}

    {% if qa_run %}
      <h2>Resultado de QA para ejercicio {{ selected_exercise.replace('_', '.') }}</h2>
      <p>
        Estado general:
        {% if success %}
          <span class="ok">OK (tests completados)</span>
        {% else %}
          <span class="fail">FALLÓ (ver detalles abajo)</span>
        {% endif %}
      </p>
      <h3>Salida completa de QA</h3>
      <pre>{{ output }}</pre>
    {% endif %}

    <script>
      // Al cambiar el ejercicio seleccionado, recargar la página para mostrar el enunciado
      const select = document.getElementById('exercise_id');
      if (select) {
        select.addEventListener('change', function () {
          if (this.value) {
            const url = new URL(window.location.href);
            url.searchParams.set('exercise_id', this.value);
            window.location.href = url.toString();
          }
        });
      }
    </script>
  </body>
  </html>
"""


@app.route("/", methods=["GET"])
def index():
    selected_exercise = request.args.get("exercise_id", "")
    exercise_statement = EXERCISE_STATEMENTS.get(selected_exercise, "")
    return render_template_string(
        INDEX_TEMPLATE,
        exercises=EXERCISES,
        selected_exercise=selected_exercise,
        exercise_statement=exercise_statement,
        qa_run=False,
        success=False,
        output="",
    )


@app.route("/qa", methods=["POST"])
def qa():
    exercise_id = request.form.get("exercise_id")
    code_text = request.form.get("code_text", "")

    if not exercise_id or exercise_id not in EXERCISES or not code_text.strip():
        return redirect(url_for("index"))

    # Guardar la respuesta del estudiante en la carpeta submissions
    submissions_dir = os.path.join(os.path.dirname(__file__), "submissions")
    os.makedirs(submissions_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"ejercicio_{exercise_id}_estudiante_{timestamp}.py"
    submission_path = os.path.join(submissions_dir, filename)
    with open(submission_path, "w", encoding="utf-8") as f:
        f.write(code_text)

    # Ejecutar el runner de QA para esta entrega
    cmd = [
        "python",
        "QA/run_qa_submission.py",
        exercise_id,
        submission_path,
    ]
    completed = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
    )

    output = completed.stdout + "\n" + completed.stderr
    success = completed.returncode == 0

    exercise_statement = EXERCISE_STATEMENTS.get(exercise_id, "")

    return render_template_string(
        INDEX_TEMPLATE,
        exercises=EXERCISES,
        selected_exercise=exercise_id,
        exercise_statement=exercise_statement,
        code_text=code_text,
        qa_run=True,
        success=success,
        output=output,
    )


if __name__ == "__main__":
    # Ejecutar servidor en modo desarrollo
    app.run(debug=True)
