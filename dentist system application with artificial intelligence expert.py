#Add required Libraries..!
from random import choice
from experta import *
#Create Class..!
class ill(Fact):
    pass
#Set the Rules..!
class dental_disase(KnowledgeEngine):
    @Rule(ill(situation="bleeding"))
    def bleeding(self):
        print("If there is bleeding while brushing, there may be dental discomfort. See a dentist..!")
    @Rule(ill(situation="prolonged bleeding"))
    def prolonged_bleeding(self):
        print("If there is long bleeding while brushing, your gums have receded. See a dentist..!")
    @Rule(ill(situation="gum recession"))
    def gum_recession(self):
        print("If there is gingival recession and tooth root is visible, get a filling..!")
    @Rule(ill(situation="gum discoloration"))
    def gum_discoloration(self):
        print("If there is a color change in the teeth caused by food and drink, clean your teeth..!")
    @Rule(ill(situation="gingival bruising"))
    def gingival_bruising(self):
        print("If there is bruising when a new tooth is erupting, go to the dentist..!")
    @Rule(ill(situation="tooth decay"))
    def tooth_decay(self):
        print("If you have painless cavities on your teeth, get a filling..!")
    @Rule(ill(situation="severe caries"))
    def severe_caries(self):
        print("If you have advanced decay in your teeth, have root canal treatment and filling..!")
        
        
dentist=dental_disase()
dentist.reset()
dentist.declare(ill(durum=choice(["bleeding", "prolonged bleeding", "gum recession", "dum discoloration", "gingival bruising", "tooth decay", "severse caries"])))
dentist.run()