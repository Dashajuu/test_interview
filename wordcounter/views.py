from django.shortcuts import render, redirect
from .forms import UploadFileForm, WordCountForm
from .models import UploadedFile
from .word_counter import WordCounter


def home(request):
    if request.method == 'POST':
        if 'upload_file' in request.POST:
            upload_form = UploadFileForm(request.POST, request.FILES)
            if upload_form.is_valid():
                file = upload_form.cleaned_data['file']
                uploaded_file = UploadedFile(file=file)
                uploaded_file.save()
                return redirect('home')
        elif 'word_count' in request.POST:
            word_form = WordCountForm(request.POST)
            if word_form.is_valid():
                word = word_form.cleaned_data['word']
                word_counter = WordCounter()
                count = word_counter.wordcount(word)
                return render(request, 'home.html', {'word_form': word_form, 'upload_form': UploadFileForm(),
                                                     'count': count})
        elif 'clear_memory' in request.POST:
            UploadedFile.objects.all().delete()
            return redirect('home')
    else:
        upload_form = UploadFileForm()
        word_form = WordCountForm()
    return render(request, 'home.html', {'upload_form': upload_form, 'word_form': word_form})
