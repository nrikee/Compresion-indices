# Compresión de índices
Implementación de los algoritmos de compresion de índices vistos en la asignatura *Sistemas de almacenamiento y recuperación de la información* (SAR), de la Universitat Politécnica de Valencia.

## Codificación variable en bytes
Dado un entero ```G```, se pretende codificarlo de forma que usemos el menor número de bits. Para esto es necesario una **codificación variable en bytes**.

### Fundamentos
 * De cada byte, se usan los 7 bits de menor peso.
 * El bit restante, es el bit de continuación ```c```
 * Si G <= 127, se codifica en los 7 bits de menor peso, y se fija ```c = 1```
 * Si no, se van usando bytes adicionales, reservándose en cada byte el bit ```c```.
  * En el byte de menor peso, ```c = 1```
  * En el resto, ```c = 0```

## Códigos gamma
El código gamma es la forma de comprimir a nivel de bit más conocida. Su principal característica es que para valores pequeños, usa pocos bits.

### Fundamentos
 * Se representa mediante la concatenación de ```length``` y ```offset```
 * ```offset``` es ```G``` en binario, con el bit de mayor peso.
 * ```length``` es la longitud del offset codificada en **unario**.
