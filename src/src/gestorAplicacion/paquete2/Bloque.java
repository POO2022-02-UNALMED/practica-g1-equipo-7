package paquete2;

public abstract class Bloque {
	private int capacidad;
	private int id;
	
	
	public Bloque() {
		
	}
	
	public Bloque(int capacidad, int id) {
		this.capacidad = capacidad;
		this.id = id;
	}
	
	//setters y getters
	public int getCapacidad() {
		return capacidad;
	}
	public void setCapacidad(int capacidad) {
		this.capacidad = capacidad;
	}
	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	
	//metodo abstracto
	abstract void mejorarCapacidad();
	
}
