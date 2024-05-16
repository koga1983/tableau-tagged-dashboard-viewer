import streamlit as st
from utils.tableau import get_tags, get_dashboards
import streamlit.components.v1 as components

# Streamlit settings
st.set_page_config(page_title="Tableau Tagged Dashboard Viewer", layout="wide")

# Title
st.title("Tableau Tagged Dashboard Viewer")

# Fetch tags
tags = get_tags()
selected_tag = st.selectbox('Select a tag to filter dashboards', options=[""] + tags)

# Fetch and display dashboards
if selected_tag:
    dashboards = get_dashboards(selected_tag)
    if dashboards:
        st.subheader("Dashboards List")
        for dashboard in dashboards:
            st.write(f"### {dashboard['workbook_name']} - {dashboard['view_name']}")
            st.write(f"**Owner ID:** {dashboard['owner']}")
            st.write(f"**Last Updated:** {dashboard['updated_at'].strftime('%Y-%m-%d %H:%M:%S')}")

            # Adjust height of the embedded dashboard
            height = st.slider(f'Adjust height for {dashboard["view_name"]}', min_value=600, max_value=1600, value=1000, key=dashboard['view_name'])

            # Embed the dashboard
            server_url = st.secrets["tableau"]["server_url"].rstrip('/')
            site_id = st.secrets["tableau"]["site_id"]
            site_root = f"/t/{site_id}" if site_id else ""
            view_url = f"{server_url}{site_root}/views/{dashboard['view_url']}?:embed=y&:showVizHome=no"
            embed_code = f"""
            <script type="module" src="{server_url}/javascripts/api/tableau.embedding.3.latest.min.js"></script>
            <tableau-viz id='tableau-viz-{dashboard["view_name"]}' src='{view_url}' width='100%' height='{height}' toolbar='bottom'></tableau-viz>
            """
            components.html(embed_code, height=height)
