### Purpose of this Project

Transform data from the [COVID-19 epidemiological bulletins of the state of São Paulo-Brazil](http://www.saude.sp.gov.br/cve-centro-de-vigilancia-epidemiologica-prof.-alexandre-vranjac/areas-de-vigilancia/doencas-de-transmissao-respiratoria/coronavirus-covid-19/situacao-epidemiologica) that are in PDF to the CSV format for the purposes of statistical analysis and creation of a heat map of COVID-19 dispersion in the state.

I am making the data of the epidemiological bulletins available in csv format [here](https://www.kaggle.com/clovesgtx/covid19-municpios-de-so-paulo) in kaggle platform.

The heat map can be found [here](https://www.kaggle.com/clovesgtx/mapa-das-mortes-por-covid-19-em-s-o-paulo) and will be updated weekly on weekends.

### How use?

To update the CSV in question just go [here](http://www.saude.sp.gov.br/cve-centro-de-vigilancia-epidemiologica-prof.-alexandre-vranjac/areas-de-vigilancia/doencas-de-transmissao-respiratoria/coronavirus-covid-19/situacao-epidemiologica), make the download of the latest epidemiological bulletin, save it in the *bulletins directory* and rename it in fomat *boletim_<nº of boletim>_<date day-month-year>.pdf* (e.g "coronavirus180420_52situacao_epidemiologica" as "boletim_52_18-04-20.pdf").

To install the required packages run:

```sh
$ pip3 install -r requirements.txt
```
With all the bulletin saved in the directory, run:
```sh
$ python3 pdf_parser.py --path "./bulletins"
```
This will generate a CSV called "covid-19-municipios-sp.csv" in the *bulletins directory*.
