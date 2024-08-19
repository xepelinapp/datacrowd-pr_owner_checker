# PR  Owner Checker

## Qué es esto?
El GHA Owner Checker es una pequeña utilidad en Python que revisa el usuario que envía un PR, y, si **no** es un usuario válido para lanzar un PR hacia ramas protegidas (`devel`, `main`), detiene la acción donde este programa está implementado.

## Qué problema resuelve?
El problema inicial se produce en repositorios con chequeos costosos: en este momento, cualquier usuario registrado en la organización objetivo, puede enviar un Pull Request hacia ramas protegidas. Esto lanza acciones costosas, tanto en tiempo como en recursos computacionales. En ese sentido, lo que buscamos resolver es la ejecución de estas acciones costosas y atajarlas a tiempo.

## ⚠️ ESTA VERSIÓN ES UNA POC EN ESTADO BETA DE DESARROLLO ⚠️
El desarrollo de **PR Owner Checker** está en **etapa beta de prueba de concepto**. Es por ello que, en este punto, los cambios que se introduzcan ⚠️**pueden no ser retrocompatibles**⚠️. Tengan en consideración esto a la hora de revisar e implementar esta GitHub Action.

## Cómo usarlo?

### Tech stack
Esta aplicación tiene el siguiente stack:

* Lenguaje: Python 3.10
* Contenerización: Docker (a través de `Dockerfile`)
* Requisitos:
    * `gh` CLI/API instalado y configurado (se configura en tiempo de compilación)
    * Una llave de acceso a GitHub y la organización y repositorios objetivo (se entrega a la GitHub Action como input; ver `action.yml`)

### Instalación y revisión de código
Para instalar la aplicación, es necesario:

1. Clonar el repositorio en un ambiente local
```bash
git clone https://github.com/jtapia-xepelin/pr_owner_checker.git
cd datacrowd-github_actions_owner_checker
```

2. Crear un ambiente virtual de Python en la carpeta recién creada.
    * En este ejemplo, lo crearemos usando `virtualenv`, con el nombre "`venv`"
```bash
virtualenv venv --python 3.10
```

3. Activar el ambiente virtual
    * En este ejemplo, usaremos el nombre de ambiente virtual "`venv`"
```bash
source venv/bin/activate
```

4. Instalar las dependencias
```bash
pip install -r requirements.txt
```

5. Revisar el código en la carpeta `src/`. Al ser una GitHub Action en forma, no es posible ejecutarla en local, sólo en GitHub.

### Output esperado
Cuando se ejecuta la aplicación, se obtiene un output similar al siguiente:

```bash
Run jtapia-xepelin/pr_owner_checker@test-branch
2023-11-25 16:28:14,109 || 1:MainProcess > logger.py - info || INFO :: Getting team members from 'data-crowd' on GitHub teams for org 'xepelinapp'...
2023-11-25 16:28:14,284 || 1:MainProcess > logger.py - info || INFO :: Proceeding...
2023-11-25 16:28:14,284 || 1:MainProcess > logger.py - info || INFO :: Getting PR info for PR #1 on repo 'xepelinapp/dbt-dw-data-team'...
2023-11-25 16:28:14,655 || 1:MainProcess > logger.py - info || INFO :: PR author: daniel-castelblanco-xepelin; is PR author valid? True
2023-11-25 16:28:14,655 || 1:MainProcess > logger.py - info || INFO :: True
```

## (POC) Gaps
Dado que esta herramienta está en etapa de POC, existen los siguientes gaps a cerrar en su desarrollo final:

- [x] El Owner Checker debe ejecutarse sobre una GitHub Action, no sobre un ambiente local
- [x] El Owner Checker debe tomar la información del Pull Request en curso
- [ ] El Owner Checker debe ser capaz de recopilar información de varios equipos de `GitHub/xepelinapp`
- [ ] El Owner Checker debe ser capaz de entregar retroalimentación a un Pull Request
- [ ] El Owner Checker debe ser capaz de tomar acciones sobre un Pull Request

## TODO/WIP

- [x] Probar el Owner Checker sobre un ambiente de GHA Local
- [x] Probar el Owner Checker sobre un ambiente de GHA remoto
- [x] Probar que el Owner Checker obtenga las características del PR actual
- [ ] Desarrollar la obtención de datos de varios equipos
- [ ] Desarrollar la toma de decisiones sobre un PR
- [ ] Desarrollar la entrega de retroalimentación sobre un PR

## Pregus? Problemas?
Si tienes preguntas o problemas o quieres iniciar una conversación sobre este programa, puedes abrir [un Issue en GitHub](https://github.com/jtapia-xepelin/pr_owner_checker/issues).
