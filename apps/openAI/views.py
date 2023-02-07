import os

import openai

from django.shortcuts import render


def gerente_image_from_txt(request):
    openai.api_key = os.getenv('OPENAI_KEY', None)
    urls = []
    user_input = ''

    if request.method == 'POST':
        if request.POST.get('user_input') is not None:
            user_input = request.POST.get('user_input')
            response = openai.Image.create(
                prompt=user_input,
                size='256x256'  # 512 x 512 | 1024 x 1024
            )

            for data in response.data:
                urls.append(data.url)

    context = {'urls': urls, 'user_input': user_input}

    return render(request, "openAI.html", context)
