# Miniproyecto4_Simulacion

### Ejercicio - Servidores
Suponga que usted está a cargo de definir la arquitectura a usar en el lanzamiento de su próxima aplicación web:
C3 (sistema de contabilidad de la carreta contadora). La junta directiva le ha solicitado que encuentre el mejor servicio de hosting para el proyecto. Después de una investigación gigante, usted concluye que las mejores opciones se reducen a las siguientes dos:

1. Proveedor 1 - Mountain Mega Computing: Tienen una infraestructura de servidor único, con mucha potencia de procesamiento. Ellos se enorgullecen al indicar que su servidor Enterprise puede atender hasta 100 solicitudes por segundo.
2. Proveedor 2 - Pizzita computing: Tienen una infraestructura de múltiples servidores (en nube). Cada servidor es medianamente potente, y en su promoción indican que se paga únicamente la cantidad de servidores que su aplicación requiera. Luego de su análisis de esta oferta, usted infiere que cada servidor tiene a lo sumo una décima parte de la potencia del servidor promocionado por Mountain Mega Computing.

Las pruebas de estrés iniciales, y las proyecciones calculadas para los primeros dos años luego del lanzamiento, indican que su aplicación jamás excederá los 2,400 solicitudes por minuto.Una auditoría y análisis de benchmark a sistemas similares al suyo indican que las solicitudes deberían llegar como un proceso de Poisson, y que el tiempo de servicio de cada solicitud (sin importar la arquitectura de servidor usada) es modelado adecuadamente por una variable aleatoria exponencial.
Mañana tiene que presentar su decisión final a la junta directiva del proyecto. Como no tiene tiempo para hacer una investigación a detalle con los clientes de cada proveedor, decide creer en su promoción y hacer una simulación para concluir cuál será la mejor opción

### Tasks
1. Modele, simule y analice el comportamiento de ambos sistemas durante una hora de ejecución de C3, y para cada sistema responda;
    - ¿Cuántas solicitudes atendió cada servidor
    - ¿Cuánto tiempo estuvo cada servidor ocupado
    - ¿Cuánto tiempo estuvo cada servidor desocupado (iddle)
    - ¿Cuánto tiempo en total estuvieron las solicitudes en cola
    - En promedio ¿cuánto tiempo estuvo cada solicitud en cola
    - En promedio, ¿cuántas solicitudes estuvieron en cola cada segundo
    - ¿Cuál es el momento de la salida de la última solicitud
2. Determine empíricamente cuántos servidores se necesitaría “alquilar” en Pizzita computing para asegurar que siempre habrá al menos un servidor disponible para atender una solicitud dada (en otras palabras,una solicitud nunca tiene que esperar en cola).
3. Se espera que apartir del tercer año del lanzamiento de su aplicación,la cantidad de usuarios sufra un alza, y por tanto deberán atender como máximo 6000 solicitudes por minuto. Resuelva el inciso 1 y 2 para esta nueva configuración.
4. Emita una recomendación para la junta directiva