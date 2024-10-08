{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "d104dbdd-ad6e-4104-8e23-6282e28cea78",
   "metadata": {},
   "source": [
    "# EXPERIMENT 3: PYTHON DATA ANALYSIS (PANDAS)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5ff49198-3d2a-4851-a02c-74c7586106bd",
   "metadata": {},
   "source": [
    "Name: Arabelle Y. Villarin\n",
    "\n",
    "Section: 2ECE-D‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ Date Submitted: September 19, 2024¶"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "a65b4bc3-5a0a-422b-9317-c89a70deed42",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6e20fddc-e0c9-4b17-9fab-67dfaa9508aa",
   "metadata": {},
   "source": [
    "### Problem 2"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "477e1c44-d17f-4393-97e3-ec574d62eae5",
   "metadata": {},
   "source": [
    "#### A."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 127,
   "id": "9b958981-9e02-4e1f-96f4-326a6fb36dae",
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
       "      <th>mpg</th>\n",
       "      <th>disp</th>\n",
       "      <th>drat</th>\n",
       "      <th>qsec</th>\n",
       "      <th>am</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>21.0</td>\n",
       "      <td>160.0</td>\n",
       "      <td>3.90</td>\n",
       "      <td>16.46</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>21.0</td>\n",
       "      <td>160.0</td>\n",
       "      <td>3.90</td>\n",
       "      <td>17.02</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>22.8</td>\n",
       "      <td>108.0</td>\n",
       "      <td>3.85</td>\n",
       "      <td>18.61</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>21.4</td>\n",
       "      <td>258.0</td>\n",
       "      <td>3.08</td>\n",
       "      <td>19.44</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>18.7</td>\n",
       "      <td>360.0</td>\n",
       "      <td>3.15</td>\n",
       "      <td>17.02</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    mpg   disp  drat   qsec  am\n",
       "0  21.0  160.0  3.90  16.46   1\n",
       "1  21.0  160.0  3.90  17.02   1\n",
       "2  22.8  108.0  3.85  18.61   1\n",
       "3  21.4  258.0  3.08  19.44   0\n",
       "4  18.7  360.0  3.15  17.02   0"
      ]
     },
     "execution_count": 127,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Loads the corresponding .csv file for cars\n",
    "cars = pd.read_csv('cars.csv')\n",
    "cars\n",
    "\n",
    "#Displays the first five rows of odd columns\n",
    "cars.iloc[:5, [1, 3, 5, 7, 9]]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3116bf74-b9ba-49b0-bebb-a1ddaa54b9ab",
   "metadata": {},
   "source": [
    "#### B."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "id": "7acfeb9d-7dfa-4f9d-b5bb-80f133279a27",
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
       "      <td>3.9</td>\n",
       "      <td>2.62</td>\n",
       "      <td>16.46</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       Model   mpg  cyl   disp   hp  drat    wt   qsec  vs  am  gear  carb\n",
       "0  Mazda RX4  21.0    6  160.0  110   3.9  2.62  16.46   0   1     4     4"
      ]
     },
     "execution_count": 103,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Displays the row that contains Mazda RX4\n",
    "cars.loc[cars['Model'] == 'Mazda RX4']"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bf415ada-41a5-49ac-afac-eff782b2247c",
   "metadata": {},
   "source": [
    "#### C."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "id": "51e2224f-d59e-4742-b079-cdb7755e8df5",
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
       "      <th>cyl</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>23</th>\n",
       "      <td>8</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    cyl\n",
       "23    8"
      ]
     },
     "execution_count": 105,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Displays the 'cyl' of 'Camaro Z28'\n",
    "cars.loc[cars['Model'] == 'Camaro Z28',['cyl']]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "86c59019-726e-4ccf-9c5e-6ec41000c024",
   "metadata": {},
   "source": [
    "#### D."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 118,
   "id": "90fa150f-1336-4fc0-b71c-eebd1469a9ba",
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
       "      <th>cyl</th>\n",
       "      <th>gear</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>4</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>23</th>\n",
       "      <td>8</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>28</th>\n",
       "      <td>8</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    cyl  gear\n",
       "18    4     4\n",
       "23    8     3\n",
       "28    8     5"
      ]
     },
     "execution_count": 118,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Displays the 'cyl' and 'gear' of 'Camaro Z28', 'Ford Pantera L', and 'Honda Civic'\n",
    "cars.loc[cars['Model'].isin(['Camaro Z28', 'Ford Pantera L', 'Honda Civic'])][['cyl', 'gear']]"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "anaconda-2024.02-py310",
   "language": "python",
   "name": "conda-env-anaconda-2024.02-py310-py"
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
   "version": "3.10.14"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
