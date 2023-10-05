#!/usr/bin/env python
import pandas as pd, sys, fileinput, functools as ft

dfs = []
for file in fileinput.input():
    dfs.append(pd.read_csv(fileinput.filename(),sep="\t"))
    fileinput.nextfile()
df = ft.reduce(lambda  left,right: pd.merge(left,right,on=['strain'],how='outer'), dfs)
df.to_csv('metadataCluster.tsv', sep="\t")
