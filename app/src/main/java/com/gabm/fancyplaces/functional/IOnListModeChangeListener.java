

package com.gabm.fancyplaces.functional;

public interface IOnListModeChangeListener {
    int MODE_NORMAL = 0;
    int MODE_MULTI_SELECT = 1;

    void onListModeChange(int newMode);
}
