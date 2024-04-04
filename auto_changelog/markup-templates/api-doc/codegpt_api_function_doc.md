
### **{{functionName}}**
- {{description}}

**Params:** 
{% for param in params %}
- {{param.name}}: {{param.type}}{% if param.description %} - {{param.description}}{% endif %}
{% endfor %}


```shell 
curl --request {{apiCall.method}} \
     --url {{apiCall.endpoint}} \
{% for header in apiCall.headers %}
     --header '{{header.key}}: {{header.value}}' \
{% endfor %}
```

#### Example response from current docs:
```json
{{exampleResponse}}
```
#### My response using curl:
```json
{{userResponse}}
```

////END
