from django.db import models

# Create your models here.


class Personas_voto(models.Model):
    sexo_choices_1 = (
        ("Masculino", "Masculino"),
        ("Femenino", "Femenino"),
        ("S/D", "S/D"),
    )
    sexo_choices_2 = (
        ("M", "M"),
        ("F", "F"),
        ("S/D", "S/D"),
    )

    si_no_choices = (
        ("SI",'SI'),
        ("NO", 'NO'),
    )

    cedula = models.IntegerField(verbose_name='Cedula',primary_key=True,blank=False,null=False,)
    nombre = models.CharField(max_length=100,verbose_name='Nombres')
    apellido = models.CharField(max_length=100,verbose_name='Apellidos')
    matricula = models.IntegerField(verbose_name='Matricula', default=0)
    sexo = models.CharField(choices=sexo_choices_1,verbose_name='Sexo',max_length=100)
    universidad = models.CharField(max_length=100,verbose_name='Universidad')
    egreso = models.IntegerField(verbose_name='Egreso', default=0)
    fechaNacimiento = models.DateField(verbose_name='Fecha Nacimiento')
    estaHabilitado = models.CharField(choices=si_no_choices,verbose_name="Esta Habilitado?",max_length=100)
    fechaJuramento = models.DateField(verbose_name='Fecha Juramento')
    nroActualJuramento = models.IntegerField(verbose_name='Nro. Actual Juramento', default=0)
    fechaMatricula = models.DateField(verbose_name='Fecha Matricula')
    prePadron = models.CharField(choices=si_no_choices,verbose_name="Pre Padron",max_length=100)
    ok_2017 = models.CharField(choices=si_no_choices,verbose_name="2017 Ok - Padron 2017",max_length=100)
    voto_2017 = models.CharField(choices=si_no_choices,verbose_name="Voto 2017",max_length=100)
    sexo_2017 = models.CharField(choices=sexo_choices_2,verbose_name='Sexo 2017',max_length=100)
    dep_2017 = models.CharField(max_length=100,verbose_name="Dep 2017")
    nomdep_2017 = models.CharField(max_length=100,verbose_name="Nombre Departamento 2017")
    dis_2017 = models.CharField(max_length=100,verbose_name="Dis 2017")
    nomdis_2017 = models.CharField(max_length=100,verbose_name="Nombre Distrito 2017")
    zon_2017 = models.CharField(max_length=100,verbose_name="Zona 2017")
    nomzon_2017 = models.CharField(max_length=100,verbose_name='Nombre Zona 2017')
    loc_2017 = models.CharField(max_length=100,verbose_name='Loc 2017')
    nomloc_2017 = models.CharField(max_length=100, verbose_name='Nombre Loc 2017')
    mesa_2017 = models.CharField(max_length=100,verbose_name='Mesa 2017')
    orden_2017 = models.CharField(max_length=100,verbose_name='Orden 2017')
    edad_2017 = models.CharField(max_length=100, verbose_name='Edad 2017')
    part_2017 = models.CharField(max_length=100, verbose_name='Partido 2017')

    telefono = models.CharField(max_length=100, verbose_name='Telefono')
    celular = models.CharField(max_length=100, verbose_name='Celular')
    direccion = models.CharField(max_length=100, verbose_name='Direccion')

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'

    def __str__(self):
        return str(self.cedula) + ' - ' + self.apellido + ', ' + self.nombre





class Personas_votante(models.Model):
    sexo_choices_1 = (
        ("Masculino", "Masculino"),
        ("Femenino", "Femenino"),
        ("S/D", "S/D"),
    )
    sexo_choices_2 = (
        ("M", "M"),
        ("F", "F"),
        ("S/D", "S/D"),
    )

    si_no_choices = (
        ("SI",'SI'),
        ("NO", 'NO'),
    )

    si_no_choices_2 = (
        ("Si", 'Si'),
        ("N0", 'No'),
    )

    cedula = models.IntegerField(verbose_name='Cedula',primary_key=True,blank=False,null=False,)
    nombre = models.CharField(max_length=100,verbose_name='Nombres',blank=True,null=True,)
    apellido = models.CharField(max_length=100,verbose_name='Apellidos',blank=True,null=True,)
    matricula = models.IntegerField(verbose_name='Matricula', default=0,blank=True,null=True,)
    sexo = models.CharField(choices=sexo_choices_1,verbose_name='Sexo',max_length=100,blank=True,null=True,)
    universidad = models.CharField(max_length=100,verbose_name='Universidad',blank=True,null=True,)
    egreso = models.IntegerField(verbose_name='Egreso', default=0,blank=True,null=True,)
    fechaNacimiento = models.DateField(verbose_name='Fecha Nacimiento',blank=True,null=True,)
    estaHabilitado = models.CharField(choices=si_no_choices_2,verbose_name="Esta Habilitado?",max_length=100,blank=True,null=True,)
    fechaJuramento = models.DateField(verbose_name='Fecha Juramento',blank=True,null=True,)
    nroActualJuramento = models.IntegerField(verbose_name='Nro. Actual Juramento', default=0,blank=True,null=True,)
    fechaMatricula = models.DateField(verbose_name='Fecha Matricula',blank=True,null=True,)
    prePadron = models.CharField(choices=si_no_choices,verbose_name="Pre Padron",max_length=100,blank=True,null=True,)
    ok_2017 = models.CharField(choices=si_no_choices,verbose_name="2017 Ok - Padron 2017",max_length=100,blank=True,null=True,)
    voto_2017 = models.CharField(choices=si_no_choices,verbose_name="Voto 2017",max_length=100,blank=True,null=True,)
    sexo_2017 = models.CharField(choices=sexo_choices_2,verbose_name='Sexo 2017',max_length=100,blank=True,null=True,)
    dep_2017 = models.CharField(max_length=100,verbose_name="Dep 2017",blank=True,null=True,)
    nomdep_2017 = models.CharField(max_length=100,verbose_name="Nombre Departamento 2017",blank=True,null=True,)
    dis_2017 = models.CharField(max_length=100,verbose_name="Dis 2017",blank=True,null=True,)
    nomdis_2017 = models.CharField(max_length=100,verbose_name="Nombre Distrito 2017",blank=True,null=True,)
    zon_2017 = models.CharField(max_length=100,verbose_name="Zona 2017",blank=True,null=True,)
    nomzon_2017 = models.CharField(max_length=100,verbose_name='Nombre Zona 2017',blank=True,null=True,)
    loc_2017 = models.CharField(max_length=100,verbose_name='Loc 2017',blank=True,null=True,)
    nomloc_2017 = models.CharField(max_length=100, verbose_name='Nombre Loc 2017',blank=True,null=True,)
    mesa_2017 = models.CharField(max_length=100,verbose_name='Mesa 2017',blank=True,null=True,)
    orden_2017 = models.CharField(max_length=100,verbose_name='Orden 2017',blank=True,null=True,)
    edad_2017 = models.CharField(max_length=100, verbose_name='Edad 2017',blank=True,null=True,)
    part_2017 = models.CharField(max_length=100, verbose_name='Partido 2017',blank=True,null=True,)

    telefono = models.CharField(max_length=100, verbose_name='Telefono',blank=True,null=True,)
    celular = models.CharField(max_length=100, verbose_name='Celular',blank=True,null=True,)
    direccion = models.CharField(max_length=100, verbose_name='Direccion',blank=True,null=True,)

    class Meta:
        verbose_name = 'Persona Votante'
        verbose_name_plural = 'Personas Votantes'

    def __str__(self):
        return str(self.cedula) + ' - ' + self.apellido + ', ' + self.nombre



class Personas_votante_prod(models.Model):
    sexo_choices_1 = (
        ("Masculino", "Masculino"),
        ("Femenino", "Femenino"),
        ("S/D", "S/D"),
    )
    sexo_choices_2 = (
        ("M", "M"),
        ("F", "F"),
        ("S/D", "S/D"),
    )

    si_no_choices = (
        ("SI",'SI'),
        ("NO", 'NO'),
    )

    si_no_choices_2 = (
        ("Si", 'Si'),
        ("N0", 'No'),
    )

    cedula = models.IntegerField(verbose_name='Cedula',primary_key=True,blank=False,null=False,)
    nombre = models.CharField(max_length=100,verbose_name='Nombres',blank=True,null=True,)
    apellido = models.CharField(max_length=100,verbose_name='Apellidos',blank=True,null=True,)
    matricula = models.IntegerField(verbose_name='Matricula', default=0,blank=True,null=True,)
    sexo = models.CharField(choices=sexo_choices_1,verbose_name='Sexo',max_length=100,blank=True,null=True,)
    universidad = models.CharField(max_length=100,verbose_name='Universidad',blank=True,null=True,)
    egreso = models.IntegerField(verbose_name='Egreso', default=0,blank=True,null=True,)
    fechaNacimiento = models.DateField(verbose_name='Fecha Nacimiento',blank=True,null=True,)
    estaHabilitado = models.CharField(choices=si_no_choices_2,verbose_name="Esta Habilitado?",max_length=100,blank=True,null=True,)
    fechaJuramento = models.DateField(verbose_name='Fecha Juramento',blank=True,null=True,)
    nroActualJuramento = models.IntegerField(verbose_name='Nro. Actual Juramento', default=0,blank=True,null=True,)
    fechaMatricula = models.DateField(verbose_name='Fecha Matricula',blank=True,null=True,)
    prePadron = models.CharField(choices=si_no_choices,verbose_name="Pre Padron",max_length=100,blank=True,null=True,)
    ok_2017 = models.CharField(choices=si_no_choices,verbose_name="2017 Ok - Padron 2017",max_length=100,blank=True,null=True,)
    voto_2017 = models.CharField(choices=si_no_choices,verbose_name="Voto 2017",max_length=100,blank=True,null=True,)
    sexo_2017 = models.CharField(choices=sexo_choices_2,verbose_name='Sexo 2017',max_length=100,blank=True,null=True,)
    dep_2017 = models.CharField(max_length=100,verbose_name="Dep 2017",blank=True,null=True,)
    nomdep_2017 = models.CharField(max_length=100,verbose_name="Nombre Departamento 2017",blank=True,null=True,)
    dis_2017 = models.CharField(max_length=100,verbose_name="Dis 2017",blank=True,null=True,)
    nomdis_2017 = models.CharField(max_length=100,verbose_name="Nombre Distrito 2017",blank=True,null=True,)
    zon_2017 = models.CharField(max_length=100,verbose_name="Zona 2017",blank=True,null=True,)
    nomzon_2017 = models.CharField(max_length=100,verbose_name='Nombre Zona 2017',blank=True,null=True,)
    loc_2017 = models.CharField(max_length=100,verbose_name='Loc 2017',blank=True,null=True,)
    nomloc_2017 = models.CharField(max_length=100, verbose_name='Nombre Loc 2017',blank=True,null=True,)
    mesa_2017 = models.CharField(max_length=100,verbose_name='Mesa 2017',blank=True,null=True,)
    orden_2017 = models.CharField(max_length=100,verbose_name='Orden 2017',blank=True,null=True,)
    edad_2017 = models.CharField(max_length=100, verbose_name='Edad 2017',blank=True,null=True,)
    part_2017 = models.CharField(max_length=100, verbose_name='Partido 2017',blank=True,null=True,)
    osmar_telefono = models.CharField(max_length=100, verbose_name='Osmar Telefono',blank=True,null=True,)
    osmar_direccion = models.CharField(max_length=100, verbose_name='Osmar Direccion',blank=True,null=True,)
    osmar_trabajo = models.CharField(max_length=100, verbose_name='Osmar Trabajo',blank=True,null=True,)
    depurado_direccion = models.CharField(max_length=100, verbose_name='Direccion',blank=True,null=True,)
    depurado_tel1 = models.CharField(max_length=100, verbose_name='Telefono 1',blank=True,null=True,)
    depurado_tel2 = models.CharField(max_length=100, verbose_name='Telefono 2',blank=True,null=True,)
    depurado_estado = models.CharField(max_length=100, verbose_name='Estado',blank=True,null=True,)
    depurado_fallecido = models.CharField(max_length=100, verbose_name='Fallecido',blank=True,null=True,)

    class Meta:
        verbose_name = 'Personas Votante Produccion'
        verbose_name_plural = 'Personas Votante Produccion'

    def __str__(self):
        return str(self.cedula) + ' - ' + self.apellido + ', ' + self.nombre




