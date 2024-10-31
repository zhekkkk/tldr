from aiogram import types, F
from aiogram.filters.command import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile
from loader import dp, bot

from summarizer import summarize_text

class Form(StatesGroup):
    waiting_for_document = State()

@dp.message(Command("summarize"))
async def command_summarize(message: types.Message, state: FSMContext):
    await message.answer("waiting for a document to summarize")
    await state.set_state(Form.waiting_for_document)

@dp.message(Form.waiting_for_document, F.content_type==types.ContentType.DOCUMENT)
async def create_summary(message: types.Message, state:FSMContext):
    document = message.document
    file_path = 'files\\downloads\\book.pdf'
    await bot.download(document, destination=file_path)
    summary = summarize_text(file_path)
    output_doc = 'files\\output\\summary.txt'
    with open(output_doc, 'w', encoding='utf-8') as f:
        f.write(summary)
    await message.answer_document(FSInputFile(output_doc))
    await state.clear()
