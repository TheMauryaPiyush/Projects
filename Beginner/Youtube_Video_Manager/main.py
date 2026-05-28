import json

# Display all videos in the list
def list_all_videos(videos):
    print("\n")
    print("*" * 40)
    
    # Loop through videos with numbering
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']}")
    
    print("*" * 40)
        

# Add a new video to the list
def add_videos(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    
    # Append new video as dictionary
    videos.append({'name': name, 'time': time})
    
    # Save updated data to file
    save_data_helper(videos)


# Update an existing video
def update_videos(videos):
    index = int(input("Enter the video number you want to update : "))
    
    # Check valid index
    if 1 <= index <= len(videos):
        name = input("New video name : ")
        time = input("New video time : ")
        
        # Replace existing entry
        videos[index - 1] = {'name': name, 'time': time}
        
        save_data_helper(videos)
    else:
        print("Not available")


# Delete a video from the list
def delete_videos(videos):
    list_all_videos(videos)
    
    index = int(input("Enter the video number you want to delete : "))
    
    # Validate index before deleting
    if 1 <= index <= len(videos):
        del videos[index - 1]
        save_data_helper(videos)
    else:
        print("Not available")


# Load data from file (JSON format stored in .txt)
def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            # Read JSON data from file
            test = json.load(file)
            return test
    except FileNotFoundError:
        # If file doesn't exist, return empty list
        return []


# Save videos data to file
def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)


# Main program loop
def main():
    videos = load_data()
    
    while True:
        print("\n YouTube Manager")
        print("1. List all youtube videos")
        print("2. Add a youtube video")
        print("3. Update your youtube video")
        print("4. Delete a youtube video")
        print("5. Exit the app")
        
        choice = input("enter your choice: ")

        # Menu handling using match-case
        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_videos(videos)
            case '3':
                update_videos(videos)
            case '4':
                delete_videos(videos)
            case '5':
                print("Thankyou")
                break
            case _:
                print("Invalid choice")


# Entry point of program
if __name__ == "__main__":
    main()
