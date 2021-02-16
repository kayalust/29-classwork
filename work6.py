# Input functions

product_name = input("ชื่อสินค้า: ")
product_price = input("ราคาสินค้า: ")

vat = 7/100
product_vat = float(product_price) * vat
print("ภาษี:", product_vat)
print("ราคารวมภาษี:", product_vat + float(product_price))
