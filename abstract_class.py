# Abstract Class

from abc import ABC, abstractmethod

class Bank(ABC):
    
    @abstractmethod
    def bankName(self):
        pass
    
    def bankLoanInterestRate(self):
        print("1%")
    
class SBI(Bank):
    
    def bankName(self):
        print("SBI")
    
    def bankLoanInterestRate(self):
        print("5%")
        
class BOI(Bank):
    
    def bankName(self):
        print("BOI")
        
    def bankLoanInterestRate(self):
        print("10%")
        
class CB(Bank):
    
    def bankName(self):
        print("CB")
        
    def bankLoanInterestRate(self):
        print("15%")
        
sbi=SBI()
boi=BOI()
cb=CB()

sbi.bankName()
sbi.bankLoanInterestRate()

boi.bankName()
boi.bankLoanInterestRate()

cb.bankName()
cb.bankLoanInterestRate()
