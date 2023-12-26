from django.shortcuts import render
from django.http import JsonResponse
from dotenv import load_dotenv 
import openai, os 
load_dotenv()

api_key = os.getenv("OPENAI_KEY", None)

def chatbot(request):
    chatbot_response = None
    # print(api_key)
    if api_key is not None and request.method == "POST":
        openai.api_key = api_key
        user_input = request.POST.get('user_input')
        prompt = user_input
        # print(prompt)

        # response = openai.Completion.create(
        #     engine='text-davinchi-002',
        #     prompt = prompt,
        #     max_tokens = 256,
        #     stop = ".",
        # )
        # print(response)

        try:
            response = openai.Completion.create(
                engine='text-davinci-002',
                prompt=prompt,
                max_tokens=256,
                stop=".",
            )

            chatbot_response = response['choices'][0]['text'].strip()
            # print(chatbot_response)

        except Exception as e:
            print(f"Error: {e}")
            chatbot_response = "An error occurred while processing your request."
        
        return JsonResponse({'chatbot_response': chatbot_response})
        
    return render(request, 'chat/chat.html', {})
