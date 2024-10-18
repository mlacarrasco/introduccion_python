dicc ={
  "rock": {
    "autor": "Elvis",
    "year" : 1971
	},
  "clasica":{
    "autor": "Mozart",
    "year" : 1780
  },
  "jazz":{
    "autor": "Pat Metheny",
    "year": 1990
  }
}

for o_key, o_value in dicc.items():
	print(o_value)
	for i_key, i_value in o_value.items():
		print(i_key, i_value)

