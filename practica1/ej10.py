# 10 ¿Hay alguna forma de hacer recuperarse el método de Newton (es decir que continúe
# calculando) para f si la derivada f ’ se anula en algún punto durante la iteración?

#******************************************************************************
#******************************** Observaciones *******************************
#******************************************************************************
# Si, cuando la f' es nula se puede:
# * Cambiar a metodo de bisección (lo cual es mas lento pero seguramente lo mas conveniente)
# * Se puede implementar un metodo llamada "Perturbación", el cual se la agrega un valor infimo como
# 0.0001 al valor actual => 0, y continuar con el metodo
# * Se puede utilizar el ultimo valor de la derivada, esto no seria lo mas optimo en la mayoria
# de casos ya que se esta cambiando el valor de la tangente.
