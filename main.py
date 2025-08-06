
#             print("👋 Exiting...")
#             break

#         run_analysis(choice, cursor)

#     cursor.close()
#     conn.close()

# if __name__ == "__main__":
#     main()
# File: main.py

# File: main.py

import pandas as pd
from data_base.db_config import connect_db
from data_base.db_load import load_data_to_mysql
from analysis.analysis_functions import run_analysis, show_menu

def main():
    # Step 1: Load dataset
    df = pd.read_csv("data/IMDB-Movie-Data.csv")

    # Step 2: Clean data
    df.columns = [col.strip().replace(' ', '_').replace('(', '').replace(')', '') for col in df.columns]
    df.drop_duplicates(inplace=True)
    df.fillna({
        'Revenue_Millions': df['Revenue_Millions'].mean(),
        'Metascore': df['Metascore'].mean()
    }, inplace=True)
    df.dropna(inplace=True)

    # Step 3: Load to MySQL
    load_data_to_mysql(df)

    # Step 4: Connect to MySQL
    conn = connect_db()
    cursor = conn.cursor()

    while True:
        show_menu()
        choice = input("Enter your choice (0 to exit): ")

        if choice == "0":
            print("👋 Exiting...")
            break

        run_analysis(choice, cursor)

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()