def main():
    test(8,000,000, 3,000,000)
    test(10,000,000, 4,500,000)


# Don't edit below this line


def calculate_male_ratio(num_fruit_bats, num_male_bats):
    return num_male_bats / num_fruit_bats


def test(num_fruit_bats, num_male_bats):
    ratio = calculate_male_ratio(num_fruit_bats, num_male_bats)
    print(f"{ratio * 100}% of fruit bats are male")
    print("=====================================")


main()
