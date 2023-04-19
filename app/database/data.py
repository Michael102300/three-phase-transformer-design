# English Magnitudes

input_magnitudes = [
    "Input Voltage, Vin= ", 
    "Output Voltage, Vo= ", 
    "Output Current, Io= ", 
    "Output Circuit: ", 
    "Input, Output: ", 
    "Frequency Three Phase, f= ",
    "Efficiency, η(100)= ", 
    "Regulation, α= ", 
    "Flux Density, Bac= ", 
    "Magnetic Material: ", 
    "Window Utilization, Ku= ", 
    "Diode Drop, Vd= "
]

output_magnitudes = [
    "Apparent Power, Pt= ", 
    "Electrical Conditions, Ke= ", 
    "Core Geometry, Kg= ", 
    "Number of Primary Turns, Np= ", 
    "Primary Line Current, Ipl= ", 
    "Primary Phase Current, Ipp= ", 
    "Primary Bare Wire Area, Awbp= ", 
    "Primary Wire Selected, wp= ", 
    "Primary Winding Resistance, Rp= ", 
    "Total Primary Copper Loss, Pp= ", 
    "Number of Secondary Turns, Ns= ", 
    "Secondary Bare Wire Area, Awbs= ",
    "Secondary Wire Selected, ws= ", 
    "Secondary Winding Resistance, Rs= ", 
    "Secondary Line Current, Isl= ", 
    "Secondary Phase Current, Isp= ", 
    "Total Secondary Copper Loss, Ps= ", 
    "Transformer Regulation, α= ", 
    "Watts per Kilogram= ", 
    "Core Loss, Pc= ", 
    "Total Transformer Losses, Psum= ", 
    "Transformer Efficiency= ", 
    "Watts per Unit Area= ", 
    "Temperature Rise, Tr= ", 
    "Total Window Utilization"
    ]


# Magnitudes en Español

magnitudes_entrada = [
    "Voltaje de Entrada, Vin= ", 
    "Voltaje de Salida, Vo= ", 
    "Corriente de Salida, Io= ", 
    "Circuito de Salida: ", 
    "Conexión de Entrada, Conexión de Salida: ",
    "Frecuencia Trifásica, f=", 
    "Eficiencia, η(100)=", 
    "Regulación, α= ", 
    "Densidad de Flujo, Bac= ", 
    "Material Magnético: ", 
    "Factor de Uso de Ventana, Ku= ", 
    "Tensión Umbral de Diodo, Vd= "
]

magnitudes_salida = [
    "Potencia Aparente, Pt= ", 
    "Condiciones Eléctricas, Ke= ", 
    "Geometría del Núcleo, Kg= ", 
    "Número de Vueltas del Primario, Np= ", 
    "Corriente de Línea del Primario, Ipl= ", 
    "Corriente de Fase del Primario, Ipp= ", 
    "Área del Cable del Primario, Awbp= ", 
    "Cable Seleccionado para Primario, wp= ", 
    "Resistencia del Devanado Primario, Rp= ", 
    "Pérdida por Cobre del Primario, Pp= ", 
    "Número de Vueltas del Secundario, Ns= ", 
    "Área del Cable del Secundario, Awbs= ",
    "Cable Seleccionado para Secundario, ws= ", 
    "Resistencia del Devanado Secundario, Rs= ", 
    "Corriente de Línea del Secundario, Isl", 
    "Corriente de Fase del Secundario, Isp= ", 
    "Pérdida por Cobre del Secundario, Ps= ", 
    "Regulación del Transformador, α= ", 
    "Vatios por Kilogramo= ", 
    "Pérdida por el Núcleo, Pc= ", 
    "Pérdida Total del Transformador, Psum= ", 
    "Eficiencia del Transformador= ", 
    "Vatios por Únidad de Área= ", 
    "Elevación de Temperatura, Tr= ", 
    "Uso Total de Ventana= "
]


wire_table = {
    "AWG#10": [0.05261,      0.0559,     32.7],
    "AWG#11": [0.04168,      0.0445,     41.1],
    "AWG#12": [0.03308,      0.03564,    52.1],
    "AWG#13": [0.02626,      0.02836,    65.6],
    "AWG#14": [0.02082,      0.02295,    82.2],
    "AWG#15": [0.01651,      0.01837,    104.3],
    "AWG#16": [0.01307,      0.01473,    131.8],
    "AWG#17": [0.01039,      0.01168,    165.8],
    "AWG#18": [0.008228,     0.009326,   209.5],
    "AWG#19": [0.006531,     0.007539,   263.9],
    "AWG#20": [0.005188,     0.006065,   332.3],
    "AWG#21": [0.004116,     0.004837,   418.9],
    "AWG#22": [0.003243,     0.003857,   531.4],
    "AWG#23": [0.002588,     0.003135,   666],
    "AWG#24": [0.002047,     0.002514,   842.1],
    "AWG#25": [0.001623,     0.002002,   1062],
}

exercise_values = {
    "Input Voltage": 208,
    "Output Voltage": 28,
    "Output Current": 10,
    "Frequency": 60,
    "Efficiency": 95,
    "Regulation": 5,
    "Flux Density": 1.4,
    "Window Utilization": 0.4,
    "Diode Drop": 1
}

suggested_values = {
    "Input Voltage": 120,
    "Output Voltage": 12,
    "Output Current": 15,
    "Frequency": 60,
    "Efficiency": 97,
    "Regulation": 3,
    "Flux Density": 1,
    "Window Utilization": 0.3,
    "Diode Drop": 0.7
}


static_values_english = [
    "Full Bridge",
    "Delta / Delta",
    "Silicon M6X"
]

static_values_spanish = [
    "Full Bridge",
    "Delta / Delta",
    "Silicon M6X"
]

variables_magnitudes = [
    "vin",
    "vo",
    "io",
    "",
    "",
    "f",
    "n",
    "alpha",
    "b",
    "",
    "ku",
    "vd"
]

step_one_information_english = {
    "description": "The following program was designed on Python, \n it's purpose is to calculate physical properties taken \n into consideration during a three-phase transformer \ndesign, based on some parameters chosen by \nit's manufacturer, such as input and output magnitudes, \nfrequency, efficiency, regulation, among others. I'm \naddition, it was added a graphical interface to the \nsoftware, in order to make interaction between the \nuser and the machine friendlier"
}

list_units = ["VA","","cm^5","vueltas","A","A","cm^2","","Ω","W","vueltas","cm^2","","Ω","A","A","W","%","","W","W","%","W/cm^2","ºC",""]