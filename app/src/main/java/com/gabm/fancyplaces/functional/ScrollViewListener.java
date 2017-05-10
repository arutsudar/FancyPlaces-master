
package com.gabm.fancyplaces.functional;

import com.gabm.fancyplaces.ui.ObservableScrollView;

public interface ScrollViewListener {

    void onScrollChanged(ObservableScrollView scrollView, int x, int y, int oldx, int oldy);

}