"""Project pipelines."""

from data.weatherAUS import find_pipelines
from kedro.pipeline import Pipeline
from src.weather_aus.pipelines import pipeline as exploracion_inicial_pipeline


def register_pipelines() -> dict[str, Pipeline]:
    pipelines = {
        "exploracion_inicial": exploracion_inicial_pipeline.create_pipeline(),
    }
    pipelines["__default__"] = pipelines["exploracion_inicial"]
    return pipelines
