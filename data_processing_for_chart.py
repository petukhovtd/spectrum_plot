

def find_max_in_mass_mass_by_self(mass_mass):
    max_mass = []
    for mass in mass_mass:
        max_mass.append(max(mass))
    return max_mass


def find_max_in_mass_mass_by_one(mass_mass):
    max_one = 0
    for mass in mass_mass:
        if max_one < max(mass):
            max_one = max(mass)
    return max_one


def normalize_all_by_self(mass_mass):
    max_mass = find_max_in_mass_mass_by_self(mass_mass)
    for mass in range(len(mass_mass)):
        for i in range(len(mass_mass[mass])):
            mass_mass[mass][i] = mass_mass[mass][i] / max_mass[mass]
    return mass_mass


def normalize_all_to_one(mass_mass):
    max_all = find_max_in_mass_mass_by_one(mass_mass)
    for mass in range(len(mass_mass)):
        for i in range(len(mass_mass[mass])):
            mass_mass[mass][i] = mass_mass[mass][i] / max_all
    return mass_mass


def delete_const(mass_mass):
    for mass in range(len(mass_mass)):
        mass_min = min(mass_mass[mass])
        for i in range(len(mass_mass[mass])):
            mass_mass[mass][i] = mass_mass[mass][i] - mass_min
    return mass_mass


def find_cross(x, y, level):
    cross = []
    for i in range(0, len(y)-1):
        if (y[i] <= level) and (y[i+1] > level):
            cross.append(x[i])
        elif (y[i] >= level) and (y[i+1] < level):
            cross.append(x[i])
    return cross


if __name__ == "__main__":
    print("")
