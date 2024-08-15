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
    name = models.CharField(max_length=50, verbose_name='Nome')
    group = models.CharField(
        max_length=1, choices=GROUP_CHOICE, default='1', verbose_name='Grupo')
    type = models.CharField(
        max_length=1, choices=TYPE_CHOICE, default='1', verbose_name='Tipo')
    method = models.CharField(
        max_length=1, choices=METHOD_CHOICE, default='1', verbose_name='Método 50-30-20')
    planned_value = models.DecimalField(
        max_digits=10, decimal_places=2, default='0.00', verbose_name='Valor Planejado')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Usuário')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='Alterado em')

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
    name = models.CharField(max_length=50, verbose_name='Nome')
    type = models.CharField(
        max_length=2, choices=TYPE_CHOICE, default='CC', verbose_name='Tipo')
    logo = models.ImageField(
        upload_to='images/', null=True, blank=True, verbose_name='Logotipo')
    opening_balance = models.DecimalField(
        max_digits=10, decimal_places=2, default='0.00', verbose_name='Saldo Inicial')
    current_balance = models.DecimalField(
        max_digits=10, decimal_places=2, default='0.00', verbose_name='Saldo Atual')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Usuário')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='Alterado em')

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
        default=datetime.now, verbose_name='Data da Transação')
    due_date = models.DateField(
        default=datetime.now, verbose_name='Data de Vencimento')
    is_paid = models.BooleanField(default=True, verbose_name='Pago')
    account = models.ForeignKey(
        Account, on_delete=models.PROTECT, related_name='accounts', verbose_name='Conta')
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name='categories', verbose_name='categoria')
    description = models.CharField(
        max_length=50, blank=True, null=True, verbose_name='Descrição')
    transaction_value = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Valor')
    type = models.CharField(
        max_length=1, choices=TYPE_CHOICE, default='D', verbose_name='Tipo')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Usuário')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='Alterado em')

    def __str__(self):
        return f'{self.description} - {self.transaction_date} - {self.due_date} - {self.transaction_value}'

    class Meta:
        ordering = ['-transaction_date', 'due_date', 'type']
        verbose_name = 'Transação'
        verbose_name_plural = 'Transações'
