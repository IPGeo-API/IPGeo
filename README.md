# IPGeo

## About IPGeo

The IPGeo repository on GitHub is an pre-coded example of the usage of our [IPGeoSearch](https://github.com/MatthiasRathbun/IPGeo-Search) library based on the IP geolocation API found on [Our Webpage](http://ipgeo.azurewebsites.net/).

Feel Free to check out the [IPGeoSearch](https://github.com/MatthiasRathbun/IPGeo-Search) library on GitHub for more information and ways to use our API!

## Requirements

Before running on your local computer, make sure you have `python 3.6+` with the latest version of `pandas` and `IPGeoSearch` installed, your API Key, and `ipList.txt` in the same folder as the python file.

To Install Pandas, run

```cmd
pip install pandas
```

To Install IPGeoSearch, run

```cmd
pip install IPGeoSearch
```

Request.txt should be formatted in one IP address per line like such:

```txt
8.8.8.8
8.8.8.8
8.8.8.8
8.8.8.8
8.8.8.8
```

## How To Use

### Python Example

 The `results` folder will have all the `.json` and `.csv` files stored in it after running.

To query IP using our sample file, run

```cmd
python request.py
```

in your command prompt environment with the pandas installed.

Files named `x.x.x.x.csv` and `x.x.x.x.json` are saved which have the relevant information regarding your IP Search. Files are named with the IP in the file Name. An example csv for a search of Google's IP `8.8.8.8` would be named `8.8.8.8.csv`.
