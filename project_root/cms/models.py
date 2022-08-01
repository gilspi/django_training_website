from django.db import models

# Create your models here.
class CmsSlider(models.Model):
    cms_img = models.ImageField(upload_to='sliderimg/')
    cms_title = models.CharField(verbose_name='Title', max_length=200)
    cms_text = models.CharField(verbose_name='Text', max_length=200)
    cms_css = models.CharField(verbose_name='CSS class', null=True, default='-', max_length=200)

    def __str__(self):
        return self.cms_title

    class Meta:
        verbose_name = 'Slider'
        verbose_name_plural = 'Sliders' 
