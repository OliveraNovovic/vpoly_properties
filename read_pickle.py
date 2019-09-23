import pandas as pd

def add_col(df):
    new_col = []
    for i in range(1, 314):
        name = "poly_" + str(i)
        new_col.append(name)
    idx = 0
    df.insert(loc=idx, column='poly_name', value=new_col)

def main():
    pd.set_option('display.max_columns', 999)
    df = pd.read_pickle("/home/olivera/Documents/data/vpoly_properties.pkl")
    df_urban_profile = pd.read_pickle("/home/olivera/Documents/data/urban_profile.pkl")
    print(df_urban_profile)

    #add_col(df_urban_profile)
    #df_urban_profile.to_pickle("/home/olivera/Documents/data/urban_profile1.pkl")

if __name__ == '__main__':
    main()