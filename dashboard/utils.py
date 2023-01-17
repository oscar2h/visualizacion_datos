def get_top5(data):
    data.loc[:,"total"] = data.loc[:, range(2005,2017)].sum(axis=1)
    data.sort_values("total", inplace = True, ascending = False)
    top5 = data.iloc[:5]
    return top5

def get_kpi(data,region, kpi):
    TotalKPI_Region = data[data['Region'] == region]
    TotalKPI_Region = TotalKPI_Region[kpi].iloc[-1]
    return TotalKPI_Region