def price_per_km(name,on_road, fuel_price, economy, years, yearly_service_cost, extra_cost, driven):
    fuel_cost = economy/fuel_price

    service_cost = yearly_service_cost*years

    final_price = on_road + (driven/fuel_cost) + service_cost + extra_cost

    print(f"{name}: {round(final_price/driven,2)} rs/km")

price_per_km("Triumph speed 400",270000, 110, 25, 3, 7000, 15000, 30000)
price_per_km("KTM Duke 250",270000, 110, 32, 3, 4500, 15000, 30000)
price_per_km("RTR 310", 306000, 110, 35,3, 6500, 15000, 30000)
