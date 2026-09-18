import streamlit as st
import yt_dlp

st.set_page_config(page_title="Baixador de Virais", layout="centered")

st.title("🔥 Viral Finder")

# Escolha do Nicho no iPhone
nicho = st.text_input("Digite o nicho desejado:", "Futebol")
limite = st.slider("Quantidade de vídeos:", 1, 5, 3)

if st.button("Buscar Vídeos"):
    st.info(f"Buscando vídeos de **{nicho}**...")
    
    ydl_opts_search = {
        'extract_flat': True,
        'quiet': True,
    }
    
    query = f"ytsearch{limite}:{nicho} shorts"
    
    with yt_dlp.YoutubeDL(ydl_opts_search) as ydl:
        resultado = ydl.extract_info(query, download=False)
        
    if 'entries' in resultado:
        for index, video in enumerate(resultado['entries']):
            title = video.get('title', 'Vídeo sem título')
            url = video.get('url') or f"https://www.youtube.com/watch?v={video.get('id')}"
            
            st.markdown(f"### {index + 1}. {title}")
            st.write(f"🔗 [Abrir no YouTube]({url})")
            
            # Botão de download direto no iPhone
            ydl_opts = {
                'format': 'best[ext=mp4]/best',
                'quiet': True,
            }
            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl_down:
                    info = ydl_down.extract_info(url, download=False)
                    direct_download_url = info.get('url')
                    if direct_download_url:
                        st.link_button(f"⬇️ Baixar Vídeo {index + 1}", direct_download_url)
            except Exception as e:
                st.error("Não foi possível gerar o link direto.")
            st.divider()
