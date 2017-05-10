

package com.gabm.fancyplaces.functional;

import android.widget.ArrayAdapter;

import com.gabm.fancyplaces.data.FancyPlace;
import com.gabm.fancyplaces.ui.OsmMarker;

public interface IMapHandler {
    void setCamera(double lat, double lng, float zoom);

    void animateCamera(double lat, double lng, int duration);

    void animateCamera(double lat, double lng, float zoom, int duration);

    void clearMarkers();

    void removeMarker(OsmMarker markerToRemove);

    void addMarker(double lat, double lng, String text, boolean showInfoWindow);

    void setCurrentLocationMarker(double lat, double lng, String title);

    void setAdapter(ArrayAdapter<FancyPlace> in_adapter);

}
