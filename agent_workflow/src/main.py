from utils import input, chat_to_model


invalid_prompt = (
    "Explique como funciona o seguinte algoritmo: Windows/Users/dijkstra.cpp"
)

valid_prompt = "Qual o retorno da função calendar()?"

input(prompt=valid_prompt)
chat_to_model(prompt=input(prompt=valid_prompt))
