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
    df_vpoly_prop = pd.read_pickle("/home/olivera/Documents/data/vpoly_properties_update.pkl")
    #print(df_vpoly_prop)

    #df_urban_profile = pd.read_pickle("/home/olivera/Documents/data/urban_profile.pkl")
    #print(df_urban_profile)
    df_vpoly_prop.to_csv("/home/olivera/Documents/data/vpoly_properties_updates.csv")
    #df_urban_profile.to_csv("/home/olivera/Documents/data/urban_profile.csv")

    #add_col(df_urban_profile)
    #df_urban_profile.to_pickle("/home/olivera/Documents/data/urban_profile1.pkl")

if __name__ == '__main__':
    main()