import re

from .models import UploadedFile


class WordCounter:
    @staticmethod
    def wordcount(word):
        try:
            uploaded_file = UploadedFile.objects.latest('id')
            with open(uploaded_file.file.path, 'r') as file:
                text = file.read()
                words = re.findall(r'\b[A-Za-z]+\b', text)
                count = words.count(word)
                return count
        except UploadedFile.DoesNotExist:
            return None