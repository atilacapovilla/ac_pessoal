from apps.finance.models import *


class Category(models.Model):
    TYPES_CHOICES = [
        ('receita', 'Receita'),
        ('despesa', 'Despesa'),
        ('investimento', 'Investimento'),
        ('transferencia', 'Transferência'),
    ]
    NATURES_CHOICES = [
        ('fixa', 'Fixa'),
        ('variavel', 'Variável'),
    ]
    PRIORITIES_CHOISES = [
        ('essencial', 'Essencial(50%)'),
        ('superflua', 'Superflua(30%)'),
        ('reserva', 'Reserva(20%)'),
    ]

    name = models.CharField(
        max_length=50,
        verbose_name='Nome'
    )
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name='Categoria Pai',
        related_name='children'
    )
    order = models.IntegerField(
        verbose_name='Ordem de Apresentação'
    )
    category_type = models.CharField(
        max_length=15,
        choices=TYPES_CHOICES,
        default='despesa',
        verbose_name='Tipo de Categoria'
    )
    category_nature = models.CharField(
        max_length=15,
        choices=NATURES_CHOICES,
        default='fixa',
        verbose_name='Natureza da Categoria'
    )
    category_priority = models.CharField(
        max_length=15,
        choices=PRIORITIES_CHOISES,
        default='essencial',
        verbose_name='Prioridade(Método 50/30/20)'
    )
    planned_value = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default='0.00',
        verbose_name='Valor Planejado'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Usuário'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Criado em'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Alterado em'
    )
    active = models.BooleanField(
        'Categoria Ativa', default=True
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['name']
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
