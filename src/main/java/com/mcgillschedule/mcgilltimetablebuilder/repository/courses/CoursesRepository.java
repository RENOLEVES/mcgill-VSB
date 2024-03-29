package com.mcgillschedule.mcgilltimetablebuilder.repository.courses;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import com.mcgillschedule.mcgilltimetablebuilder.model.mysql.Courses;

import java.util.List;


@Repository
public interface CoursesRepository extends JpaRepository<Courses, Integer>{
    @Query("SELECT c FROM Courses c WHERE courseCode LIKE %?1%")
    List<RelevantCourse> findAllRelevantCourse(String info);

    @Query("SELECT c.courseId FROM Courses c WHERE c.courseCode = ?1 AND (c.sectionCode LIKE %?2% OR c.sectionCode LIKE '%Y%')")
    String findMatchCourseId(String CourseCode, String SectionCode);

}