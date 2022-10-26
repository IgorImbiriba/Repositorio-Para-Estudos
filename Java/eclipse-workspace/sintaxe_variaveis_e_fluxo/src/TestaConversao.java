
public class TestaConversao {
	public static void main (String[] args) {
		
		double salario = 1270.50;
		float pontoFlutuante = 3.14f; 
		
		int valor = (int)salario; // 32bits
		System.out.println(valor);
		
		long numeroGrande = 87432498732498732l; // 64 bits
		short valorPequeno = 1253; // 16 bits
		byte b = 127;
		
	}
}
