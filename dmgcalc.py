
class GIDMGCALC:
        def user_inputs(self):
            atk,crate,cdmg = input("Your ATK: "),input("Your CRATE: "),input("Your CDMG: ")
            GIDMGCALC().digitfinalization(atk,crate,cdmg)
        
        def digitfinalization(self,atk,crate,cdmg):
                crate1,cdmg1 = str(crate)[0] if int(crate) > 100 else 0,str(cdmg)[0] if int(cdmg) > 100 else 0
                crate2,cdmg2 = str(crate)[2::] if not crate1 == 0 else int(crate),str(cdmg)[1::] if not cdmg1 == 0 else int(cdmg)
                crate3,cdmg3 = str(crate1) + "." + str(crate2), str(cdmg1) + "." + str(cdmg2)
                GIDMGCALC().calculation(atk,crate3,cdmg3)
        
        def calculation(self,atk,crate,cdmg):
            dmgcalc = float(atk)*(1+float(crate)*float(cdmg))
            print("Ur avarage: "), print(int(dmgcalc))

GIDMGCALC().user_inputs()
