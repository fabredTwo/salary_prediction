# salary_prediction

Aplicacion web con FastAPI para predecir salario a partir del modelo guardado en `salary_model.pkl`.

La interfaz es un `index.html` estatico y FastAPI expone el endpoint `POST /predict` para calcular la prediccion.

## Ejecutar

Instala dependencias:

```bash
pip install -r requirements.txt
```

Levanta el servidor:

```bash
uvicorn main:app --reload
```

Abre en el navegador:

```text
http://127.0.0.1:8000
```
