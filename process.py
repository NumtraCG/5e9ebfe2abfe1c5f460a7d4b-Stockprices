import json
import Connectors
import Transformations
import AutoML
try:
    Stockprices_DBFS = Connectors.DBFSConnector.fetch(
        [], {}, "5e9ebfe2abfe1c5f460a7d4c", spark, "{'url': '/Demo/Predicting_Stock_prices.csv', 'file_type': 'Delimeted', 'dbfs_token': 'dapib8073bbfa952efa9d363b234ce06e2c6', 'dbfs_domain': 'westus.azuredatabricks.net', 'delimiter': ',', 'is_header': 'Use Header Line'}")

except Exception as ex:
    print(ex)
try:
    Stockprices_AutoFE = Transformations.TransformationMain.run(["5e9ebfe2abfe1c5f460a7d4c"], {"5e9ebfe2abfe1c5f460a7d4c": Stockprices_DBFS}, "5e9ebfe2abfe1c5f460a7d4d", spark, json.dumps({"FE": [{"transformationsData": {"feature_label": "Date"}, "feature": "Date", "type": "string", "selected": "True", "replaceby": "max", "stats": {"count": "1512", "mean": "", "stddev": "", "min": "1/1/2018", "max": "9/8/2017", "missing": "0"}, "transformation": "String Indexer"}, {"transformationsData": {}, "feature": "Month", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "1512", "mean": "6.53", "stddev": "3.46", "min": "1", "max": "12", "missing": "0"}}, {"transformationsData": {}, "feature": "Company", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "1512", "mean": "5.63", "stddev": "2.92", "min": "1", "max": "10", "missing": "0"}}, {"transformationsData": {}, "feature": "Open", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "1512", "mean": "1345.27", "stddev": "2118.03", "min": "35.349998", "max": "9966.0", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "High", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "1512", "mean": "1357.19", "stddev": "2134.24", "min": "36.549999", "max": "9996.400391", "missing": "0"}, "transformation": ""}, {"transformationsData": {
    }, "feature": "Low", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "1512", "mean": "1333.03", "stddev": "2101.51", "min": "34.599998", "max": "9700.25", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "Prev Close", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "1512", "mean": "1346.03", "stddev": "2121.18", "min": "35.349998", "max": "9801.5", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "Adj Close", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "1512", "mean": "1335.24", "stddev": "2107.53", "min": "35.349998", "max": "9801.5", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "Volume", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "1512", "mean": "3880877.61", "stddev": "5653428.74", "min": "43411", "max": "82202480", "missing": "0"}}, {"transformationsData": {}, "feature": "Close", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "1512", "mean": "1344.89", "stddev": "2117.57", "min": "35.349998", "max": "9801.5", "missing": "0"}, "transformation": ""}, {"feature": "Date_transform", "transformation": "", "transformationsData": {}, "type": "real", "selected": "True", "stats": {"count": "1512", "mean": "107.98", "stddev": "69.88", "min": "0.0", "max": "249.0", "missing": "0"}}]}))

except Exception as ex:
    print(ex)
try:
    AutoML.functionRegression(Stockprices_AutoFE, [
                              "Date", "Month", "Company", "Open", "High", "Low", "Prev Close", "Adj Close", "Volume"], "Close")

except Exception as ex:
    print(ex)
