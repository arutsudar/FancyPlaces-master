
package com.gabm.fancyplaces.functional;

import android.graphics.Bitmap;
import android.os.AsyncTask;

import com.gabm.fancyplaces.data.ImageFile;

public class ImageFileLoaderTask extends AsyncTask<ImageFile, Void, Bitmap> {
    private OnImageLoaderCompletedListener onImageLoaderCompletedListener = null;

    public ImageFileLoaderTask(OnImageLoaderCompletedListener imageLoaderCompletedListener) {
        // Use a WeakReference to ensure the ImageView can be garbage collected
        onImageLoaderCompletedListener = imageLoaderCompletedListener;
    }

    // Decode image in background.
    @Override
    protected Bitmap doInBackground(ImageFile... data) {
        return data[0].loadThumbnail();
    }

    // Once complete, see if ImageView is still around and set bitmap.
    @Override
    protected void onPostExecute(Bitmap bitmap) {
        if (bitmap != null) {

            if (onImageLoaderCompletedListener != null)
                onImageLoaderCompletedListener.onImageLoaderCompleted(bitmap);
        }
    }

    public interface OnImageLoaderCompletedListener {
        void onImageLoaderCompleted(Bitmap bitmap);
    }
}
