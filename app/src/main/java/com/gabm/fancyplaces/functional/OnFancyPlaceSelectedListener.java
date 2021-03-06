
package com.gabm.fancyplaces.functional;

public interface OnFancyPlaceSelectedListener {
    int INTENT_VIEW = 0;
    int INTENT_EDIT = 1;
    int INTENT_DELETE = 2;
    int INTENT_SHARE = 3;
    int INTENT_CREATE_NEW = 4;
    int INTENT_EXPORT_TO_GPX = 5;

    void onFancyPlaceSelected(int id, int intent);
}
