package gestorAplicacion.paquete2;

import gestorAplicacion.paquete1.*;
import java.util.*;
public class Restaurante extends Bloque{
	private Map<String, String> menuDiario = new HashMap<String, String>();
	private ArrayList<Estudiante> estudiantesPAE = new ArrayList<Estudiante>();
	
	
	//Constructor 
	
	
	public Restaurante() {
		
	}
	
	public Restaurante(int capacidad, int id, Map<String, String> menuDiario, ArrayList<Estudiante> estudiantesPAE) {
		super(capacidad, id);
		this.menuDiario = menuDiario;
		this.estudiantesPAE = estudiantesPAE;
	}
	
	//setters y  getters
	public Map<String, String> getMenuDiario() {
		return menuDiario;
	}
	
	public void setMenuDiario(Map<String, String> menuDiario) {
		this.menuDiario = menuDiario;
	}
	public ArrayList<Estudiante> getEstudiantesPAE() {
		return estudiantesPAE;
	}
	public void setEstudiantesPAE(ArrayList<Estudiante> estudiantesPAE) {
		this.estudiantesPAE = estudiantesPAE;
	}
	
	//metodos
	
	
	//metodos abstractos
	
	public void mejorarCapacidad() {
		this.setCapacidad(getCapacidad()+2);
	}
	
	
}
