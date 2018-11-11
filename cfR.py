import requests

subscription_key = "7529be7464ce482485e0e7c1896cca0e"
assert subscription_key

face_api_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect'

headers = {'Content-Type': 'application/octet-stream', 'Ocp-Apim-Subscription-Key': subscription_key}
params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,' +
    'emotion,hair,makeup,occlusion,accessories,blur,exposure,noise'
}

def frCheck(img):
    data = img
    response = requests.post(face_api_url, params=params, headers=headers, data=data)
    faces = response.json()

    threatScore = 0
    threatWeights = {'happiness': -3, "neutral": -1, "sadness": 5, "contempt": 6, "surprise": 15, "disgust": 15, 'fear': 25, 'anger':25}
    emotionAverage = {'happiness': 0, "neutral": 0, "sadness": 0, "contempt": 0, "surprise": 0, "disgust": 0, 'fear': 0, 'anger':0}

    faceCount = len(faces)
    emotions = []
    for f in faces:
        print(faces)
        es = faces[0]['faceAttributes']['emotion']
        for e in es:
            em = es[e]
            if em > 0:
                emotionAverage[e] += em

    for e in emotionAverage:
        if emotionAverage[e] > 0:
            threatScore += threatWeights[e] * emotionAverage[e]/faceCount

    print(faces)
    return threatScore




