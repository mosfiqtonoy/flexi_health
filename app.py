import streamlit as st
import pandas as pd

# ------------------------
# PAGE CONFIG
# ------------------------
st.set_page_config(
    page_title="Flexi Health Bangladesh",
    page_icon="🏥",
    layout="wide"
)

# ------------------------
# SESSION INIT
# ------------------------
if "wallet" not in st.session_state:
    st.session_state.wallet = 0.0

if "savings" not in st.session_state:
    st.session_state.savings = []

if "medicine_orders" not in st.session_state:
    st.session_state.medicine_orders = []

if "donors" not in st.session_state:
    st.session_state.donors = pd.DataFrame({
        "Name": ["Rahim", "Karim", "Sabbir", "Nusrat"],
        "Blood Group": ["A+", "B+", "O+", "AB+"],
        "City": ["Dhaka", "Chattogram", "Rajshahi", "Sylhet"],
        "Phone": ["01711111111", "01822222222", "01933333333", "01644444444"]
    })

# ------------------------
# SIDEBAR
# ------------------------
menu = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Recharge Savings",
        "Health Wallet",
        "Blood Bank",
        "Ambulance",
        "Medicine",
        "Telemedicine"
    ]
)

# ------------------------
# HOME
# ------------------------
if menu == "Home":
    st.title("Flexi Health Bangladesh")

    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/f/f9/Flag_of_Bangladesh.svg",
        width=180
    )

    st.markdown("""
    ### Smart Health & Emergency System (Demo Project)

    Features:
    - Mobile recharge savings
    - Emergency ambulance support
    - Blood donor search
    - Medicine ordering system
    - Telemedicine booking
    """)

    st.success("System Running Successfully 🚀")

# ------------------------
# RECHARGE SAVINGS
# ------------------------
elif menu == "Recharge Savings":
    st.title("Recharge Savings")

    with st.form("recharge_form"):
        number = st.text_input("Mobile Number")
        recharge = st.number_input("Recharge Amount (BDT)", min_value=0.0)
        submit = st.form_submit_button("Recharge")

    if submit and number:
        saved = recharge * 0.10
        st.session_state.wallet += saved

        st.session_state.savings.append({
            "Mobile": number,
            "Recharge": recharge,
            "Saved": saved
        })

        st.success("Recharge Successful!")
        st.info(f"৳{saved:.2f} added to wallet")

# ------------------------
# HEALTH WALLET
# ------------------------
elif menu == "Health Wallet":
    st.title("Health Wallet")

    st.metric("Total Saved", f"৳ {st.session_state.wallet:.2f}")

    if st.session_state.savings:
        df = pd.DataFrame(st.session_state.savings)
        st.dataframe(df)
    else:
        st.warning("No transaction history yet")

# ------------------------
# BLOOD BANK
# ------------------------
elif menu == "Blood Bank":
    st.title("Blood Donor Search")

    blood_group = st.selectbox(
        "Blood Group",
        ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]
    )

    city = st.selectbox(
        "City",
        ["Dhaka", "Chattogram", "Rajshahi", "Khulna", "Sylhet", "Barishal"]
    )

    if st.button("Find Donor"):
        df = st.session_state.donors
        result = df[(df["Blood Group"] == blood_group) & (df["City"] == city)]

        if not result.empty:
            st.dataframe(result)
        else:
            st.error("No donor found")

# ------------------------
# AMBULANCE
# ------------------------
elif menu == "Ambulance":
    st.title("Emergency Ambulance")

    location = st.text_input("Enter Location")

    if st.button("Call Ambulance"):
        if location:
            st.error("Emergency Request Sent 🚨")
            st.write(f"Ambulance is coming to: {location}")
        else:
            st.warning("Please enter location")

# ------------------------
# MEDICINE
# ------------------------
elif menu == "Medicine":
    st.title("Medicine Order")

    with st.form("med_form"):
        medicine = st.text_input("Medicine Name")
        quantity = st.number_input("Quantity", min_value=1)
        address = st.text_area("Delivery Address")
        submit = st.form_submit_button("Place Order")

    if submit:
        st.session_state.medicine_orders.append({
            "Medicine": medicine,
            "Quantity": quantity,
            "Address": address
        })

        st.success("Order Confirmed!")
        st.info("Delivery will arrive soon 🚚")

# ------------------------
# TELEMEDICINE
# ------------------------
elif menu == "Telemedicine":
    st.title("Telemedicine")

    doctor = st.selectbox(
        "Choose Doctor",
        ["Medicine Specialist", "Heart Specialist", "Child Specialist", "Skin Specialist"]
    )

    problem = st.text_area("Describe Your Problem")

    if st.button("Book Consultation"):
        if problem:
            st.success(f"Appointment booked with {doctor}")
            st.info("Doctor will contact you soon 📞")
        else:
            st.warning("Please describe your problem")
