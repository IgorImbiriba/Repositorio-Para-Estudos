
public class TestaEscopo {
	public static void main(String[] args) {
		System.out.println("Testando condicionais");
		// sysout -> crtl + espaÃÂ§o

		int idade = 30;
		int quantidadePessoas = 3; 
		boolean acompanhado;
		
		if (quantidadePessoas >= 2) {
			acompanhado = true; 	
		}else {
			acompanhado = false;
		}

		if (idade >= 20 && acompanhado) {
			System.out.println("Seja bem-vindo");
		}else {	
		
			System.out.println("Infelizmente você nao pode entrar");
		}
		
	}
}


