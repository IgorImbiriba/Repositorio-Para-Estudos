
public class TestaCondicional {
	public static void main(String[] args) {
		System.out.println("Testando condicionais");
		// sysout -> crtl + espaço

		int idade = 3;
		int quantidadePessoas = 3; 

		if (idade >= 20) {
			System.out.println("Voc� tem 18 anos ou mais");
			System.out.println("Seja bem-vindo");
		}else if(quantidadePessoas >= 2){
			System.out.println("Voc� nao tem 18, mas pode entrar, "
					+ "pois esta companhado");
		}else {	
		
			System.out.println("Infelizmente voc� nao pode entrar");
		}
	}
}
