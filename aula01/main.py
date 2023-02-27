from fastapi import FastAPI
from models import Curso

app = FastAPI()
cursos = {
    1: {
        "nome": "Python",
        "aulas": 20,
        "horas": 80,
        "instrutor": "Cleber"    },
    2: {
        "nome": "Java",
        "aulas": 15,
        "horas": 60,
        "instrutor": "Leonardo"    }
}
@app.get('/cursos')
async def get_cursos():
    return cursos

@app.get('/cursos/{curso_id}')
async def get_cursos(curso_id : int):
  try:
    curso = curso[curso_id]
  # curso.update({"id" : curso_id}) 
    return curso
  except KeyError:
    raise HTPPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")



@app.post('/cursos', status_code=status.HTTP_201_CREATED)
async def post_curso(curso:Curso):
  if curso.id not in cursos:
    next_id = len(cursos) + 1
    curso.id = next_id
    cursos[next_id] = curso
    return curso
  else:
    raise HTTPException(status_code=status.HTTP_409_CONFLIT, detail=f"Já existe um curso com o ID {curso_id}")



@app.put('/cursos/{curso_}')
async def put_curso (curso_id : int , curso: Curso):
  if curso_id in cursos:
    cursos[curso_id] = curso
    return curso
  else: 
    raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"Esse
  Curso Não Existe.")


@app.delete('/cursos/{curso_}')
async def delete_curso(curso_id:int):
  if curso_id in cursos:
    del cursos[curso_id]
    return Response(status_code = status.HTTP_204_NO_CONTENT)

  else:
    raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"Esse
  Curso Não Existe.")

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host='127.0.0.1', port=8000, log_level='info', reload=True)
    