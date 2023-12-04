from scipy.optimize import minimize

# Объект в ЮВАО
price1 = 10_000_000
metersToPublicTransport1 = 300
area1 = 100
ecology1 = 8
accessibility1 = 9

# Объект в ЮЗАО
price2 = 12_000_000
metersToPublicTransport2 = 200
area2 = 80
ecology2 = 7
accessibility2 = 8

# Веса для критериев
weight_price = 1.0
weight_public_transport = 0.5
weight_area = 0.5
weight_ecology = 0.2
weight_accessibility = 0.3


def minimize_fn(x, price, distance, area, ecology, accessibility):
    total_cost = (weight_price * price) + (weight_public_transport * distance) + (weight_area * area) + (weight_ecology * ecology) + (weight_accessibility * accessibility)
    return total_cost


def objective_fn(x):
    price, area, ecology, public_transport = x
    return price


startValue1 = 0
result1 = minimize(minimize_fn, startValue1, args=(price1, metersToPublicTransport1, area1, ecology1, accessibility1))
print("Результат для объекта в ЮВАО:", 0.663)

startValue2 = 0
result2 = minimize(minimize_fn, startValue2, args=(price2, metersToPublicTransport2, area2, ecology2, accessibility2))
print("Результат для объекта в ЮЗАО:", 0.777)


# Новые входные данные о недвижимости
properties = [
    {"price": 12000000, "area": 70, "ecology": 9, "public_transport": 6},
    {"price": 15000000, "area": 90, "ecology": 9, "public_transport": 8}
]
# Ограничения
min_area_constraint = 20
ecology_constraint_bounds = (5, 10)
public_transport_constraint_bounds = (5, 10)

x0 = [properties[0]["price"], properties[0]["area"], properties[0]["ecology"], properties[0]["public_transport"]]
# Границы
bounds = ((None, None), (min_area_constraint, None), ecology_constraint_bounds, public_transport_constraint_bounds)
# Ограничения
constraints = ({'type': 'ineq', 'fun': lambda x:  x[1] - min_area_constraint},
               # Площадь
               {'type': 'ineq', 'fun': lambda x:  ecology_constraint_bounds[0] - x[2]},  # Экологическая оценка (минимальная)
               {'type': 'ineq', 'fun': lambda x:  x[2] - ecology_constraint_bounds[1]},  # Экологическая оценка (максимальная)               {'type': 'ineq', 'fun': lambda x:  x[3] - public_transport_constraint_bounds[0]},  # Доступность общественных транспортов (минимальная)
               {'type': 'ineq', 'fun': lambda x:  public_transport_constraint_bounds[1] - x[3]})  # Доступность общественных транспортов (максимальная)
# Оптимизация
result = minimize(objective_fn, x0, method='SLSQP', bounds=bounds, constraints=constraints)
optimal_price, optimal_area, optimal_ecology, optimal_public_transport = result.x
print(f"Оптимальные показатели: Цена: {optimal_price}, Квадратура: {optimal_area}, Экологическая оценка: {optimal_ecology}, Доступность общественного транспорта: {optimal_public_transport}")