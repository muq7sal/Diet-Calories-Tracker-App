import streamlit as st
import pandas as pd

# ---------------------------
# Page Config & Title
# ---------------------------
st.set_page_config(page_title="🍎 Diet Calorie Tracker", page_icon="🥗", layout="centered")
st.title("🥗 Diet Calorie Tracker")
st.markdown("Track your daily food intake and calories easily!")

# ---------------------------
# Food Calorie Database (Sample)
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
}

# ---------------------------
# Initialize session data
# ---------------------------
if "diet_log" not in st.session_state:
    st.session_state.diet_log = []

# ---------------------------
# Input Section
# ---------------------------
st.subheader("🍽️ Add Your Meal")

col1, col2 = st.columns(2)
with col1:
    food_item = st.selectbox("Select Food Item", list(food_data.keys()))
with col2:
    quantity = st.number_input("Quantity (servings)", min_value=1, value=1)

if st.button("Add to Log"):
    calories = food_data[food_item] * quantity
    st.session_state.diet_log.append({"Food": food_item, "Quantity": quantity, "Calories": calories})
    st.success(f"Added {quantity} serving(s) of {food_item} — **{calories} kcal**")

# ---------------------------
# Display Diet Log
# ---------------------------
if st.session_state.diet_log:
    st.subheader("📋 Today's Food Log")
    df = pd.DataFrame(st.session_state.diet_log)
    df.index += 1
    st.dataframe(df, use_container_width=True)

    total_calories = df["Calories"].sum()
    st.metric("🔥 Total Calories Consumed", f"{total_calories} kcal")

    # Reset or Download
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🧹 Reset Log"):
            st.session_state.diet_log = []
            st.experimental_rerun()
    with col2:
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("💾 Download Log", csv, "diet_log.csv", "text/csv")

else:
    st.info("No food items added yet. Start tracking your meals above!")

# ---------------------------
# Footer
# ---------------------------
st.markdown("---")
st.markdown("💡 *Tip: Use this app daily to monitor your calorie intake and stay healthy!*")
