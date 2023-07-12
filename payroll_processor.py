class Employee:
    def __init__(self,name):
        self.name=name
        
    def calculatePay(self):
        pass
        
class SalariedEmployee(Employee):
    def __init__(self,name,salary):
        super().__init__(name)
        self.salary=salary
        
    def calculatePay(self):
        return self.salary
    
    
class HourlyEmployee(Employee):
    def __init__(self,name,hourly_rate,hours_worked):
        super().__init__(name)
        self.hourly_rate=hourly_rate
        self.hours_worked=hours_worked
        
    def calculatePay(self):
        return self.hourly_rate*self.hours_worked
    
salaried_employee=SalariedEmployee("Poorna",75000)
print("Salary of Monthly salary employee: ",salaried_employee.calculatePay())

hourly_Employee = HourlyEmployee("Vaishu",100,300)
print("Salary of Hourly salary employee: ", hourly_Employee.calculatePay() ) 
    