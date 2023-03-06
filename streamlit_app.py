import streamlit as st
import pydeck as pdk

st.set_page_config(page_title='My MapFrappe', layout='wide', page_icon=':world_map:')


# Streamlit application
def main():
    st.header("""My MapFrappe""")
    col1, col2 = st.columns(2)
    with col1:
        map_style = st.selectbox(
            'Select map style',
            (
                "mapbox://styles/mapbox/streets-v12",
                "mapbox://styles/mapbox/satellite-v9",
                "mapbox://styles/mapbox/light-v11",
                "mapbox://styles/mapbox/satellite-streets-v12",
                "mapbox://styles/mapbox/navigation-night-v1"
            ))

    with col2:
        zoom = st.slider('Set zoom: <- country - city - house ->', 8, 19, 11)

    col3, col4, col5 = st.columns([1, 1, 2])
    with col3:
        coord_left = st.text_input('Coordinates left', '48.783333, 9.183333')

    with col4:
        coord_right = st.text_input('Coordinates right', '46.65581, 32.6178')

    with col5:
        diameter = st.slider('Set diameter, km', 0, 50, 0, 1)

    [lat_l, lon_l] = [round(float(x.strip()), 6) for x in coord_left.split(',')]
    [lat_r, lon_r] = [round(float(x.strip()), 6) for x in coord_right.split(',')]

    col6, col7 = st.columns(2)
    with col6:
        st.pydeck_chart(
            pdk.Deck(
                map_style=map_style,
                initial_view_state=pdk.ViewState(
                    latitude=lat_l,
                    longitude=lon_l,
                    zoom=zoom
                ),
                layers=[
                    pdk.Layer(
                        "ScatterplotLayer",
                        data=[lon_l, lat_l],
                        get_position=[lon_l, lat_l],
                        get_fill_color=[255, 140, 0, 50],
                        get_line_color=[0, 0, 0],
                        get_radius=(diameter * 1000) / 2
                    ),
                ],
            )
        )

    with col7:
        st.pydeck_chart(
            pdk.Deck(
                map_style=map_style,
                initial_view_state=pdk.ViewState(
                    latitude=lat_r,
                    longitude=lon_r,
                    zoom=zoom
                ),
                layers=[
                    pdk.Layer(
                        "ScatterplotLayer",
                        data=[lon_r, lat_r],
                        get_position=[lon_r, lat_r],
                        get_fill_color=[255, 140, 0, 50],
                        get_line_color=[0, 0, 0],
                        get_radius=(diameter * 1000) / 2
                    ),
                ],
            )
        )


if __name__ == '__main__':
    main()
