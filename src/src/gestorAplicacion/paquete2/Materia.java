package gestorAplicacion.paquete2;

public class Materia {
	private String nombre;
	private float nota;
	
	//Constructores
	public Materia() {
		
	}
	
	public Materia(String nombre, float nota) {
		this.nombre = nombre;
		this.nota = nota;
	}
	//setters y getters
	public String getNombre() {
		return nombre;
	}
	public void setNombre(String nombre) {
		this.nombre = nombre;
	}
	public float getNota() {
		return nota;
	}
	public void setNota(float nota) {
		this.nota = nota;
	}
	
	
	
}
