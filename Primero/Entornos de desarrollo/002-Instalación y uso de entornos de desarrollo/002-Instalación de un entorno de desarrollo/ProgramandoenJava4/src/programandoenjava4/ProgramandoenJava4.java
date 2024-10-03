/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package programandoenjava4;

/**
 *
 * @author josevicente
 */
public class ProgramandoenJava4 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // Start time
        long inicio = System.currentTimeMillis();
        System.out.println(inicio);

        // Variables
        int iteraciones = 100000000000;
        double numero = 1.00000000065;

        // Loop for multiplication
        for (int i = 0; i < iteraciones; i++) {
            numero *= 1.000000045;
        }

        // End time
        long finalTime = System.currentTimeMillis();
        System.out.println(finalTime);

        // Calculate and print total time
        long tiempoTotal = finalTime - inicio;
        System.out.println((double) tiempoTotal / 1000);  // Convert from milliseconds to seconds
    }
    
}
