from DTO.SocioNegocio import SocioNegocio
class Cliente(SocioNegocio):
    def __init__(self,run,nombre,apellido,direccion,fono,correo,
                 tipo_cliente,montoCredito,deuda):
        super().__init__(run,nombre,apellido,direccion,fono,correo)
        self.tipo_cliente=tipo_cliente
        self.montoCredito=montoCredito
        self.deuda=deuda

    def __str__(self):
        return f"Cliente: {self.run} - {self.nombre} {self.apellido} - Tipo: {self.tipo_cliente} - Monto Crédito: {self.montoCredito} - Deuda: {self.deuda}"
    
    def pagar(self, monto):
        if monto >0:
            self.deuda -= monto
            print(f"Pago de {monto} realizado. Nueva deuda: {self.deuda}")
        else:
            print("Monto de pago inválido. Debe ser mayor a 0.")