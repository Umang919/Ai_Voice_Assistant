import openai
openai.api_key = ""

response = openai.Completion.create(
  model="gpt-3.5-turbo-instruct",
  prompt="write an email to boss for promotion",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)

'''
{
  "id": "cmpl-93okJp8ZNs6YcN0EocmOhwQ0FbPQ5",
  "object": "text_completion",
  "created": 1710697079,
  "model": "gpt-3.5-turbo-instruct",
  "choices": [
    {
      "text": "\n\nSubject: Request for Promotion\n\nDear [Boss's Name],\n\nI am writing this email to express my interest in the [position/role] that has recently become available at [company name]. I have been working as a [current position] for [duration] now and I believe that with my skills, experience, and dedication, I am ready to take on more responsibilities and challenges in a higher role.\n\nDuring my time at [company name], I have consistently strived to exceed expectations and deliver high-quality work. I have successfully completed [specific projects or achievements] and have received positive feedback from both my colleagues and clients. I have also taken the initiative to learn new skills and have actively participated in training programs to enhance my knowledge and abilities.\n\nI am confident that I possess the necessary qualifications and qualities to excel in the [position/role] that I am applying for. I am a quick learner, have excellent problem-solving skills, and can work efficiently under pressure. I am also a team player and have demonstrated strong leadership skills in my current role.\n\nI am eager to contribute my skills and expertise to the growth and success of [company name] in a higher position. I believe that a promotion would not only benefit me personally but also significantly contribute to the company's goals",
      "index": 0,
      "logprobs": null,
      "finish_reason": "length"
    }
  ],
  "usage": {
    "prompt_tokens": 7,
    "completion_tokens": 256,
    "total_tokens": 263
  }
}
'''