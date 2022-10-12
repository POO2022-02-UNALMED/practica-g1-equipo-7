package gestorAplicacion.paquete2;

import gestorAplicacion.paquete1.*;
import java.util.*;

public class Salon extends Bloque {
	private ArrayList<Estudiante> Estudiantes = new ArrayList<Estudiante>();
	private int curso;
	private Profesor profesorAsignado;
	
	//Constructores
	public Salon() {
		
	}
	
	public Salon(int capacidad,int id,ArrayList<Estudiante> estudiantes, int curso, Profesor profesorAsignado) {
		super(capacidad, id);
		Estudiantes = estudiantes;
		this.curso = curso;
		this.profesorAsignado = profesorAsignado;
	}
	//setters y getters
	public ArrayList<Estudiante> getEstudiantes() {
		return Estudiantes;
	}
	public void setEstudiantes(ArrayList<Estudiante> estudiantes) {
		Estudiantes = estudiantes;
	}
	public int getCurso() {
		return curso;
	}
	public void setCurso(int curso) {
		this.curso = curso;
	}
	public Profesor getProfesorAsignado() {
		return profesorAsignado;
	}
	public void setProfesorAsignado(Profesor profesorAsignado) {
		this.profesorAsignado = profesorAsignado;
	}
	
	//metodos
	public float promedioCurso() {
		float prom = 0;
		for(int i=0;i<this.Estudiantes.size();i++) {
			prom+=this.Estudiantes.get(i).getPromedio();
		}
		
		return(prom/this.Estudiantes.size());
	}
	
	//metodos abstractos
	public void mejorarCapacidad() {
		this.setCapacidad(this.getCapacidad()+2);
	}
}
