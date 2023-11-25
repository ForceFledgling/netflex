#!/bin/bash

# Удаляем предыдущие сборки
rm -rf dist/*

# Создаем дистрибутив asyncio-telnet
python3 setup.asyncio_telnet.py sdist

# Создаем дистрибутив asyncio-telnet
python3 setup.netflex.py sdist

# Используем twine для публикации
twine upload dist/*
