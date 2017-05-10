

package com.gabm.fancyplaces.functional.io;

import com.gabm.fancyplaces.data.FancyPlace;

import java.io.File;
import java.util.List;

public interface IImporter {
    List<FancyPlace> ReadFancyPlaces(String fileName);
}
