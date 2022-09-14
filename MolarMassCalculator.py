molar_mass = {'H': 1.008, 'He': 4.0026, 'Li' : 6.94, 'Be' : 9.0122, 'B' : 10.81, 'C' : 12.011, 'N' : 14.007,
              'O':15.999, 'F' : 18.998, 'Ne' : 20.180, 'Na' : 22.990, 'Mg': 24.305, 'Al' : 26.982, 'Si' : 28.085,
              'P' : 30.974, 'S' : 32.06, 'Cl' : 35.45, 'Ar' : 39.948, 'K' : 39.098, 'Ca' : 40.078, 'Sc' : 44.956,
              'Ti' : 47.867, 'V' : 50.942, 'Cr' : 51.996, 'Mn' : 54.938, 'Fe' : 55.845, 'Co' : 58.933, 'Ni' : 58.693,
              'Cu' : 63.546, 'Zn' : 65.38, 'Ga' : 69.723, 'Ge' : 72.630, 'As' : 74.922, 'Se' : 78.971, 'Br' : 79.904,
              'Kr' : 83.798, 'Rb' : 85.468, 'Sr' : 87.62, 'Y' : 88.906, 'Zr' : 91.22, 'Nb' : 92.906, 'Mo' : 95.95, 'Tc' : 98,
              'Ru' : 101.07, 'Rh' : 102.91, 'Pd' : 106.42, 'Ag' : 107.87, 'Cd' : 112.41, 'In' : 114.82, 'Sn' : 118.71, 'Sb' : 121.76,
              'Te' : 127.60 ,'I' : 126.90, 'Xe' : 131.29, 'Cs' : 132.91, 'Ba' : 137.33, 'Hf' : 178.49, 'Ta' : 180.95, 'W' : 183.84,
              'Re' : 186.2, 'Os' : 190.23, 'Ir' : 192.22, 'Pt' : 195.08, 'Au' : 196.97, 'Hg' : 200.59, 'Tl' : 204.38, 'Pb' : 207.2,
              'Bi' : 208.98, 'Po' : 209, 'At' : 210, 'Rn' : 222, 'Fr' : 223, 'Ra' : 226, 'Rf' : 267, 'Db' : 268, 'Sg' : 269, 'Bh' : 270, 'Hs' : 277}

def calculate(compound):
    atoms = []
    total = -1
    result = 0
    while len(compound) != 0:
        if compound[0].isupper():
            total +=1
            atoms.append(compound[0])
            compound = compound[1:]
        else:
            atoms[total] += compound[0]
            compound = compound[1:]
    for i in atoms:
        str = ""
        num = 0
        for j in range(len(i)):
            if i[j].isupper() or i[j].islower():
                str += i[j]
                num +=1
        i = i[num:]
        if str not in molar_mass:
            print("Atom named: " + "\"" + str + "\"" + " not found. Return -1")
            return -1
        if len(i) == 0:
            result += molar_mass[str]
        else:
            result += molar_mass[str] * int(i)
    return result


if __name__ == "__main__":
    print(calculate("H2O"))
    print(calculate("H"))
    print(calculate("HCl"))
    print(calculate("C6H12O6"))
