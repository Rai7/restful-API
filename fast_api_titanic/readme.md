To test the `/titanic` endpoint in Postman, you can follow these steps:

1. **Launch Postman**: Open the Postman application.

2. **Create a new request**:
   - Click on the "New" button in the top-left corner.
   - Select "Request" to create a new request.

3. **Set request details**:
   - Choose the request type as POST.
   - Enter the URL where your FastAPI server is running, followed by `/titanic`. For example, `http://localhost:8000/titanic`.

4. **Set request headers**:
   - If your endpoint expects headers, you can add them here. In this case, there are no specific headers required.

5. **Set request body**:
   - Select the "Body" tab.
   - Choose "JSON" as the format.
   - Enter your test data in JSON format. The JSON should match the structure defined by the `TitanicData` Pydantic model.
     For example:
     ```json
     {
       "passanger_class": 1,
       "gender": "female",
       "age": 25,
       "sibling_spouse": 1,
       "parent_children": 0,
       "fare": 100
     }
     ```

6. **Send the request**:
   - Click on the "Send" button to send the request.

7. **View the response**:
   - Postman will display the response received from your FastAPI server. You should see the predicted result along with the label name.

By following these steps, you can use Postman to test your FastAPI `/titanic` endpoint by sending POST requests with different sets of input data. Adjust the input data according to your testing requirements.