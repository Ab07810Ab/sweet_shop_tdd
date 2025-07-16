# streamlit_app.py
import streamlit as st
from sweet import Sweet
from sweet_shop import SweetShop

# Ensure persistent shop instance
if "shop" not in st.session_state:
    st.session_state.shop = SweetShop()

shop = st.session_state.shop

st.set_page_config(page_title="Sweet Shop Management System", layout="centered")
st.title("\U0001F36C Sweet Shop Management System")

menu = st.sidebar.radio("Navigation", [
    "Add Sweet", "View Sweets", "Search Sweets", "Purchase Sweet", "Restock Sweet", "Delete Sweet"
])

# Add Sweet
if menu == "Add Sweet":
    st.header("➕ Add New Sweet")
    id = st.number_input("Sweet ID", min_value=1, step=1)
    name = st.text_input("Sweet Name")
    category = st.selectbox("Category", ["chocolate", "candy", "pastry", "dry sweet", "bengali sweet"])
    price = st.number_input("Price (₹)", min_value=0.0, step=0.5)
    quantity = st.number_input("Quantity", min_value=1, step=1)

    if st.button("Add Sweet"):
        new_sweet = Sweet(id, name, category, price, quantity)
        if shop.add_sweet(new_sweet):
            st.success("Sweet added successfully!")
        else:
            st.error("Sweet with this ID already exists.")

# View Sweets
elif menu == "View Sweets":
    st.header("📋 All Available Sweets")
    sweets = shop.get_all_sweets()
    
    if sweets:
        sweet_data = [{
            "ID": s.id,
            "Name": s.name,
            "Category": s.category,
            "Price (₹)": s.price,
            "Quantity": s.quantity
        } for s in sweets]

        st.table(sweet_data)
    else:
        st.warning("No sweets available.")

# Search Sweets
elif menu == "Search Sweets":
    st.header("🔍 Search Sweets")
    search_type = st.radio("Search by", ["Name", "Category", "Price Range"])
    results = []
    if search_type == "Name":
        name_query = st.text_input("Enter name keyword")
        if name_query:
            results = shop.search_by_name(name_query)
            

    elif search_type == "Category":
        category_query = st.selectbox("Choose category", ["chocolate", "candy", "pastry", "dry sweet", "bengali sweet"])
        results = shop.search_by_category(category_query)
        

    elif search_type == "Price Range":
        min_price = st.number_input("Min Price", min_value=0.0, step=0.5)
        max_price = st.number_input("Max Price", min_value=0.0, step=0.5)
        if max_price >= min_price:
            results = shop.search_by_price_range(min_price, max_price)
            
        else:
            st.error("Max price should be greater than or equal to Min price")
    # ✅ Display results in a table if any found
    if results:
        sweet_data = [{
            "ID": s.id,
            "Name": s.name,
            "Category": s.category,
            "Price (₹)": s.price,
            "Quantity": s.quantity
        } for s in results]

        st.table(sweet_data)  # You can also use st.dataframe(sweet_data)
    elif search_type != "Price Range" or (max_price >= min_price):
        st.warning("No sweets found for the selected criteria.")

# Purchase Sweet
elif menu == "Purchase Sweet":
    st.header("🛒 Purchase Sweet")
    sweet_id = st.number_input("Enter Sweet ID", min_value=1, step=1)
    quantity = st.number_input("Quantity to purchase", min_value=1, step=1)
    if st.button("Purchase"):
        try:
            shop.purchase(sweet_id, quantity)
            st.success("Purchase successful! Stock updated.")
        except ValueError as e:
            st.error(str(e))

#Restock Sweet
elif menu == "Restock Sweet":
    st.header("📦 Restock Sweet")
    sweet_id = st.number_input("Enter Sweet ID to restock", min_value=1, step=1)
    restock_qty = st.number_input("Quantity to add", min_value=1, step=1)
    if st.button("Restock"):
        try:
            shop.restock(sweet_id, restock_qty)
            st.success("Sweet restocked successfully!")
        except ValueError as e:
            st.error(str(e))
            


# Delete Sweet
elif menu == "Delete Sweet":
    st.header("❌ Delete Sweet")
    sweet_id = st.number_input("Enter Sweet ID to delete", min_value=1, step=1)
    if st.button("Delete"):
        if shop.delete_sweet(sweet_id):
            st.success("Sweet deleted successfully!")
        else:
            st.error("Sweet not found with given ID.")