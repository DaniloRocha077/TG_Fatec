import time
import streamlit as st
import pydantic
from connection.database import buscar_trabalhos

# Configurações da página
st.set_page_config(page_title="Buscar", page_icon="📤")
st.write("""
# Buscar Temas e palavras-chave
""")

st.markdown("Aqui você poderá buscar o seu tema ou palavra chave para saber se no banco de dados da Fatec Mogi Mirim já existe um trablho com o mesmo tema ou ter idéias para novos temas")

# Criar um container para exibir os resultados da busca
with st.form("form_busca"):
    st.header("Busca de trabalhos")

    # Criar os campos para a busca
    palavra_chave = st.text_input("Digite a palavra chave do seu trabalho ou que deseja procurar")

    # Criar um botão para realizar a busca
    buscar = st.form_submit_button("Buscar")
    if buscar:
        with st.spinner('Procurando...'):
            time.sleep(3)
            st.success('Busca Finalizada!')

        # Exibir os resultados da busca
        resultados = buscar_trabalhos(palavra_chave)
        if len(resultados) == 0:
            st.error("Nenhum resultado encontrado.")
        else:
            container = st.container()
            with container:
                st.header("Resultados da busca")
                for resultado in resultados:
                    with st.expander(f"{resultado[3]} ({resultado[5]})(Palavra-chave: {resultado[7]}) - clique para visualizar o resumo, introdução e conclusão"):
                        class TextoJustificado(pydantic.BaseModel):
                            st.subheader("Resumo")
                            text: str
                        text = resultado[6]
                        justified_text = f'<div style="text-align: justify">{text}</div>'
                        st.markdown(justified_text, unsafe_allow_html=True)
                        st.write("Palavras-chave:", resultado[7])
                        class TextoJustificado(pydantic.BaseModel):
                            st.subheader("Introdução")
                            text: str
                        text = resultado[8]
                        justified_text = f'<div style="text-align: justify">{text}</div>'
                        st.markdown(justified_text, unsafe_allow_html=True)
                        class TextoJustificado(pydantic.BaseModel):
                            st.subheader("Consideraçõs Finais")
                            text: str
                        text = resultado[9]
                        justified_text = f'<div style="text-align: justify">{text}</div>'
                        st.markdown(justified_text, unsafe_allow_html=True)