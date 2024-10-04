import os

# getting a directory as an input from user
directory_path = 'C:/Users/Amin/OneDrive/Desktop/project2/monitor' # /content/txt_files

# Initiation step
# status = {}
status = dict()
for file_name in os.listdir(directory_path):
    file_path = os.path.join(directory_path, file_name)
    file_creation_time = os.path.getctime(file_path)
    file_modification_time = os.path.getmtime(file_path)
    status[file_path] = {'creation_time': file_creation_time, 'modification_time': file_modification_time}



# Program realtime
while True:
    try:
        files_write = []
        for file_name in os.listdir(directory_path):
            #if len(file_name.split('.')) < 2:
             #   continue # This file_name actualy is a folder.
            file_path = os.path.join(directory_path, file_name)
            if file_path not in list(status.keys()): # New file created
                status[file_path] = {'creation_time': os.path.getctime(file_path), 'modification_time': os.path.getmtime(file_path)}
                text = f"File created: {file_name}\n"
                files_write.append(text)

            elif status[file_path]['modification_time'] != os.path.getmtime(file_path): # File modified
                status[file_path]['modification_time'] = os.path.getmtime(file_path)
                text = f"File modified: {file_name}\n"
                files_write.append(text)

        for key in list(status.keys()):
            file_name = key.split('/')[-1]
            if file_name not in os.listdir(directory_path): # File deleted
                text = f"File deleted: {file_name}\n"
                files_write.append(text)
                del status[key]


        with open('log.txt', 'a') as f:
            for line in files_write:
                f.write(line)
        # sleep(2)
    except Exception as e:
        print(f"Error occured: {e}")
        break