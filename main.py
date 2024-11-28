from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "system", "content": "You are a helpful assistant."}, {
        "role": "user", "content": "Donde me recomiendas ir a comer?"}],
    user="gsulloa@uc.cl",
    store=True,
    metadata={"user_id": "gsulloa@uc.cl", "type": "Demo"}
)

print(response)
