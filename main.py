import face_recognition
import sys
import os

def main():
    if len(sys.argv) != 3:
        print("Use case: python3 main.py {initialImage} {imageDirectory}")
        return

    initial_image = sys.argv[1]
    images_directory = sys.argv[2]

    # Validate the directory
    files = process_directory(images_directory)
    if not files:
        print("Invalid directory provided in the second argument.")
        return

    # Process the image to be compared to the directory
    image1_encodings = recognized_faces(initial_image)
    if not image1_encodings:
        print(f"No faces found in {initial_image}.")
        return

    for image_file in files:
        image_path = os.path.join(images_directory, image_file)
        image2_encodings = recognized_faces(image_path)
        if not image2_encodings:
            print(f"No faces found in {image_file}, skipping.")
            continue

        for image2_encoding in image2_encodings:
            result = face_recognition.compare_faces(image1_encodings, image2_encoding)
            if any(result):
                print(f"Photos match. {image_file} is a match to the provided person.")

def process_directory(directory_path):
    if os.path.isdir(directory_path):
        valid_extensions = ('.jpg', '.jpeg', '.png')
        files = [f for f in os.listdir(directory_path) if f.lower().endswith(valid_extensions)]
        return files
    return False

def recognized_faces(image_file):
    image = face_recognition.load_image_file(image_file)

    face_encodings = face_recognition.face_encodings(image)
    return face_encodings

if __name__ == "__main__":
    main()

