import os

def rename_images(folder_path):
    # Get a list of all files in the folder
    files = os.listdir(folder_path)
    
    # Filter the list to include only files with image extensions
    image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff')
    images = [file for file in files if file.lower().endswith(image_extensions)]
    
    # Sort the images to maintain a consistent order
    images.sort()
    
    # Rename each image to a temporary name to avoid conflicts
    temp_names = []
    for index, image in enumerate(images, start=1):
        # Get the file extension
        extension = os.path.splitext(image)[1]
        
        # Define the temporary name
        temp_name = f"temp_{index}{extension}"
        
        # Define the full path for the old and temporary names
        old_path = os.path.join(folder_path, image)
        temp_path = os.path.join(folder_path, temp_name)
        
        # Rename the file to the temporary name
        os.rename(old_path, temp_path)
        temp_names.append(temp_name)
    
    # Rename each image from the temporary name to the final name
    for index, temp_name in enumerate(temp_names, start=1):
        # Get the file extension
        extension = os.path.splitext(temp_name)[1]
        
        # Define the final name
        final_name = f"{index}{extension}"
        
        # Define the full path for the temporary and final names
        temp_path = os.path.join(folder_path, temp_name)
        final_path = os.path.join(folder_path, final_name)
        
        # Rename the file to the final name
        os.rename(temp_path, final_path)
    
    print(f"Renamed {len(images)} images successfully.")

# Example usage
folder_path = r'D:\folk art dataset\Tikuli Art (Bihar)'
rename_images(folder_path)
