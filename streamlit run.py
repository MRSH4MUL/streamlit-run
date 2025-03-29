import streamlit as st
import random
import qrcode
from io import BytesIO

def generate_salami():
    return random.randint(10, 500)  # Generates a random salami amount

def generate_qr(data):
    qr = qrcode.make(data)
    buf = BytesIO()
    qr.save(buf, format="PNG")
    return buf.getvalue()

st.title("মো: শিমুল ঈদ সালামি অ্যাপ")

st.header("ঈদ মোবারক! আপনার সালামি নিন")

if st.button("সালামি নিন"):
    amount = generate_salami()
    st.success(f"আপনি {amount} টাকা সালামি পেয়েছেন! 🎉")
    qr_code = generate_qr(f"আপনার সালামি: {amount} টাকা")
    st.image(qr_code, caption="আপনার সালামির QR কোড")

st.header("ঈদ শুভেচ্ছা পাঠান")
message = st.text_input("আপনার শুভেচ্ছা বার্তা লিখুন")
recipient = st.text_input("প্রাপকের নাম লিখুন")
if st.button("পাঠান"):
    if message and recipient:
        st.success(f"{recipient} কে আপনার বার্তাটি পাঠানো হয়েছে: {message}")
        qr_code = generate_qr(f"{recipient} এর জন্য শুভেচ্ছা: {message}")
        st.image(qr_code, caption="শুভেচ্ছার QR কোড")
    else:
        st.error("দয়া করে বার্তা এবং প্রাপকের নাম লিখুন")