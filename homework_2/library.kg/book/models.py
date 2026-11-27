from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name='Type in the titile of the book')
    image_1 = models.ImageField(upload_to='book/', verbose_name='Load first cover art of the book')
    image_2 = models.ImageField(upload_to='book/', verbose_name='Load second cover art of the book')
    description = models.TextField(verbose_name='Give a short description of the book', blank=True)
    GENRE =(
        ('Fantasy', 'Fantasy'),
        ('Science Fiction', 'Science Fiction'),
        ('Mystery', 'Mystery'),
        ('Thriller', 'Thriller'),
        ('Romance', 'Romance'),
        ('Historical Fiction', 'Historical Fiction'),
        ('Horror', 'Horror'),
        ('Literary Fiction', 'Literary Fiction'),
        ('Biography', 'Biography'),
        ('Non-Fiction', 'Non-Fiction'),
    )
    genre = models.CharField(max_length=100, choices=GENRE, default='Fantasy', verbose_name='Select a genre')
    audio_book = models.FileField(upload_to='book/', verbose_name='Upload audio file of the audiobook')
    author = models.CharField(max_length=100, verbose_name='Type in the name of the author')
    count_pages = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(9999999)], verbose_name='Type in the number of pages')
    create_data_book = models.DateField(verbose_name='Type in the date of the publishing the book')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}-{self.created_at}'

    class Meta:
        verbose_name = 'book'
        verbose_name_plural = 'books'