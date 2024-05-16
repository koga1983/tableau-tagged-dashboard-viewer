import streamlit as st
import tableauserverclient as TSC

# Load Tableau Server credentials
token_name = st.secrets["tableau"]["token_name"]
personal_access_token = st.secrets["tableau"]["personal_access_token"]
site_id = st.secrets["tableau"]["site_id"]
server_url = st.secrets["tableau"]["server_url"]

# Tableau Server client authentication
tableau_auth = TSC.PersonalAccessTokenAuth(token_name, personal_access_token, site_id)
server = TSC.Server(server_url, use_server_version=True)

@st.cache_data(ttl=600)
def get_tags():
    tags = []
    with server.auth.sign_in(tableau_auth):
        for workbook in TSC.Pager(server.workbooks.get):
            tags.extend(workbook.tags)
    return list(set(tags))  # Remove duplicates and convert to list

@st.cache_data(ttl=600)
def get_dashboards(selected_tag=None):
    dashboards = []
    with server.auth.sign_in(tableau_auth):
        req_option = TSC.RequestOptions()
        if selected_tag:
            req_option.filter.add(
                TSC.Filter(TSC.RequestOptions.Field.Tags, TSC.RequestOptions.Operator.Equals, selected_tag))
        for workbook in TSC.Pager(server.workbooks.get, req_option):
            server.workbooks.populate_views(workbook)
            for view in workbook.views:
                view_content_url = view.content_url.replace('/sheets', '')
                dashboards.append({
                    "workbook_name": workbook.name,
                    "view_name": view.name,
                    "view_url": view_content_url,
                    "owner": workbook.owner_id,
                    "updated_at": workbook.updated_at
                })
    return dashboards
