{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "6d6dc44a-6a64-4d32-b69b-ad73650e7a9d",
   "metadata": {},
   "source": [
    "# EXPERIMENT 3: PYTHON DATA ANALYSIS (PANDAS)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "afa1d67a-f6a3-4bef-9563-082970f82bb0",
   "metadata": {},
   "source": [
    "Name: Arabelle Y. Villarin\n",
    "\n",
    "Section: 2ECE-D‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ Date Submitted: September 19, 2024¶"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "3ef12cb0-470d-4999-a7c8-e326965c5d45",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8942b382-b8c1-45c2-aa4d-9424013b5dff",
   "metadata": {},
   "source": [
    "### Problem 1"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cfacdb9a-928a-419d-8b35-a45838716c4c",
   "metadata": {},
   "source": [
    "#### A."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "a41f65a0-7ba3-4f36-8612-01ed41d80205",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Model</th>\n",
       "      <th>mpg</th>\n",
       "      <th>cyl</th>\n",
       "      <th>disp</th>\n",
       "      <th>hp</th>\n",
       "      <th>drat</th>\n",
       "      <th>wt</th>\n",
       "      <th>qsec</th>\n",
       "      <th>vs</th>\n",
       "      <th>am</th>\n",
       "      <th>gear</th>\n",
       "      <th>carb</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Mazda RX4</td>\n",
       "      <td>21.0</td>\n",
       "      <td>6</td>\n",
       "      <td>160.0</td>\n",
       "      <td>110</td>\n",
       "      <td>3.90</td>\n",
       "      <td>2.620</td>\n",
       "      <td>16.46</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Mazda RX4 Wag</td>\n",
       "      <td>21.0</td>\n",
       "      <td>6</td>\n",
       "      <td>160.0</td>\n",
       "      <td>110</td>\n",
       "      <td>3.90</td>\n",
       "      <td>2.875</td>\n",
       "      <td>17.02</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Datsun 710</td>\n",
       "      <td>22.8</td>\n",
       "      <td>4</td>\n",
       "      <td>108.0</td>\n",
       "      <td>93</td>\n",
       "      <td>3.85</td>\n",
       "      <td>2.320</td>\n",
       "      <td>18.61</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Hornet 4 Drive</td>\n",
       "      <td>21.4</td>\n",
       "      <td>6</td>\n",
       "      <td>258.0</td>\n",
       "      <td>110</td>\n",
       "      <td>3.08</td>\n",
       "      <td>3.215</td>\n",
       "      <td>19.44</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Hornet Sportabout</td>\n",
       "      <td>18.7</td>\n",
       "      <td>8</td>\n",
       "      <td>360.0</td>\n",
       "      <td>175</td>\n",
       "      <td>3.15</td>\n",
       "      <td>3.440</td>\n",
       "      <td>17.02</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "               Model   mpg  cyl   disp   hp  drat     wt   qsec  vs  am  gear  \\\n",
       "0          Mazda RX4  21.0    6  160.0  110  3.90  2.620  16.46   0   1     4   \n",
       "1      Mazda RX4 Wag  21.0    6  160.0  110  3.90  2.875  17.02   0   1     4   \n",
       "2         Datsun 710  22.8    4  108.0   93  3.85  2.320  18.61   1   1     4   \n",
       "3     Hornet 4 Drive  21.4    6  258.0  110  3.08  3.215  19.44   1   0     3   \n",
       "4  Hornet Sportabout  18.7    8  360.0  175  3.15  3.440  17.02   0   0     3   \n",
       "\n",
       "   carb  \n",
       "0     4  \n",
       "1     4  \n",
       "2     1  \n",
       "3     1  \n",
       "4     2  "
      ]
     },
     "execution_count": 65,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Loads the corresponding .csv file for cars\n",
    "cars = pd.read_csv('cars.csv')\n",
    "cars\n",
    "\n",
    "#Displays the first five rows of the resulting cars\n",
    "cars.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e55724ba-876b-46d0-8870-7c28f6dcc2eb",
   "metadata": {},
   "source": [
    "#### B."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "e6ba91fb-2c93-4dd2-bd7a-833259d2ee60",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Model</th>\n",
       "      <th>mpg</th>\n",
       "      <th>cyl</th>\n",
       "      <th>disp</th>\n",
       "      <th>hp</th>\n",
       "      <th>drat</th>\n",
       "      <th>wt</th>\n",
       "      <th>qsec</th>\n",
       "      <th>vs</th>\n",
       "      <th>am</th>\n",
       "      <th>gear</th>\n",
       "      <th>carb</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>27</th>\n",
       "      <td>Lotus Europa</td>\n",
       "      <td>30.4</td>\n",
       "      <td>4</td>\n",
       "      <td>95.1</td>\n",
       "      <td>113</td>\n",
       "      <td>3.77</td>\n",
       "      <td>1.513</td>\n",
       "      <td>16.9</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>5</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>28</th>\n",
       "      <td>Ford Pantera L</td>\n",
       "      <td>15.8</td>\n",
       "      <td>8</td>\n",
       "      <td>351.0</td>\n",
       "      <td>264</td>\n",
       "      <td>4.22</td>\n",
       "      <td>3.170</td>\n",
       "      <td>14.5</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>5</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>29</th>\n",
       "      <td>Ferrari Dino</td>\n",
       "      <td>19.7</td>\n",
       "      <td>6</td>\n",
       "      <td>145.0</td>\n",
       "      <td>175</td>\n",
       "      <td>3.62</td>\n",
       "      <td>2.770</td>\n",
       "      <td>15.5</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>5</td>\n",
       "      <td>6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>30</th>\n",
       "      <td>Maserati Bora</td>\n",
       "      <td>15.0</td>\n",
       "      <td>8</td>\n",
       "      <td>301.0</td>\n",
       "      <td>335</td>\n",
       "      <td>3.54</td>\n",
       "      <td>3.570</td>\n",
       "      <td>14.6</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>5</td>\n",
       "      <td>8</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>31</th>\n",
       "      <td>Volvo 142E</td>\n",
       "      <td>21.4</td>\n",
       "      <td>4</td>\n",
       "      <td>121.0</td>\n",
       "      <td>109</td>\n",
       "      <td>4.11</td>\n",
       "      <td>2.780</td>\n",
       "      <td>18.6</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             Model   mpg  cyl   disp   hp  drat     wt  qsec  vs  am  gear  \\\n",
       "27    Lotus Europa  30.4    4   95.1  113  3.77  1.513  16.9   1   1     5   \n",
       "28  Ford Pantera L  15.8    8  351.0  264  4.22  3.170  14.5   0   1     5   \n",
       "29    Ferrari Dino  19.7    6  145.0  175  3.62  2.770  15.5   0   1     5   \n",
       "30   Maserati Bora  15.0    8  301.0  335  3.54  3.570  14.6   0   1     5   \n",
       "31      Volvo 142E  21.4    4  121.0  109  4.11  2.780  18.6   1   1     4   \n",
       "\n",
       "    carb  \n",
       "27     2  \n",
       "28     4  \n",
       "29     6  \n",
       "30     8  \n",
       "31     2  "
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Displays the last five rows of the resulting cars\n",
    "cars.tail()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "anaconda-panel-2023.05-py310",
   "language": "python",
   "name": "conda-env-anaconda-panel-2023.05-py310-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
