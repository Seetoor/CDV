library(plotly) # Aby zainstalować wklejw konsolę komendę: install.packages("plotly")

data <- read.csv2("/Users/kornel_rozumek/Desktop/data.csv", sep = ";")

prod_name_by_id = c("ryż", "Mięso wołowe bez kości", "Filety z morszczuka mrożone", "Masło świeże o zawartości tłuszczu ok. 82,5% za 200 g", "Papierosy za 20 szt.", "Spodnie (6-11 lat) z tkaniny typu jeans (2)", "Zimna woda z miejskiej sieci wodociągowej - za 1m3", "Ciepła woda - za 1m3", "Wizyta u lekarza specjalisty", "Bilet do kina")

voi_name_by_id = c("polska", "dolnoslaskie", "kujawsko-pomorskie", "lubelskie", "lubuskie" , "lodzkie", "malopolskie", "mazowieckie", "opolskie", "podkarpackie", "podlaskie", "pomorskie", "slaskie", "swietokrzyskie", "warminsko-mazurskie", "wielkopolskie", "zachodniopomorskie")

# Funkcja umożliwiająca łączenie ciągów znaków string poprzez znak +
`+` <- function(e1, e2) {
  if (is.character(e1) | is.character(e2)) {
    paste0(e1, e2)
  } else {
    base::`+`(e1, e2)
  }
}

#Funkcja zmieniająca wartości NA na 0
exception_missing_data <- function(data) {
  new_data = c()
  for(data_val in y) {
    if(is.na(data_val)) {
      new_data <- c(new_data, 0)
    } else {
      new_data <- c(new_data, data_val)
    }
  }
  return(new_data)
}

# Funkcja zwracająca wartość dominanty
getmode <- function(v) {
  uniqv <- unique(v)
  uniqv[which.max(tabulate(match(v, uniqv)))]
}

# Funkcja wyświetlająca dodatkowe informacje o danych
about_data <- function(data, product, voi) {
  print("Produkt: " + product)
  print("Obszar: " + voi)
  print("Dominanta: " + getmode(data))
  print("Mediana: " + median(data))
  print("Średnia: " + mean(data))
  
  readline(prompt="Kliknij enter, aby zobaczyć kolejny zestaw danych...")
}

# Funkcja wyciągająca z pliku .csv, miesięczne dane dotyczące cen danego produktu w odniesieniu do konkretnego wojewódźtwa i roku
get_data <- function(voivodeship, year, selected_prod) {
  voivodeship = voi_name_by_id[voivodeship]
    
  if(year >= 2006 & year <= 2019) {
    start = year - 2003
  } else {
    stop("year parametr must be 2006-2019")
  }
  
  if(selected_prod >= 1 & selected_prod <= 10){
    selected_prod = (selected_prod - 1) * 14
  } else {
    stop("selected_prod parametr must be 1-10")
  }
  
  retval <- subset( data, tolower(Nazwa) == voivodeship)
  nex = 0
  values = c()
  for (val in 3:(length(retval))-1){
    if(val == start + selected_prod | nex == val){
      v <- unname(retval[val])
      values <- c(values, v)
      nex = val + 140
    }
  }
  return(unlist(values))
}

# Funkcja wyświetlająca sformatowany wykres
make_plot <- function(y, product, voi) {
  x <- c(1:length(y))
  plot_data <- data.frame(x, y)
  p <- plot_ly(plot_data, x = ~x, y = ~y, type = 'scatter', mode = 'lines') %>%
    layout(
      title = "Wykres zmienności cen (" + product + ")(" + voi + ")(Lata 2006-2019)",
      xaxis = list(title = "Kolejne miesiące od stycznia 2006 roku"),
      yaxis = list(title = "Cena (zł)")
    )
  print(p)
}

# Końcowy skrypt
for (product in 1:10) {
  for(voi in 1:17) {
    y = c()
    for (year in 2006:2019) {
      y <- c(y, get_data(voi, year, product))
    }
    make_plot(exception_missing_data(y), prod_name_by_id[product], voi_name_by_id[voi])
    about_data(exception_missing_data(y), prod_name_by_id[product], voi_name_by_id[voi])
  }
}