package com.intelsenseai.service;

import com.intelsenseai.client.AiClient;
import com.intelsenseai.entity.Feedback;
import com.intelsenseai.repository.FeedbackRepository;
import org.springframework.stereotype.Service;

import java.util.Map;

@Service
public class FeedbackService {

    private final FeedbackRepository feedbackRepository;
    private final AiClient aiClient;

    public FeedbackService(FeedbackRepository feedbackRepository, AiClient aiClient) {
        this.feedbackRepository = feedbackRepository;
        this.aiClient = aiClient;
    }

    public Feedback submitFeedback(String text, String source) {
        Map<String, Object> aiResponse = aiClient.predict(text, source);
        Feedback feedback = new Feedback();
        feedback.setText(text);
        feedback.setSource(source);
        feedback.setAiResult(aiResponse.toString());
        return feedbackRepository.save(feedback);
    }
}
