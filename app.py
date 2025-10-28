import streamlit as st
import pandas as pd

# ---------------------------
# Page Configuration
# ---------------------------
st.set_page_config(page_title="🍎 Diet Calorie Tracker", page_icon="🥗", layout="centered")

st.title("🥗 Diet Calorie Tracker")
st.markdown("Easily track your daily calorie intake and stay on top of your diet goals!")

# ---------------------------
# Food Calorie Database (Updated)
# ---------------------------
food_data = {
    "Apple": 52,
    "Banana": 89,
    "Orange": 43,
    "Egg (boiled)": 68,
    "Bread Slice": 80,
    "Rice (1 cup)": 206,
    "Chicken Breast (100g)": 165,
    "Milk (1 glass)": 150,
    "Oatmeal (1 bowl)": 158,
    "Almonds (10 pcs)": 70,
    "Paneer (100g)": 265,
    "Potato (boiled)": 87,
    "Coffee (no sugar)": 5,
    "Green Tea": 2,
    "Salad (1 bowl)": 33,
}

# ---------------------------
# Initialize session state
# ---------------------------
if "diet_log" not in st.session_state:
    st.session_state.diet_log = []

# ---------------------------
# Add Meal Section
# ---------------------------
st.subheader("🍽️ Add Your Meal")

col1, col2, col3 = st.columns([3, 2, 1])

with col1:
    food_item = st.selectbox("Select Food Item", list(food_data.keys()), index=0)
with col2:
    quantity = st.number_input("Quantity (servings)", min_value=1, value=1)
with col3:
    st.write("")  # For spacing
    if st.button("➕ Add"):
        calories = food_data[food_item] * quantity
        st.session_state.diet_log.append({"Food": food_item, "Quantity": quantity, "Calories": calories})
        st.success(f"Added {quantity} serving(s) of {food_item} — **{calories} kcal**")

# ---------------------------
# Display Log Section
# ---------------------------
if st.session_state.diet_log:
    st.subheader("📋 Today's Food Log")
    df = pd.DataFrame(st.session_state.diet_log)
    df.index += 1
    st.dataframe(df, use_container_width=True)

    total_calories = df["Calories"].sum()
    st.metric("🔥 Total Calories Consumed", f"{total_calories} kcal")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🧹 Reset Log"):
            st.session_state.diet_log = []
            st.experimental_rerun()
    with col2:
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("💾 Download Log", csv, "diet_log.csv", "text/csv")

else:
    st.info("No food items added yet. Start logging your meals above!")

# ---------------------------
# Footer
# ---------------------------
st.markdown("---")
st.markdown("💡 *Tip: Keep your daily calorie goal in mind and choose wisely!*")

