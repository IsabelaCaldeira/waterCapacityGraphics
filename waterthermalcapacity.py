import numpy as np 
import matplotlib.pyplot as plt

Pb = 1850 # Puissance de la bouillard  en W

def heat(Pb, temp):
    return Pb * temp

def heatCapacity(Pb, temp, m, TemperaIni):
    return heat(Pb, temp) / (m * (100 - TemperaIni))

#Experience avec thermo
temps1  = np.arange(0, 191, 1) #s
temperature1 = np.loadtxt('temperature1.txt') #°C

Cv1 = heatCapacity(Pb, temps1[-1], 1, temperature1[0])

#Simulation Experience avec thermo
Cv_eau = 4180 #J/g°C
Q = Cv_eau * 1 * (100 - temperature1[0])
temps_simulation = np.arange(0, Q/Pb, 1)
temperature_simulation = np.linspace(24, 100, int(Q/Pb) + 1)

#Experience sans le thermomethe
temps_sansthermo = np.arange(0,170,1)
temperature_sansthermo = np.linspace(23,100,170)

#Simulation Experience sans le thermomethe
temps_simulation_sansthermo = np.arange(0, Q/Pb, 1)
temperature_simulation_sansthermo = np.linspace(23, 100, int(Q/Pb) + 1)

#Graphique 
plt.figure(figsize=(12, 5))
plt.subplot(1,2,1)
plt.axis([0, 190, 24, 100])
plt.plot(temps1, temperature1, 'b')
plt.plot(temps_simulation, temperature_simulation, 'c--')
plt.xlabel('Temps(s)'); plt.ylabel('Temperature(°C)')
plt.title('Comparation des Mesures vs Simulation avec thermometre')
plt.savefig('comparationAvecThermo.png')
plt.legend(['Experience avec Thermo', 'Simulation Experience thermo'])
plt.minorticks_on()
plt.grid()

plt.subplot(1,2,2)
plt.axis([0, temps_simulation_sansthermo[-1], temperature_sansthermo[0], 100])
plt.plot(temps_sansthermo,temperature_sansthermo, 'y')
plt.plot(temps_simulation_sansthermo, temperature_simulation_sansthermo, 'r--')
plt.xlabel('Temps(s)'); plt.ylabel('Temperature(°C)')
plt.title('Comparation des Mesures vs Simulation sans thermometre')
plt.savefig('comparationSansThermo.png')
plt.legend(['Experience s/ thermometre','Simulation Experience s/thermometre'])
plt.minorticks_on()
plt.grid()
plt.show()
