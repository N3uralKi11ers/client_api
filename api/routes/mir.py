from fastapi import APIRouter
from typing import Optional, List
import random

from schemas import CardMIR

router = APIRouter()


def generate_mir_card() -> str:
    digits = [random.randint(0, 9) for _ in range(16)]
    digits = [str(digit) for digit in digits]
    result = ' '.join(''.join(digits[i:i+4]) for i in range(0, 16, 4))
    return result


def random_color() -> str:
    return random.choice([
        '#00120B', 
        '#395756',
        '#7261A3',
        '#4F5D75',
        '#CF995F',
        '#8C5F66',
        '#CB769E',
    ])


@router.get(
    '/',
    name="MIR cards",
    description="""
    This is a blank for MIR cards
    """,
    response_model=List[CardMIR],
)
def get_mir_cards(
    user: Optional[str] = None
):
    cards: List[CardMIR] = []
    for _ in range(random.randint(1, 9)):
        card_number = generate_mir_card()
        card_color = random_color()

        card = CardMIR(
            card_number=card_number,
            color=card_color
        )

        cards.append(card)
    
    return cards