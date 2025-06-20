from fastapi import APIRouter
import numpy as np

router = APIRouter()

@router.get("")
def hello_world() -> dict:
    return {"msg": "Hello, World!"}

@router.get("/matrix")
def matrix_mult() -> dict:
    a = np.random.randint(0, 10, (10, 10)).tolist()
    b = np.random.randint(0, 10, (10, 10)).tolist()
    product = (np.dot(a, b)).tolist()
    return {
        "matrix_a": a,
        "matrix_b": b,
        "product": product
    }
