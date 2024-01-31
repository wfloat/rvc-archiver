import sgqlc.types
import sgqlc.types.relay


schema = sgqlc.types.Schema()


# Unexport Node/PageInfo, let schema re-declare them
schema -= sgqlc.types.relay.Node
schema -= sgqlc.types.relay.PageInfo


__docformat__ = 'markdown'


########################################################################
# Scalars and Enumerations
########################################################################
Boolean = sgqlc.types.Boolean

Float = sgqlc.types.Float

ID = sgqlc.types.ID

Int = sgqlc.types.Int

String = sgqlc.types.String


########################################################################
# Input Objects
########################################################################
class CreateAIHubVoiceModelInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('checksum_md5_for_weights', 'creator_text', 'derived_model_id', 'download_count', 'filename', 'name', 'version')
    checksum_md5_for_weights = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='checksumMD5ForWeights')

    creator_text = sgqlc.types.Field(String, graphql_name='creatorText')

    derived_model_id = sgqlc.types.Field(ID, graphql_name='derivedModelId')

    download_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='downloadCount')

    filename = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='filename')

    name = sgqlc.types.Field(String, graphql_name='name')

    version = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='version')



class CreateTextToSpeechInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('input_text', 'ouput_url', 'voice_model_id')
    input_text = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='inputText')

    ouput_url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='ouputUrl')

    voice_model_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='voiceModelId')



class CreateVoiceModelBackupUrlInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('url', 'voice_model_id')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')

    voice_model_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='voiceModelId')



class CreateVoiceModelConfigInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('voice_model_id',)
    voice_model_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='voiceModelId')



class CreateVoiceModelInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('checksum_md5_for_added', 'checksum_md5_for_weights', 'checksum_sha256_for_added', 'checksum_sha256_for_weights', 'filesize', 'hidden', 'name', 'processed')
    checksum_md5_for_added = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='checksumMD5ForAdded')

    checksum_md5_for_weights = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='checksumMD5ForWeights')

    checksum_sha256_for_added = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='checksumSHA256ForAdded')

    checksum_sha256_for_weights = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='checksumSHA256ForWeights')

    filesize = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='filesize')

    hidden = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hidden')

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')

    processed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='processed')



class CreateVoiceModelProfileInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('accent', 'confidence', 'fictional', 'gender', 'model_trained_on_english_probability', 'name', 'native_language', 'relevant_tags', 'voice_model_id')
    accent = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='accent')

    confidence = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='confidence')

    fictional = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='fictional')

    gender = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='gender')

    model_trained_on_english_probability = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='modelTrainedOnEnglishProbability')

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')

    native_language = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='nativeLanguage')

    relevant_tags = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='relevantTags')

    voice_model_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='voiceModelId')



class UpdateAIHubVoiceModelInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('checksum_md5_for_weights', 'creator_text', 'derived_model_id', 'download_count', 'filename', 'id', 'name', 'version')
    checksum_md5_for_weights = sgqlc.types.Field(String, graphql_name='checksumMD5ForWeights')

    creator_text = sgqlc.types.Field(String, graphql_name='creatorText')

    derived_model_id = sgqlc.types.Field(ID, graphql_name='derivedModelId')

    download_count = sgqlc.types.Field(Int, graphql_name='downloadCount')

    filename = sgqlc.types.Field(String, graphql_name='filename')

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    name = sgqlc.types.Field(String, graphql_name='name')

    version = sgqlc.types.Field(String, graphql_name='version')



class UpdateTextToSpeechInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'input_text', 'ouput_url', 'voice_model_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    input_text = sgqlc.types.Field(String, graphql_name='inputText')

    ouput_url = sgqlc.types.Field(String, graphql_name='ouputUrl')

    voice_model_id = sgqlc.types.Field(ID, graphql_name='voiceModelId')



class UpdateVoiceModelBackupUrlInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'url', 'voice_model_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    url = sgqlc.types.Field(String, graphql_name='url')

    voice_model_id = sgqlc.types.Field(ID, graphql_name='voiceModelId')



class UpdateVoiceModelConfigInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'voice_model_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    voice_model_id = sgqlc.types.Field(ID, graphql_name='voiceModelId')



class UpdateVoiceModelInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('checksum_md5_for_added', 'checksum_md5_for_weights', 'checksum_sha256_for_added', 'checksum_sha256_for_weights', 'filesize', 'hidden', 'id', 'name', 'processed')
    checksum_md5_for_added = sgqlc.types.Field(String, graphql_name='checksumMD5ForAdded')

    checksum_md5_for_weights = sgqlc.types.Field(String, graphql_name='checksumMD5ForWeights')

    checksum_sha256_for_added = sgqlc.types.Field(String, graphql_name='checksumSHA256ForAdded')

    checksum_sha256_for_weights = sgqlc.types.Field(String, graphql_name='checksumSHA256ForWeights')

    filesize = sgqlc.types.Field(Int, graphql_name='filesize')

    hidden = sgqlc.types.Field(Boolean, graphql_name='hidden')

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    name = sgqlc.types.Field(String, graphql_name='name')

    processed = sgqlc.types.Field(Boolean, graphql_name='processed')



class UpdateVoiceModelProfileInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('accent', 'confidence', 'fictional', 'gender', 'id', 'model_trained_on_english_probability', 'name', 'native_language', 'relevant_tags', 'voice_model_id')
    accent = sgqlc.types.Field(String, graphql_name='accent')

    confidence = sgqlc.types.Field(Float, graphql_name='confidence')

    fictional = sgqlc.types.Field(Boolean, graphql_name='fictional')

    gender = sgqlc.types.Field(String, graphql_name='gender')

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    model_trained_on_english_probability = sgqlc.types.Field(Float, graphql_name='modelTrainedOnEnglishProbability')

    name = sgqlc.types.Field(String, graphql_name='name')

    native_language = sgqlc.types.Field(String, graphql_name='nativeLanguage')

    relevant_tags = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='relevantTags')

    voice_model_id = sgqlc.types.Field(ID, graphql_name='voiceModelId')




########################################################################
# Output Objects and Interfaces
########################################################################
class AIHubVoiceModel(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('backup_urls', 'checksum_md5_for_weights', 'creator_text', 'derived_model', 'derived_model_id', 'download_count', 'filename', 'id', 'name', 'profile', 'version')
    backup_urls = sgqlc.types.Field(sgqlc.types.non_null('AIHubVoiceModelBackupUrlsConnection'), graphql_name='backupUrls', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `after` (`String`)None
    * `before` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    checksum_md5_for_weights = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='checksumMD5ForWeights')

    creator_text = sgqlc.types.Field(String, graphql_name='creatorText')

    derived_model = sgqlc.types.Field('VoiceModel', graphql_name='derivedModel')

    derived_model_id = sgqlc.types.Field(ID, graphql_name='derivedModelId')

    download_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='downloadCount')

    filename = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='filename')

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    name = sgqlc.types.Field(String, graphql_name='name')

    profile = sgqlc.types.Field('VoiceModelProfile', graphql_name='profile')

    version = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='version')



class AIHubVoiceModelBackupUrlsConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('AIHubVoiceModelBackupUrlsEdge')), graphql_name='edges')

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')



class AIHubVoiceModelBackupUrlsEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')

    node = sgqlc.types.Field(sgqlc.types.non_null('VoiceModelBackupUrl'), graphql_name='node')



class AIHubVoiceModelsConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('AIHubVoiceModelsEdge')), graphql_name='edges')

    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')



class AIHubVoiceModelsEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')

    node = sgqlc.types.Field(sgqlc.types.non_null(AIHubVoiceModel), graphql_name='node')



class Mutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('create_aihub_voice_model', 'create_text_to_speech', 'create_voice_model', 'create_voice_model_backup_url', 'create_voice_model_config', 'create_voice_model_profile', 'update_aihub_voice_model', 'update_text_to_speech', 'update_voice_model', 'update_voice_model_backup_url', 'update_voice_model_config', 'update_voice_model_profile')
    create_aihub_voice_model = sgqlc.types.Field(sgqlc.types.non_null(AIHubVoiceModel), graphql_name='createAIHubVoiceModel', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateAIHubVoiceModelInput), graphql_name='input', default=None)),
))
    )
    '''Arguments:

    * `input` (`CreateAIHubVoiceModelInput!`)None
    '''

    create_text_to_speech = sgqlc.types.Field(sgqlc.types.non_null('TextToSpeech'), graphql_name='createTextToSpeech', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateTextToSpeechInput), graphql_name='input', default=None)),
))
    )
    '''Arguments:

    * `input` (`CreateTextToSpeechInput!`)None
    '''

    create_voice_model = sgqlc.types.Field(sgqlc.types.non_null('VoiceModel'), graphql_name='createVoiceModel', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateVoiceModelInput), graphql_name='input', default=None)),
))
    )
    '''Arguments:

    * `input` (`CreateVoiceModelInput!`)None
    '''

    create_voice_model_backup_url = sgqlc.types.Field(sgqlc.types.non_null('VoiceModelBackupUrl'), graphql_name='createVoiceModelBackupUrl', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateVoiceModelBackupUrlInput), graphql_name='input', default=None)),
))
    )
    '''Arguments:

    * `input` (`CreateVoiceModelBackupUrlInput!`)None
    '''

    create_voice_model_config = sgqlc.types.Field(sgqlc.types.non_null('VoiceModelConfig'), graphql_name='createVoiceModelConfig', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateVoiceModelConfigInput), graphql_name='input', default=None)),
))
    )
    '''Arguments:

    * `input` (`CreateVoiceModelConfigInput!`)None
    '''

    create_voice_model_profile = sgqlc.types.Field(sgqlc.types.non_null('VoiceModelProfile'), graphql_name='createVoiceModelProfile', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateVoiceModelProfileInput), graphql_name='input', default=None)),
))
    )
    '''Arguments:

    * `input` (`CreateVoiceModelProfileInput!`)None
    '''

    update_aihub_voice_model = sgqlc.types.Field(sgqlc.types.non_null(AIHubVoiceModel), graphql_name='updateAIHubVoiceModel', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateAIHubVoiceModelInput), graphql_name='input', default=None)),
))
    )
    '''Arguments:

    * `input` (`UpdateAIHubVoiceModelInput!`)None
    '''

    update_text_to_speech = sgqlc.types.Field(sgqlc.types.non_null('TextToSpeech'), graphql_name='updateTextToSpeech', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateTextToSpeechInput), graphql_name='input', default=None)),
))
    )
    '''Arguments:

    * `input` (`UpdateTextToSpeechInput!`)None
    '''

    update_voice_model = sgqlc.types.Field(sgqlc.types.non_null('VoiceModel'), graphql_name='updateVoiceModel', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateVoiceModelInput), graphql_name='input', default=None)),
))
    )
    '''Arguments:

    * `input` (`UpdateVoiceModelInput!`)None
    '''

    update_voice_model_backup_url = sgqlc.types.Field(sgqlc.types.non_null('VoiceModelBackupUrl'), graphql_name='updateVoiceModelBackupUrl', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateVoiceModelBackupUrlInput), graphql_name='input', default=None)),
))
    )
    '''Arguments:

    * `input` (`UpdateVoiceModelBackupUrlInput!`)None
    '''

    update_voice_model_config = sgqlc.types.Field(sgqlc.types.non_null('VoiceModelConfig'), graphql_name='updateVoiceModelConfig', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateVoiceModelConfigInput), graphql_name='input', default=None)),
))
    )
    '''Arguments:

    * `input` (`UpdateVoiceModelConfigInput!`)None
    '''

    update_voice_model_profile = sgqlc.types.Field(sgqlc.types.non_null('VoiceModelProfile'), graphql_name='updateVoiceModelProfile', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateVoiceModelProfileInput), graphql_name='input', default=None)),
))
    )
    '''Arguments:

    * `input` (`UpdateVoiceModelProfileInput!`)None
    '''



class PageInfo(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('end_cursor', 'has_next_page', 'has_previous_page', 'start_cursor')
    end_cursor = sgqlc.types.Field(String, graphql_name='endCursor')

    has_next_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasNextPage')

    has_previous_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasPreviousPage')

    start_cursor = sgqlc.types.Field(String, graphql_name='startCursor')



class Query(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('aihub_voice_model', 'aihub_voice_models', 'text_to_speech', 'text_to_speeches', 'voice_model', 'voice_model_backup_url', 'voice_model_backup_urls', 'voice_model_config', 'voice_model_configs', 'voice_model_profile', 'voice_model_profiles', 'voice_models')
    aihub_voice_model = sgqlc.types.Field(sgqlc.types.non_null('AIHubVoiceModel'), graphql_name='AIHubVoiceModel', args=sgqlc.types.ArgDict((
        ('checksum_md5_for_weights', sgqlc.types.Arg(String, graphql_name='checksumMD5ForWeights', default=None)),
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
))
    )
    '''Arguments:

    * `checksum_md5_for_weights` (`String`)None
    * `id` (`ID`)None
    '''

    aihub_voice_models = sgqlc.types.Field(sgqlc.types.non_null(AIHubVoiceModelsConnection), graphql_name='AIHubVoiceModels', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('min_download_count', sgqlc.types.Arg(Int, graphql_name='minDownloadCount', default=None)),
))
    )
    '''Arguments:

    * `after` (`String`)None
    * `before` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    * `min_download_count` (`Int`)None
    '''

    text_to_speech = sgqlc.types.Field(sgqlc.types.non_null('TextToSpeech'), graphql_name='TextToSpeech', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    '''Arguments:

    * `id` (`ID!`)None
    '''

    text_to_speeches = sgqlc.types.Field(sgqlc.types.non_null('TextToSpeechesConnection'), graphql_name='TextToSpeeches', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `after` (`String`)None
    * `before` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    voice_model = sgqlc.types.Field(sgqlc.types.non_null('VoiceModel'), graphql_name='VoiceModel', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    '''Arguments:

    * `id` (`ID!`)None
    '''

    voice_model_backup_url = sgqlc.types.Field(sgqlc.types.non_null('VoiceModelBackupUrl'), graphql_name='VoiceModelBackupUrl', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    '''Arguments:

    * `id` (`ID!`)None
    '''

    voice_model_backup_urls = sgqlc.types.Field(sgqlc.types.non_null('VoiceModelBackupUrlsConnection'), graphql_name='VoiceModelBackupUrls', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `after` (`String`)None
    * `before` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    voice_model_config = sgqlc.types.Field(sgqlc.types.non_null('VoiceModelConfig'), graphql_name='VoiceModelConfig', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    '''Arguments:

    * `id` (`ID!`)None
    '''

    voice_model_configs = sgqlc.types.Field(sgqlc.types.non_null('VoiceModelConfigsConnection'), graphql_name='VoiceModelConfigs', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `after` (`String`)None
    * `before` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    voice_model_profile = sgqlc.types.Field(sgqlc.types.non_null('VoiceModelProfile'), graphql_name='VoiceModelProfile', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    '''Arguments:

    * `id` (`ID!`)None
    '''

    voice_model_profiles = sgqlc.types.Field(sgqlc.types.non_null('VoiceModelProfilesConnection'), graphql_name='VoiceModelProfiles', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `after` (`String`)None
    * `before` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    voice_models = sgqlc.types.Field(sgqlc.types.non_null('VoiceModelsConnection'), graphql_name='VoiceModels', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `after` (`String`)None
    * `before` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''



class TextToSpeech(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'input_text', 'ouput_url', 'voice_model', 'voice_model_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    input_text = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='inputText')

    ouput_url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='ouputUrl')

    voice_model = sgqlc.types.Field(sgqlc.types.non_null('VoiceModel'), graphql_name='voiceModel')

    voice_model_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='voiceModelId')



class TextToSpeechesConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('TextToSpeechesEdge')), graphql_name='edges')

    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')



class TextToSpeechesEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')

    node = sgqlc.types.Field(sgqlc.types.non_null(TextToSpeech), graphql_name='node')



class VoiceModel(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('checksum_md5_for_added', 'checksum_md5_for_weights', 'checksum_sha256_for_added', 'checksum_sha256_for_weights', 'filesize', 'hidden', 'id', 'model_config', 'name', 'processed', 'source_model', 'text_to_speeches')
    checksum_md5_for_added = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='checksumMD5ForAdded')

    checksum_md5_for_weights = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='checksumMD5ForWeights')

    checksum_sha256_for_added = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='checksumSHA256ForAdded')

    checksum_sha256_for_weights = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='checksumSHA256ForWeights')

    filesize = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='filesize')

    hidden = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hidden')

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    model_config = sgqlc.types.Field('VoiceModelConfig', graphql_name='modelConfig')

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')

    processed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='processed')

    source_model = sgqlc.types.Field(AIHubVoiceModel, graphql_name='sourceModel')

    text_to_speeches = sgqlc.types.Field(sgqlc.types.non_null('VoiceModelTextToSpeechesConnection'), graphql_name='textToSpeeches', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `after` (`String`)None
    * `before` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''



class VoiceModelBackupUrl(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'url', 'voice_model', 'voice_model_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')

    voice_model = sgqlc.types.Field(sgqlc.types.non_null(AIHubVoiceModel), graphql_name='voiceModel')

    voice_model_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='voiceModelId')



class VoiceModelBackupUrlsConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('VoiceModelBackupUrlsEdge')), graphql_name='edges')

    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')



class VoiceModelBackupUrlsEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')

    node = sgqlc.types.Field(sgqlc.types.non_null(VoiceModelBackupUrl), graphql_name='node')



class VoiceModelConfig(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'voice_model', 'voice_model_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    voice_model = sgqlc.types.Field(sgqlc.types.non_null(VoiceModel), graphql_name='voiceModel')

    voice_model_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='voiceModelId')



class VoiceModelConfigsConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('VoiceModelConfigsEdge')), graphql_name='edges')

    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')



class VoiceModelConfigsEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')

    node = sgqlc.types.Field(sgqlc.types.non_null(VoiceModelConfig), graphql_name='node')



class VoiceModelProfile(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('accent', 'confidence', 'fictional', 'gender', 'id', 'model_trained_on_english_probability', 'name', 'native_language', 'relevant_tags', 'voice_model', 'voice_model_id')
    accent = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='accent')

    confidence = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='confidence')

    fictional = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='fictional')

    gender = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='gender')

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    model_trained_on_english_probability = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='modelTrainedOnEnglishProbability')

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')

    native_language = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='nativeLanguage')

    relevant_tags = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='relevantTags')

    voice_model = sgqlc.types.Field(sgqlc.types.non_null(AIHubVoiceModel), graphql_name='voiceModel')

    voice_model_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='voiceModelId')



class VoiceModelProfilesConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('VoiceModelProfilesEdge')), graphql_name='edges')

    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')



class VoiceModelProfilesEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')

    node = sgqlc.types.Field(sgqlc.types.non_null(VoiceModelProfile), graphql_name='node')



class VoiceModelTextToSpeechesConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('VoiceModelTextToSpeechesEdge')), graphql_name='edges')

    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')



class VoiceModelTextToSpeechesEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')

    node = sgqlc.types.Field(sgqlc.types.non_null(TextToSpeech), graphql_name='node')



class VoiceModelsConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('VoiceModelsEdge')), graphql_name='edges')

    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')



class VoiceModelsEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')

    node = sgqlc.types.Field(sgqlc.types.non_null(VoiceModel), graphql_name='node')




########################################################################
# Unions
########################################################################

########################################################################
# Schema Entry Points
########################################################################
schema.query_type = Query
schema.mutation_type = Mutation
schema.subscription_type = None

