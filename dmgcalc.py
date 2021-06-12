

atk,crate,cdmg = input("Your ATK: "),input("Your CRATE: "),input("Your CDMG: ")

crate1,cdmg1 = str(crate)[0] if int(crate) > 100 else 0,str(cdmg)[0] if int(cdmg) > 100 else 0
crate2,cdmg2 = str(crate)[2::] if not crate1 == 0 else int(crate),str(cdmg)[1::] if not cdmg1 == 0 else int(cdmg)
crate3,cdmg3 = str(crate1) + "." + str(crate2), str(cdmg1) + "." + str(cdmg2)


dmgcalc = float(atk)*(1+float(crate3)*float(cdmg3))
print(int(dmgcalc))
