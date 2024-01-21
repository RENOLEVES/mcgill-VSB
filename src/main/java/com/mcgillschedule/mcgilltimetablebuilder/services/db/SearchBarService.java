package com.mcgillschedule.mcgilltimetablebuilder.services.db;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.mcgillschedule.mcgilltimetablebuilder.repository.courses.CoursesRepository;
import com.mcgillschedule.mcgilltimetablebuilder.repository.courses.RelevantCourse;

@Service
public class SearchBarService {
    
    @Autowired
    private CoursesRepository coursesRepository;

    public List<RelevantCourse> getRelevantCoursesInfo(String info){
        List<RelevantCourse> course = coursesRepository.findAllRelevantCourse(info);
        return course;
    }

}