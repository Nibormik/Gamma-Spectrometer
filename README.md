# Gamma-Spectrometer
This is a Compact Gammaspectrometer Based On the Scematics and component choise of the [Open-Gamma-Detector](https://github.com/Open-Gamma-Project/Open-Gamma-Detector).
Its only Designed for testing purposes and should never be used in a production enviorment.  
<br>
This version of the Gamma spectrometer was designed with a few strict restrictions in mind.

#### Restrictions
<br>
The main rrestrictions:  <br>

- Power
    - <= 50ma
    - 5v
    - low noise
- physical limitations
    - pcb
        - width 50mm
        - height 30 mm
    - rocket interior diameter 98mm
        - max center height from pcb 38 mm
        - max edge height from pcb 28 mm 
- comunication
    - analog rocket input
        - update frequencey 2000hz - 4000hz
        - 8 bit resolution
    - digital input
        - 8bit digital paralell
        - estimated update frequency 20hz

## Similarities between projects

since this is based upon the schematic of the Open Gamma Detector there are not allot of diffrences
main diffrences are diffrent cpu and the comunication method
due to the enviorment to way comunictation is not possible so the bord does not support it

The scintilator end general operational methon of the systen is equal to that of the Opgen Gamma Detecto


