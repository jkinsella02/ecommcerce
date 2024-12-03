from model.models import Product


class ProductDAO:
    def __init__(self):
        """
        Initializes the ProductDAO with a sample collection of products.
        """
        self.products = [
            Product(1, "Casio Retro", "Casio", 40.00, "digital", "static/images/product/casio-retro.jpg"),
            Product(2, "Rolex", "Rolex", 18.00, "analog", "static/images/product/silver-rolex.jpg"),
            Product(3, "Seiko", "Seiko", 25.00, "analog", "static/images/product/seiko-silver.jpg"),
            Product(4, "Omega Solias", "Omega", 40.00, "analog", "static/images/product/omega-solias.jpg"),
            Product(5, "Samsung Active", "Samsung", 25.00, "smart", "static/images/product/samsung-active.png"),
            Product(6, "Apple Watch SE", "Apple", 120.00, "smart", "static/images/product/smart-watch.png"),
            Product(7, "Tiffiney", "Tiffiney", 18.00, "analog", "static/images/product/tiffiny.jpg"),
            Product(8, "Garmin", "Garmin", 40.00, "smart", "static/images/product/garmin.jpg")
        ]

    def getAllProducts(self):
        """
        Retrieves all products in the catalog.
        """
        return self.products

    def getProduct(self, product_id):
        """
        Retrieves a single product by its ID.

        Args:
            product_id (int): The ID of the product to retrieve.

        Returns:
            Product: The product with the given ID, or None if not found.
        """
        for product in self.products:
            if product.product_id == product_id:
                return product
        return None  # Product not found


# Example usage of ProductDAO
def main_with_dao():
    product_dao = ProductDAO()

    print("All Products:")
    for product in product_dao.getAllProducts():
        print(product)

    print("\nFetching Product by ID (ID: 2):")
    product = product_dao.getProduct(2)
    if product:
        print(product)
    else:
        print("Product not found.")


if __name__ == "__main__":
    main_with_dao()
