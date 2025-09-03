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



generate_url = "https://api.aivideoapi.com/runway/generate/video"
status_url   = "https://api.aivideoapi.com/status"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

payload = {
    "text_prompt": "A serene mountain landscape at dawn",
    "model": "gen3",
    "width": 1280,
    "height": 768,
    "seed": 42,
    "callback_url": "",
    "time": 5
}

# Gửi yêu cầu tạo video
response = requests.post(generate_url, json=payload, headers=headers)
if response.status_code != 200:
    print("Lỗi khi tạo video:", response.status_code, response.text)
else:
    result = response.json()
    uuid = result.get("uuid") or result.get("id")
    print("UUID:", uuid)

    # Poll endpoint để kiểm tra tiến độ
    while True:
        time.sleep(3)
        r2 = requests.get(status_url, params={"uuid": uuid}, headers=headers)
        if r2.status_code != 200:
            print("Lỗi khi kiểm tra trạng thái:", r2.status_code, r2.text)
            break

        status_data = r2.json()
        status = status_data.get("status")
        print("Trạng thái:", status)
        if status == "success":
            print("Video URL:", status_data.get("video_url"), "GIF URL (nếu có):", status_data.get("gif_url"))
            break
        elif status == "failed":
            print("Job thất bại:", status_data.get("error"), "Code lỗi:", status_data.get("error_code"))
            break
        # Nếu là "in queue" hoặc "submitted", tiếp tục đợi

