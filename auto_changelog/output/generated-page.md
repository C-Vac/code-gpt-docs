
### **Completion**
- The /completion endpoint in the CodeGPT API is designed for user interaction with an AI Agent. To use this endpoint, you send a POST request with a structured JSON object in the body and your API Key in the header.

**Params:** 
- agentId: string - agentId
- messages: json 
- format: string - "text" or "json"(Default)
- stream: boolean - false or true(Default)


```shell 
curl --request POST \
     --url https://api-beta.codegpt.co/api/v1/chat/completions \
     --header 'accept: application/json' \
     --header 'authorization: Bearer {{apiToken}}' \
     --header 'content-type: application/json' \
```

#### Example response from current docs:
```json
{
 
  "agentId": "0000-0000-0000-0000",
  "stream":true,
  "format":"json"
  "messages":
  [{
    "content": "What is the meaning of life?",
    "role": "user"
  }]
}
```
#### My response using curl:
```json
{}
```

### **List Agents**
- The List function in an AI agents API is useful for obtaining a general overview of the available AI agents, their features, and capabilities, making it easier to select the most suitable agent for a specific task or application.

**Params:** 


```shell 
curl --request GET \
     --url https://api-beta.codegpt.co/api/v1/agent \
     --header 'accept: application/json' \
     --header 'authorization: Bearer {{apiToken}}' \
```

#### Example response from current docs:
```json
[
  {
    "status": "published",
    "name": "Agent 1",
    "documentId": [],
    "description": "Description of the agent",
    "prompt": "You are a helpful assistant",
    "topk": 3,
    "temperature": 0.7,
    "model": "gpt-3.5-turbo",
    "welcome": "Hello, how can I help you?",
    "maxTokens": 1024,
    "id": "0000-0000-0000-0000",
    "user_created": "0000-0000-0000-0000",
    "date_created": "2023-01-01T12:00:00.000Z"
  }
]
```
#### My response using curl:
```json
{}
```

