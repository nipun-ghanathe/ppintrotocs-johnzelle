# avg2.py
# A simple program to average two exam scores


def main():
    print("This program computes the average of given exam scores.\n")

    scores = input("Enter your exam scores separated by a comma: ").split(",")
    num = len(scores)
    scores = map(float, scores)
    average = sum(scores) / num
    print(f"The average of the scores is {average:.1f}")


main()
