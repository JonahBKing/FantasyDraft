import pandas as pd
pd.options.display.width = 0
import os

qb = pd.read_csv('./Projections/FantasyPros_Fantasy_Football_Projections_QB.csv')
qb = qb[qb.FPTS != 0]
qb.insert(2, column="Position", value="QB")
qb_move = qb.pop("FPTS")
qb.insert(3, "FPTS", qb_move)
qb.insert(4, column="abv_avg", value=(qb.FPTS - qb.FPTS.mean()))
qb.insert(5, column="SD_abv_avg", value=(qb.abv_avg/qb.FPTS.std()))
qb.insert(6, column="SD_over_next", value=((qb.abv_avg - qb.abv_avg.shift(-1))/qb.FPTS.std()))
qb.insert(7, column="SD_over_next_5", value=((qb.FPTS-qb.FPTS.rolling(5).mean().shift(-5))
                                             / qb.FPTS.rolling(5).std().shift(-5)))

print(qb.head(10))
##########################################
rb = pd.read_csv('./Projections/FantasyPros_Fantasy_Football_Projections_RB.csv')
rb.insert(2, column="Position", value="RB")
rb_move = rb.pop("FPTS")
rb.insert(3, "FPTS", rb_move)
rb.insert(4, column="abv_avg", value=(rb.FPTS - rb.FPTS.mean()))
rb.insert(5, column="SD_abv_avg", value=(rb.abv_avg/rb.FPTS.std()))

#print(rb.head())


wr = pd.read_csv('./Projections/FantasyPros_Fantasy_Football_Projections_WR.csv')
wr.insert(2, column="Position", value="WR")

te = pd.read_csv('./Projections/FantasyPros_Fantasy_Football_Projections_TE.csv')
te.insert(2, column="Position", value="TE")

k = pd.read_csv('./Projections/FantasyPros_Fantasy_Football_Projections_K.csv')
k.insert(2, column="Position", value="K")


files = [file for file in os.listdir('./Projections')]

all_data = pd.DataFrame()

for file in files:
    df = pd.read_csv('./Projections/'+file)
    all_data = pd.concat([all_data, df])

all_data.to_csv("all_data.csv", index=False)