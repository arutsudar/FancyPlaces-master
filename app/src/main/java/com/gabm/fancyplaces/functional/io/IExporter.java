
package com.gabm.fancyplaces.functional.io;

import com.gabm.fancyplaces.data.FancyPlace;

import java.io.File;
import java.util.List;

public interface IExporter {
    boolean WriteToFile(List<FancyPlace> fpList, String fileNameWithExt);

    boolean WriteToFile(FancyPlace fancyPlace, String fileNameWithExt);
}
