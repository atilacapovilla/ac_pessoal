from datetime import datetime
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    GROUP_CHOICE = (
        ('1', 'Receita'),
        ('2', 'Despesa'),
        ('3', 'Investimento'),
        ('4', 'Transferencia')
    )
    TYPE_CHOICE = (
        ('1', 'Fixa'),
        ('2', 'Variavel')
    )
    METHOD_CHOICE = (
        ('1', 'Essencial'),
        ('2', 'Superfluo'),
        ('3', 'Divida ou Investimento')
    )
    name = models.CharField(
        'nome',
        max_length=50)
    group = models.CharField(
        'grupo',
        max_length=1,
        choices=GROUP_CHOICE,
        default='1')
    type = models.CharField(
        'tipo',
        max_length=1,
        choices=TYPE_CHOICE,
        default='1')
    method = models.CharField(
        'método 50-30-20',
        max_length=1,
        choices=METHOD_CHOICE,
        default='1')
    planned_value = models.DecimalField(
        'valor planejamento',
        max_digits=10,
        decimal_places=2,
        default='0.00')
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Usuário')
    created_at = models.DateTimeField(
        auto_now_add=True)
    updated_at = models.DateTimeField(
        auto_now=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['group', 'name']
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class Account(models.Model):
    TYPE_CHOICE = (
        ('CC', 'Conta Corrente'),
        ('DN', 'Dinheiro'),
        ('CT', 'Cartão Crédito'),
        ('IN', 'Investimentos')
    )
    name = models.CharField(
        'nome',
        max_length=50)
    type = models.CharField(
        'tipo',
        max_length=2,
        choices=TYPE_CHOICE,
        default='CC')
    logo = models.ImageField(
        'logotipo',
        upload_to='images/',
        null=True,
        blank=True)
    opening_balance = models.DecimalField(
        'saldo inicial',
        max_digits=10,
        decimal_places=2,
        default='0.00')
    current_balance = models.DecimalField(
        'saldo atual',
        max_digits=10,
        decimal_places=2,
        default='0.00')
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Usuário')
    created_at = models.DateTimeField(
        auto_now_add=True)
    updated_at = models.DateTimeField(
        auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Conta'
        verbose_name_plural = 'Contas'


class Transaction(models.Model):
    TYPE_CHOICE = (
        ('C', 'Credito'),
        ('D', 'Debito'),
    )
    transaction_date = models.DateField(
        'data transação',
        default=datetime.now)
    due_date = models.DateField(
        'data vencimento',
        default=datetime.now)
    payment_date = models.DateField(
        'data pagamento',
        null=True,
        blank=True)
    account = models.ForeignKey(
        Account,
        on_delete=models.PROTECT,
        related_name='accounts',
        verbose_name='conta')
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='categories',
        verbose_name='categoria')
    description = models.CharField(
        'descrição',
        max_length=50,
        blank=True,
        null=True)
    transaction_value = models.DecimalField(
        'valor',
        max_digits=10,
        decimal_places=2)
    type = models.CharField(
        'tipo',
        max_length=1,
        choices=TYPE_CHOICE, default='D')
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Usuário')
    created_at = models.DateTimeField(
        auto_now_add=True)
    updated_at = models.DateTimeField(
        auto_now=True)

    def __str__(self):
        return f'{self.description} - {self.transaction_date} - {self.due_date} - {self.payment_date} - {self.transaction_value}'

    class Meta:
        ordering = ['-transaction_date', 'due_date', 'payment_date', 'type']
        verbose_name = 'Transação'
        verbose_name_plural = 'Transações'
