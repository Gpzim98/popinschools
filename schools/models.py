from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models import Avg


class School(models.Model):
    """
        School model class.
        Set school information in database models
    """
    short_phrase = models.TextField(null=True, blank=True)

    name = models.CharField(
        _(u'School Name'),
        max_length=255,
        unique=True,
        db_index=True
    )

    logo_image = models.ImageField(
        _(u"Upload o logo do seu computador"),
        upload_to='schools',
        blank=True
    )
    address = models.CharField(
        _(u"School Address"),
        help_text=_(u"Note que vc precisa colocar o endereco completo da escola"),
        max_length=255,
        db_index=True
    )

    youtube_channel_link = models.CharField(
        _(u"Youtube Channel"),
        help_text=_(u"Set the link for yout youtube channel or video"),
        max_length=255
    )

    facebook_page = models.CharField(
        _(u"Facebook Page"),
        help_text=_(u"Facebook Page"),
        max_length=255
    )

    website = models.CharField(
        _(u"WebSite"),
        help_text=_(u"Your website"),
        max_length=255
    )

    instagram = models.CharField(
        _(u"Instagram"),
        max_length=255,
        help_text=_(u"Instagram profile")
    )

    admin_email = models.EmailField(
        _(u'Email'),
        max_length=100,
        unique=True,
        help_text=_(u"Email de contato da escola")
    )

    phone = models.CharField(
        _(u'telefone'),
        max_length=18,
        null=True,
        help_text=_(u"Ex.: +55 11 91001 0101")
    )

    registration_fee = models.DecimalField(
        _(u"Registration Fee Price"),
        max_digits=10,
        help_text=_(u"Registration Fee Price"),
        decimal_places=2,
        null=True,
        blank=True
    )

    workbook = models.DecimalField(
        _(u"Workbook Price"),
        max_digits=10,
        help_text=_(u"HWorkbook Price"),
        decimal_places=2,
        null=True,
        blank=True
    )

    refounds = models.DecimalField(
        _(u"Redounds"),
        max_digits=10,
        help_text=_(u"Refounds"),
        decimal_places=2,
        null=True,
        blank=True
    )

    low_season = models.CharField(
        _(u"Low season"),
        max_length=400,
        help_text=_(u"Low season"),
        null=True,
        blank=True
    )

    high_season = models.CharField(
        _(u"High season"),
        max_length=400,
        help_text=_(u"High season"),
        null=True,
        blank=True
    )

    embeded_map = models.TextField()

    def __str__(self):
        return self.name

    def get_image(self):
        return self.logo_image.url if self.logo_image else 'assets/img/circle2.png'

    @property
    def ratings(self):
        rating_total = self.ratings_set.get_queryset().aggregate(
            Avg('stars')).get('stars__avg')
        rating_total = round(rating_total, 2) if rating_total else 0
        return rating_total


class ImageGalery(models.Model):
    image = models.ImageField(upload_to='galery')
    created_at = models.DateTimeField(auto_now_add=True)
    school = models.ForeignKey(School)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.image.name


class Videos(models.Model):
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    school = models.ForeignKey(School)
    url = models.URLField()


class EventsOffered(models.Model):
    DAYS_WEEK = (
        ('1', _('Domingo')),
        ('2', _('Segunda-feira')),
        ('3', _('Terça-feira')),
        ('4', _('Quarta-feira')),
        ('5', _('Quinta-feira')),
        ('6', _('Sexta')),
        ('7', _('Sábado')),
    )
    description = models.CharField(max_length=100)

    day = models.CharField(
        max_length=1,
        verbose_name=_('Dia da semana'),
        choices=DAYS_WEEK)

    price = models.DecimalField(
        max_digits=5, decimal_places=2)
    school = models.ForeignKey(School)

    def __str__(self):
        return self.description
