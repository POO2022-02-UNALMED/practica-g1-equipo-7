package paquete1;

public class Persona {
	private String nombre;
	private int id;
	private int edad;
	
	
	//Constructores
	public Persona() {
		
	}
	public Persona(String nombre, int id, int edad) {
		this.nombre = nombre;
		this.id = id;
		this.edad = edad;
	}
	//metodos set y get
	public String getNombre() {
		return nombre;
	}
	public void setNombre(String nombre) {
		this.nombre = nombre;
	}
	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public int getEdad() {
		return edad;
	}
	public void setEdad(int edad) {
		this.edad = edad;
	}
	
	
	//metodos de la clase
	
}