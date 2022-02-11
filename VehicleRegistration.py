import random
import string
class VehicleGeneralInfo:
    brand: str    
    catalog_price: int
    is_electric: bool
    
    def __init__(self, brand, catalog_price, is_electric) -> None:
        self.brand = brand        
        self.catalog_price = catalog_price
        self.is_electric = is_electric

    def get_tax_rate(self) -> float:
        tax_rate = 0.2
        if self.is_electric:
            tax_rate = 0.3
        return tax_rate
    
    def calculate_sale_price(self) -> int:
        return self.catalog_price + self.catalog_price * self.get_tax_rate()
    
    def print_vehicle_general_info(self):
        print(f"Brand: {self.brand}")        
        print(f"Catalog Price: {self.catalog_price}")
        print(f"Tax Rate: {self.get_tax_rate()}")
        print(f"Sale Price: {self.calculate_sale_price()}")
        
        
    

class VehicleRegistrationInfo:
    registration_id: str
    license: str
    info: VehicleGeneralInfo

    def __init__(self, registration_id, license, info) -> None:
        self.registration_id = registration_id
        self.license = license
        self.info = info

    def print_vehicle_registration_info(self):
        print(f"Registration ID: {self.registration_id}")
        print(f"License: {self.license}")
        self.info.print_vehicle_general_info()


class VehicleRegistry:
    vehicle_init_values = {}

    def add_to_vehicle_init_values(self, brand, catalog_price, is_electric) -> None:
        self.vehicle_init_values[brand] = VehicleGeneralInfo(brand,catalog_price,is_electric)

    def __init__(self) -> None:
        self.add_to_vehicle_init_values("Toyota Corolla",20000,False)
        self.add_to_vehicle_init_values("Tesla 3",50000,True)
        self.add_to_vehicle_init_values("Honda CRV",30000,False)
        self.add_to_vehicle_init_values("Hyundai Electric",40000,True)
    
    def generate_registration_id(self, length) -> str:
        return "".join(random.choices(string.ascii_uppercase + string.digits,k=length))

    def generate_license(self,registration_id) -> str:
        return self.generate_registration_id(6)[:3] + ' - ' + self.generate_registration_id(6)[3:]

    def register_vehicle(self,brand):
        registration_id = self.generate_registration_id(6)
        license = self.generate_license(registration_id)
        return VehicleRegistrationInfo(registration_id, license, self.vehicle_init_values[brand])


if __name__ == "__main__":
    vr = VehicleRegistry()
    vehicle = vr.register_vehicle("Honda CRV")
    vehicle.print_vehicle_registration_info()