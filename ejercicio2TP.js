/*Ejercicio2: 
Escribe una función que tome un array de números como parámetro y devuelva un nuevo
array con los números ordenados de forma ascendente.
*/

// Definimos la función ordenarAscendente
function ordenarAscendente(arrayNumeros) {
    const arrayOrdenado = arrayNumeros.sort((a, b) => a - b);
    return arrayOrdenado;
  }
  
  const numerosDesordenados = [12, 3, 9, 7, 15, 6];
  
  // Llamamos a la función ordenarAscendente con el array de números desordenados como argumento
  const numerosOrdenados = ordenarAscendente(numerosDesordenados);
  
  // Mostramos el resultado en la consola
  console.log("Array desordenado:", numerosDesordenados);
  console.log("Array ordenado:", numerosOrdenados);
  