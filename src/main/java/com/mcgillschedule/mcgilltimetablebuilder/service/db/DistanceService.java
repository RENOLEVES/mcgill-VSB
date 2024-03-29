package com.mcgillschedule.mcgilltimetablebuilder.service.db;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import com.mcgillschedule.mcgilltimetablebuilder.repository.distance.DistancesRepository;

@Service
public class DistanceService {

    @Autowired
    private DistancesRepository distancesRepository;

    public Integer getDistance(String origin, String destination) {

        Integer distance = distancesRepository.findDistanceByLocation(origin, destination);
        return distance != null ? distance : -1; // 如果未找到距离，返回 -1
        
    }

    public Integer getDuration(String origin, String destination){
        Integer duration = distancesRepository.findDurationByLocation(origin, destination);
        return duration != null ? duration : -1; // 如果未找到时间，返回 -1
    }
}