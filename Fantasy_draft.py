import pandas as pd
pd.options.display.width = 0
import os
import re

drafted = []
nones = ['na', 'n', 'none', 'noone', ' ' ,'']

for i in range(0, 150):
    element = input("Who was picked: ").lower()
    if element.lower() in nones:
        pass
    else:
        drafted.append(element)
    turn = input("Is it your turn (Y/N/Q if finished)?: ")
    if turn.lower() == "n":
        continue
    elif turn.lower() == "q":
        print(drafted)
        break
    elif turn.lower() == "y":
        need = input("What position do you need (ALL,QB,RB,WR,FLEX,TE,K)?: ")
        if need.lower() == "qb":
            qb = pd.read_csv('./Projections/FantasyPros_Fantasy_Football_Projections_QB.csv')
            qb = qb[~qb.Player.str.contains('|'.join(drafted), flags=re.IGNORECASE)]
            qb = qb[qb.FPTS != 0]
            qb.insert(2, column="Position", value="QB")
            qb_move = qb.pop("FPTS")
            qb.insert(3, "FPTS", qb_move)
            qb.insert(4, column="abv_avg", value=(qb.FPTS - qb.FPTS.mean()))
            qb.insert(5, column="SD_abv_avg", value=(qb.abv_avg / qb.FPTS.std()))
            qb.insert(6, column="SD_over_next", value=((qb.abv_avg - qb.abv_avg.shift(-1)) / qb.FPTS.std()))
            qb.insert(7, column="SD_over_next_5", value=((qb.FPTS - qb.FPTS.rolling(5).mean().shift(-5))
                                                         / qb.FPTS.rolling(5).std().shift(-5)))
            qb = qb[['Player', 'Team', 'Position', 'FPTS', 'abv_avg', 'SD_abv_avg', 'SD_over_next', 'SD_over_next_5']]
            print(qb.head(10))
        elif need.lower() == "rb":
            rb = pd.read_csv('./Projections/FantasyPros_Fantasy_Football_Projections_RB.csv')
            rb = rb[~rb.Player.str.contains('|'.join(drafted), flags=re.IGNORECASE)]
            rb = rb[rb.FPTS != 0]
            rb.insert(2, column="Position", value="RB")
            rb_move = rb.pop("FPTS")
            rb.insert(3, "FPTS", rb_move)
            rb.insert(4, column="abv_avg", value=(rb.FPTS - rb.FPTS.mean()))
            rb.insert(5, column="SD_abv_avg", value=(rb.abv_avg / rb.FPTS.std()))
            rb.insert(6, column="SD_over_next", value=((rb.abv_avg - rb.abv_avg.shift(-1)) / rb.FPTS.std()))
            rb.insert(7, column="SD_over_next_5", value=((rb.FPTS - rb.FPTS.rolling(5).mean().shift(-5))
                                                         / rb.FPTS.rolling(5).std().shift(-5)))
            rb = rb[['Player', 'Team', 'Position', 'FPTS', 'abv_avg', 'SD_abv_avg', 'SD_over_next', 'SD_over_next_5']]
            print(rb.head(10))
        elif need.lower() == "wr":
            wr = pd.read_csv('./Projections/FantasyPros_Fantasy_Football_Projections_WR.csv')
            wr = wr[~wr.Player.str.contains('|'.join(drafted), flags=re.IGNORECASE)]
            wr = wr[wr.FPTS != 0]
            wr.insert(2, column="Position", value="WR")
            wr_move = wr.pop("FPTS")
            wr.insert(3, "FPTS", wr_move)
            wr.insert(4, column="abv_avg", value=(wr.FPTS - wr.FPTS.mean()))
            wr.insert(5, column="SD_abv_avg", value=(wr.abv_avg / wr.FPTS.std()))
            wr.insert(6, column="SD_over_next", value=((wr.abv_avg - wr.abv_avg.shift(-1)) / wr.FPTS.std()))
            wr.insert(7, column="SD_over_next_5", value=((wr.FPTS - wr.FPTS.rolling(5).mean().shift(-5))
                                                         / wr.FPTS.rolling(5).std().shift(-5)))
            wr = wr[['Player', 'Team', 'Position', 'FPTS', 'abv_avg', 'SD_abv_avg', 'SD_over_next', 'SD_over_next_5']]
            print(wr.head(10))
        elif need.lower() == "te":
            te = pd.read_csv('./Projections/FantasyPros_Fantasy_Football_Projections_TE.csv')
            te = te[~te.Player.str.contains('|'.join(drafted), flags=re.IGNORECASE)]
            te = te[te.FPTS != 0]
            te.insert(2, column="Position", value="TE")
            te_move = te.pop("FPTS")
            te.insert(3, "FPTS", te_move)
            te.insert(4, column="abv_avg", value=(te.FPTS - te.FPTS.mean()))
            te.insert(5, column="SD_abv_avg", value=(te.abv_avg / te.FPTS.std()))
            te.insert(6, column="SD_over_next", value=((te.abv_avg - te.abv_avg.shift(-1)) / te.FPTS.std()))
            te.insert(7, column="SD_over_next_5", value=((te.FPTS - te.FPTS.rolling(5).mean().shift(-5))
                                                         / te.FPTS.rolling(5).std().shift(-5)))
            te = te[['Player', 'Team', 'Position', 'FPTS', 'abv_avg', 'SD_abv_avg', 'SD_over_next', 'SD_over_next_5']]
            print(te.head(10))
        elif need.lower() == "k":
            k = pd.read_csv('./Projections/FantasyPros_Fantasy_Football_Projections_K.csv')
            k = k[~k.Player.str.contains('|'.join(drafted), flags=re.IGNORECASE)]
            k = k[k.FPTS != 0]
            k.insert(2, column="Position", value="K")
            k_move = k.pop("FPTS")
            k.insert(3, "FPTS", k_move)
            k.insert(4, column="abv_avg", value=(k.FPTS - k.FPTS.mean()))
            k.insert(5, column="SD_abv_avg", value=(k.abv_avg / k.FPTS.std()))
            k.insert(6, column="SD_over_next", value=((k.abv_avg - k.abv_avg.shift(-1)) / k.FPTS.std()))
            k.insert(7, column="SD_over_next_5", value=((k.FPTS - k.FPTS.rolling(5).mean().shift(-5))
                                                        / k.FPTS.rolling(5).std().shift(-5)))
            k = k[['Player', 'Team', 'Position', 'FPTS', 'abv_avg', 'SD_abv_avg', 'SD_over_next', 'SD_over_next_5']]
            print(k.head(10))
        elif need.lower() == "flex":
            wr = pd.read_csv('./Projections/FantasyPros_Fantasy_Football_Projections_WR.csv')
            wr.insert(2, column="Position", value="WR")
            wr = wr[['Player', 'Team', 'Position', 'FPTS']]
            rb = pd.read_csv('./Projections/FantasyPros_Fantasy_Football_Projections_RB.csv')
            rb.insert(2, column="Position", value="RB")
            rb = rb[['Player', 'Team', 'Position', 'FPTS']]
            fx = [rb, wr]
            flex = pd.concat(fx)
            flex = flex[~flex.Player.str.contains('|'.join(drafted), flags=re.IGNORECASE)]
            flex = flex[flex.FPTS != 0]
            flex.insert(4, column="abv_avg", value=(flex.FPTS - flex.FPTS.mean()))
            flex.insert(5, column="SD_abv_avg", value=(flex.abv_avg / flex.FPTS.std()))
            flex.insert(6, column="SD_over_next", value=((flex.abv_avg - flex.abv_avg.shift(-1)) / flex.FPTS.std()))
            flex.insert(7, column="SD_over_next_5", value=((flex.FPTS - flex.FPTS.rolling(5).mean().shift(-5))
                                                         / flex.FPTS.rolling(5).std().shift(-5)))
            flex = flex[['Player', 'Team', 'Position', 'FPTS', 'abv_avg', 'SD_abv_avg', 'SD_over_next', 'SD_over_next_5']]
            flex = flex.sort_values(by='SD_abv_avg', ascending=False)
            print(flex.head(10))
        elif need.lower() == "all":
            qb = pd.read_csv('./Projections/FantasyPros_Fantasy_Football_Projections_QB.csv')
            qb = qb[qb.FPTS != 0]
            qb.insert(2, column="Position", value="QB")
            qb_move = qb.pop("FPTS")
            qb.insert(3, "FPTS", qb_move)
            qb.insert(4, column="abv_avg", value=(qb.FPTS - qb.FPTS.mean()))
            qb.insert(5, column="SD_abv_avg", value=(qb.abv_avg / qb.FPTS.std()))
            qb.insert(6, column="SD_over_next", value=((qb.abv_avg - qb.abv_avg.shift(-1)) / qb.FPTS.std()))
            qb.insert(7, column="SD_over_next_5", value=((qb.FPTS - qb.FPTS.rolling(5).mean().shift(-5))
                                                         / qb.FPTS.rolling(5).std().shift(-5)))
            qb = qb[['Player', 'Team', 'Position', 'FPTS', 'abv_avg', 'SD_abv_avg', 'SD_over_next', 'SD_over_next_5']]
            wr = pd.read_csv('./Projections/FantasyPros_Fantasy_Football_Projections_WR.csv')
            wr = wr[wr.FPTS != 0]
            wr.insert(2, column="Position", value="WR")
            wr_move = wr.pop("FPTS")
            wr.insert(3, "FPTS", wr_move)
            wr.insert(4, column="abv_avg", value=(wr.FPTS - wr.FPTS.mean()))
            wr.insert(5, column="SD_abv_avg", value=(wr.abv_avg / wr.FPTS.std()))
            wr.insert(6, column="SD_over_next", value=((wr.abv_avg - wr.abv_avg.shift(-1)) / wr.FPTS.std()))
            wr.insert(7, column="SD_over_next_5", value=((wr.FPTS - wr.FPTS.rolling(5).mean().shift(-5))
                                                         / wr.FPTS.rolling(5).std().shift(-5)))
            wr = wr[['Player', 'Team', 'Position', 'FPTS', 'abv_avg', 'SD_abv_avg', 'SD_over_next', 'SD_over_next_5']]
            rb = pd.read_csv('./Projections/FantasyPros_Fantasy_Football_Projections_RB.csv')
            rb = rb[rb.FPTS != 0]
            rb.insert(2, column="Position", value="RB")
            rb_move = rb.pop("FPTS")
            rb.insert(3, "FPTS", rb_move)
            rb.insert(4, column="abv_avg", value=(rb.FPTS - rb.FPTS.mean()))
            rb.insert(5, column="SD_abv_avg", value=(rb.abv_avg / rb.FPTS.std()))
            rb.insert(6, column="SD_over_next", value=((rb.abv_avg - rb.abv_avg.shift(-1)) / rb.FPTS.std()))
            rb.insert(7, column="SD_over_next_5", value=((rb.FPTS - rb.FPTS.rolling(5).mean().shift(-5))
                                                         / rb.FPTS.rolling(5).std().shift(-5)))
            rb = rb[['Player', 'Team', 'Position', 'FPTS', 'abv_avg', 'SD_abv_avg', 'SD_over_next', 'SD_over_next_5']]
            te = pd.read_csv('./Projections/FantasyPros_Fantasy_Football_Projections_TE.csv')
            te = te[te.FPTS != 0]
            te.insert(2, column="Position", value="TE")
            te_move = te.pop("FPTS")
            te.insert(3, "FPTS", te_move)
            te.insert(4, column="abv_avg", value=(te.FPTS - te.FPTS.mean()))
            te.insert(5, column="SD_abv_avg", value=(te.abv_avg / te.FPTS.std()))
            te.insert(6, column="SD_over_next", value=((te.abv_avg - te.abv_avg.shift(-1)) / te.FPTS.std()))
            te.insert(7, column="SD_over_next_5", value=((te.FPTS - te.FPTS.rolling(5).mean().shift(-5))
                                                         / te.FPTS.rolling(5).std().shift(-5)))
            te = te[['Player', 'Team', 'Position', 'FPTS', 'abv_avg', 'SD_abv_avg', 'SD_over_next', 'SD_over_next_5']]
            k = pd.read_csv('./Projections/FantasyPros_Fantasy_Football_Projections_K.csv')
            k = k[k.FPTS != 0]
            k.insert(2, column="Position", value="K")
            k_move = k.pop("FPTS")
            k.insert(3, "FPTS", k_move)
            k.insert(4, column="abv_avg", value=(k.FPTS - k.FPTS.mean()))
            k.insert(5, column="SD_abv_avg", value=(k.abv_avg / k.FPTS.std()))
            k.insert(6, column="SD_over_next", value=((k.abv_avg - k.abv_avg.shift(-1)) / k.FPTS.std()))
            k.insert(7, column="SD_over_next_5", value=((k.FPTS - k.FPTS.rolling(5).mean().shift(-5))
                                                        / k.FPTS.rolling(5).std().shift(-5)))
            k = k[['Player', 'Team', 'Position', 'FPTS', 'abv_avg', 'SD_abv_avg', 'SD_over_next', 'SD_over_next_5']]
            dfs = [qb, rb, wr, te, k]
            guys = pd.concat(dfs).sort_values(by='SD_abv_avg', ascending=False)
            guys = guys[~guys.Player.str.contains('|'.join(drafted), flags=re.IGNORECASE)]
            print(guys.head(10))
        else:
            continue
