from utils import validate_input, chat_to_model



prompt = validate_input(prompt='qual o retorno das funções desde programa?')
print(chat_to_model(prompt))


