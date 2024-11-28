from openai import OpenAI
from photo import take_picture
import base64

client = OpenAI()

take_picture()
encoded_string = ""
with open("temp.jpg", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "system", "content": "You are a helpful assistant."}, {
        "role": "user", "content": [{"type": "text", "text": "Dime que hay en la foto"}, {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{encoded_string}"}}]
    }],
    user="gsulloa@uc.cl",
    store=True,
    metadata={"user_id": "gsulloa@uc.cl", "type": "Demo"}
)

print(response)
