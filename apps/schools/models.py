from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from ..utils.rating_categories import RATINGS_CATEGORIES
from ..profile.models import Profile
from django.db.models import Avg


from apps.adresses.models import Address


class Accommodation(models.Model):

    TYPE_OF_ACOMMODATIONS = (
        ("school_house", "Student Acommodation"),
        ("home_stay", "Home Stay"),
        ("hostel", "Hostel")
    )

    is_beakfest_included = models.BooleanField(
        _(u"Is BreakFeast included?"),
        help_text=_(u"Is BreakFest Included?"),
        default=False
    )

    is_lunch_included = models.BooleanField(
        _(u"Is Lunch included?"),
        help_text=_(u"Is lunch Included?"),
        default=False
    )

    is_dinner_included = models.BooleanField(
        _(u"Is Dinner Included?"),
        help_text=_(u"Is dinner Included?"),
        default=False
    )

    is_tv_in_the_bedroom = models.BooleanField(
        _(u"Do you have a tv in the bedroom?"),
        help_text=_(u"Do you have a tv in the bedroom?"),
        default=False
    )

    is_wardrobe_in_the_bedroom = models.BooleanField(
        _("Do you have a wardrobe in the bedroom?"),
        help_text=_(u"Do you have a wardrobe in the bedroom?"),
        default=False
    )

    is_air_in_the_badroom = models.BooleanField(
        _("Do you have a air conditioning in the bedroom?"),
        help_text=_(u"Do you have a air conditioning in the bedroom?"),
        default=False
    )

    duration = models.CharField(
        _(u"Period of stay in"),
        help_text=_(u"Time of acomodation"),
        max_length=255
    )

    wifi_free = models.BooleanField(
        _(u"Do you have free wifi?"),
        help_text=_(u"Do you have free wifi?"),
        default=False
    )

    time_to_school = models.CharField(
        _(u"How much time it take from the school?"),
        max_length=255,
        help_text=_(u"How much time it take from the school?")
    )

    differentials = models.CharField(
        _(u"Tell Me about your differentials"),
        help_text=_(u"What is your accomodation's differential"),
        max_length=255
    )

    def __str__(self):
        return str(self.id)


class Languages(models.Model):
    description = models.CharField(max_length=20)
    initials = models.CharField(max_length=5)

    def __str__(self):
        return self.description + ' - ' + self.initials


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
    address = models.ForeignKey(
        Address, help_text=_(u"Informe o endereço da escola"),
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
        blank=True,
        default=0
    )

    workbook = models.DecimalField(
        _(u"Workbook Price"),
        max_digits=10,
        help_text=_(u"HWorkbook Price"),
        decimal_places=2,
        null=True,
        blank=True,
        default=0
    )

    refounds = models.DecimalField(
        _(u"Redounds"),
        max_digits=10,
        help_text=_(u"Refounds"),
        decimal_places=2,
        null=True,
        blank=True,
        default=0
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

    accomodation = models.ForeignKey(
        Accommodation, null=True, blank=True)

    language = models.ForeignKey(
        Languages, null=True, blank=True)

    @property
    def events(self):
        return self.eventsoffered_set.get_queryset()

    @property
    def ratings(self):
        rating_total = self.ratings_set.get_queryset().aggregate(
            Avg('stars')).get('stars__avg')
        # rating_total = round(rating_total, 2) if rating_total else 0
        return rating_total

    @property
    def galery(self):
        return self.imagegalery_set.get_queryset()

    @property
    def videos(self):
        return self.videos_set.get_queryset()

    def __str__(self):
        return self.name

    def get_image(self):
        return self.logo_image.url if self.logo_image else '/static/assets/img/circle2.png'

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('school-profile', kwargs={'pk': str(self.id)})


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
    embeded_code = models.TextField(default='')


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

    @property
    def week_day(self):
        a = {'1': _('Domingo'),
             '2': _('Segunda-feira'),
             '3': _('Terça-feira'),
             '4': _('Quarta-feira'),
             '5': _('Quinta-feira'),
             '6': _('Sexta-feira'),
             '7': _('Sábado')
             }
        return a.get(str(self.day))

    def __str__(self):
        return self.description


class Ratings(models.Model):
    def __str__(self):
        return str(self.stars)

    school = models.ForeignKey(
        School,
    )
    user = models.ForeignKey(
        Profile,
    )
    type_of_rating = models.CharField(
        _(u"Ratings"),
        choices=RATINGS_CATEGORIES,
        max_length=15
    )
    stars = models.IntegerField(
        _(u"How many Stars Do you think this school diserve?"),
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    comment = models.CharField(
        _(u"Why this note?"),
        max_length=255,
        help_text=_(u"Why Would you like to do this rating?")
    )
    class Meta:
        unique_together = ("school", "user", "type_of_rating")


class Course(models.Model):
    CLASS_TYPE = (
        ('individual', 'Individual'),
        ('group', 'Group'),
    )

    SHIFTS = (
        ('morning', 'Morning'),
        ('afternoon', 'Afternoon'),
        ('night', 'Night'),
    )

    school = models.ForeignKey(
        School
    )
    description = models.CharField(
        max_length=150, help_text='Course description'
    )
    price = models.DecimalField(
        max_digits=6, decimal_places=2, help_text='Price'
    )
    visa_needed = models.BooleanField(
        help_text='Visa is needed?'
    )
    classes_type = models.CharField(
        max_length=20, choices=CLASS_TYPE
    )
    shift = models.CharField(
        max_length=20, choices=SHIFTS
    )

    def __str__(self):
        return self.description + ' - ' + str(self.price)


class Comment(models.Model):
    user = models.ForeignKey(Profile)
    school = models.ForeignKey(School)
    comment = models.TextField()
    approved = models.BooleanField(default=True)

    def __str__(self):
        return self.user.user.first_name
