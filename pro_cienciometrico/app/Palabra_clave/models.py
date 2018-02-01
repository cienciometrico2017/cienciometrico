from django.db import models
from app.Sub_Lin_Investigacion.models import sub_lin_investigacion
from app.Investigador.models import investigador
from app.Ambito_Investigativo.models import ambito_investigativo
# Create your models here.
class palabra_clave(models.Model):
 Tipo_Termino = models.CharField(max_length=100)
 Termino=models.CharField(max_length=20)
 sub_lin_investigacion =models.ForeignKey(sub_lin_investigacion,null=True ,blank=True,on_delete=models.CASCADE)
 investigador=models.ForeignKey(investigador,null=True ,blank=True,on_delete=models.CASCADE)
 ambito_investigativo = models.ForeignKey(ambito_investigativo, null=True, blank=True, on_delete=models.CASCADE)
 def __str__(self): return '{}'.format(self.Termino)