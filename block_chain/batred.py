
import pickle
with open("known_faces.dat", "rb") as face_data_file:
    known_face_encodings, known_face_metadata = pickle.load(face_data_file)
    print(known_face_metadata)
    print("Known faces loaded from disk.")
