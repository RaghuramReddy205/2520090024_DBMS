package com.example.studentmanagement.service;

import com.example.studentmanagement.entity.Student;
import com.example.studentmanagement.repository.StudentRepository;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class StudentService {

    private final StudentRepository repository;

    public StudentService(StudentRepository repository) {
        this.repository = repository;
    }

    // Create Student
    public Student create(Student student) {
        return repository.save(student);
    }

    // Read All Students
    public List<Student> getAll() {
        return repository.findAll();
    }

    // Read One Student by ID
    public Optional<Student> getById(Long id) {
        return repository.findById(id);
    }

    // Update Student
    public Student update(Long id, Student data) {
        Student student = repository.findById(id)
                .orElseThrow(() -> new RuntimeException("Student not found with id: " + id));

        student.setName(data.getName());
        student.setDepartment(data.getDepartment());
        student.setEmail(data.getEmail());

        return repository.save(student);
    }

    // Delete Student
    public void delete(Long id) {
        repository.deleteById(id);
    }
}