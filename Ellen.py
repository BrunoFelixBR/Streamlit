#para rodar: python -m streamlit run Ellen.py
import streamlit as st
import plotly.express as px

st.title("De 0 a 10 quanto você acha que eu te amo? 🤔")
st.subheader("Escolha a opção:")
st.write("Dica: Eu amo muito mesmo")

#escolha = st.radio("Escolha um Gráfico", ["1", "2", "3" , "4" , "5" , "6" , "7" , "8" , "9" , "10"])
escolha = st.radio("Escolha uma das opções abaixo:", ["N/A", 1, 2, 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10])

if escolha == 1:
    st.title("Amoooor, deve ter clicado errado, sabe que eu amo muito mais que isso ai, pode aumentar a nota!!!!!!")

if escolha == 2:
    st.title("Errou, amo muito mais que isso, aumenta ai!")

if escolha == 3:
    st.title("Errou, Sabe que te amo mais do que a minha própria vida né?")

if escolha == 4:
    st.title("Errou, não sabe o que 'Daqui até a eternidade' significa?")

if escolha == 5:
    st.title("Errou, Sabe que eu comprei uma casa contigo né?")

if escolha == 6:
    st.title("Errou, Errou feio, errou rude!")

if escolha == 7:
    st.title("Errou, amo muito mais que isso!")

if escolha == 8:
    st.title("Errou, Essa nota está muito baixa para o quanto eu te amo!")

if escolha == 9:
    st.title("Errou, aiai eu quero que responda com mais sinceridade!")

if escolha == 10:
    st.title("Errou, amo muito mais que isso, amo infinitamente, mas como aqui só vai até 10 eu tenho que usar a nota 10 ❤️")

    st.audio(data="Ellen_audio.wav",format="wav",loop=True)


    st.subheader("Aceita viver comigo pra sempre?")


    escolha_2 = st.radio("Escolha uma das opções", ["N/A", "Não","Sim", "óbvio que sim"])

    if escolha_2 == "óbvio que sim":
        st.title("Ebaaaaaa te amoooooooooo muitoooooooo!!!!!!!!!!!!!!")

    if escolha_2 == "Sim":
        st.title("Ebaaaaaa te amoooooooooo!!!!!!!!!!!!!!")


    if escolha_2 == "Não":
        st.title("Tarde demais, já aceitou casar comigo")

