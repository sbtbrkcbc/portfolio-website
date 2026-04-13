from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import FileResponse
import os
import logging

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/cv", tags=["cv"])

CV_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "static", "cv")

@router.get("/download")
async def download_cv(lang: str = Query(default="en", regex="^(en|it|tr)$")):
    """
    Download CV in specified language
    """
    cv_filename = f"cv_{lang}.pdf"
    cv_path = os.path.join(CV_DIR, cv_filename)
    
    if not os.path.exists(cv_path):
        logger.warning(f"CV file not found: {cv_path}")
        raise HTTPException(
            status_code=404,
            detail=f"CV not available in {lang.upper()} language"
        )
    
    logger.info(f"CV download requested: {lang}")
    
    return FileResponse(
        path=cv_path,
        filename=f"Sabit_Burak_Cebeci_CV_{lang.upper()}.pdf",
        media_type="application/pdf",
        headers={
            "Content-Disposition": f"attachment; filename=Sabit_Burak_Cebeci_CV_{lang.upper()}.pdf"
        }
    )