from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.base import Runnable
from langchain_core.runnables.history import RunnableWithMessageHistory

message_history = ChatMessageHistory()

def add_chat_history(runnable: Runnable):
    return RunnableWithMessageHistory(
        runnable,
        lambda _: message_history,
        input_messages_key="input",
        history_messages_key="chat_history",
    )
