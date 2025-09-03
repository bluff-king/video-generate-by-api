from google import genai
from google.genai import types
from dotenv import load_dotenv
import os, time, requests

# Load API key
load_dotenv("./key.env")
api_key = os.getenv("GOOGLE_API_KEY")
API_KEY = os.getenv("RUNWAY_API_KEY")
if not api_key and not API_KEY:
    raise ValueError("GOOGLE_API_KEY environment variable not set")

# # Đúng cú pháp SDK mới
# client = genai.Client(api_key=api_key)

# prompt = """ A boss is at oval table, he point to the board and talk to all his employees. Employees listen and comply"""

# operation = client.models.generate_videos(
#     model="veo-3.0-generate-preview",
#     prompt=prompt,
# )

# # Poll the operation status until the video is ready.
# while not operation.done:
#     print("Waiting for video generation to complete...")
#     time.sleep(10)
#     operation = client.operations.get(operation)

# # Download the generated video.
# generated_video = operation.response.generated_videos[0]
# client.files.download(file=generated_video.video)
# generated_video.video.save("dialogue_example.mp4")
# print("Generated video saved to dialogue_example.mp4")



