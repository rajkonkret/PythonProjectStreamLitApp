import streamlit as st
# pip install "streamlit[auth]"
st.set_page_config(
    page_title="Portal firmowy",
    layout="wide"
)

# --------------------------------------------------
# LOGOWANIE
# --------------------------------------------------
st.write(st.secrets.auth.redirect_uri)

if not st.user.is_logged_in:
    st.title("🔐 Portal firmowy")

    st.info(
        "Zaloguj się swoim kontem Microsoft 365 "
        "używanym w Outlooku lub Teams."
    )

    if st.button("Zaloguj przez Microsoft 365"):
        st.login("microsoft")

    st.stop()


# --------------------------------------------------
# DANE UŻYTKOWNIKA
# --------------------------------------------------

name = st.user.get("name", "Użytkownik")
email = st.user.get("email", "")

# --------------------------------------------------
# ROLE
# W realnej aplikacji najlepiej trzymać je w bazie danych
# albo pobierać z Microsoft Entra ID.
# --------------------------------------------------

ADMINS = {
    "admin@firma.pl",
    "jan.kowalski@firma.pl",
}

if email.lower() in ADMINS:
    role = "admin"
else:
    role = "user"


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.title("Portal")

    st.write(f"👤 **{name}**")
    st.caption(email)

    st.write(f"Rola: **{role}**")

    st.divider()

    if role == "admin":
        page = st.radio(
            "Menu",
            [
                "Strona główna",
                "Raporty",
                "Panel administratora",
            ]
        )

    else:
        page = st.radio(
            "Menu",
            [
                "Strona główna",
                "Raporty",
            ]
        )

    st.divider()

    if st.button("Wyloguj"):
        st.logout()


# --------------------------------------------------
# STRONA GŁÓWNA
# --------------------------------------------------

if page == "Strona główna":

    st.title(f"Witaj, {name} 👋")

    st.write(
        "Jesteś zalogowany swoim kontem Microsoft 365."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Użytkownik",
            name
        )

    with col2:
        st.metric(
            "Rola",
            role
        )

    with col3:
        st.metric(
            "Status",
            "Zalogowany"
        )


# --------------------------------------------------
# RAPORTY
# --------------------------------------------------

elif page == "Raporty":

    st.title("📊 Raporty")

    st.write(
        "Ta strona jest dostępna zarówno dla "
        "administratorów, jak i zwykłych użytkowników."
    )

    st.dataframe(
        {
            "Miesiąc": [
                "Styczeń",
                "Luty",
                "Marzec",
            ],
            "Sprzedaż": [
                120000,
                135000,
                148000,
            ],
        }
    )


# --------------------------------------------------
# ADMIN
# --------------------------------------------------

elif page == "Panel administratora":

    # dodatkowa ochrona
    if role != "admin":
        st.error("Nie masz uprawnień do tej strony.")
        st.stop()

    st.title("⚙️ Panel administratora")

    st.success(
        "Ten ekran widzi tylko administrator."
    )

    st.subheader("Użytkownicy")

    st.dataframe(
        {
            "Użytkownik": [
                "Anna Nowak",
                "Jan Kowalski",
                "Adam Wiśniewski",
            ],
            "Rola": [
                "user",
                "admin",
                "user",
            ],
        }
    )

    st.subheader("Operacje administracyjne")

    if st.button("Wyczyść cache"):
        st.cache_data.clear()
        st.success("Cache został wyczyszczony.")
