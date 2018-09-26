from google.cloud import datastore
from flask import current_app
from datetime import datetime

builtin_list = list


def get_client():
    return datastore.Client(current_app.config['PROJECT_ID'], namespace=current_app.config['NAMESPACE'])


def from_datastore(entity):
    """Translates Datastore results into the format expected by the
    application.
    Datastore typically returns:
        [Entity{key: (kind, id), prop: val, ...}]
    This returns:
        {id: id, prop: val, ...}
    """
    if not entity:
        return None
    if isinstance(entity, builtin_list):
        entity = entity.pop()

    entity['id'] = entity.key.name
    return entity


def db_list(kind, limit=10, cursor=None):
    ds = get_client()

    query = ds.query(kind=kind)
    query_iterator = query.fetch(limit=limit, start_cursor=cursor)
    page = next(query_iterator.pages)

    entities = builtin_list(map(from_datastore, page))
    next_cursor = (
        query_iterator.next_page_token.decode('utf-8')
        if query_iterator.next_page_token else None)

    return (None if len(entities) == 0 else entities[0]), next_cursor


def db_list_by_filter(kind, prop, operator, value, limit=10, cursor=None):
    ds = get_client()

    query = ds.query(kind=kind)
    query.add_filter(prop, operator, value)
    query_iterator = query.fetch(limit=limit, start_cursor=cursor)
    page = next(query_iterator.pages)

    entities = builtin_list(map(from_datastore, page))
    next_cursor = (
        query_iterator.next_page_token.decode('utf-8')
        if query_iterator.next_page_token else None)

    return (None if len(entities) == 0 else entities[0]), next_cursor


def db_read(kind, id):
    ds = get_client()
    key = ds.key(kind, id)
    results = ds.get(key)
    return from_datastore(results)


def db_update(kind, data):
    ds = get_client()
    key = ds.key(kind, data['id'])

    entity = datastore.Entity(
        key=key)

    data['updated_at'] = datetime.utcnow()
    entity.update(data)
    ds.put(entity)
    return from_datastore(entity)

def db_get_embedded_entity(kind):
    ds = get_client()
    key = ds.key(kind)

    entity = datastore.Entity(
        key=key)
    return entity


def db_create(kind, data):
    ds = get_client()
    key = ds.key(kind, data['id'])

    entity = datastore.Entity(
        key=key)

    now = datetime.utcnow()
    data['updated_at'] = now
    entity.update(data)
    ds.put(entity)
    return from_datastore(entity)


def db_delete(kind, id):
    ds = get_client()
    key = ds.key(kind, id)
    ds.delete(key)
