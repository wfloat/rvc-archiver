from openai import OpenAI
import os
import base64
import requests

# OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

client = OpenAI()
# image_a = encode_image("frames/4976.jpg")
# image_b = encode_image("frames/5001.jpg")
# image_c = encode_image("frames/5026.jpg")
# image_a = encode_image("icespice/bad_0.png")
# image_b = encode_image("icespice/bad_1.png")
image_a = encode_image("icespice/stiched.jpg")
# image_b = encode_image("icespice/1.png")
# image_c = encode_image("icespice/2.png")

response = client.chat.completions.create(
  model="gpt-4-vision-preview",
  messages=[
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Does the music artist named Ice Spice appear in every frame of this frame sequence? I need you to output only this dict filled in {is_pictured_in_each: bool}"
          # "text": "Does Ice Spice appear in each frame of this sequence of frames? Is her mouth moving? I need you to output only this dict filled in {is_pictured_in_each: bool, is_mouth_moving: bool}"
          # "text": "Does Omni-Man appear in this sequence of frames? Is he speaking? How is he feeling emotionally? I need you to output only this dict filled in {is_pictured: bool, is_speaking: bool, emotion: 'normal' | 'angry' | 'happy' | 'sad' | None}"
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{image_a}",
            "detail": "low"
          }
        },
        # {
        #   "type": "image_url",
        #   "image_url": {
        #     "url": f"data:image/jpeg;base64,{image_b}",
        #     "detail": "low"
        #   }
        # },
        # {
        #   "type": "image_url",
        #   "image_url": {
        #     "url": f"data:image/jpeg;base64,{image_b}",
        #     "detail": "low"
        #   }
        # },
        # {
        #   "type": "image_url",
        #   "image_url": {
        #     "url": f"data:image/jpeg;base64,{image_d}",
        #     "detail": "low"
        #   }
        # },
        # {
        #   "type": "image_url",
        #   "image_url": {
        #     "url": f"data:image/jpeg;base64,{image_c}",
        #     "detail": "low"
        #   }
        # }
      ],
    }
  ],
  max_tokens=300,
)

print(response.choices[0])

response = client.chat.completions.create(
  model="gpt-4-vision-preview",
  messages=[
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Does Ice Spice's mouth move between each frame of this frame sequence? I need you to output only this dict filled in {is_speaking: bool}"
          # "text": "Does Ice Spice appear in each frame of this sequence of frames? Is her mouth moving? I need you to output only this dict filled in {is_pictured_in_each: bool, is_mouth_moving: bool}"
          # "text": "Does Omni-Man appear in this sequence of frames? Is he speaking? How is he feeling emotionally? I need you to output only this dict filled in {is_pictured: bool, is_speaking: bool, emotion: 'normal' | 'angry' | 'happy' | 'sad' | None}"
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{image_a}",
            "detail": "low"
          }
        },
        # {
        #   "type": "image_url",
        #   "image_url": {
        #     "url": f"data:image/jpeg;base64,{image_b}",
        #     "detail": "low"
        #   }
        # },
        # {
        #   "type": "image_url",
        #   "image_url": {
        #     "url": f"data:image/jpeg;base64,{image_b}",
        #     "detail": "low"
        #   }
        # },
        # {
        #   "type": "image_url",
        #   "image_url": {
        #     "url": f"data:image/jpeg;base64,{image_d}",
        #     "detail": "low"
        #   }
        # },
        # {
        #   "type": "image_url",
        #   "image_url": {
        #     "url": f"data:image/jpeg;base64,{image_c}",
        #     "detail": "low"
        #   }
        # }
      ],
    }
  ],
  max_tokens=300,
)

print(response.choices[0])