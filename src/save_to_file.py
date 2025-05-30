import json
import logging

logger = logging.getLogger("save_to_file")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('logs/save_to_file.log', mode='a', encoding="utf-8", delay=False)
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s)')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def save_to_file(data: list, file_path: str) -> None :
    """Сохранение данных по указанному пути"""
    try:
        logger.info(f'Записываем данные в файл {file_path}')
        with open(file_path, 'w', encoding='utf-8') as data_file:
            json.dump(data, data_file)
    except Exception as ex:
        logger.error(f"Произошла ошибка: {ex}")

