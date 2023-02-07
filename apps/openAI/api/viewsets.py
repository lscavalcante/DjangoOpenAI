import openai, os

from rest_framework.exceptions import APIException, ValidationError
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from apps.openAI.api.serializers import GenereteImageSerializer


class OpenIaAPI(ViewSet):
    serializer_class = None

    def list(self, request, *args, **kwargs):
        return Response([])

    @action(detail=False, methods=['post'], serializer_class=GenereteImageSerializer)
    def generete_image(self, request):
        try:
            openai.api_key = os.getenv('OPENAI_KEY', None)
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)

            response = openai.Image.create(
                prompt=serializer.validated_data.get('image_description'),
                size='256x256'  # 512 x 512 | 1024 x 1024
            )
            return Response(response)
        except openai.InvalidRequestError as e:
            raise ValidationError(e.user_message)
        except APIException as e:
            raise e
        except Exception as e:
            raise ValidationError(f'{e}')
