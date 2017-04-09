from django.db import models


class Country(models.Model):
    name = models.CharField(
        max_length=150, unique=True, verbose_name='Nome',
        help_text='Informe o nome deste país'
    )

    class Meta:
        verbose_name = 'País'
        verbose_name_plural = 'Países'

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(
        max_length=100, verbose_name='Nome',
        help_text='Informe o nome da região'
    )

    class Meta:
        verbose_name = 'Região'
        verbose_name_plural = 'Regiões'

    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField(
        max_length=100, verbose_name='Nome',
        help_text='Informe o nome do estado')
    country = models.ForeignKey(
        Country, verbose_name='País',
        help_text='Selecione ou cadastre o País deste estado')
    region = models.ForeignKey(
        Region, verbose_name='Região',
        help_text='Selecione ou cadastre a região do país esta este estado'
    )
    abbreviation = models.CharField(
        max_length=2, help_text='Sigla do estado ou província',
        verbose_name='Sigla do estado ou província')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'


class City(models.Model):
    name = models.CharField(
        max_length=100, verbose_name='Nome',
        help_text='Informe o nome da cidade')
    state = models.ForeignKey(
        State, verbose_name='Estado',
        help_text='Selecione ou cadastre o estado/província desta cidade')
    cep = models.CharField(
        max_length=20, null=True, blank=True,
        verbose_name='CEP', help_text='Informe apenas se o CEP for por cidade')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'


class Neighborhood(models.Model):
    name = models.CharField(
        max_length=100, verbose_name='Nome',
        help_text='Nome do bairro'
    )
    city = models.ForeignKey(
        City, verbose_name='Cidade',
        help_text='Selecione ou cadastre a cidade deste bairro')
    cep = models.CharField(
        max_length=20, null=True, blank=True, verbose_name='Nome',
        help_text='Informe apenas se o CEP for por bairro')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Bairro'
        verbose_name_plural = 'Bairros'


class Address(models.Model):
    street = models.CharField(
        max_length=200, verbose_name='Rua/avenida/viela/praça',
        help_text='Nome da rua/avenida/viela')
    number = models.CharField(
        max_length=7, verbose_name='Número', help_text='Número da casa/prédio')
    neighborhood = models.ForeignKey(
        Neighborhood, verbose_name='Bairro', help_text='Selecione ou cadastre um novo bairro')
    cep = models.CharField(
        max_length=20, null=True, blank=True, verbose_name='CEP',
        help_text='Informe apenas se o CEP for por endereço(CEP da casa ou prédio)')
    complement = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Complemento',
        help_text=
        '''
            Informações adicionais sobre o endereço, exemplo:
            Próximo aos correios
        '''
    )

    def __str__(self):
        return self.street + ' nº ' + str(self.number) + ' - ' \
               + self.neighborhood.name

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'
