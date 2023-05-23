import streamlit as st

# Configurações da página
st.set_page_config(page_title="Manuais e Documentação", page_icon="📤")
# file_path = (
#   "Templates/ADS_TG_2S2022_Nome_Aluno_data_Anexo_X_Autorizacao_publicacao_um_autor.docx")
st.markdown("### 🤔 Está com dúvida na estrutura ou na formatação do trabalho!")
st.markdown("Faça download do manual de formatação de trabalho, estrutura do TG(TCC), formalização, autorização e declaração")

def download_and_show_file(label, file_path, name):
    with open(file_path, 'rb') as f:
        data = f.read()
    st.download_button(label=label,
                       data=data,
                       file_name=name,
                       mime='application/vnd.openxmlformats-officedocument.wordprocessingml.document')


if st.button('Formalização'):
    label = "Formalização - TG1"
    file_path = "Templates/Formalizacao_TG1.docx"
    file_name = "Formalizacao_TG1.docx"
    download_and_show_file(label, file_path, file_name)

    label1 = "Formalização - TG2"
    file_path1 = "Templates/Formalizacao_TG2.docx"
    file_name1 = "Formalizacao_TG2.docx"
    download_and_show_file(label1, file_path1, file_name1)

if st.button('Manual TG'):
    label = "Manual - TG"
    file_path = "Templates/Manual_de_Formatação.pdf"
    file_name = "Manual_de_Formatação.pdf"
    download_and_show_file(label, file_path, file_name)


if st.button('Autorização para Publicação'):
    label = "Autorização 1 Autor"
    file_path = "Templates/ADS_TG_2S2022_Nome_Aluno_data_Anexo_X_Autorizacao_publicacao_um_autor.docx"
    file_name = "ADS_TG_2S2022_Nome_Aluno_data_Anexo_X_Autorizacao_publicacao_um_autor.docx"
    download_and_show_file(label, file_path, file_name)

    label1 = "Autorização 2 ou mais Autores"
    file_path1 = "Templates/ADS_TG_2S2022_Nome_Alunos1-2-3-data_Anexo_X_Autorizacao_para_publicacao_dois_ou_mais_autores.docx"
    file_name1 = "ADS_TG_2S2022_Nome_Alunos1-2-3-data_Anexo_X_Autorizacao_para_publicacao_dois_ou_mais_autores.docx"
    download_and_show_file(label1, file_path1, file_name1)

if st.button('Orientações Gerais para TG'):
    label = "Orientações TG"
    file_path = "Templates/OrientacoesGeraisTG_ADS.pdf"
    file_name = "OrientacoesGeraisTG_ADS.pdf"
    download_and_show_file(label, file_path, file_name)

if st.button('Declaração de Inexistência de Plágio'):
    label = "Declaração"
    file_path = "Templates/ADS_TG_2S2022_Nome_Aluno_data_Anexo_X_Declaracao_de_inexistencia_de_plagio_um_autor.docx"
    file_name = "ADS_TG_2S2022_Nome_Aluno_data_Anexo_X_Declaracao_de_inexistencia_de_plagio_um_autor.docx"
    download_and_show_file(label, file_path, file_name)

if st.button('Autorização de Uso de Nome'):
    label = "Termo de Autorização"
    file_path = "Templates/TERMO_DE_AUTORIZAO_DE_USO_DE_NOME.docx"
    file_name = "TERMO_DE_AUTORIZAO_DE_USO_DE_NOME.docx"
    download_and_show_file(label, file_path, file_name)