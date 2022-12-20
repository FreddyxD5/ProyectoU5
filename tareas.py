"""
1.-Para la parte del login deben hacer uso de simpleJWT, y debe contar con las mismas
funcionalidades que el login desarrollado en sesiones anteriores. (Terminado)

2.-La API deberá contar con el CRUD para todos los modelos presentados.(Terminado)

3.-Deben crear roles para el uso de la API.
    Anónimo: No puede acceder a la API
    Usuario normal: Puede realizar POST de los pagos y hacer GET de todas las vistas.
    Admin: Tiene acceso al CRUD de todas las vistas.
    (Pendiente)(Hecho a medias xd)

4.-La vista creada para el modelo de servicios debe ser estática,
    por lo que debe contar únicamente con el método GET.(Terminado)

5.-La vista creada para el modelo Expired_payments, sólo debe admitir GET y POST(Terminado)

6.-Añadir Paginación de 100 resultados por página.(Terminado)

7.-Añadir filtro de búsqueda en Payment_user para los campos de fecha de pago y fecha de expiración.(Pendiente)

8.-Si la fecha de pago supera a la fecha de expiración, se debe crear un registro automático en Expired_payments.(Terminado)

9.-Implementar Throttling para la vista de pagos con 1000 request por día y
las demás de 2000 por día. Para las pruebas realizar con 3 y 7 respectivamente. (Terminado)

10.-Generar la documentación de toda su API.(Terminado)
"""