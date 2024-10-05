import pandas as pd

def main():
    # Read data from a CSV file
    df = pd.read_csv('data.csv')
    print("Original Data:")
    print(df.head())

    # Perform data manipulation
    df['new_column'] = df['existing_column'] * 2
    print("\nModified Data:")
    print(df.head())

    # Save the modified data to a new CSV file
    df.to_csv('modified_data.csv', index=False)
    print("\nModified data saved to 'modified_data.csv'")

if __name__ == "__main__":
    main()
