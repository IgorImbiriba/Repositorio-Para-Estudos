
public class TestaCondicional {
	public static void main(String[] args) {
		System.out.println("Testando condicionais");
		// sysout -> crtl + espaÃ§o

		int idade = 3;
		int quantidadePessoas = 3; 

		if (idade >= 20) {
			System.out.println("Você tem 18 anos ou mais");
			System.out.println("Seja bem-vindo");
		}else if(quantidadePessoas >= 2){
			System.out.println("Você nao tem 18, mas pode entrar, "
					+ "pois esta companhado");
		}else {	
		
			System.out.println("Infelizmente você nao pode entrar");
		}
	}
}
