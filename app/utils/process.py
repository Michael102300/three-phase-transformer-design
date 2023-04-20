from numpy import *
from app.database.data import *

def get_type_of_wire(magnitude: float, data: dict):
    keys = list(data.keys())
    diff = []
    for i in keys:
        diff.append(round(abs((data[i][0]-magnitude)), 5))
    awg = sorted(diff)[0]
    return [keys[diff.index(awg)]][0]


def get_lamination(magnitude: float, data: dict):
    keys = list(data.keys())
    diff = []
    for i in keys:
        diff.append(round(abs(data[i][3]-magnitude), 5))
    kg = sorted(diff)[0]
    return [keys[diff.index(kg)]][0]


def calculus(parameters: dict, language: str):

    Vi = parameters["Input Voltage"]
    Vo = parameters["Output Voltage"]
    Io = parameters["Output Current"]
    f = parameters["Frequency"]
    n = parameters["Efficiency"]
    alpha = parameters["Regulation"]
    B = parameters["Flux Density"]
    Ku = parameters["Window Utilization"]
    Vd = parameters["Diode Drop"]

    dict = {}
    list = []

    # Get efficiency as a percentage
    n = n/100

    # Step 1: Calculate Apparent Power
    Po = Io*(Vo+2*Vd)
    Pt = Po*((1.05)/(n)+1.05)  # Watts
    Pt = round(Pt)
    list.append(Pt)

    # Step 2: Calculate Electrical Conditions
    Ke = 2.86*(f**2)*(B**2)*(10**-4)  # No units
    Ke = round(Ke, 2)
    list.append(Ke)

    # Step 3: Calculate the Core Geometry
    Kg = (Pt)/(2*Ke*alpha)  # cm^5
    Kg = round(Kg)
    list.append(Kg)

    # Step 4: Core Number for Lamination
    lamination = get_lamination(Kg, lamination_table)
    Wtfe = lamination_table[lamination][0]
    Ac = lamination_table[lamination][5]
    Wa = lamination_table[lamination][2]
    MLT = lamination_table[lamination][1]
    At = lamination_table[lamination][4]
    list.append(lamination)

    # Step 5: Calculate the number of primary turns
    Np = (Vi*(10**4))/(4.44*B*Ac*f)  # Turns
    Np = round(Np)
    list.append(Np)

    # Step 6: Calculate the primary line current
    Ipl = (Po)/(3*Vi*n)  # Amps
    Ipl = round(Ipl, 3)
    list.append(Ipl)

    # Step 7: Calculate the primar yphase current
    Ipp = (Ipl)/(sqrt(3))
    Ipp = round(Ipp, 3)  # Amps
    list.append(Ipp)

    # Step 8: Calculate the primary bare wire area
    Kup = Ku/2
    Awpb = (Kup*Wa)/(4*Np)
    Awpb = round(Awpb, 5)  # cm**2
    list.append(Awpb)

    # Step 9: The selection of the primary wire would be from the Wire Table in Chapter 4
    wp = get_type_of_wire(Awpb, wire_table)
    Awbp = wire_table[wp][0]
    Awinsp = wire_table[wp][1]
    R_1 = wire_table[wp][2]
    list.append(wp)

    # Step 10: Calculate the primary windind resistance
    Rp = MLT*Np*R_1*(10**-6)
    Rp = round(Rp, 1)  # Ohms
    list.append(Rp)

    # Step 11: Calculate the total primary copper
    Pp = 3*(Ipp**2)*Rp
    Pp = round(Pp, 2)  # Watts
    list.append(Pp)

    # Step 12: Calculate the secondary turns
    Vs = 0.740*(Vo+2*Vd)
    Ns = (Np*Vs)/(Vi)*(1+(alpha)/(100))
    Ns = round(Ns)  # Turns
    list.append(Ns)

    # Step 13: Calculate the secondary bare wire area
    Kus = Ku-Kup
    Awsb = (Kus*Wa)/(4*Ns)
    Awsb = round(Awsb, 4)  # cm^2
    list.append(Awsb)

    # Step 14: The selection of the secondary wire will be from the Wire Table in Chapter 4
    ws = get_type_of_wire(Awsb, wire_table)
    Awbs = wire_table[ws][0]
    Awinss = wire_table[ws][1]
    R_2 = wire_table[ws][2]
    list.append(ws)

    # Step 15: Calculate the secondary winding resistance
    Rs = MLT*Ns*R_2*(10**-6)
    Rs = round(Rs, 3)  # Ohms
    list.append(Rs)

    # Step 16: Calculate the secondary line current
    Isl = 0.471*Io
    Isl = round(Isl, 2)  # Amps
    list.append(Isl)

    # Step 17: Calculate the secondary phase current
    Isp = Isl/(sqrt(3))
    Isp = round(Isp, 2)  # Amps
    list.append(Isp)

    # Step 18: Calculate the total secondary copper loss
    Ps = 3*(Isp**2)*Rs
    Ps = round(Ps, 2)  # Watts
    list.append(Ps)

    # Step 19: Calculate the transformer regulation
    Pcu = Pp+Ps
    alpha_2 = (Pcu/Po)*100
    alpha_2 = round(alpha_2, 2)  # %
    list.append(alpha_2)

    # Step 20: Calculate the watts per kilogram
    Wk = 0.0005577*(60**1.68)*(B**1.86)
    Wk = round(Wk, 2)
    list.append(Wk)

    # Step 21: Calculate the core loss
    Pfe = Wk*Wtfe
    Pfe = round(Pfe, 2)  # Watts
    list.append(Pfe)

    # Step 22: Summarize the total transformer losses
    Psum = Pp+Ps+Pfe
    Psum = round(Psum, 3)  # Watts
    list.append(Psum)

    # Step 23: Calculate the transformes efficiency
    n_2 = (Po*100)/(Po+Psum)
    n_2 = round(n_2, 1)  # %
    list.append(n_2)

    # Step 24: Calculate the watts per unit area
    psi = (Psum)/(At)
    psi = round(psi, 4)  # watts per cm^2
    list.append(psi)

    # Step 25: Calculate the temperature rise
    Tr = 450*(psi**0.826)
    Tr = round(Tr)  # ºC
    list.append(Tr)

    # Step 26: Calculate the total window utilization
    Ku = (4*Np*Awbp)/(Wa)+(4*Ns*Awbs)/(Wa)
    Ku = round(Ku, 3)
    list.append(Ku)

    if language=="en":
        for i in range(len(list)):
            dict[output_magnitudes[i]] = list[i]
    elif language=="es":
        for i in range(len(list)):
            dict[magnitudes_salida[i]] = list[i]
            
    return dict

def dict_for_units(keys: list, units: list):
    dict = {}
    for i in range(len(keys)):
        dict[keys[i]] = units[i]
    return dict