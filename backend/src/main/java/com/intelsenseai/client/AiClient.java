package com.intelsenseai.client;

import com.intelsenseai.service.JwtService;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.util.Map;

@Service
public class AiClient {

    private final RestTemplate restTemplate;
    private final String baseUrl;
    private final JwtService jwtService;

    public AiClient(@Value("${ai.service.base-url}") String baseUrl, JwtService jwtService) {
        this.baseUrl = baseUrl;
        this.jwtService = jwtService;
        this.restTemplate = new RestTemplate();
    }

    public Map<String, Object> predict(String text, String source) {
        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);
        headers.set("Authorization", "Bearer " + jwtService.generateToken("backend-service"));
        Map<String, Object> body = Map.of("text", text, "source", source);
        HttpEntity<Map<String, Object>> request = new HttpEntity<>(body, headers);
        return restTemplate.postForObject(baseUrl + "/predict", request, Map.class);
    }
}
