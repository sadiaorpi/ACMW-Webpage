from django.views.generic.edit import CreateView
from .models import Photo 
from .forms import PhotoForm 

class PhotoUploadView(CreateView):
    model = Photo
    form_class = PhotoForm
    template_name = 'photos.html' 
    success_url = '/photos/'  

    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)
