package paquete1;

import paquete2.*;
import java.util.*;
public class Profesor extends Persona{
	private Salon salonAsignado;
	private String jornada;
	private ArrayList<Materia> materias = new ArrayList<Materia>();
	private int salario;
	
	//Constructor
	
	public Profesor() {
		
	}
	public Profesor(String nombre,int id,int edad,Salon salonAsignado, String jornada, ArrayList<Materia> materias, int salario) {
		super(nombre, id, edad);
		this.salonAsignado = salonAsignado;
		this.jornada = jornada;
		this.materias = materias;
		this.salario = salario;
	}
	//setters y getters
	public Salon getSalonAsignado() {
		return salonAsignado;
	}
	public void setSalonAsignado(Salon salonAsignado) {
		this.salonAsignado = salonAsignado;
	}
	public String getJornada() {
		return jornada;
	}
	public void setJornada(String jornada) {
		this.jornada = jornada;
	}
	public ArrayList<Materia> getMaterias() {
		return materias;
	}
	public void setMaterias(ArrayList<Materia> materias) {
		this.materias = materias;
	}
	public int getSalario() {
		return salario;
	}
	public void setSalario(int salario) {
		this.salario = salario;
	} 
	
	//metodos
	
	
}
