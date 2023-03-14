import openai
import os
import urllib.request

openai.api_key = "your API key goes here"

def image_creation():
    prompt = ""
    print("Input your image prompt and hit 'enter' twice to submit.")
    while True:
        line = input()
        if line:
            prompt += line + '\n'
        else:
            break

    response = openai.Image.create(
        prompt = prompt,
        size = "1024x1024",
        n = 1
    )

    image_url = response['data'][0]['url']

    save_directory = "Images"
    
    if not os.path.exists("Images"):
        os.mkdir("Images")
    
    # Extract the image file name from the URL.
    # Would be better to have the file name be the actual prompt, not the resulting URL.
    # But I'm too lazy to do that right now.
    image_file_name = image_url.split("/")[-1]
    image_file_name += ".png"
    save_path = os.path.join(save_directory, image_file_name)

    # Download the image and save it to the specified directory
    urllib.request.urlretrieve(image_url, save_path)

    print(f"Image saved to {save_path}")

    # Check what OS the user is running, automatically open the image in default browser
    if os.name == "nt":
        os.startfile(image_url)
    else:
        os.system("open " + url)
        
while True:
    image_creation()
