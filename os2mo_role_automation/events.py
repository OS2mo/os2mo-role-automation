# SPDX-FileCopyrightText: Magenta ApS <https://magenta.dk>
# SPDX-License-Identifier: MPL-2.0
from uuid import UUID

from fastapi import APIRouter
from fastramqpi.events import Event

router = APIRouter()


@router.post("/events/ituser")
async def ituser(event: Event[UUID]) -> None:
    print("reconciling", event.subject)
