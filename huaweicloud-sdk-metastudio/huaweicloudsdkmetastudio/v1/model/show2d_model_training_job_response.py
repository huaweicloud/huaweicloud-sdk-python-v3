# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Show2dModelTrainingJobResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'name': 'str',
        'state': 'str',
        'asset_id': 'str',
        'project_id': 'str',
        'cover_download_url': 'str',
        'last_update_time': 'str',
        'create_time': 'str',
        'contact': 'str',
        'batch_name': 'str',
        'tags': 'list[str]',
        'model_version': 'str',
        'matting_type': 'str',
        'model_resolution': 'str',
        'app_user_id': 'str',
        'is_flexus': 'bool',
        'is_only_human_model': 'bool',
        'training_video_download_url': 'str',
        'id_card_image1_download_url': 'str',
        'id_card_image2_download_url': 'str',
        'grant_file_download_url': 'str',
        'pre_beauty_image_download_url': 'str',
        'action_video_download_url': 'str',
        'post_beauty_image_download_url': 'str',
        'audio_file_download_url': 'str',
        'operation_logs': 'list[OperationLogInfo]',
        'verify_video_matting_info': 'list[VerifyVideoMattingInfo]',
        'comment_logs': 'list[CommentLogInfo]',
        'samples': 'list[ActionSampleInfo]',
        'is_mask_file_uploaded': 'bool',
        'mask_file_download_url': 'str',
        'verify_video_download_url': 'str',
        'markable_video_download_url': 'str',
        'traning_video_mark_info': 'TrainingVideoMarkInfo',
        'inference_data_process_video_mark_info': 'InferenceVideoMarkInfo',
        'inference_data_process_action_mark_info': 'InferenceActionMarkInfo',
        'inference_data_process_chat_action_mark_info': 'InferenceActionMarkInfo',
        'inference_data_process_eye_correction_mark_info': 'InferenceEyeCorrectionMarkInfo',
        'is_background_replacement': 'bool',
        'worker_type': 'list[str]',
        'voice_train_job_id': 'str',
        'flexus_retry_count': 'int',
        'audio_source_type': 'str',
        'supported_service': 'list[SupportedServiceEnum]',
        'allocated_resource': 'TrainingAllocatedResource',
        'x_request_id': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'name': 'name',
        'state': 'state',
        'asset_id': 'asset_id',
        'project_id': 'project_id',
        'cover_download_url': 'cover_download_url',
        'last_update_time': 'last_update_time',
        'create_time': 'create_time',
        'contact': 'contact',
        'batch_name': 'batch_name',
        'tags': 'tags',
        'model_version': 'model_version',
        'matting_type': 'matting_type',
        'model_resolution': 'model_resolution',
        'app_user_id': 'app_user_id',
        'is_flexus': 'is_flexus',
        'is_only_human_model': 'is_only_human_model',
        'training_video_download_url': 'training_video_download_url',
        'id_card_image1_download_url': 'id_card_image1_download_url',
        'id_card_image2_download_url': 'id_card_image2_download_url',
        'grant_file_download_url': 'grant_file_download_url',
        'pre_beauty_image_download_url': 'pre_beauty_image_download_url',
        'action_video_download_url': 'action_video_download_url',
        'post_beauty_image_download_url': 'post_beauty_image_download_url',
        'audio_file_download_url': 'audio_file_download_url',
        'operation_logs': 'operation_logs',
        'verify_video_matting_info': 'verify_video_matting_info',
        'comment_logs': 'comment_logs',
        'samples': 'samples',
        'is_mask_file_uploaded': 'is_mask_file_uploaded',
        'mask_file_download_url': 'mask_file_download_url',
        'verify_video_download_url': 'verify_video_download_url',
        'markable_video_download_url': 'markable_video_download_url',
        'traning_video_mark_info': 'traning_video_mark_info',
        'inference_data_process_video_mark_info': 'inference_data_process_video_mark_info',
        'inference_data_process_action_mark_info': 'inference_data_process_action_mark_info',
        'inference_data_process_chat_action_mark_info': 'inference_data_process_chat_action_mark_info',
        'inference_data_process_eye_correction_mark_info': 'inference_data_process_eye_correction_mark_info',
        'is_background_replacement': 'is_background_replacement',
        'worker_type': 'worker_type',
        'voice_train_job_id': 'voice_train_job_id',
        'flexus_retry_count': 'flexus_retry_count',
        'audio_source_type': 'audio_source_type',
        'supported_service': 'supported_service',
        'allocated_resource': 'allocated_resource',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, job_id=None, name=None, state=None, asset_id=None, project_id=None, cover_download_url=None, last_update_time=None, create_time=None, contact=None, batch_name=None, tags=None, model_version=None, matting_type=None, model_resolution=None, app_user_id=None, is_flexus=None, is_only_human_model=None, training_video_download_url=None, id_card_image1_download_url=None, id_card_image2_download_url=None, grant_file_download_url=None, pre_beauty_image_download_url=None, action_video_download_url=None, post_beauty_image_download_url=None, audio_file_download_url=None, operation_logs=None, verify_video_matting_info=None, comment_logs=None, samples=None, is_mask_file_uploaded=None, mask_file_download_url=None, verify_video_download_url=None, markable_video_download_url=None, traning_video_mark_info=None, inference_data_process_video_mark_info=None, inference_data_process_action_mark_info=None, inference_data_process_chat_action_mark_info=None, inference_data_process_eye_correction_mark_info=None, is_background_replacement=None, worker_type=None, voice_train_job_id=None, flexus_retry_count=None, audio_source_type=None, supported_service=None, allocated_resource=None, x_request_id=None):
        r"""Show2dModelTrainingJobResponse

        The model defined in huaweicloud sdk

        :param job_id: 任务ID。
        :type job_id: str
        :param name: 分身数字人模型名称。该名称会作为资产库中分身数字人模型资产名称。
        :type name: str
        :param state: 任务的状态。  与MetaStudio Console上用户看到的状态映射关系如下：  - 待提交   * WAIT_FILE_UPLOAD: 待上传文件  - 系统审核中   * AUTO_VERIFYING: 自动审核中   * MANUAL_VERIFYING: 人工审核中  - 系统审核未通过   * AUTO_VERIFY_FAILED: 自动审核失败   * MANUAL_VERIFY_FAILED: 人工审核失败  - 算法训练中   &gt; 算法训练中的状态仅管理员需要处理，普通用户仅需要显示“算法训练中”即可。   * MANUAL_VERIFY_SUCCESS: 审核通过，等待预处理资源   * WAIT_TRAINING_DATA_PREPROCESS: 等待训练数据预处理   * TRAINING_DATA_PREPROCESSING: 训练数据预处理中   * TRAINING_DATA_PREPROCESS_FAILED: 训练数据预处理失败   * TRAINING_DATA_PREPROCESS_SUCCESS: 训练数据预处理完成，等待训练资源中   * TRAINING: 训练中   * TRAIN_FAILED: 训练失败   * TRAIN_SUCCESS: 训练完成，等待预处理资源   * INFERENCE_DATA_PREPROCESSING: 推理数据预处理中   * INFERENCE_DATA_PREPROCESS_FAILED: 推理数据预处理失败   * WAIT_MAIN_FILE_UPLOAD: 等待主文件上传   * MANUAL_STOP_INFERENCE_DATA_PREPROCESS: 人工中止推理预处理   * MANUAL_STOP_TRAIN: 人工中止训练   * MANUAL_STOP_TRAINING_DATA_PREPROCESS: 人工中止训练预处理   * WAIT_ADMIN_CONFIRM: 等待管理员审核   * WAIT_COMPILE: 等待转编译   * COMPILING: 转编译中   * COMPILE_FAILED: 转编译失败   * WAIT_GENERATE_ACTION: 等待原子动作生成   * WAIT_ARRANGE: 等待编排   * ACTION_GENERATE_DATA_PROCESSING: 原子动作生成中   * MANUAL_STOP_ACTION_GENERATE_DATA_PROCESSING: 人工中止动作生成   * MANUAL_STOP_ACTION_GENERATE_ORI_PROCESSING: 人工中止动作编排   * ACTION_GENERATE_ORI_PROCESSING: 动作编排中   * ACTION_GENERATE_DATA_FAILED: 动作生成失败   * ACTION_GENERATE_ORI_FAILED: 生成动作编排资产失败   * ACTION_GENERATE_ORI_SUCCESS: 动作编排成功   * GENERATE_ACTION_PREPROCESS_FAILED: 生成动作编排原子动作失败   * WAIT_ADMIN_CALIBRATION: 等待管理员确认动作信息   * WAIT_ASSET_SYNC: 等待资产同步  - 待用户审核，仅NA白名单用户有该状态   * WAIT_USER_CONFIRM: 等待用户确认训练效果  - 用户驳回，仅NA白名单用户有该状态   * JOB_REJECT: 驳回任务  - 已完成   * JOB_SUCCESS: 训练任务完成（普通用户任务的完成状态，此时用户已经可以使用模型）   * JOB_FINISH: 任务结束，是最终状态，不支持修改此状态(NA用户任务的完成状态，并且此状态表明模型效果已通过用户的验收)  - 挂起，仅NA白名单用户有该状态   * JOB_PENDING: 挂起任务
        :type state: str
        :param asset_id: 模型资产ID。
        :type asset_id: str
        :param project_id: 模型资产所属项目ID。
        :type project_id: str
        :param cover_download_url: 分身数字人模型封面下载URL。URL有效期24小时。
        :type cover_download_url: str
        :param last_update_time: 用户最近一次更新任务的时间（包括租户创建或者重新提交），格式遵循：RFC 3339。 例 “2020-07-30T10:43:17Z”
        :type last_update_time: str
        :param create_time: 创建时间，格式遵循：RFC 3339。 例 “2020-07-30T10:43:17Z”
        :type create_time: str
        :param contact: 分身数字人训练任务创建者的手机号。
        :type contact: str
        :param batch_name: 分身数字人训练任务的批次名称。
        :type batch_name: str
        :param tags: 分身数字人训练任务标签。
        :type tags: list[str]
        :param model_version: 分身数字人模型版本。默认是V3.2版本模型。 * V3.2：V3.2版本模型 &gt; * V3和V2版本已废弃不用
        :type model_version: str
        :param matting_type: 抠图类型。默认是AI。 * AI：AI抠图 * MANUAL：人工抠图
        :type matting_type: str
        :param model_resolution: 分身数字人模型分辨率。默认是1080P。 * 1080P：1080P。支持1080P及720P的视频输出。 * 4K：4K。支持4K、1080P及720P的视频输出。
        :type model_resolution: str
        :param app_user_id: 自定义用户id（如创建任务时设置了X-App-UserId则会携带）。
        :type app_user_id: str
        :param is_flexus: 是否是基础版的形象训练
        :type is_flexus: bool
        :param is_only_human_model: 是否只训练形象模型，不训练声音模型。仅Flexus版本时有效，默认false。
        :type is_only_human_model: bool
        :param training_video_download_url: 分身数字人训练视频下载URL。24小时内有效。
        :type training_video_download_url: str
        :param id_card_image1_download_url: 身份证正面照片下载URL。24小时内有效。
        :type id_card_image1_download_url: str
        :param id_card_image2_download_url: 身份证反面照片下载URL。24小时内有效。
        :type id_card_image2_download_url: str
        :param grant_file_download_url: 授权书下载URL。24小时内有效。
        :type grant_file_download_url: str
        :param pre_beauty_image_download_url: 美白前图片下载url。
        :type pre_beauty_image_download_url: str
        :param action_video_download_url: 动作视频
        :type action_video_download_url: str
        :param post_beauty_image_download_url: 美白后图片下载url。
        :type post_beauty_image_download_url: str
        :param audio_file_download_url: 音频文件下载url。
        :type audio_file_download_url: str
        :param operation_logs: 操作日志列表。
        :type operation_logs: list[:class:`huaweicloudsdkmetastudio.v1.OperationLogInfo`]
        :param verify_video_matting_info: 生成抠图验证视频时不抠图区域。
        :type verify_video_matting_info: list[:class:`huaweicloudsdkmetastudio.v1.VerifyVideoMattingInfo`]
        :param comment_logs: 评论记录列表。
        :type comment_logs: list[:class:`huaweicloudsdkmetastudio.v1.CommentLogInfo`]
        :param samples: 动作视频样例。
        :type samples: list[:class:`huaweicloudsdkmetastudio.v1.ActionSampleInfo`]
        :param is_mask_file_uploaded: 遮罩文件是否已上传。
        :type is_mask_file_uploaded: bool
        :param mask_file_download_url: 遮罩下载URL。24小时内有效。
        :type mask_file_download_url: str
        :param verify_video_download_url: 制作审核视频
        :type verify_video_download_url: str
        :param markable_video_download_url: 标注视频url下载链接。24小时内有效。
        :type markable_video_download_url: str
        :param traning_video_mark_info: 
        :type traning_video_mark_info: :class:`huaweicloudsdkmetastudio.v1.TrainingVideoMarkInfo`
        :param inference_data_process_video_mark_info: 
        :type inference_data_process_video_mark_info: :class:`huaweicloudsdkmetastudio.v1.InferenceVideoMarkInfo`
        :param inference_data_process_action_mark_info: 
        :type inference_data_process_action_mark_info: :class:`huaweicloudsdkmetastudio.v1.InferenceActionMarkInfo`
        :param inference_data_process_chat_action_mark_info: 
        :type inference_data_process_chat_action_mark_info: :class:`huaweicloudsdkmetastudio.v1.InferenceActionMarkInfo`
        :param inference_data_process_eye_correction_mark_info: 
        :type inference_data_process_eye_correction_mark_info: :class:`huaweicloudsdkmetastudio.v1.InferenceEyeCorrectionMarkInfo`
        :param is_background_replacement: 分身数字人是否需要背景替换。需要背景替换的分身数字人训练视频需要绿幕拍摄。
        :type is_background_replacement: bool
        :param worker_type: 转编译任务机型
        :type worker_type: list[str]
        :param voice_train_job_id: 声音训练任务id。
        :type voice_train_job_id: str
        :param flexus_retry_count: flexus版本任务剩余可以重训的次数，每重训一次减1，减到0时不可再重训。
        :type flexus_retry_count: int
        :param audio_source_type: 声音来源类型 * VIDEO：视频中抽取音频 * AUDIO：单独上传的音频
        :type audio_source_type: str
        :param supported_service: 该任务所生成的模型支持的业务类型，可多选。  Flexus版数字人仅支持选择“VIDEO_2D”。
        :type supported_service: list[:class:`huaweicloudsdkmetastudio.v1.SupportedServiceEnum`]
        :param allocated_resource: 
        :type allocated_resource: :class:`huaweicloudsdkmetastudio.v1.TrainingAllocatedResource`
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(Show2dModelTrainingJobResponse, self).__init__()

        self._job_id = None
        self._name = None
        self._state = None
        self._asset_id = None
        self._project_id = None
        self._cover_download_url = None
        self._last_update_time = None
        self._create_time = None
        self._contact = None
        self._batch_name = None
        self._tags = None
        self._model_version = None
        self._matting_type = None
        self._model_resolution = None
        self._app_user_id = None
        self._is_flexus = None
        self._is_only_human_model = None
        self._training_video_download_url = None
        self._id_card_image1_download_url = None
        self._id_card_image2_download_url = None
        self._grant_file_download_url = None
        self._pre_beauty_image_download_url = None
        self._action_video_download_url = None
        self._post_beauty_image_download_url = None
        self._audio_file_download_url = None
        self._operation_logs = None
        self._verify_video_matting_info = None
        self._comment_logs = None
        self._samples = None
        self._is_mask_file_uploaded = None
        self._mask_file_download_url = None
        self._verify_video_download_url = None
        self._markable_video_download_url = None
        self._traning_video_mark_info = None
        self._inference_data_process_video_mark_info = None
        self._inference_data_process_action_mark_info = None
        self._inference_data_process_chat_action_mark_info = None
        self._inference_data_process_eye_correction_mark_info = None
        self._is_background_replacement = None
        self._worker_type = None
        self._voice_train_job_id = None
        self._flexus_retry_count = None
        self._audio_source_type = None
        self._supported_service = None
        self._allocated_resource = None
        self._x_request_id = None
        self.discriminator = None

        self.job_id = job_id
        self.name = name
        self.state = state
        if asset_id is not None:
            self.asset_id = asset_id
        if project_id is not None:
            self.project_id = project_id
        if cover_download_url is not None:
            self.cover_download_url = cover_download_url
        if last_update_time is not None:
            self.last_update_time = last_update_time
        if create_time is not None:
            self.create_time = create_time
        if contact is not None:
            self.contact = contact
        if batch_name is not None:
            self.batch_name = batch_name
        if tags is not None:
            self.tags = tags
        if model_version is not None:
            self.model_version = model_version
        if matting_type is not None:
            self.matting_type = matting_type
        if model_resolution is not None:
            self.model_resolution = model_resolution
        if app_user_id is not None:
            self.app_user_id = app_user_id
        if is_flexus is not None:
            self.is_flexus = is_flexus
        if is_only_human_model is not None:
            self.is_only_human_model = is_only_human_model
        if training_video_download_url is not None:
            self.training_video_download_url = training_video_download_url
        if id_card_image1_download_url is not None:
            self.id_card_image1_download_url = id_card_image1_download_url
        if id_card_image2_download_url is not None:
            self.id_card_image2_download_url = id_card_image2_download_url
        if grant_file_download_url is not None:
            self.grant_file_download_url = grant_file_download_url
        if pre_beauty_image_download_url is not None:
            self.pre_beauty_image_download_url = pre_beauty_image_download_url
        if action_video_download_url is not None:
            self.action_video_download_url = action_video_download_url
        if post_beauty_image_download_url is not None:
            self.post_beauty_image_download_url = post_beauty_image_download_url
        if audio_file_download_url is not None:
            self.audio_file_download_url = audio_file_download_url
        if operation_logs is not None:
            self.operation_logs = operation_logs
        if verify_video_matting_info is not None:
            self.verify_video_matting_info = verify_video_matting_info
        if comment_logs is not None:
            self.comment_logs = comment_logs
        if samples is not None:
            self.samples = samples
        if is_mask_file_uploaded is not None:
            self.is_mask_file_uploaded = is_mask_file_uploaded
        if mask_file_download_url is not None:
            self.mask_file_download_url = mask_file_download_url
        if verify_video_download_url is not None:
            self.verify_video_download_url = verify_video_download_url
        if markable_video_download_url is not None:
            self.markable_video_download_url = markable_video_download_url
        if traning_video_mark_info is not None:
            self.traning_video_mark_info = traning_video_mark_info
        if inference_data_process_video_mark_info is not None:
            self.inference_data_process_video_mark_info = inference_data_process_video_mark_info
        if inference_data_process_action_mark_info is not None:
            self.inference_data_process_action_mark_info = inference_data_process_action_mark_info
        if inference_data_process_chat_action_mark_info is not None:
            self.inference_data_process_chat_action_mark_info = inference_data_process_chat_action_mark_info
        if inference_data_process_eye_correction_mark_info is not None:
            self.inference_data_process_eye_correction_mark_info = inference_data_process_eye_correction_mark_info
        if is_background_replacement is not None:
            self.is_background_replacement = is_background_replacement
        if worker_type is not None:
            self.worker_type = worker_type
        if voice_train_job_id is not None:
            self.voice_train_job_id = voice_train_job_id
        if flexus_retry_count is not None:
            self.flexus_retry_count = flexus_retry_count
        if audio_source_type is not None:
            self.audio_source_type = audio_source_type
        if supported_service is not None:
            self.supported_service = supported_service
        if allocated_resource is not None:
            self.allocated_resource = allocated_resource
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def job_id(self):
        r"""Gets the job_id of this Show2dModelTrainingJobResponse.

        任务ID。

        :return: The job_id of this Show2dModelTrainingJobResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this Show2dModelTrainingJobResponse.

        任务ID。

        :param job_id: The job_id of this Show2dModelTrainingJobResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def name(self):
        r"""Gets the name of this Show2dModelTrainingJobResponse.

        分身数字人模型名称。该名称会作为资产库中分身数字人模型资产名称。

        :return: The name of this Show2dModelTrainingJobResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Show2dModelTrainingJobResponse.

        分身数字人模型名称。该名称会作为资产库中分身数字人模型资产名称。

        :param name: The name of this Show2dModelTrainingJobResponse.
        :type name: str
        """
        self._name = name

    @property
    def state(self):
        r"""Gets the state of this Show2dModelTrainingJobResponse.

        任务的状态。  与MetaStudio Console上用户看到的状态映射关系如下：  - 待提交   * WAIT_FILE_UPLOAD: 待上传文件  - 系统审核中   * AUTO_VERIFYING: 自动审核中   * MANUAL_VERIFYING: 人工审核中  - 系统审核未通过   * AUTO_VERIFY_FAILED: 自动审核失败   * MANUAL_VERIFY_FAILED: 人工审核失败  - 算法训练中   > 算法训练中的状态仅管理员需要处理，普通用户仅需要显示“算法训练中”即可。   * MANUAL_VERIFY_SUCCESS: 审核通过，等待预处理资源   * WAIT_TRAINING_DATA_PREPROCESS: 等待训练数据预处理   * TRAINING_DATA_PREPROCESSING: 训练数据预处理中   * TRAINING_DATA_PREPROCESS_FAILED: 训练数据预处理失败   * TRAINING_DATA_PREPROCESS_SUCCESS: 训练数据预处理完成，等待训练资源中   * TRAINING: 训练中   * TRAIN_FAILED: 训练失败   * TRAIN_SUCCESS: 训练完成，等待预处理资源   * INFERENCE_DATA_PREPROCESSING: 推理数据预处理中   * INFERENCE_DATA_PREPROCESS_FAILED: 推理数据预处理失败   * WAIT_MAIN_FILE_UPLOAD: 等待主文件上传   * MANUAL_STOP_INFERENCE_DATA_PREPROCESS: 人工中止推理预处理   * MANUAL_STOP_TRAIN: 人工中止训练   * MANUAL_STOP_TRAINING_DATA_PREPROCESS: 人工中止训练预处理   * WAIT_ADMIN_CONFIRM: 等待管理员审核   * WAIT_COMPILE: 等待转编译   * COMPILING: 转编译中   * COMPILE_FAILED: 转编译失败   * WAIT_GENERATE_ACTION: 等待原子动作生成   * WAIT_ARRANGE: 等待编排   * ACTION_GENERATE_DATA_PROCESSING: 原子动作生成中   * MANUAL_STOP_ACTION_GENERATE_DATA_PROCESSING: 人工中止动作生成   * MANUAL_STOP_ACTION_GENERATE_ORI_PROCESSING: 人工中止动作编排   * ACTION_GENERATE_ORI_PROCESSING: 动作编排中   * ACTION_GENERATE_DATA_FAILED: 动作生成失败   * ACTION_GENERATE_ORI_FAILED: 生成动作编排资产失败   * ACTION_GENERATE_ORI_SUCCESS: 动作编排成功   * GENERATE_ACTION_PREPROCESS_FAILED: 生成动作编排原子动作失败   * WAIT_ADMIN_CALIBRATION: 等待管理员确认动作信息   * WAIT_ASSET_SYNC: 等待资产同步  - 待用户审核，仅NA白名单用户有该状态   * WAIT_USER_CONFIRM: 等待用户确认训练效果  - 用户驳回，仅NA白名单用户有该状态   * JOB_REJECT: 驳回任务  - 已完成   * JOB_SUCCESS: 训练任务完成（普通用户任务的完成状态，此时用户已经可以使用模型）   * JOB_FINISH: 任务结束，是最终状态，不支持修改此状态(NA用户任务的完成状态，并且此状态表明模型效果已通过用户的验收)  - 挂起，仅NA白名单用户有该状态   * JOB_PENDING: 挂起任务

        :return: The state of this Show2dModelTrainingJobResponse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this Show2dModelTrainingJobResponse.

        任务的状态。  与MetaStudio Console上用户看到的状态映射关系如下：  - 待提交   * WAIT_FILE_UPLOAD: 待上传文件  - 系统审核中   * AUTO_VERIFYING: 自动审核中   * MANUAL_VERIFYING: 人工审核中  - 系统审核未通过   * AUTO_VERIFY_FAILED: 自动审核失败   * MANUAL_VERIFY_FAILED: 人工审核失败  - 算法训练中   > 算法训练中的状态仅管理员需要处理，普通用户仅需要显示“算法训练中”即可。   * MANUAL_VERIFY_SUCCESS: 审核通过，等待预处理资源   * WAIT_TRAINING_DATA_PREPROCESS: 等待训练数据预处理   * TRAINING_DATA_PREPROCESSING: 训练数据预处理中   * TRAINING_DATA_PREPROCESS_FAILED: 训练数据预处理失败   * TRAINING_DATA_PREPROCESS_SUCCESS: 训练数据预处理完成，等待训练资源中   * TRAINING: 训练中   * TRAIN_FAILED: 训练失败   * TRAIN_SUCCESS: 训练完成，等待预处理资源   * INFERENCE_DATA_PREPROCESSING: 推理数据预处理中   * INFERENCE_DATA_PREPROCESS_FAILED: 推理数据预处理失败   * WAIT_MAIN_FILE_UPLOAD: 等待主文件上传   * MANUAL_STOP_INFERENCE_DATA_PREPROCESS: 人工中止推理预处理   * MANUAL_STOP_TRAIN: 人工中止训练   * MANUAL_STOP_TRAINING_DATA_PREPROCESS: 人工中止训练预处理   * WAIT_ADMIN_CONFIRM: 等待管理员审核   * WAIT_COMPILE: 等待转编译   * COMPILING: 转编译中   * COMPILE_FAILED: 转编译失败   * WAIT_GENERATE_ACTION: 等待原子动作生成   * WAIT_ARRANGE: 等待编排   * ACTION_GENERATE_DATA_PROCESSING: 原子动作生成中   * MANUAL_STOP_ACTION_GENERATE_DATA_PROCESSING: 人工中止动作生成   * MANUAL_STOP_ACTION_GENERATE_ORI_PROCESSING: 人工中止动作编排   * ACTION_GENERATE_ORI_PROCESSING: 动作编排中   * ACTION_GENERATE_DATA_FAILED: 动作生成失败   * ACTION_GENERATE_ORI_FAILED: 生成动作编排资产失败   * ACTION_GENERATE_ORI_SUCCESS: 动作编排成功   * GENERATE_ACTION_PREPROCESS_FAILED: 生成动作编排原子动作失败   * WAIT_ADMIN_CALIBRATION: 等待管理员确认动作信息   * WAIT_ASSET_SYNC: 等待资产同步  - 待用户审核，仅NA白名单用户有该状态   * WAIT_USER_CONFIRM: 等待用户确认训练效果  - 用户驳回，仅NA白名单用户有该状态   * JOB_REJECT: 驳回任务  - 已完成   * JOB_SUCCESS: 训练任务完成（普通用户任务的完成状态，此时用户已经可以使用模型）   * JOB_FINISH: 任务结束，是最终状态，不支持修改此状态(NA用户任务的完成状态，并且此状态表明模型效果已通过用户的验收)  - 挂起，仅NA白名单用户有该状态   * JOB_PENDING: 挂起任务

        :param state: The state of this Show2dModelTrainingJobResponse.
        :type state: str
        """
        self._state = state

    @property
    def asset_id(self):
        r"""Gets the asset_id of this Show2dModelTrainingJobResponse.

        模型资产ID。

        :return: The asset_id of this Show2dModelTrainingJobResponse.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        r"""Sets the asset_id of this Show2dModelTrainingJobResponse.

        模型资产ID。

        :param asset_id: The asset_id of this Show2dModelTrainingJobResponse.
        :type asset_id: str
        """
        self._asset_id = asset_id

    @property
    def project_id(self):
        r"""Gets the project_id of this Show2dModelTrainingJobResponse.

        模型资产所属项目ID。

        :return: The project_id of this Show2dModelTrainingJobResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this Show2dModelTrainingJobResponse.

        模型资产所属项目ID。

        :param project_id: The project_id of this Show2dModelTrainingJobResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def cover_download_url(self):
        r"""Gets the cover_download_url of this Show2dModelTrainingJobResponse.

        分身数字人模型封面下载URL。URL有效期24小时。

        :return: The cover_download_url of this Show2dModelTrainingJobResponse.
        :rtype: str
        """
        return self._cover_download_url

    @cover_download_url.setter
    def cover_download_url(self, cover_download_url):
        r"""Sets the cover_download_url of this Show2dModelTrainingJobResponse.

        分身数字人模型封面下载URL。URL有效期24小时。

        :param cover_download_url: The cover_download_url of this Show2dModelTrainingJobResponse.
        :type cover_download_url: str
        """
        self._cover_download_url = cover_download_url

    @property
    def last_update_time(self):
        r"""Gets the last_update_time of this Show2dModelTrainingJobResponse.

        用户最近一次更新任务的时间（包括租户创建或者重新提交），格式遵循：RFC 3339。 例 “2020-07-30T10:43:17Z”

        :return: The last_update_time of this Show2dModelTrainingJobResponse.
        :rtype: str
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        r"""Sets the last_update_time of this Show2dModelTrainingJobResponse.

        用户最近一次更新任务的时间（包括租户创建或者重新提交），格式遵循：RFC 3339。 例 “2020-07-30T10:43:17Z”

        :param last_update_time: The last_update_time of this Show2dModelTrainingJobResponse.
        :type last_update_time: str
        """
        self._last_update_time = last_update_time

    @property
    def create_time(self):
        r"""Gets the create_time of this Show2dModelTrainingJobResponse.

        创建时间，格式遵循：RFC 3339。 例 “2020-07-30T10:43:17Z”

        :return: The create_time of this Show2dModelTrainingJobResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this Show2dModelTrainingJobResponse.

        创建时间，格式遵循：RFC 3339。 例 “2020-07-30T10:43:17Z”

        :param create_time: The create_time of this Show2dModelTrainingJobResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def contact(self):
        r"""Gets the contact of this Show2dModelTrainingJobResponse.

        分身数字人训练任务创建者的手机号。

        :return: The contact of this Show2dModelTrainingJobResponse.
        :rtype: str
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        r"""Sets the contact of this Show2dModelTrainingJobResponse.

        分身数字人训练任务创建者的手机号。

        :param contact: The contact of this Show2dModelTrainingJobResponse.
        :type contact: str
        """
        self._contact = contact

    @property
    def batch_name(self):
        r"""Gets the batch_name of this Show2dModelTrainingJobResponse.

        分身数字人训练任务的批次名称。

        :return: The batch_name of this Show2dModelTrainingJobResponse.
        :rtype: str
        """
        return self._batch_name

    @batch_name.setter
    def batch_name(self, batch_name):
        r"""Sets the batch_name of this Show2dModelTrainingJobResponse.

        分身数字人训练任务的批次名称。

        :param batch_name: The batch_name of this Show2dModelTrainingJobResponse.
        :type batch_name: str
        """
        self._batch_name = batch_name

    @property
    def tags(self):
        r"""Gets the tags of this Show2dModelTrainingJobResponse.

        分身数字人训练任务标签。

        :return: The tags of this Show2dModelTrainingJobResponse.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this Show2dModelTrainingJobResponse.

        分身数字人训练任务标签。

        :param tags: The tags of this Show2dModelTrainingJobResponse.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def model_version(self):
        r"""Gets the model_version of this Show2dModelTrainingJobResponse.

        分身数字人模型版本。默认是V3.2版本模型。 * V3.2：V3.2版本模型 > * V3和V2版本已废弃不用

        :return: The model_version of this Show2dModelTrainingJobResponse.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        r"""Sets the model_version of this Show2dModelTrainingJobResponse.

        分身数字人模型版本。默认是V3.2版本模型。 * V3.2：V3.2版本模型 > * V3和V2版本已废弃不用

        :param model_version: The model_version of this Show2dModelTrainingJobResponse.
        :type model_version: str
        """
        self._model_version = model_version

    @property
    def matting_type(self):
        r"""Gets the matting_type of this Show2dModelTrainingJobResponse.

        抠图类型。默认是AI。 * AI：AI抠图 * MANUAL：人工抠图

        :return: The matting_type of this Show2dModelTrainingJobResponse.
        :rtype: str
        """
        return self._matting_type

    @matting_type.setter
    def matting_type(self, matting_type):
        r"""Sets the matting_type of this Show2dModelTrainingJobResponse.

        抠图类型。默认是AI。 * AI：AI抠图 * MANUAL：人工抠图

        :param matting_type: The matting_type of this Show2dModelTrainingJobResponse.
        :type matting_type: str
        """
        self._matting_type = matting_type

    @property
    def model_resolution(self):
        r"""Gets the model_resolution of this Show2dModelTrainingJobResponse.

        分身数字人模型分辨率。默认是1080P。 * 1080P：1080P。支持1080P及720P的视频输出。 * 4K：4K。支持4K、1080P及720P的视频输出。

        :return: The model_resolution of this Show2dModelTrainingJobResponse.
        :rtype: str
        """
        return self._model_resolution

    @model_resolution.setter
    def model_resolution(self, model_resolution):
        r"""Sets the model_resolution of this Show2dModelTrainingJobResponse.

        分身数字人模型分辨率。默认是1080P。 * 1080P：1080P。支持1080P及720P的视频输出。 * 4K：4K。支持4K、1080P及720P的视频输出。

        :param model_resolution: The model_resolution of this Show2dModelTrainingJobResponse.
        :type model_resolution: str
        """
        self._model_resolution = model_resolution

    @property
    def app_user_id(self):
        r"""Gets the app_user_id of this Show2dModelTrainingJobResponse.

        自定义用户id（如创建任务时设置了X-App-UserId则会携带）。

        :return: The app_user_id of this Show2dModelTrainingJobResponse.
        :rtype: str
        """
        return self._app_user_id

    @app_user_id.setter
    def app_user_id(self, app_user_id):
        r"""Sets the app_user_id of this Show2dModelTrainingJobResponse.

        自定义用户id（如创建任务时设置了X-App-UserId则会携带）。

        :param app_user_id: The app_user_id of this Show2dModelTrainingJobResponse.
        :type app_user_id: str
        """
        self._app_user_id = app_user_id

    @property
    def is_flexus(self):
        r"""Gets the is_flexus of this Show2dModelTrainingJobResponse.

        是否是基础版的形象训练

        :return: The is_flexus of this Show2dModelTrainingJobResponse.
        :rtype: bool
        """
        return self._is_flexus

    @is_flexus.setter
    def is_flexus(self, is_flexus):
        r"""Sets the is_flexus of this Show2dModelTrainingJobResponse.

        是否是基础版的形象训练

        :param is_flexus: The is_flexus of this Show2dModelTrainingJobResponse.
        :type is_flexus: bool
        """
        self._is_flexus = is_flexus

    @property
    def is_only_human_model(self):
        r"""Gets the is_only_human_model of this Show2dModelTrainingJobResponse.

        是否只训练形象模型，不训练声音模型。仅Flexus版本时有效，默认false。

        :return: The is_only_human_model of this Show2dModelTrainingJobResponse.
        :rtype: bool
        """
        return self._is_only_human_model

    @is_only_human_model.setter
    def is_only_human_model(self, is_only_human_model):
        r"""Sets the is_only_human_model of this Show2dModelTrainingJobResponse.

        是否只训练形象模型，不训练声音模型。仅Flexus版本时有效，默认false。

        :param is_only_human_model: The is_only_human_model of this Show2dModelTrainingJobResponse.
        :type is_only_human_model: bool
        """
        self._is_only_human_model = is_only_human_model

    @property
    def training_video_download_url(self):
        r"""Gets the training_video_download_url of this Show2dModelTrainingJobResponse.

        分身数字人训练视频下载URL。24小时内有效。

        :return: The training_video_download_url of this Show2dModelTrainingJobResponse.
        :rtype: str
        """
        return self._training_video_download_url

    @training_video_download_url.setter
    def training_video_download_url(self, training_video_download_url):
        r"""Sets the training_video_download_url of this Show2dModelTrainingJobResponse.

        分身数字人训练视频下载URL。24小时内有效。

        :param training_video_download_url: The training_video_download_url of this Show2dModelTrainingJobResponse.
        :type training_video_download_url: str
        """
        self._training_video_download_url = training_video_download_url

    @property
    def id_card_image1_download_url(self):
        r"""Gets the id_card_image1_download_url of this Show2dModelTrainingJobResponse.

        身份证正面照片下载URL。24小时内有效。

        :return: The id_card_image1_download_url of this Show2dModelTrainingJobResponse.
        :rtype: str
        """
        return self._id_card_image1_download_url

    @id_card_image1_download_url.setter
    def id_card_image1_download_url(self, id_card_image1_download_url):
        r"""Sets the id_card_image1_download_url of this Show2dModelTrainingJobResponse.

        身份证正面照片下载URL。24小时内有效。

        :param id_card_image1_download_url: The id_card_image1_download_url of this Show2dModelTrainingJobResponse.
        :type id_card_image1_download_url: str
        """
        self._id_card_image1_download_url = id_card_image1_download_url

    @property
    def id_card_image2_download_url(self):
        r"""Gets the id_card_image2_download_url of this Show2dModelTrainingJobResponse.

        身份证反面照片下载URL。24小时内有效。

        :return: The id_card_image2_download_url of this Show2dModelTrainingJobResponse.
        :rtype: str
        """
        return self._id_card_image2_download_url

    @id_card_image2_download_url.setter
    def id_card_image2_download_url(self, id_card_image2_download_url):
        r"""Sets the id_card_image2_download_url of this Show2dModelTrainingJobResponse.

        身份证反面照片下载URL。24小时内有效。

        :param id_card_image2_download_url: The id_card_image2_download_url of this Show2dModelTrainingJobResponse.
        :type id_card_image2_download_url: str
        """
        self._id_card_image2_download_url = id_card_image2_download_url

    @property
    def grant_file_download_url(self):
        r"""Gets the grant_file_download_url of this Show2dModelTrainingJobResponse.

        授权书下载URL。24小时内有效。

        :return: The grant_file_download_url of this Show2dModelTrainingJobResponse.
        :rtype: str
        """
        return self._grant_file_download_url

    @grant_file_download_url.setter
    def grant_file_download_url(self, grant_file_download_url):
        r"""Sets the grant_file_download_url of this Show2dModelTrainingJobResponse.

        授权书下载URL。24小时内有效。

        :param grant_file_download_url: The grant_file_download_url of this Show2dModelTrainingJobResponse.
        :type grant_file_download_url: str
        """
        self._grant_file_download_url = grant_file_download_url

    @property
    def pre_beauty_image_download_url(self):
        r"""Gets the pre_beauty_image_download_url of this Show2dModelTrainingJobResponse.

        美白前图片下载url。

        :return: The pre_beauty_image_download_url of this Show2dModelTrainingJobResponse.
        :rtype: str
        """
        return self._pre_beauty_image_download_url

    @pre_beauty_image_download_url.setter
    def pre_beauty_image_download_url(self, pre_beauty_image_download_url):
        r"""Sets the pre_beauty_image_download_url of this Show2dModelTrainingJobResponse.

        美白前图片下载url。

        :param pre_beauty_image_download_url: The pre_beauty_image_download_url of this Show2dModelTrainingJobResponse.
        :type pre_beauty_image_download_url: str
        """
        self._pre_beauty_image_download_url = pre_beauty_image_download_url

    @property
    def action_video_download_url(self):
        r"""Gets the action_video_download_url of this Show2dModelTrainingJobResponse.

        动作视频

        :return: The action_video_download_url of this Show2dModelTrainingJobResponse.
        :rtype: str
        """
        return self._action_video_download_url

    @action_video_download_url.setter
    def action_video_download_url(self, action_video_download_url):
        r"""Sets the action_video_download_url of this Show2dModelTrainingJobResponse.

        动作视频

        :param action_video_download_url: The action_video_download_url of this Show2dModelTrainingJobResponse.
        :type action_video_download_url: str
        """
        self._action_video_download_url = action_video_download_url

    @property
    def post_beauty_image_download_url(self):
        r"""Gets the post_beauty_image_download_url of this Show2dModelTrainingJobResponse.

        美白后图片下载url。

        :return: The post_beauty_image_download_url of this Show2dModelTrainingJobResponse.
        :rtype: str
        """
        return self._post_beauty_image_download_url

    @post_beauty_image_download_url.setter
    def post_beauty_image_download_url(self, post_beauty_image_download_url):
        r"""Sets the post_beauty_image_download_url of this Show2dModelTrainingJobResponse.

        美白后图片下载url。

        :param post_beauty_image_download_url: The post_beauty_image_download_url of this Show2dModelTrainingJobResponse.
        :type post_beauty_image_download_url: str
        """
        self._post_beauty_image_download_url = post_beauty_image_download_url

    @property
    def audio_file_download_url(self):
        r"""Gets the audio_file_download_url of this Show2dModelTrainingJobResponse.

        音频文件下载url。

        :return: The audio_file_download_url of this Show2dModelTrainingJobResponse.
        :rtype: str
        """
        return self._audio_file_download_url

    @audio_file_download_url.setter
    def audio_file_download_url(self, audio_file_download_url):
        r"""Sets the audio_file_download_url of this Show2dModelTrainingJobResponse.

        音频文件下载url。

        :param audio_file_download_url: The audio_file_download_url of this Show2dModelTrainingJobResponse.
        :type audio_file_download_url: str
        """
        self._audio_file_download_url = audio_file_download_url

    @property
    def operation_logs(self):
        r"""Gets the operation_logs of this Show2dModelTrainingJobResponse.

        操作日志列表。

        :return: The operation_logs of this Show2dModelTrainingJobResponse.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.OperationLogInfo`]
        """
        return self._operation_logs

    @operation_logs.setter
    def operation_logs(self, operation_logs):
        r"""Sets the operation_logs of this Show2dModelTrainingJobResponse.

        操作日志列表。

        :param operation_logs: The operation_logs of this Show2dModelTrainingJobResponse.
        :type operation_logs: list[:class:`huaweicloudsdkmetastudio.v1.OperationLogInfo`]
        """
        self._operation_logs = operation_logs

    @property
    def verify_video_matting_info(self):
        r"""Gets the verify_video_matting_info of this Show2dModelTrainingJobResponse.

        生成抠图验证视频时不抠图区域。

        :return: The verify_video_matting_info of this Show2dModelTrainingJobResponse.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.VerifyVideoMattingInfo`]
        """
        return self._verify_video_matting_info

    @verify_video_matting_info.setter
    def verify_video_matting_info(self, verify_video_matting_info):
        r"""Sets the verify_video_matting_info of this Show2dModelTrainingJobResponse.

        生成抠图验证视频时不抠图区域。

        :param verify_video_matting_info: The verify_video_matting_info of this Show2dModelTrainingJobResponse.
        :type verify_video_matting_info: list[:class:`huaweicloudsdkmetastudio.v1.VerifyVideoMattingInfo`]
        """
        self._verify_video_matting_info = verify_video_matting_info

    @property
    def comment_logs(self):
        r"""Gets the comment_logs of this Show2dModelTrainingJobResponse.

        评论记录列表。

        :return: The comment_logs of this Show2dModelTrainingJobResponse.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.CommentLogInfo`]
        """
        return self._comment_logs

    @comment_logs.setter
    def comment_logs(self, comment_logs):
        r"""Sets the comment_logs of this Show2dModelTrainingJobResponse.

        评论记录列表。

        :param comment_logs: The comment_logs of this Show2dModelTrainingJobResponse.
        :type comment_logs: list[:class:`huaweicloudsdkmetastudio.v1.CommentLogInfo`]
        """
        self._comment_logs = comment_logs

    @property
    def samples(self):
        r"""Gets the samples of this Show2dModelTrainingJobResponse.

        动作视频样例。

        :return: The samples of this Show2dModelTrainingJobResponse.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.ActionSampleInfo`]
        """
        return self._samples

    @samples.setter
    def samples(self, samples):
        r"""Sets the samples of this Show2dModelTrainingJobResponse.

        动作视频样例。

        :param samples: The samples of this Show2dModelTrainingJobResponse.
        :type samples: list[:class:`huaweicloudsdkmetastudio.v1.ActionSampleInfo`]
        """
        self._samples = samples

    @property
    def is_mask_file_uploaded(self):
        r"""Gets the is_mask_file_uploaded of this Show2dModelTrainingJobResponse.

        遮罩文件是否已上传。

        :return: The is_mask_file_uploaded of this Show2dModelTrainingJobResponse.
        :rtype: bool
        """
        return self._is_mask_file_uploaded

    @is_mask_file_uploaded.setter
    def is_mask_file_uploaded(self, is_mask_file_uploaded):
        r"""Sets the is_mask_file_uploaded of this Show2dModelTrainingJobResponse.

        遮罩文件是否已上传。

        :param is_mask_file_uploaded: The is_mask_file_uploaded of this Show2dModelTrainingJobResponse.
        :type is_mask_file_uploaded: bool
        """
        self._is_mask_file_uploaded = is_mask_file_uploaded

    @property
    def mask_file_download_url(self):
        r"""Gets the mask_file_download_url of this Show2dModelTrainingJobResponse.

        遮罩下载URL。24小时内有效。

        :return: The mask_file_download_url of this Show2dModelTrainingJobResponse.
        :rtype: str
        """
        return self._mask_file_download_url

    @mask_file_download_url.setter
    def mask_file_download_url(self, mask_file_download_url):
        r"""Sets the mask_file_download_url of this Show2dModelTrainingJobResponse.

        遮罩下载URL。24小时内有效。

        :param mask_file_download_url: The mask_file_download_url of this Show2dModelTrainingJobResponse.
        :type mask_file_download_url: str
        """
        self._mask_file_download_url = mask_file_download_url

    @property
    def verify_video_download_url(self):
        r"""Gets the verify_video_download_url of this Show2dModelTrainingJobResponse.

        制作审核视频

        :return: The verify_video_download_url of this Show2dModelTrainingJobResponse.
        :rtype: str
        """
        return self._verify_video_download_url

    @verify_video_download_url.setter
    def verify_video_download_url(self, verify_video_download_url):
        r"""Sets the verify_video_download_url of this Show2dModelTrainingJobResponse.

        制作审核视频

        :param verify_video_download_url: The verify_video_download_url of this Show2dModelTrainingJobResponse.
        :type verify_video_download_url: str
        """
        self._verify_video_download_url = verify_video_download_url

    @property
    def markable_video_download_url(self):
        r"""Gets the markable_video_download_url of this Show2dModelTrainingJobResponse.

        标注视频url下载链接。24小时内有效。

        :return: The markable_video_download_url of this Show2dModelTrainingJobResponse.
        :rtype: str
        """
        return self._markable_video_download_url

    @markable_video_download_url.setter
    def markable_video_download_url(self, markable_video_download_url):
        r"""Sets the markable_video_download_url of this Show2dModelTrainingJobResponse.

        标注视频url下载链接。24小时内有效。

        :param markable_video_download_url: The markable_video_download_url of this Show2dModelTrainingJobResponse.
        :type markable_video_download_url: str
        """
        self._markable_video_download_url = markable_video_download_url

    @property
    def traning_video_mark_info(self):
        r"""Gets the traning_video_mark_info of this Show2dModelTrainingJobResponse.

        :return: The traning_video_mark_info of this Show2dModelTrainingJobResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.TrainingVideoMarkInfo`
        """
        return self._traning_video_mark_info

    @traning_video_mark_info.setter
    def traning_video_mark_info(self, traning_video_mark_info):
        r"""Sets the traning_video_mark_info of this Show2dModelTrainingJobResponse.

        :param traning_video_mark_info: The traning_video_mark_info of this Show2dModelTrainingJobResponse.
        :type traning_video_mark_info: :class:`huaweicloudsdkmetastudio.v1.TrainingVideoMarkInfo`
        """
        self._traning_video_mark_info = traning_video_mark_info

    @property
    def inference_data_process_video_mark_info(self):
        r"""Gets the inference_data_process_video_mark_info of this Show2dModelTrainingJobResponse.

        :return: The inference_data_process_video_mark_info of this Show2dModelTrainingJobResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.InferenceVideoMarkInfo`
        """
        return self._inference_data_process_video_mark_info

    @inference_data_process_video_mark_info.setter
    def inference_data_process_video_mark_info(self, inference_data_process_video_mark_info):
        r"""Sets the inference_data_process_video_mark_info of this Show2dModelTrainingJobResponse.

        :param inference_data_process_video_mark_info: The inference_data_process_video_mark_info of this Show2dModelTrainingJobResponse.
        :type inference_data_process_video_mark_info: :class:`huaweicloudsdkmetastudio.v1.InferenceVideoMarkInfo`
        """
        self._inference_data_process_video_mark_info = inference_data_process_video_mark_info

    @property
    def inference_data_process_action_mark_info(self):
        r"""Gets the inference_data_process_action_mark_info of this Show2dModelTrainingJobResponse.

        :return: The inference_data_process_action_mark_info of this Show2dModelTrainingJobResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.InferenceActionMarkInfo`
        """
        return self._inference_data_process_action_mark_info

    @inference_data_process_action_mark_info.setter
    def inference_data_process_action_mark_info(self, inference_data_process_action_mark_info):
        r"""Sets the inference_data_process_action_mark_info of this Show2dModelTrainingJobResponse.

        :param inference_data_process_action_mark_info: The inference_data_process_action_mark_info of this Show2dModelTrainingJobResponse.
        :type inference_data_process_action_mark_info: :class:`huaweicloudsdkmetastudio.v1.InferenceActionMarkInfo`
        """
        self._inference_data_process_action_mark_info = inference_data_process_action_mark_info

    @property
    def inference_data_process_chat_action_mark_info(self):
        r"""Gets the inference_data_process_chat_action_mark_info of this Show2dModelTrainingJobResponse.

        :return: The inference_data_process_chat_action_mark_info of this Show2dModelTrainingJobResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.InferenceActionMarkInfo`
        """
        return self._inference_data_process_chat_action_mark_info

    @inference_data_process_chat_action_mark_info.setter
    def inference_data_process_chat_action_mark_info(self, inference_data_process_chat_action_mark_info):
        r"""Sets the inference_data_process_chat_action_mark_info of this Show2dModelTrainingJobResponse.

        :param inference_data_process_chat_action_mark_info: The inference_data_process_chat_action_mark_info of this Show2dModelTrainingJobResponse.
        :type inference_data_process_chat_action_mark_info: :class:`huaweicloudsdkmetastudio.v1.InferenceActionMarkInfo`
        """
        self._inference_data_process_chat_action_mark_info = inference_data_process_chat_action_mark_info

    @property
    def inference_data_process_eye_correction_mark_info(self):
        r"""Gets the inference_data_process_eye_correction_mark_info of this Show2dModelTrainingJobResponse.

        :return: The inference_data_process_eye_correction_mark_info of this Show2dModelTrainingJobResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.InferenceEyeCorrectionMarkInfo`
        """
        return self._inference_data_process_eye_correction_mark_info

    @inference_data_process_eye_correction_mark_info.setter
    def inference_data_process_eye_correction_mark_info(self, inference_data_process_eye_correction_mark_info):
        r"""Sets the inference_data_process_eye_correction_mark_info of this Show2dModelTrainingJobResponse.

        :param inference_data_process_eye_correction_mark_info: The inference_data_process_eye_correction_mark_info of this Show2dModelTrainingJobResponse.
        :type inference_data_process_eye_correction_mark_info: :class:`huaweicloudsdkmetastudio.v1.InferenceEyeCorrectionMarkInfo`
        """
        self._inference_data_process_eye_correction_mark_info = inference_data_process_eye_correction_mark_info

    @property
    def is_background_replacement(self):
        r"""Gets the is_background_replacement of this Show2dModelTrainingJobResponse.

        分身数字人是否需要背景替换。需要背景替换的分身数字人训练视频需要绿幕拍摄。

        :return: The is_background_replacement of this Show2dModelTrainingJobResponse.
        :rtype: bool
        """
        return self._is_background_replacement

    @is_background_replacement.setter
    def is_background_replacement(self, is_background_replacement):
        r"""Sets the is_background_replacement of this Show2dModelTrainingJobResponse.

        分身数字人是否需要背景替换。需要背景替换的分身数字人训练视频需要绿幕拍摄。

        :param is_background_replacement: The is_background_replacement of this Show2dModelTrainingJobResponse.
        :type is_background_replacement: bool
        """
        self._is_background_replacement = is_background_replacement

    @property
    def worker_type(self):
        r"""Gets the worker_type of this Show2dModelTrainingJobResponse.

        转编译任务机型

        :return: The worker_type of this Show2dModelTrainingJobResponse.
        :rtype: list[str]
        """
        return self._worker_type

    @worker_type.setter
    def worker_type(self, worker_type):
        r"""Sets the worker_type of this Show2dModelTrainingJobResponse.

        转编译任务机型

        :param worker_type: The worker_type of this Show2dModelTrainingJobResponse.
        :type worker_type: list[str]
        """
        self._worker_type = worker_type

    @property
    def voice_train_job_id(self):
        r"""Gets the voice_train_job_id of this Show2dModelTrainingJobResponse.

        声音训练任务id。

        :return: The voice_train_job_id of this Show2dModelTrainingJobResponse.
        :rtype: str
        """
        return self._voice_train_job_id

    @voice_train_job_id.setter
    def voice_train_job_id(self, voice_train_job_id):
        r"""Sets the voice_train_job_id of this Show2dModelTrainingJobResponse.

        声音训练任务id。

        :param voice_train_job_id: The voice_train_job_id of this Show2dModelTrainingJobResponse.
        :type voice_train_job_id: str
        """
        self._voice_train_job_id = voice_train_job_id

    @property
    def flexus_retry_count(self):
        r"""Gets the flexus_retry_count of this Show2dModelTrainingJobResponse.

        flexus版本任务剩余可以重训的次数，每重训一次减1，减到0时不可再重训。

        :return: The flexus_retry_count of this Show2dModelTrainingJobResponse.
        :rtype: int
        """
        return self._flexus_retry_count

    @flexus_retry_count.setter
    def flexus_retry_count(self, flexus_retry_count):
        r"""Sets the flexus_retry_count of this Show2dModelTrainingJobResponse.

        flexus版本任务剩余可以重训的次数，每重训一次减1，减到0时不可再重训。

        :param flexus_retry_count: The flexus_retry_count of this Show2dModelTrainingJobResponse.
        :type flexus_retry_count: int
        """
        self._flexus_retry_count = flexus_retry_count

    @property
    def audio_source_type(self):
        r"""Gets the audio_source_type of this Show2dModelTrainingJobResponse.

        声音来源类型 * VIDEO：视频中抽取音频 * AUDIO：单独上传的音频

        :return: The audio_source_type of this Show2dModelTrainingJobResponse.
        :rtype: str
        """
        return self._audio_source_type

    @audio_source_type.setter
    def audio_source_type(self, audio_source_type):
        r"""Sets the audio_source_type of this Show2dModelTrainingJobResponse.

        声音来源类型 * VIDEO：视频中抽取音频 * AUDIO：单独上传的音频

        :param audio_source_type: The audio_source_type of this Show2dModelTrainingJobResponse.
        :type audio_source_type: str
        """
        self._audio_source_type = audio_source_type

    @property
    def supported_service(self):
        r"""Gets the supported_service of this Show2dModelTrainingJobResponse.

        该任务所生成的模型支持的业务类型，可多选。  Flexus版数字人仅支持选择“VIDEO_2D”。

        :return: The supported_service of this Show2dModelTrainingJobResponse.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.SupportedServiceEnum`]
        """
        return self._supported_service

    @supported_service.setter
    def supported_service(self, supported_service):
        r"""Sets the supported_service of this Show2dModelTrainingJobResponse.

        该任务所生成的模型支持的业务类型，可多选。  Flexus版数字人仅支持选择“VIDEO_2D”。

        :param supported_service: The supported_service of this Show2dModelTrainingJobResponse.
        :type supported_service: list[:class:`huaweicloudsdkmetastudio.v1.SupportedServiceEnum`]
        """
        self._supported_service = supported_service

    @property
    def allocated_resource(self):
        r"""Gets the allocated_resource of this Show2dModelTrainingJobResponse.

        :return: The allocated_resource of this Show2dModelTrainingJobResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.TrainingAllocatedResource`
        """
        return self._allocated_resource

    @allocated_resource.setter
    def allocated_resource(self, allocated_resource):
        r"""Sets the allocated_resource of this Show2dModelTrainingJobResponse.

        :param allocated_resource: The allocated_resource of this Show2dModelTrainingJobResponse.
        :type allocated_resource: :class:`huaweicloudsdkmetastudio.v1.TrainingAllocatedResource`
        """
        self._allocated_resource = allocated_resource

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this Show2dModelTrainingJobResponse.

        :return: The x_request_id of this Show2dModelTrainingJobResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this Show2dModelTrainingJobResponse.

        :param x_request_id: The x_request_id of this Show2dModelTrainingJobResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Show2dModelTrainingJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
