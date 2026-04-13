from fastapi import APIRouter, HTTPException, status
from motor.motor_asyncio import AsyncIOMotorDatabase
from models.contact import ContactMessage, ContactMessageCreate
import logging

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/contact", tags=["contact"])

@router.post("", response_model=ContactMessage, status_code=status.HTTP_201_CREATED)
async def create_contact_message(message: ContactMessageCreate, db: AsyncIOMotorDatabase):
    """
    Create a new contact message
    """
    try:
        contact_message = ContactMessage(**message.dict())
        result = await db.contact_messages.insert_one(contact_message.dict())
        
        logger.info(f"Contact message created: {contact_message.id} from {contact_message.email}")
        
        return contact_message
    except Exception as e:
        logger.error(f"Error creating contact message: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to save contact message"
        )

@router.get("/messages", response_model=list[ContactMessage])
async def get_contact_messages(db: AsyncIOMotorDatabase, limit: int = 50, skip: int = 0):
    """
    Get all contact messages (admin endpoint)
    """
    try:
        messages = await db.contact_messages.find().sort("created_at", -1).skip(skip).limit(limit).to_list(limit)
        return [ContactMessage(**msg) for msg in messages]
    except Exception as e:
        logger.error(f"Error fetching contact messages: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch contact messages"
        )