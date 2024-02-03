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


def mutation_create_voice_model():
    _op = sgqlc.operation.Operation(
        _schema_root.mutation_type,
        name="CreateVoiceModel",
        variables=dict(
            input=sgqlc.types.Arg(sgqlc.types.non_null(_schema.CreateVoiceModelInput))
        ),
    )
    _op_create_voice_model = _op.create_voice_model(input=sgqlc.types.Variable("input"))
    _op_create_voice_model.checksum_md5_for_added()
    _op_create_voice_model.checksum_md5_for_weights()
    _op_create_voice_model.checksum_sha256_for_added()
    _op_create_voice_model.checksum_sha256_for_weights()
    _op_create_voice_model.filesize_for_weights()
    _op_create_voice_model.filesize_for_added()
    _op_create_voice_model.hidden()
    _op_create_voice_model.id()
    _op_create_voice_model.name()
    _op_create_voice_model.processed()
    return _op


def mutation_update_aihub_voice_model():
    _op = sgqlc.operation.Operation(
        _schema_root.mutation_type,
        name="UpdateAIHubVoiceModel",
        variables=dict(
            input=sgqlc.types.Arg(
                sgqlc.types.non_null(_schema.UpdateAIHubVoiceModelInput)
            )
        ),
    )
    _op_update_aihub_voice_model = _op.update_aihub_voice_model(
        input=sgqlc.types.Variable("input")
    )
    _op_update_aihub_voice_model.checksum_md5_for_weights()
    _op_update_aihub_voice_model.creator_text()
    _op_update_aihub_voice_model.derived_model_id()
    _op_update_aihub_voice_model.download_count()
    _op_update_aihub_voice_model.filename()
    _op_update_aihub_voice_model.id()
    _op_update_aihub_voice_model.name()
    _op_update_aihub_voice_model.version()
    return _op


def mutation_create_voice_model_config():
    _op = sgqlc.operation.Operation(
        _schema_root.mutation_type,
        name="CreateVoiceModelConfig",
        variables=dict(
            input=sgqlc.types.Arg(
                sgqlc.types.non_null(_schema.CreateVoiceModelConfigInput)
            )
        ),
    )
    _op_create_voice_model_config = _op.create_voice_model_config(
        input=sgqlc.types.Variable("input")
    )
    _op_create_voice_model_config.artifact_protection()
    _op_create_voice_model_config.audio_resampling()
    _op_create_voice_model_config.f0_curve()
    _op_create_voice_model_config.filter_radius()
    _op_create_voice_model_config.id()
    _op_create_voice_model_config.pitch_extraction_method()
    _op_create_voice_model_config.quality_score()
    _op_create_voice_model_config.search_feature_ratio()
    _op_create_voice_model_config.transpose_pitch()
    _op_create_voice_model_config.voice_model_id()
    _op_create_voice_model_config.volume_envelope_scaling()
    return _op


class Mutation:
    create_aihub_voice_model = mutation_create_aihub_voice_model()
    create_voice_model = mutation_create_voice_model()
    create_voice_model_backup_url = mutation_create_voice_model_backup_url()
    create_voice_model_config = mutation_create_voice_model_config()
    create_voice_model_profile = mutation_create_voice_model_profile()
    update_aihub_voice_model = mutation_update_aihub_voice_model()


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
    _op_aihub_voice_models_edges_node_backup_urls = (
        _op_aihub_voice_models_edges_node.backup_urls(first=20)
    )
    _op_aihub_voice_models_edges_node_backup_urls_edges = (
        _op_aihub_voice_models_edges_node_backup_urls.edges()
    )
    _op_aihub_voice_models_edges_node_backup_urls_edges_node = (
        _op_aihub_voice_models_edges_node_backup_urls_edges.node()
    )
    _op_aihub_voice_models_edges_node_backup_urls_edges_node.id()
    _op_aihub_voice_models_edges_node_backup_urls_edges_node.url()
    _op_aihub_voice_models_edges_node_backup_urls_edges_node.voice_model_id()
    return _op


def query_voice_models():
    _op = sgqlc.operation.Operation(
        _schema_root.query_type,
        name="VoiceModels",
        variables=dict(after=sgqlc.types.Arg(_schema.String)),
    )
    _op_voice_models = _op.voice_models(first=50, after=sgqlc.types.Variable("after"))
    _op_voice_models_edges = _op_voice_models.edges()
    _op_voice_models_edges.cursor()
    _op_voice_models_edges_node = _op_voice_models_edges.node()
    _op_voice_models_edges_node.checksum_md5_for_added()
    _op_voice_models_edges_node.checksum_md5_for_weights()
    _op_voice_models_edges_node.checksum_sha256_for_added()
    _op_voice_models_edges_node.checksum_sha256_for_weights()
    _op_voice_models_edges_node.filesize_for_added()
    _op_voice_models_edges_node.filesize_for_weights()
    _op_voice_models_edges_node.hidden()
    _op_voice_models_edges_node.id()
    _op_voice_models_edges_node.name()
    _op_voice_models_edges_node.processed()
    _op_voice_models_edges_node_source_model = (
        _op_voice_models_edges_node.source_model()
    )
    _op_voice_models_edges_node_source_model_inferred_profile = (
        _op_voice_models_edges_node_source_model.inferred_profile()
    )
    _op_voice_models_edges_node_source_model_inferred_profile.gender()
    _op_voice_models_edges_node_source_model_inferred_profile.name()
    _op_voice_models_edges_node_source_model_inferred_profile.id()
    _op_voice_models_page_info = _op_voice_models.page_info()
    _op_voice_models_page_info.end_cursor()
    _op_voice_models_page_info.has_next_page()
    _op_voice_models_page_info.has_previous_page()
    _op_voice_models_page_info.start_cursor()
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
    _op_aihub_voice_model_inferred_profile = _op_aihub_voice_model.inferred_profile()
    _op_aihub_voice_model_inferred_profile.accent()
    _op_aihub_voice_model_inferred_profile.confidence()
    _op_aihub_voice_model_inferred_profile.fictional()
    _op_aihub_voice_model_inferred_profile.gender()
    _op_aihub_voice_model_inferred_profile.id()
    _op_aihub_voice_model_inferred_profile.model_trained_on_english_probability()
    _op_aihub_voice_model_inferred_profile.name()
    _op_aihub_voice_model_inferred_profile.native_language()
    _op_aihub_voice_model_inferred_profile.relevant_tags()
    _op_aihub_voice_model_inferred_profile.voice_model_id()
    return _op


class Query:
    aihub_voice_model_using_checksum_md5_for_weights = (
        query_aihub_voice_model_using_checksum_md5_for_weights()
    )
    aihub_voice_models = query_aihub_voice_models()
    voice_models = query_voice_models()


class Operations:
    mutation = Mutation
    query = Query
