package paquete2;

import paquete1.Estudiante;
public class Matricula {
	private int valor;
	private Estudiante estudiante;
	private boolean pagada;
	private String codigo;
	
	//Constructores
	
	public Matricula() {
		
	}
	
	public Matricula(int valor, Estudiante estudiante, boolean pagada, String codigo) {
		this.valor = valor;
		this.estudiante = estudiante;
		this.pagada = pagada;
		this.codigo = codigo;
	}
	
	//setters y getters
	public int getValor() {
		return valor;
	}
	public void setValor(int valor) {
		this.valor = valor;
	}
	public Estudiante getEstudiante() {
		return estudiante;
	}
	public void setEstudiante(Estudiante estudiante) {
		this.estudiante = estudiante;
	}
	public boolean isPagada() {
		return pagada;
	}
	public void setPagada(boolean pagada) {
		this.pagada = pagada;
	}
	public String getCodigo() {
		return codigo;
	}
	public void setCodigo(String codigo) {
		this.codigo = codigo;
	}
	
	
}
