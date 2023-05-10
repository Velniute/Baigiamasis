1.
Naudojantis "BeautifulSoup" biblioteka surenkami naudotų automobilių duomenyss iš "autobilis.lt" svetainės.
Naudojant "train_test_split" funkciją iš "sklearn.model_selection" bibliotekos surinkti duomenys yra suskaidomi į mokymosi ir testavimo rinkinius.
Mokymosi ir testavimo rinkiniai išsaugoti atskirose CSV failuose.
2.
Kodas nuskaito duomenų failą "train_duomenys.csv", tada naudoja "clean_data" funkciją, kad apdorotų duomenis. Ši funkcija atlieka keletą veiksmų, tokių kaip simbolių pakeitimas, duomenų tipų keitimas, klaidingų duomenų pašalinimas ir duomenų rikiavimas. Galiausiai apdoroti duomenys yra išsaugomi į naują failą "df_clean.csv".
3.
Sukuriamas Random Forest algoritmo modelis, kuris spėja naudotų automobilių kainas remiantis keliais automobilio charakteristikų stulpeliais, tokiais kaip metai, variklio galia, rida, markė, kebulo tipas, kuro tipas ir pavaru dezes tipas.
Kodas pradeda nuskaitant duomenis iš "df_clean.csv" failo, kuris jau buvo apdorotas ir išvalytas. Tada stulpeliai yra suskirstomi pagal jų tipą - numeriniai ir kategoriniai stulpeliai. Numeriniai stulpeliai yra transformuojami naudojant StandardScaler() objektą, o kategoriniai stulpeliai yra transformuojami naudojant OneHotEncoder() objektą.
Tada naudojamas ColumnTransformer() objektas, kuris sujungia transformavimo objektus (numerinių ir kategorinių stulpelių), o tada sujungia su modelio objektu naudojant Pipeline() objektą. Tai leidžia modelio objektą sujungti su transformavimo objektu ir suteikia galimybę lengvai ir greitai transformuoti ir naudoti duomenis.
Kitame žingsnyje mokymui ir testavimui yra pasiruošti duomenys naudojant train_test_split() metodą. Tada sukurtas Random Forest modelis yra apmokomas su mokymo duomenimis naudojant fit() metodą, o tikslumas ir MSE (vidutinis kvadratinis paklaida) yra apskaičiuojami naudojant score() ir mean_squared_error() metodus atitinkamai su testavimo duomenimis.
Galiausiai, modelio tikslumas ir MSE reikšmė yra spausdinami.
4.
Amokytas modelis panaudojamas prognozuoti kainas ant naujų test duomenų, atskirtų nuscrapinus duomenis iš svetainės.
