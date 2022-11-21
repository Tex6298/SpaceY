for index in launch_sites_df.index:
    launch_site_lat = launch_sites_df['Lat'][index]
    launch_site_lon = launch_sites_df['Long'][index]
    sites = launch_sites_df['Launch Site'][index]
   
    for site, targets in site_dict.items():
        if site == sites:
            i=0
            for target in targets:
                target_lat = target[0]
                target_lon = target[1]
                distance_target = calculate_distance(launch_site_lat, launch_site_lon, target_lat, target_lon)
                coordinates = [launch_site_lat, launch_site_lon], [target_lat, target_lon]
                lines=folium.PolyLine(locations=coordinates, weight=1)
                coordinate = [target_lat,target_lon]
                print("Distance of ", site, " to ", location[i],":", distance_target, "km")
                i+=1
                distance_marker = folium.Marker(
                    coordinate,
                    icon=DivIcon(
                    icon_size=(20,20),
                icon_anchor=(0,0),
                html='<div style="font-size: 12; color:#d35400;"><b>%s</b></div>' % "{:10.2f} KM".format(distance_target),
                    )
                )
                site_map.add_child(distance_marker)
                site_map.add_child(lines)


