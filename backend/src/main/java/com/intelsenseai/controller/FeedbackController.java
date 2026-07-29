package com.intelsenseai.controller;

import com.intelsenseai.dto.FeedbackRequest;
import com.intelsenseai.entity.Feedback;
import com.intelsenseai.service.FeedbackService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/feedback")
public class FeedbackController {

    private final FeedbackService feedbackService;

    public FeedbackController(FeedbackService feedbackService) {
        this.feedbackService = feedbackService;
    }

    @PostMapping
    public ResponseEntity<Feedback> submit(@RequestBody FeedbackRequest request) {
        Feedback saved = feedbackService.submitFeedback(request.getText(), request.getSource());
        return ResponseEntity.ok(saved);
    }
}
