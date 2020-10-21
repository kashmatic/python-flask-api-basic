# python-flask-api-basic

```
export FLASK_CONFIG='development'
export FLASK_APP=run.py

flask db init
flask db migrate
flask db upgrade
```


API calls

Get all players
```
GET /players
[
    {
        "uuid": "0cacd2cc-e6b9-4f76-9481-69d43ce1dc88",
        "team": "SeattleSeahawks",
        "name": "RussellWilson"
    }
]
```

A player
```
GET /player?0cacd2cc-e6b9-4f76-9481-69d43ce1dc88
POST /player?name=RyanTannehill&team=MiamiDolphins
PUT /player?uuid=76a7ab24-c8f2-4a95-aee0-ecbaa355085e&name=RyanTannelhill&team=TennesseeTitans
DELETE /player?uuid=76a7ab24-c8f2-4a95-aee0-ecbaa355085e
```
