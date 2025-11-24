import os
import shutil
import subprocess
import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) != 3:
        print("Uso: python QA/run_qa_submission.py <id_ejercicio> <ruta_respuesta>")
        return 1

    exercise_id = sys.argv[1]  # por ejemplo "1_1"
    submission_path = Path(sys.argv[2]).resolve()

    base_dir = Path(__file__).resolve().parent.parent
    soluciones_dir = base_dir / "soluciones"

    solution_filename = f"ejercicio_{exercise_id}.py"
    solution_path = soluciones_dir / solution_filename

    if not solution_path.exists():
        print(f"No existe la solución de referencia: {solution_path}")
        return 1

    if not submission_path.exists():
        print(f"No se encontró el archivo de respuesta: {submission_path}")
        return 1

    backup_path = solution_path.with_suffix(".py.bak")

    # Copiamos la solución de referencia a un backup y la respuesta del estudiante
    # a la ruta de la solución, para que los tests usen el código del estudiante.
    try:
        shutil.copy2(solution_path, backup_path)
        shutil.copy2(submission_path, solution_path)

        # Ejecutar toda la batería de tests; el resultado incluirá los casos
        # correspondientes al ejercicio modificado.
        cmd = ["python", "-m", "unittest", "QA.test_soluciones"]
        completed = subprocess.run(cmd, cwd=base_dir, capture_output=True, text=True)

        print(completed.stdout)
        if completed.stderr:
            print(completed.stderr, file=sys.stderr)

        return completed.returncode
    finally:
        # Restaurar la solución original para no afectar otros usos del repositorio.
        if backup_path.exists():
            shutil.copy2(backup_path, solution_path)
            os.remove(backup_path)


if __name__ == "__main__":
    raise SystemExit(main())

