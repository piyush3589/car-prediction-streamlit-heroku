mkdir -p ~/.streamlit/

echo "\
[server]\n\
port = $PORT\n\
headless = true\n\
enableCORS=true\n\
\n\
" > ~/.streamlit/config.toml