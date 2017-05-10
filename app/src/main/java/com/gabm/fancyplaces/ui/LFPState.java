
package com.gabm.fancyplaces.ui;

import android.os.Parcel;
import android.os.Parcelable;

import com.gabm.fancyplaces.data.ImageFile;

public class LFPState implements Parcelable {
    public int mode = 1;
    public ImageFile OriginalImageFile = null;
    public int curMenu = 0;

    LFPState() {
    }

    LFPState(Parcel in) {
        mode = in.readInt();
        OriginalImageFile = in.readParcelable(ImageFile.class.getClassLoader());
        curMenu = in.readInt();
    }

    @Override
    public int describeContents() {
        return 0;
    }

    @Override
    public void writeToParcel(Parcel dest, int flags) {
        dest.writeInt(mode);
        dest.writeParcelable(OriginalImageFile, flags);
        dest.writeInt(curMenu);

    }
}
