def linear_search_product(product_list, target_product):
    indices = []
    for i in range(len(product_list)):
        if product_list[i] == target_product:
            indices.append(i)
    return indices
products = ["Apple", "Banana", "Orange", "Apple", "Grapes", "Apple"]
target = "Apple"
result = linear_search_product(products, target)
print(result)  # Output: [0, 3, 5]
