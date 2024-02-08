from datetime import datetime, time


def main():
    print("The Timer Program\n")

    # Start the timer
    input("Press Enter to start...")
    start_time = datetime.now()
    print("Start Time: ", start_time)
    print()

    # Stop the timer
    input("Press Enter to stop...")
    end_time = datetime.now()
    print("End Time: ", end_time)
    print()

    # calculating elapsed time
    elapsed_time = end_time - start_time
    print("Elapsed time:", elapsed_time)

main()
