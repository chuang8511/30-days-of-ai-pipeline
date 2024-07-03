import streamlit as st
import requests
import base64
import json

# api_token = " "
api_token = st.text_input("Instill AI API token", type="password")
url = 'https://api.instill.tech/v1beta/users/chunhao094/pipelines/automatic-key/trigger'

def image_to_base64(image):
    return base64.b64encode(image.read()).decode('utf-8')
st.title('Image Upload and API Trigger')
uploaded_file = st.file_uploader("Choose an image", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    # Convert uploaded image to base64
    image_base64 = image_to_base64(uploaded_file)
    
    # Display the image
    st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)
    
    # Prepare the payload
    payload = {
        "inputs": [
            {
                "image": image_base64
            }
        ]
    }
    
    # Display the payload (for debugging purposes)
    st.write(payload)
    
    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_token}'
    }
    
        # Make the API request
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    
    # Display the response
    if response.status_code == 200:
        st.success("API triggered successfully!")
        st.json(response.json())

        # process simplified business logic
        object_detection_results = response.json()["outputs"][0]["result"]
        people_count = 0
        book_count = 0
        for object_detection_result in object_detection_results:
            if object_detection_result["score"] > 0.75:
                if object_detection_result["category"] == "person":
                    people_count += 1
                elif object_detection_result["category"] == "book":
                    book_count += 1

        if people_count != 2 and book_count != 1:
            st.write("This upload should auto-reject because the image does not follow the principal")
            


    else:
        st.error("Failed to trigger API")
        st.write(response.text)
        
