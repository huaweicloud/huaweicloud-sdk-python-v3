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
        'training_video_download_url': 'str',
        'id_card_image1_download_url': 'str',
        'id_card_image2_download_url': 'str',
        'grant_file_download_url': 'str',
        'operation_logs': 'list[OperationLogInfo]',
        'comment_logs': 'list[CommentLogInfo]',
        'is_mask_file_uploaded': 'bool',
        'mask_file_download_url': 'str',
        'verify_video_download_url': 'str',
        'markable_video_download_url': 'str',
        'inference_data_process_video_mark_info': 'InferenceVideoMarkInfo',
        'inference_data_process_action_mark_info': 'InferenceActionMarkInfo',
        'inference_data_process_eye_correction_mark_info': 'InferenceEyeCorrectionMarkInfo',
        'is_background_replacement': 'bool',
        'worker_type': 'list[str]',
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
        'training_video_download_url': 'training_video_download_url',
        'id_card_image1_download_url': 'id_card_image1_download_url',
        'id_card_image2_download_url': 'id_card_image2_download_url',
        'grant_file_download_url': 'grant_file_download_url',
        'operation_logs': 'operation_logs',
        'comment_logs': 'comment_logs',
        'is_mask_file_uploaded': 'is_mask_file_uploaded',
        'mask_file_download_url': 'mask_file_download_url',
        'verify_video_download_url': 'verify_video_download_url',
        'markable_video_download_url': 'markable_video_download_url',
        'inference_data_process_video_mark_info': 'inference_data_process_video_mark_info',
        'inference_data_process_action_mark_info': 'inference_data_process_action_mark_info',
        'inference_data_process_eye_correction_mark_info': 'inference_data_process_eye_correction_mark_info',
        'is_background_replacement': 'is_background_replacement',
        'worker_type': 'worker_type',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, job_id=None, name=None, state=None, asset_id=None, project_id=None, cover_download_url=None, last_update_time=None, create_time=None, contact=None, batch_name=None, tags=None, model_version=None, matting_type=None, model_resolution=None, app_user_id=None, training_video_download_url=None, id_card_image1_download_url=None, id_card_image2_download_url=None, grant_file_download_url=None, operation_logs=None, comment_logs=None, is_mask_file_uploaded=None, mask_file_download_url=None, verify_video_download_url=None, markable_video_download_url=None, inference_data_process_video_mark_info=None, inference_data_process_action_mark_info=None, inference_data_process_eye_correction_mark_info=None, is_background_replacement=None, worker_type=None, x_request_id=None):
        """Show2dModelTrainingJobResponse

        The model defined in huaweicloud sdk

        :param job_id: 任务ID。
        :type job_id: str
        :param name: 分身数字人模型名称。该名称会作为资产库中分身数字人模型资产名称。
        :type name: str
        :param state: 任务的状态。 * WAIT_FILE_UPLOAD：待上传文件 * AUTO_VERIFYING：自动审核中 * AUTO_VERIFY_FAILED：自动审核失败 * MANUAL_VERIFYING：人工审核中 * MANUAL_VERIFY_FAILED：人工审核失败 * MANUAL_VERIFY_SUCCESS：审核通过，等待预处理资源 * TRAINING_DATA_PREPROCESSING：训练数据预处理中 * TRAINING_DATA_PREPROCESS_FAILED：训练数据预处理失败 * TRAINING_DATA_PREPROCESS_SUCCESS：训练数据预处理完成，等待训练资源中 * TRAINING：训练中 * TRAIN_FAILED：训练失败 * TRAIN_SUCCESS：训练完成，等待预处理资源 * INFERENCE_DATA_PREPROCESSING：推理数据预处理中 * INFERENCE_DATA_PREPROCESS_FAILED：推理数据预处理失败 * WAIT_MASK_UPLOAD：等待遮罩上传 * WAIT_MAIN_FILE_UPLOAD：等待主文件上传 * JOB_SUCCESS：训练任务完成 * WAIT_USER_CONFIRM：等待用户确认训练效果 * JOB_REJECT：驳回任务 * JOB_PENDING：挂起任务 * JOB_FINISH：任务结束，是最终状态，不支持修改此状态。
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
        :param contact: 分身数字人训练任务创建者联系方式，如手机或邮箱等。
        :type contact: str
        :param batch_name: 分身数字人训练任务的批次名称。
        :type batch_name: str
        :param tags: 分身数字人训练任务标签。
        :type tags: list[str]
        :param model_version: 分身数字人模型版本。默认是V3版本模型。 * V2: V2版本模型 * V3：V3版本模型 * V3.2：V3.2版本模型
        :type model_version: str
        :param matting_type: 抠图类型。默认是AI。 * AI：AI抠图 * MANUAL：人工抠图
        :type matting_type: str
        :param model_resolution: 分身数字人模型分辨率。默认是1080P。 * 1080P：1080P。支持1080P及720P的视频输出。 * 4K：4K。支持4K、1080P及720P的视频输出。
        :type model_resolution: str
        :param app_user_id: 自定义用户id（如创建任务时设置了X-App-UserId则会携带）。
        :type app_user_id: str
        :param training_video_download_url: 分身数字人训练视频下载URL。24小时内有效。
        :type training_video_download_url: str
        :param id_card_image1_download_url: 身份证正面照片下载URL。24小时内有效。
        :type id_card_image1_download_url: str
        :param id_card_image2_download_url: 身份证反面照片下载URL。24小时内有效。
        :type id_card_image2_download_url: str
        :param grant_file_download_url: 授权书下载URL。24小时内有效。
        :type grant_file_download_url: str
        :param operation_logs: 操作日志列表。
        :type operation_logs: list[:class:`huaweicloudsdkmetastudio.v1.OperationLogInfo`]
        :param comment_logs: 评论记录列表。
        :type comment_logs: list[:class:`huaweicloudsdkmetastudio.v1.CommentLogInfo`]
        :param is_mask_file_uploaded: 遮罩文件是否已上传。
        :type is_mask_file_uploaded: bool
        :param mask_file_download_url: 遮罩下载URL。24小时内有效。
        :type mask_file_download_url: str
        :param verify_video_download_url: 制作审核视频
        :type verify_video_download_url: str
        :param markable_video_download_url: 标注视频url下载链接。24小时内有效。
        :type markable_video_download_url: str
        :param inference_data_process_video_mark_info: 
        :type inference_data_process_video_mark_info: :class:`huaweicloudsdkmetastudio.v1.InferenceVideoMarkInfo`
        :param inference_data_process_action_mark_info: 
        :type inference_data_process_action_mark_info: :class:`huaweicloudsdkmetastudio.v1.InferenceActionMarkInfo`
        :param inference_data_process_eye_correction_mark_info: 
        :type inference_data_process_eye_correction_mark_info: :class:`huaweicloudsdkmetastudio.v1.InferenceEyeCorrectionMarkInfo`
        :param is_background_replacement: 分身数字人是否需要背景替换。需要背景替换的分身数字人训练视频需要绿幕拍摄。
        :type is_background_replacement: bool
        :param worker_type: 转编译任务机型
        :type worker_type: list[str]
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
        self._training_video_download_url = None
        self._id_card_image1_download_url = None
        self._id_card_image2_download_url = None
        self._grant_file_download_url = None
        self._operation_logs = None
        self._comment_logs = None
        self._is_mask_file_uploaded = None
        self._mask_file_download_url = None
        self._verify_video_download_url = None
        self._markable_video_download_url = None
        self._inference_data_process_video_mark_info = None
        self._inference_data_process_action_mark_info = None
        self._inference_data_process_eye_correction_mark_info = None
        self._is_background_replacement = None
        self._worker_type = None
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
        if training_video_download_url is not None:
            self.training_video_download_url = training_video_download_url
        if id_card_image1_download_url is not None:
            self.id_card_image1_download_url = id_card_image1_download_url
        if id_card_image2_download_url is not None:
            self.id_card_image2_download_url = id_card_image2_download_url
        if grant_file_download_url is not None:
            self.grant_file_download_url = grant_file_download_url
        if operation_logs is not None:
            self.operation_logs = operation_logs
        if comment_logs is not None:
            self.comment_logs = comment_logs
        if is_mask_file_uploaded is not None:
            self.is_mask_file_uploaded = is_mask_file_uploaded
        if mask_file_download_url is not None:
            self.mask_file_download_url = mask_file_download_url
        if verify_video_download_url is not None:
            self.verify_video_download_url = verify_video_download_url
        if markable_video_download_url is not None:
            self.markable_video_download_url = markable_video_download_url
        if inference_data_process_video_mark_info is not None:
            self.inference_data_process_video_mark_info = inference_data_process_video_mark_info
        if inference_data_process_action_mark_info is not None:
            self.inference_data_process_action_mark_info = inference_data_process_action_mark_info
        if inference_data_process_eye_correction_mark_info is not None:
            self.inference_data_process_eye_correction_mark_info = inference_data_process_eye_correction_mark_info
        if is_background_replacement is not None:
            self.is_background_replacement = is_background_replacement
        if worker_type is not None:
            self.worker_type = worker_type
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def job_id(self):
        """Gets the job_id of this Show2dModelTrainingJobResponse.

        任务ID。

        :return: The job_id of this Show2dModelTrainingJobResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this Show2dModelTrainingJobResponse.

        任务ID。

        :param job_id: The job_id of this Show2dModelTrainingJobResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def name(self):
        """Gets the name of this Show2dModelTrainingJobResponse.

        分身数字人模型名称。该名称会作为资产库中分身数字人模型资产名称。

        :return: The name of this Show2dModelTrainingJobResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Show2dModelTrainingJobResponse.

        分身数字人模型名称。该名称会作为资产库中分身数字人模型资产名称。

        :param name: The name of this Show2dModelTrainingJobResponse.
        :type name: str
        """
        self._name = name

    @property
    def state(self):
        """Gets the state of this Show2dModelTrainingJobResponse.

        任务的状态。 * WAIT_FILE_UPLOAD：待上传文件 * AUTO_VERIFYING：自动审核中 * AUTO_VERIFY_FAILED：自动审核失败 * MANUAL_VERIFYING：人工审核中 * MANUAL_VERIFY_FAILED：人工审核失败 * MANUAL_VERIFY_SUCCESS：审核通过，等待预处理资源 * TRAINING_DATA_PREPROCESSING：训练数据预处理中 * TRAINING_DATA_PREPROCESS_FAILED：训练数据预处理失败 * TRAINING_DATA_PREPROCESS_SUCCESS：训练数据预处理完成，等待训练资源中 * TRAINING：训练中 * TRAIN_FAILED：训练失败 * TRAIN_SUCCESS：训练完成，等待预处理资源 * INFERENCE_DATA_PREPROCESSING：推理数据预处理中 * INFERENCE_DATA_PREPROCESS_FAILED：推理数据预处理失败 * WAIT_MASK_UPLOAD：等待遮罩上传 * WAIT_MAIN_FILE_UPLOAD：等待主文件上传 * JOB_SUCCESS：训练任务完成 * WAIT_USER_CONFIRM：等待用户确认训练效果 * JOB_REJECT：驳回任务 * JOB_PENDING：挂起任务 * JOB_FINISH：任务结束，是最终状态，不支持修改此状态。

        :return: The state of this Show2dModelTrainingJobResponse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Show2dModelTrainingJobResponse.

        任务的状态。 * WAIT_FILE_UPLOAD：待上传文件 * AUTO_VERIFYING：自动审核中 * AUTO_VERIFY_FAILED：自动审核失败 * MANUAL_VERIFYING：人工审核中 * MANUAL_VERIFY_FAILED：人工审核失败 * MANUAL_VERIFY_SUCCESS：审核通过，等待预处理资源 * TRAINING_DATA_PREPROCESSING：训练数据预处理中 * TRAINING_DATA_PREPROCESS_FAILED：训练数据预处理失败 * TRAINING_DATA_PREPROCESS_SUCCESS：训练数据预处理完成，等待训练资源中 * TRAINING：训练中 * TRAIN_FAILED：训练失败 * TRAIN_SUCCESS：训练完成，等待预处理资源 * INFERENCE_DATA_PREPROCESSING：推理数据预处理中 * INFERENCE_DATA_PREPROCESS_FAILED：推理数据预处理失败 * WAIT_MASK_UPLOAD：等待遮罩上传 * WAIT_MAIN_FILE_UPLOAD：等待主文件上传 * JOB_SUCCESS：训练任务完成 * WAIT_USER_CONFIRM：等待用户确认训练效果 * JOB_REJECT：驳回任务 * JOB_PENDING：挂起任务 * JOB_FINISH：任务结束，是最终状态，不支持修改此状态。

        :param state: The state of this Show2dModelTrainingJobResponse.
        :type state: str
        """
        self._state = state

    @property
    def asset_id(self):
        """Gets the asset_id of this Show2dModelTrainingJobResponse.

        模型资产ID。

        :return: The asset_id of this Show2dModelTrainingJobResponse.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        """Sets the asset_id of this Show2dModelTrainingJobResponse.

        模型资产ID。

        :param asset_id: The asset_id of this Show2dModelTrainingJobResponse.
        :type asset_id: str
        """
        self._asset_id = asset_id

    @property
    def project_id(self):
        """Gets the project_id of this Show2dModelTrainingJobResponse.

        模型资产所属项目ID。

        :return: The project_id of this Show2dModelTrainingJobResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this Show2dModelTrainingJobResponse.

        模型资产所属项目ID。

        :param project_id: The project_id of this Show2dModelTrainingJobResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def cover_download_url(self):
        """Gets the cover_download_url of this Show2dModelTrainingJobResponse.

        分身数字人模型封面下载URL。URL有效期24小时。

        :return: The cover_download_url of this Show2dModelTrainingJobResponse.
        :rtype: str
        """
        return self._cover_download_url

    @cover_download_url.setter
    def cover_download_url(self, cover_download_url):
        """Sets the cover_download_url of this Show2dModelTrainingJobResponse.

        分身数字人模型封面下载URL。URL有效期24小时。

        :param cover_download_url: The cover_download_url of this Show2dModelTrainingJobResponse.
        :type cover_download_url: str
        """
        self._cover_download_url = cover_download_url

    @property
    def last_update_time(self):
        """Gets the last_update_time of this Show2dModelTrainingJobResponse.

        用户最近一次更新任务的时间（包括租户创建或者重新提交），格式遵循：RFC 3339。 例 “2020-07-30T10:43:17Z”

        :return: The last_update_time of this Show2dModelTrainingJobResponse.
        :rtype: str
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        """Sets the last_update_time of this Show2dModelTrainingJobResponse.

        用户最近一次更新任务的时间（包括租户创建或者重新提交），格式遵循：RFC 3339。 例 “2020-07-30T10:43:17Z”

        :param last_update_time: The last_update_time of this Show2dModelTrainingJobResponse.
        :type last_update_time: str
        """
        self._last_update_time = last_update_time

    @property
    def create_time(self):
        """Gets the create_time of this Show2dModelTrainingJobResponse.

        创建时间，格式遵循：RFC 3339。 例 “2020-07-30T10:43:17Z”

        :return: The create_time of this Show2dModelTrainingJobResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this Show2dModelTrainingJobResponse.

        创建时间，格式遵循：RFC 3339。 例 “2020-07-30T10:43:17Z”

        :param create_time: The create_time of this Show2dModelTrainingJobResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def contact(self):
        """Gets the contact of this Show2dModelTrainingJobResponse.

        分身数字人训练任务创建者联系方式，如手机或邮箱等。

        :return: The contact of this Show2dModelTrainingJobResponse.
        :rtype: str
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        """Sets the contact of this Show2dModelTrainingJobResponse.

        分身数字人训练任务创建者联系方式，如手机或邮箱等。

        :param contact: The contact of this Show2dModelTrainingJobResponse.
        :type contact: str
        """
        self._contact = contact

    @property
    def batch_name(self):
        """Gets the batch_name of this Show2dModelTrainingJobResponse.

        分身数字人训练任务的批次名称。

        :return: The batch_name of this Show2dModelTrainingJobResponse.
        :rtype: str
        """
        return self._batch_name

    @batch_name.setter
    def batch_name(self, batch_name):
        """Sets the batch_name of this Show2dModelTrainingJobResponse.

        分身数字人训练任务的批次名称。

        :param batch_name: The batch_name of this Show2dModelTrainingJobResponse.
        :type batch_name: str
        """
        self._batch_name = batch_name

    @property
    def tags(self):
        """Gets the tags of this Show2dModelTrainingJobResponse.

        分身数字人训练任务标签。

        :return: The tags of this Show2dModelTrainingJobResponse.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Show2dModelTrainingJobResponse.

        分身数字人训练任务标签。

        :param tags: The tags of this Show2dModelTrainingJobResponse.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def model_version(self):
        """Gets the model_version of this Show2dModelTrainingJobResponse.

        分身数字人模型版本。默认是V3版本模型。 * V2: V2版本模型 * V3：V3版本模型 * V3.2：V3.2版本模型

        :return: The model_version of this Show2dModelTrainingJobResponse.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """Sets the model_version of this Show2dModelTrainingJobResponse.

        分身数字人模型版本。默认是V3版本模型。 * V2: V2版本模型 * V3：V3版本模型 * V3.2：V3.2版本模型

        :param model_version: The model_version of this Show2dModelTrainingJobResponse.
        :type model_version: str
        """
        self._model_version = model_version

    @property
    def matting_type(self):
        """Gets the matting_type of this Show2dModelTrainingJobResponse.

        抠图类型。默认是AI。 * AI：AI抠图 * MANUAL：人工抠图

        :return: The matting_type of this Show2dModelTrainingJobResponse.
        :rtype: str
        """
        return self._matting_type

    @matting_type.setter
    def matting_type(self, matting_type):
        """Sets the matting_type of this Show2dModelTrainingJobResponse.

        抠图类型。默认是AI。 * AI：AI抠图 * MANUAL：人工抠图

        :param matting_type: The matting_type of this Show2dModelTrainingJobResponse.
        :type matting_type: str
        """
        self._matting_type = matting_type

    @property
    def model_resolution(self):
        """Gets the model_resolution of this Show2dModelTrainingJobResponse.

        分身数字人模型分辨率。默认是1080P。 * 1080P：1080P。支持1080P及720P的视频输出。 * 4K：4K。支持4K、1080P及720P的视频输出。

        :return: The model_resolution of this Show2dModelTrainingJobResponse.
        :rtype: str
        """
        return self._model_resolution

    @model_resolution.setter
    def model_resolution(self, model_resolution):
        """Sets the model_resolution of this Show2dModelTrainingJobResponse.

        分身数字人模型分辨率。默认是1080P。 * 1080P：1080P。支持1080P及720P的视频输出。 * 4K：4K。支持4K、1080P及720P的视频输出。

        :param model_resolution: The model_resolution of this Show2dModelTrainingJobResponse.
        :type model_resolution: str
        """
        self._model_resolution = model_resolution

    @property
    def app_user_id(self):
        """Gets the app_user_id of this Show2dModelTrainingJobResponse.

        自定义用户id（如创建任务时设置了X-App-UserId则会携带）。

        :return: The app_user_id of this Show2dModelTrainingJobResponse.
        :rtype: str
        """
        return self._app_user_id

    @app_user_id.setter
    def app_user_id(self, app_user_id):
        """Sets the app_user_id of this Show2dModelTrainingJobResponse.

        自定义用户id（如创建任务时设置了X-App-UserId则会携带）。

        :param app_user_id: The app_user_id of this Show2dModelTrainingJobResponse.
        :type app_user_id: str
        """
        self._app_user_id = app_user_id

    @property
    def training_video_download_url(self):
        """Gets the training_video_download_url of this Show2dModelTrainingJobResponse.

        分身数字人训练视频下载URL。24小时内有效。

        :return: The training_video_download_url of this Show2dModelTrainingJobResponse.
        :rtype: str
        """
        return self._training_video_download_url

    @training_video_download_url.setter
    def training_video_download_url(self, training_video_download_url):
        """Sets the training_video_download_url of this Show2dModelTrainingJobResponse.

        分身数字人训练视频下载URL。24小时内有效。

        :param training_video_download_url: The training_video_download_url of this Show2dModelTrainingJobResponse.
        :type training_video_download_url: str
        """
        self._training_video_download_url = training_video_download_url

    @property
    def id_card_image1_download_url(self):
        """Gets the id_card_image1_download_url of this Show2dModelTrainingJobResponse.

        身份证正面照片下载URL。24小时内有效。

        :return: The id_card_image1_download_url of this Show2dModelTrainingJobResponse.
        :rtype: str
        """
        return self._id_card_image1_download_url

    @id_card_image1_download_url.setter
    def id_card_image1_download_url(self, id_card_image1_download_url):
        """Sets the id_card_image1_download_url of this Show2dModelTrainingJobResponse.

        身份证正面照片下载URL。24小时内有效。

        :param id_card_image1_download_url: The id_card_image1_download_url of this Show2dModelTrainingJobResponse.
        :type id_card_image1_download_url: str
        """
        self._id_card_image1_download_url = id_card_image1_download_url

    @property
    def id_card_image2_download_url(self):
        """Gets the id_card_image2_download_url of this Show2dModelTrainingJobResponse.

        身份证反面照片下载URL。24小时内有效。

        :return: The id_card_image2_download_url of this Show2dModelTrainingJobResponse.
        :rtype: str
        """
        return self._id_card_image2_download_url

    @id_card_image2_download_url.setter
    def id_card_image2_download_url(self, id_card_image2_download_url):
        """Sets the id_card_image2_download_url of this Show2dModelTrainingJobResponse.

        身份证反面照片下载URL。24小时内有效。

        :param id_card_image2_download_url: The id_card_image2_download_url of this Show2dModelTrainingJobResponse.
        :type id_card_image2_download_url: str
        """
        self._id_card_image2_download_url = id_card_image2_download_url

    @property
    def grant_file_download_url(self):
        """Gets the grant_file_download_url of this Show2dModelTrainingJobResponse.

        授权书下载URL。24小时内有效。

        :return: The grant_file_download_url of this Show2dModelTrainingJobResponse.
        :rtype: str
        """
        return self._grant_file_download_url

    @grant_file_download_url.setter
    def grant_file_download_url(self, grant_file_download_url):
        """Sets the grant_file_download_url of this Show2dModelTrainingJobResponse.

        授权书下载URL。24小时内有效。

        :param grant_file_download_url: The grant_file_download_url of this Show2dModelTrainingJobResponse.
        :type grant_file_download_url: str
        """
        self._grant_file_download_url = grant_file_download_url

    @property
    def operation_logs(self):
        """Gets the operation_logs of this Show2dModelTrainingJobResponse.

        操作日志列表。

        :return: The operation_logs of this Show2dModelTrainingJobResponse.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.OperationLogInfo`]
        """
        return self._operation_logs

    @operation_logs.setter
    def operation_logs(self, operation_logs):
        """Sets the operation_logs of this Show2dModelTrainingJobResponse.

        操作日志列表。

        :param operation_logs: The operation_logs of this Show2dModelTrainingJobResponse.
        :type operation_logs: list[:class:`huaweicloudsdkmetastudio.v1.OperationLogInfo`]
        """
        self._operation_logs = operation_logs

    @property
    def comment_logs(self):
        """Gets the comment_logs of this Show2dModelTrainingJobResponse.

        评论记录列表。

        :return: The comment_logs of this Show2dModelTrainingJobResponse.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.CommentLogInfo`]
        """
        return self._comment_logs

    @comment_logs.setter
    def comment_logs(self, comment_logs):
        """Sets the comment_logs of this Show2dModelTrainingJobResponse.

        评论记录列表。

        :param comment_logs: The comment_logs of this Show2dModelTrainingJobResponse.
        :type comment_logs: list[:class:`huaweicloudsdkmetastudio.v1.CommentLogInfo`]
        """
        self._comment_logs = comment_logs

    @property
    def is_mask_file_uploaded(self):
        """Gets the is_mask_file_uploaded of this Show2dModelTrainingJobResponse.

        遮罩文件是否已上传。

        :return: The is_mask_file_uploaded of this Show2dModelTrainingJobResponse.
        :rtype: bool
        """
        return self._is_mask_file_uploaded

    @is_mask_file_uploaded.setter
    def is_mask_file_uploaded(self, is_mask_file_uploaded):
        """Sets the is_mask_file_uploaded of this Show2dModelTrainingJobResponse.

        遮罩文件是否已上传。

        :param is_mask_file_uploaded: The is_mask_file_uploaded of this Show2dModelTrainingJobResponse.
        :type is_mask_file_uploaded: bool
        """
        self._is_mask_file_uploaded = is_mask_file_uploaded

    @property
    def mask_file_download_url(self):
        """Gets the mask_file_download_url of this Show2dModelTrainingJobResponse.

        遮罩下载URL。24小时内有效。

        :return: The mask_file_download_url of this Show2dModelTrainingJobResponse.
        :rtype: str
        """
        return self._mask_file_download_url

    @mask_file_download_url.setter
    def mask_file_download_url(self, mask_file_download_url):
        """Sets the mask_file_download_url of this Show2dModelTrainingJobResponse.

        遮罩下载URL。24小时内有效。

        :param mask_file_download_url: The mask_file_download_url of this Show2dModelTrainingJobResponse.
        :type mask_file_download_url: str
        """
        self._mask_file_download_url = mask_file_download_url

    @property
    def verify_video_download_url(self):
        """Gets the verify_video_download_url of this Show2dModelTrainingJobResponse.

        制作审核视频

        :return: The verify_video_download_url of this Show2dModelTrainingJobResponse.
        :rtype: str
        """
        return self._verify_video_download_url

    @verify_video_download_url.setter
    def verify_video_download_url(self, verify_video_download_url):
        """Sets the verify_video_download_url of this Show2dModelTrainingJobResponse.

        制作审核视频

        :param verify_video_download_url: The verify_video_download_url of this Show2dModelTrainingJobResponse.
        :type verify_video_download_url: str
        """
        self._verify_video_download_url = verify_video_download_url

    @property
    def markable_video_download_url(self):
        """Gets the markable_video_download_url of this Show2dModelTrainingJobResponse.

        标注视频url下载链接。24小时内有效。

        :return: The markable_video_download_url of this Show2dModelTrainingJobResponse.
        :rtype: str
        """
        return self._markable_video_download_url

    @markable_video_download_url.setter
    def markable_video_download_url(self, markable_video_download_url):
        """Sets the markable_video_download_url of this Show2dModelTrainingJobResponse.

        标注视频url下载链接。24小时内有效。

        :param markable_video_download_url: The markable_video_download_url of this Show2dModelTrainingJobResponse.
        :type markable_video_download_url: str
        """
        self._markable_video_download_url = markable_video_download_url

    @property
    def inference_data_process_video_mark_info(self):
        """Gets the inference_data_process_video_mark_info of this Show2dModelTrainingJobResponse.

        :return: The inference_data_process_video_mark_info of this Show2dModelTrainingJobResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.InferenceVideoMarkInfo`
        """
        return self._inference_data_process_video_mark_info

    @inference_data_process_video_mark_info.setter
    def inference_data_process_video_mark_info(self, inference_data_process_video_mark_info):
        """Sets the inference_data_process_video_mark_info of this Show2dModelTrainingJobResponse.

        :param inference_data_process_video_mark_info: The inference_data_process_video_mark_info of this Show2dModelTrainingJobResponse.
        :type inference_data_process_video_mark_info: :class:`huaweicloudsdkmetastudio.v1.InferenceVideoMarkInfo`
        """
        self._inference_data_process_video_mark_info = inference_data_process_video_mark_info

    @property
    def inference_data_process_action_mark_info(self):
        """Gets the inference_data_process_action_mark_info of this Show2dModelTrainingJobResponse.

        :return: The inference_data_process_action_mark_info of this Show2dModelTrainingJobResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.InferenceActionMarkInfo`
        """
        return self._inference_data_process_action_mark_info

    @inference_data_process_action_mark_info.setter
    def inference_data_process_action_mark_info(self, inference_data_process_action_mark_info):
        """Sets the inference_data_process_action_mark_info of this Show2dModelTrainingJobResponse.

        :param inference_data_process_action_mark_info: The inference_data_process_action_mark_info of this Show2dModelTrainingJobResponse.
        :type inference_data_process_action_mark_info: :class:`huaweicloudsdkmetastudio.v1.InferenceActionMarkInfo`
        """
        self._inference_data_process_action_mark_info = inference_data_process_action_mark_info

    @property
    def inference_data_process_eye_correction_mark_info(self):
        """Gets the inference_data_process_eye_correction_mark_info of this Show2dModelTrainingJobResponse.

        :return: The inference_data_process_eye_correction_mark_info of this Show2dModelTrainingJobResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.InferenceEyeCorrectionMarkInfo`
        """
        return self._inference_data_process_eye_correction_mark_info

    @inference_data_process_eye_correction_mark_info.setter
    def inference_data_process_eye_correction_mark_info(self, inference_data_process_eye_correction_mark_info):
        """Sets the inference_data_process_eye_correction_mark_info of this Show2dModelTrainingJobResponse.

        :param inference_data_process_eye_correction_mark_info: The inference_data_process_eye_correction_mark_info of this Show2dModelTrainingJobResponse.
        :type inference_data_process_eye_correction_mark_info: :class:`huaweicloudsdkmetastudio.v1.InferenceEyeCorrectionMarkInfo`
        """
        self._inference_data_process_eye_correction_mark_info = inference_data_process_eye_correction_mark_info

    @property
    def is_background_replacement(self):
        """Gets the is_background_replacement of this Show2dModelTrainingJobResponse.

        分身数字人是否需要背景替换。需要背景替换的分身数字人训练视频需要绿幕拍摄。

        :return: The is_background_replacement of this Show2dModelTrainingJobResponse.
        :rtype: bool
        """
        return self._is_background_replacement

    @is_background_replacement.setter
    def is_background_replacement(self, is_background_replacement):
        """Sets the is_background_replacement of this Show2dModelTrainingJobResponse.

        分身数字人是否需要背景替换。需要背景替换的分身数字人训练视频需要绿幕拍摄。

        :param is_background_replacement: The is_background_replacement of this Show2dModelTrainingJobResponse.
        :type is_background_replacement: bool
        """
        self._is_background_replacement = is_background_replacement

    @property
    def worker_type(self):
        """Gets the worker_type of this Show2dModelTrainingJobResponse.

        转编译任务机型

        :return: The worker_type of this Show2dModelTrainingJobResponse.
        :rtype: list[str]
        """
        return self._worker_type

    @worker_type.setter
    def worker_type(self, worker_type):
        """Sets the worker_type of this Show2dModelTrainingJobResponse.

        转编译任务机型

        :param worker_type: The worker_type of this Show2dModelTrainingJobResponse.
        :type worker_type: list[str]
        """
        self._worker_type = worker_type

    @property
    def x_request_id(self):
        """Gets the x_request_id of this Show2dModelTrainingJobResponse.

        :return: The x_request_id of this Show2dModelTrainingJobResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this Show2dModelTrainingJobResponse.

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
