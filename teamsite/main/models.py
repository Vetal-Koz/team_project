from django.db import models


class Courses(models.Model):
    name = models.CharField(max_length=120, blank=False)
    description = models.CharField(max_length=200, blank=False)
    full_text = models.TextField()
    course_image = models.ImageField(null=True, blank=True, upload_to='images/')
    created_data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'


class Themes(models.Model):
    title = models.CharField(max_length=120, blank=False)
    full_text = models.TextField()
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Theme'
        verbose_name_plural = 'Themes'