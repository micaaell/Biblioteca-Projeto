import streamlit as st
import pandas as pd
from views import View
import time

class ListarLivroUI:
  def main():
    st.header("Livros Cadastrados")
    tab_names = ["Listar","Listar por gênero"]
    selected_tab = st.radio("Escolha uma das opções:", tab_names)
    if selected_tab == "Listar":
        ListarLivroUI.listar()
    if selected_tab == "Listar por gênero":
        ListarLivroUI.listarporgenero()

  def listar():
    livros = View.livro_listar()
    if len(livros) == 0:
      st.write("Nenhum livro cadastrado")
    else:
      dic = []
      for obj in livros: dic.append(obj.__dict__)
      df = pd.DataFrame(dic)
      st.dataframe(df)


  def listarporgenero():
    livros = View.livro_listar()
    generos = View.genero_listar()
    idGenero = st.selectbox("Selecione o Gênero", generos)

    
    if len(livros) == 0:
      st.write("Nenhum livro cadastrado")
    else:
      dic = []
      for obj in livros:
        dic.append(obj.__dict__)

    if len(generos) == 0:
      st.write("Nenhum genero cadastrado")
    else:
      dic = []
      for obj in View.livro_listar_genero(idGenero.get_id()):
        dic.append(obj.__dict__)
      df = pd.DataFrame(dic)
      st.dataframe(df)




      
