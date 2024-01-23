def timecode_to_seconds(timecode, frame_rate):
    # Convert timecode to seconds
    hh, mm, ss, ff = map(int, timecode.split(':'))
    total_frames = (hh * 3600 + mm * 60 + ss) * frame_rate + ff
    seconds = total_frames / frame_rate
    return seconds

def calculate_time_difference(file_start_timecode, error_start_time, frame_rate):
    # Convert timecodes to seconds
    file_start_seconds = timecode_to_seconds(file_start_timecode, frame_rate)
    error_start_seconds = timecode_to_seconds(error_start_time, frame_rate)

    # Calculate the time difference
    time_difference_seconds = error_start_seconds - file_start_seconds

    # Calculate the corresponding frames
    frame_difference = int(time_difference_seconds * frame_rate)

    return time_difference_seconds, frame_difference

def convert_to_hh_mm_ss_ms(time_difference_seconds):
    # Convert time difference to hh:mm:ss:ms format
    total_seconds = int(time_difference_seconds)
    ms = int((time_difference_seconds - total_seconds) * 1000)

    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    return f"{hours:02d}:{minutes:02d}:{seconds:02d}:{ms:03d}"

while True:
    # Get input from the user
    file_start_timecode = input("Enter the start timecode of the file (hh:mm:ss:ff) or 'exit' to quit: ")

    # Check if the user wants to exit
    if file_start_timecode.lower() == 'exit':
        print("Exiting the program. Goodbye!")
        break

    error_start_time = input("Enter the start time of the error (hh:mm:ss:ff): ")
    frame_rate = float(input("Enter the frame rate of the file: "))

    # Calculate and display the difference
    time_difference, frame_difference = calculate_time_difference(file_start_timecode, error_start_time, frame_rate)
    print(f"\nTime Difference: {time_difference} seconds")
    print(f"Frame Difference: {frame_difference} frames")

    # Ask if the user wants to convert to hh:mm:ss:ms
    convert_choice = input("Do you want to convert the time difference to hh:mm:ss:ms format? (yes/no): ").lower()
    if convert_choice in {'yes', 'y'}:
        hh_mm_ss_ms_result = convert_to_hh_mm_ss_ms(time_difference)
        print(f"Time Difference (hh:mm:ss:ms): {hh_mm_ss_ms_result}")

    print("\n---\n")
