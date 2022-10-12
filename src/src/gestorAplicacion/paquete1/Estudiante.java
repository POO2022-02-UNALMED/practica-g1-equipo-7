package gestorAplicacion.paquete1;

import gestorAplicacion.paquete2.*;
import java.util.*;
public class Estudiante extends Persona {
	private int anoCurso;
	private String jornada;
	private Matricula matricula;
	private boolean estadoMatricula;
	private ArrayList <Materia> materias = new ArrayList<Materia>();
	private Salon salon;
	private float promedio;
	
	//Constructores 
	public Estudiante() {
		
	}
	
	public Estudiante(String nombre, int id, int edad,int anoCurso, String jornada, Matricula matricula, boolean estadoMatricula, ArrayList<Materia> materias, Salon salon, float promedio) {
		super(nombre, id, edad);
		this.anoCurso = anoCurso;
		this.jornada = jornada;
		this.matricula = matricula;
		this.estadoMatricula = estadoMatricula;
		this.materias = materias;
		this.salon = salon;
		this.promedio = promedio;
	}
	
	//setters y getters 
	public int getAnoCurso() {
		return anoCurso;
	}
	public void setAnoCurso(int anoCurso) {
		this.anoCurso = anoCurso;
	}
	public String getJornada() {
		return jornada;
	}
	public void setJornada(String jornada) {
		this.jornada = jornada;
	}
	public Matricula getMatricula() {
		return matricula;
	}
	public void setMatricula(Matricula matricula) {
		this.matricula = matricula;
	}
	public boolean isEstadoMatricula() {
		return estadoMatricula;
	}
	public void setEstadoMatricula(boolean estadoMatricula) {
		this.estadoMatricula = estadoMatricula;
	}
	public ArrayList<Materia> getMaterias() {
		return materias;
	}
	public void setMaterias(ArrayList<Materia> materias) {
		this.materias = materias;
	}
	public Salon getSalon() {
		return salon;
	}
	public void setSalon(Salon salon) {
		this.salon = salon;
	}
	public float getPromedio() {
		return promedio;
	}
	public void setPromedio(float promedio) {
		this.promedio = promedio;
	}
	
	//metodos
	
}
