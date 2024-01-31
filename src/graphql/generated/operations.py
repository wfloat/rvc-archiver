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


def mutation_create_voice_model_profile():
    _op = sgqlc.operation.Operation(
        _schema_root.mutation_type,
        name="CreateVoiceModelProfile",
        variables=dict(
            input=sgqlc.types.Arg(
                sgqlc.types.non_null(_schema.CreateVoiceModelProfileInput)
            )
        ),
    )
    _op_create_voice_model_profile = _op.create_voice_model_profile(
        input=sgqlc.types.Variable("input")
    )
    _op_create_voice_model_profile.id()
    _op_create_voice_model_profile.name()
    _op_create_voice_model_profile.voice_model_id()
    return _op


class Mutation:
    create_aihub_voice_model = mutation_create_aihub_voice_model()
    create_voice_model_backup_url = mutation_create_voice_model_backup_url()
    create_voice_model_profile = mutation_create_voice_model_profile()


def query_aihub_voice_models():
    _op = sgqlc.operation.Operation(
        _schema_root.query_type,
        name="AIHubVoiceModels",
        variables=dict(after=sgqlc.types.Arg(_schema.String)),
    )
    _op_aihub_voice_models = _op.aihub_voice_models(
        first=100, min_download_count=75, after=sgqlc.types.Variable("after")
    )
    _op_aihub_voice_models_page_info = _op_aihub_voice_models.page_info()
    _op_aihub_voice_models_page_info.end_cursor()
    _op_aihub_voice_models_page_info.has_next_page()
    _op_aihub_voice_models_page_info.has_previous_page()
    _op_aihub_voice_models_page_info.start_cursor()
    _op_aihub_voice_models_edges = _op_aihub_voice_models.edges()
    _op_aihub_voice_models_edges_node = _op_aihub_voice_models_edges.node()
    _op_aihub_voice_models_edges_node.download_count()
    _op_aihub_voice_models_edges_node.filename()
    _op_aihub_voice_models_edges_node.name()
    _op_aihub_voice_models_edges_node.checksum_md5_for_weights()
    _op_aihub_voice_models_edges_node_inferred_profile = (
        _op_aihub_voice_models_edges_node.inferred_profile()
    )
    _op_aihub_voice_models_edges_node_inferred_profile.accent()
    _op_aihub_voice_models_edges_node_inferred_profile.confidence()
    _op_aihub_voice_models_edges_node_inferred_profile.fictional()
    _op_aihub_voice_models_edges_node_inferred_profile.gender()
    _op_aihub_voice_models_edges_node_inferred_profile.id()
    _op_aihub_voice_models_edges_node_inferred_profile.model_trained_on_english_probability()
    _op_aihub_voice_models_edges_node_inferred_profile.name()
    _op_aihub_voice_models_edges_node_inferred_profile.native_language()
    _op_aihub_voice_models_edges_node_inferred_profile.relevant_tags()
    _op_aihub_voice_models_edges_node_inferred_profile.voice_model_id()
    return _op


def query_aihub_voice_model_using_checksum_md5_for_weights():
    _op = sgqlc.operation.Operation(
        _schema_root.query_type,
        name="AIHubVoiceModelUsingChecksumMD5ForWeights",
        variables=dict(checksumMD5ForWeights=sgqlc.types.Arg(_schema.String)),
    )
    _op_aihub_voice_model = _op.aihub_voice_model(
        checksum_md5_for_weights=sgqlc.types.Variable("checksumMD5ForWeights")
    )
    _op_aihub_voice_model.creator_text()
    _op_aihub_voice_model.download_count()
    _op_aihub_voice_model.id()
    _op_aihub_voice_model.filename()
    _op_aihub_voice_model.name()
    _op_aihub_voice_model.version()
    _op_aihub_voice_model.derived_model_id()
    _op_aihub_voice_model.checksum_md5_for_weights()
    return _op


class Query:
    aihub_voice_model_using_checksum_md5_for_weights = (
        query_aihub_voice_model_using_checksum_md5_for_weights()
    )
    aihub_voice_models = query_aihub_voice_models()


class Operations:
    mutation = Mutation
    query = Query
