from fastapi import APIRouter, Depends,HTTPException
from app.database import session_local
from sqlalchemy.orm import Session
from app.models.tenant import tenant
from app.schemas.tenant import tenantcreate,tenantResponse,tenantupdate
from sqlalchemy.exc import IntegrityError

router=APIRouter(prefix="/api/v1/tenants",tags=["tenants"])

def get_db():
    db=session_local()
    try:
        yield db
    finally:
        db.close()
        
@router.post("/",response_model=tenantResponse,status_code=201)
def tenant_create(tenant_data:tenantcreate,db:Session =Depends(get_db)):
    
    tenant_form= tenant(
        name=tenant_data.name,
        email=tenant_data.email,
        phone=tenant_data.phone,
    )
    
    db.add(tenant_form)
    try:
        db.commit()
        db.refresh(tenant_form)
    except IntegrityError:
        db.rollback()
        raise  HTTPException(status_code=400, detail="email already exists")
    
    return tenant_form


@router.get("/")
def gettenants(db:Session=Depends(get_db)):
    tenantall=db.query(tenant).all()
    
    return tenantall

@router.get("/{tenant_id}",response_model=tenantResponse)
def tenantbyid(tenant_id:int,db: Session=Depends(get_db)):
    singletenant=db.query(tenant).filter(tenant.id==tenant_id).first()
    if singletenant is None:
        raise HTTPException(status_code=404,detail="not found")
        
    return singletenant

@router.post("/{tenant_id}",response_model=tenantupdate)
def tenantupdate(tenant_id:int,tenant_data:tenantupdate,db:Session=Depends(get_db)):
    singletenant=db.query(tenant).filter(tenant.id==tenant_id).first()
    
    if singletenant is None:
        raise HTTPException(status_code=404,detail="not found")
    
    tenant_updated=tenant_data.model_dump(exclude_unset=True)
    
    for field,value in tenant_updated.items():
        setattr(singletenant,field,value)
        
    db.commit()
    db.refresh(singletenant)
    
    return singletenant
    
    
@router.post("/delete_tenant/{tenant_id}")
def tenant_delete(tenant_id:int,db:Session=Depends(get_db)):
    single_tenant=db.query(tenant).filter(tenant.id==tenant_id).first()
    
    if single_tenant is None:
       raise HTTPException(status_code=404,detail="it is not found")
        
    single_tenant.is_active= False
    
    db.commit()
    db.refresh(single_tenant)
    
    return f"{single_tenant.name} is deleted"