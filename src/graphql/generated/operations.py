import sgqlc.types
import sgqlc.operation
from . import schema

_schema = schema
_schema_root = _schema.schema

__all__ = ("Operations",)


def mutation_create_aihub_voice_model():
    _op = sgqlc.operation.Operation(
        _schema_root.mutation_type,
        name="CreateAIHubVoiceModel",
        variables=dict(
            input=sgqlc.types.Arg(
                sgqlc.types.non_null(_schema.CreateAIHubVoiceModelInput)
            )
        ),
    )
    _op_create_aihub_voice_model = _op.create_aihub_voice_model(
        input=sgqlc.types.Variable("input")
    )
    _op_create_aihub_voice_model.id()
    _op_create_aihub_voice_model.name()
    _op_create_aihub_voice_model.version()
    _op_create_aihub_voice_model.filename()
    _op_create_aihub_voice_model.download_count()
    _op_create_aihub_voice_model.derived_model_id()
    _op_create_aihub_voice_model.creator_text()
    return _op


def mutation_create_voice_model_backup_url():
    _op = sgqlc.operation.Operation(
        _schema_root.mutation_type,
        name="CreateVoiceModelBackupUrl",
        variables=dict(
            input=sgqlc.types.Arg(
                sgqlc.types.non_null(_schema.CreateVoiceModelBackupUrlInput)
            )
        ),
    )
    _op_create_voice_model_backup_url = _op.create_voice_model_backup_url(
        input=sgqlc.types.Variable("input")
    )
    _op_create_voice_model_backup_url.id()
    _op_create_voice_model_backup_url.url()
    _op_create_voice_model_backup_url.voice_model_id()
    return _op


class Mutation:
    create_aihub_voice_model = mutation_create_aihub_voice_model()
    create_voice_model_backup_url = mutation_create_voice_model_backup_url()


class Operations:
    mutation = Mutation
