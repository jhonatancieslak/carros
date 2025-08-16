from openai import OpenAI

client = OpenAI(api_key='API_KEY')

def get_car_ai_bio(model, brand, year):
    message = """
    Me mostre uma descrição de venda para o carro {} {} {} em apenas 250 caracteres. 
    Fale coisas específicas desse modelo.
    Descreva especificações técnicas desse modelo de carro.
    """.format(brand, model, year)

    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role': 'user', 'content': message}
        ],
        max_tokens=1000
    )

    return response.choices[0].message["content"]
