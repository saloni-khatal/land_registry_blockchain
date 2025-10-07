import streamlit as st
from blockchain import Blockchain

# Instantiate blockchain
blockchain = Blockchain()

st.title("Land / Property Registry Blockchain")

# Add Property Record
st.subheader("Register a Property")
owner_name = st.text_input("Owner Name")
property_id = st.text_input("Property ID")
location = st.text_input("Location")
value = st.text_input("Property Value")

if st.button("Add Property & Mine Block"):
    if owner_name.strip() == "" or property_id.strip() == "" or location.strip() == "" or value.strip() == "":
        st.error("Please fill all fields")
    else:
        blockchain.add_property(owner_name, property_id, location, value)
        last_proof = blockchain.last_block['proof']
        proof = blockchain.proof_of_work(last_proof)
        prev_hash = blockchain.hash(blockchain.last_block)
        blockchain.create_block(proof, prev_hash)
        st.success(f"Property added and mined in block #{blockchain.last_block['index']}!")

st.markdown("---")

# Verify Property
st.subheader("Verify Property Ownership")
search_id = st.text_input("Enter Property ID to Verify")
if st.button("Verify"):
    result = blockchain.verify_property(search_id)
    if result:
        st.success("Property Found!")
        st.json(result)
    else:
        st.error("Property not found!")

st.markdown("---")

# Display Blockchain
st.header("Blockchain Ledger")
for block in blockchain.chain:
    st.json(block)
