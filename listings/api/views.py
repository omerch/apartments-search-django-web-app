from django.db.models import Q
from rest_framework import generics, mixins
from listings.models import Listing
from .serializers import ListingSerializer
from .permissions import IsOwnerOrReadOnly

class ListingsAPIView(mixins.CreateModelMixin, generics.ListAPIView): # DetailView CreateView FormView

    lookup_field = 'pk' # slug, id
    serializer_class = ListingSerializer
    #queryset = Listing.objects.all()

    def get_queryset(self):
        qs = Listing.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(
                Q(title__icontains=query)|
                Q(zipcode__icontains=query)
                ).distinct()
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ListingsRudView(generics.RetrieveUpdateDestroyAPIView): # DetailView CreateView FormView

    lookup_field = 'pk' # slug, id
    serializer_class = ListingSerializer
    permission_classes = [IsOwnerOrReadOnly]
    #queryset = Listing.objects.all()

    def get_queryset(self):
        return Listing.objects.all()

    #def get_objects(self):
    #    id = self.kwargs.get('id')
    #    return Listing.objects.get(id=id)