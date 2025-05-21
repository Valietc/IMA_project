# Проект IMA_project

## Описание

Этот проект моделирует работу скважины на основе Inflow Performance Relationship (IPR) и включает расчетные и визуализирующие модули.

## Структура проекта

```
IMA_project/
├── main.py                         # Точка входа
├── readme.md                       # Документация
├── requirements.txt                # Зависимости проекта
└── nodal_analysis/
    ├── __init__.py
    ├── nodal_analysis.py           # Основной расчет
    ├── plotting.py                 # Визуализация результатов
    ├── inflow_performance/
    │   ├── __init__.py
    │   └── ipr_model.py            # Классы WellInflow и InvertedWell
    └── outflow_performance/
        ├── __init__.py
        └── vlp_model.py            # Заглушка
```

## Использование

```bash
python main.py
```
