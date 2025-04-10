# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TrainingJobBasicInfo:

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
        'is_only_human_model': 'bool'
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
        'is_only_human_model': 'is_only_human_model'
    }

    def __init__(self, job_id=None, name=None, state=None, asset_id=None, project_id=None, cover_download_url=None, last_update_time=None, create_time=None, contact=None, batch_name=None, tags=None, model_version=None, matting_type=None, model_resolution=None, app_user_id=None, is_flexus=None, is_only_human_model=None):
        r"""TrainingJobBasicInfo

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
        """
        
        

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

    @property
    def job_id(self):
        r"""Gets the job_id of this TrainingJobBasicInfo.

        任务ID。

        :return: The job_id of this TrainingJobBasicInfo.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this TrainingJobBasicInfo.

        任务ID。

        :param job_id: The job_id of this TrainingJobBasicInfo.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def name(self):
        r"""Gets the name of this TrainingJobBasicInfo.

        分身数字人模型名称。该名称会作为资产库中分身数字人模型资产名称。

        :return: The name of this TrainingJobBasicInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this TrainingJobBasicInfo.

        分身数字人模型名称。该名称会作为资产库中分身数字人模型资产名称。

        :param name: The name of this TrainingJobBasicInfo.
        :type name: str
        """
        self._name = name

    @property
    def state(self):
        r"""Gets the state of this TrainingJobBasicInfo.

        任务的状态。  与MetaStudio Console上用户看到的状态映射关系如下：  - 待提交   * WAIT_FILE_UPLOAD: 待上传文件  - 系统审核中   * AUTO_VERIFYING: 自动审核中   * MANUAL_VERIFYING: 人工审核中  - 系统审核未通过   * AUTO_VERIFY_FAILED: 自动审核失败   * MANUAL_VERIFY_FAILED: 人工审核失败  - 算法训练中   > 算法训练中的状态仅管理员需要处理，普通用户仅需要显示“算法训练中”即可。   * MANUAL_VERIFY_SUCCESS: 审核通过，等待预处理资源   * WAIT_TRAINING_DATA_PREPROCESS: 等待训练数据预处理   * TRAINING_DATA_PREPROCESSING: 训练数据预处理中   * TRAINING_DATA_PREPROCESS_FAILED: 训练数据预处理失败   * TRAINING_DATA_PREPROCESS_SUCCESS: 训练数据预处理完成，等待训练资源中   * TRAINING: 训练中   * TRAIN_FAILED: 训练失败   * TRAIN_SUCCESS: 训练完成，等待预处理资源   * INFERENCE_DATA_PREPROCESSING: 推理数据预处理中   * INFERENCE_DATA_PREPROCESS_FAILED: 推理数据预处理失败   * WAIT_MAIN_FILE_UPLOAD: 等待主文件上传   * MANUAL_STOP_INFERENCE_DATA_PREPROCESS: 人工中止推理预处理   * MANUAL_STOP_TRAIN: 人工中止训练   * MANUAL_STOP_TRAINING_DATA_PREPROCESS: 人工中止训练预处理   * WAIT_ADMIN_CONFIRM: 等待管理员审核   * WAIT_COMPILE: 等待转编译   * COMPILING: 转编译中   * COMPILE_FAILED: 转编译失败   * WAIT_GENERATE_ACTION: 等待原子动作生成   * WAIT_ARRANGE: 等待编排   * ACTION_GENERATE_DATA_PROCESSING: 原子动作生成中   * MANUAL_STOP_ACTION_GENERATE_DATA_PROCESSING: 人工中止动作生成   * MANUAL_STOP_ACTION_GENERATE_ORI_PROCESSING: 人工中止动作编排   * ACTION_GENERATE_ORI_PROCESSING: 动作编排中   * ACTION_GENERATE_DATA_FAILED: 动作生成失败   * ACTION_GENERATE_ORI_FAILED: 生成动作编排资产失败   * ACTION_GENERATE_ORI_SUCCESS: 动作编排成功   * GENERATE_ACTION_PREPROCESS_FAILED: 生成动作编排原子动作失败   * WAIT_ADMIN_CALIBRATION: 等待管理员确认动作信息   * WAIT_ASSET_SYNC: 等待资产同步  - 待用户审核，仅NA白名单用户有该状态   * WAIT_USER_CONFIRM: 等待用户确认训练效果  - 用户驳回，仅NA白名单用户有该状态   * JOB_REJECT: 驳回任务  - 已完成   * JOB_SUCCESS: 训练任务完成（普通用户任务的完成状态，此时用户已经可以使用模型）   * JOB_FINISH: 任务结束，是最终状态，不支持修改此状态(NA用户任务的完成状态，并且此状态表明模型效果已通过用户的验收)  - 挂起，仅NA白名单用户有该状态   * JOB_PENDING: 挂起任务

        :return: The state of this TrainingJobBasicInfo.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this TrainingJobBasicInfo.

        任务的状态。  与MetaStudio Console上用户看到的状态映射关系如下：  - 待提交   * WAIT_FILE_UPLOAD: 待上传文件  - 系统审核中   * AUTO_VERIFYING: 自动审核中   * MANUAL_VERIFYING: 人工审核中  - 系统审核未通过   * AUTO_VERIFY_FAILED: 自动审核失败   * MANUAL_VERIFY_FAILED: 人工审核失败  - 算法训练中   > 算法训练中的状态仅管理员需要处理，普通用户仅需要显示“算法训练中”即可。   * MANUAL_VERIFY_SUCCESS: 审核通过，等待预处理资源   * WAIT_TRAINING_DATA_PREPROCESS: 等待训练数据预处理   * TRAINING_DATA_PREPROCESSING: 训练数据预处理中   * TRAINING_DATA_PREPROCESS_FAILED: 训练数据预处理失败   * TRAINING_DATA_PREPROCESS_SUCCESS: 训练数据预处理完成，等待训练资源中   * TRAINING: 训练中   * TRAIN_FAILED: 训练失败   * TRAIN_SUCCESS: 训练完成，等待预处理资源   * INFERENCE_DATA_PREPROCESSING: 推理数据预处理中   * INFERENCE_DATA_PREPROCESS_FAILED: 推理数据预处理失败   * WAIT_MAIN_FILE_UPLOAD: 等待主文件上传   * MANUAL_STOP_INFERENCE_DATA_PREPROCESS: 人工中止推理预处理   * MANUAL_STOP_TRAIN: 人工中止训练   * MANUAL_STOP_TRAINING_DATA_PREPROCESS: 人工中止训练预处理   * WAIT_ADMIN_CONFIRM: 等待管理员审核   * WAIT_COMPILE: 等待转编译   * COMPILING: 转编译中   * COMPILE_FAILED: 转编译失败   * WAIT_GENERATE_ACTION: 等待原子动作生成   * WAIT_ARRANGE: 等待编排   * ACTION_GENERATE_DATA_PROCESSING: 原子动作生成中   * MANUAL_STOP_ACTION_GENERATE_DATA_PROCESSING: 人工中止动作生成   * MANUAL_STOP_ACTION_GENERATE_ORI_PROCESSING: 人工中止动作编排   * ACTION_GENERATE_ORI_PROCESSING: 动作编排中   * ACTION_GENERATE_DATA_FAILED: 动作生成失败   * ACTION_GENERATE_ORI_FAILED: 生成动作编排资产失败   * ACTION_GENERATE_ORI_SUCCESS: 动作编排成功   * GENERATE_ACTION_PREPROCESS_FAILED: 生成动作编排原子动作失败   * WAIT_ADMIN_CALIBRATION: 等待管理员确认动作信息   * WAIT_ASSET_SYNC: 等待资产同步  - 待用户审核，仅NA白名单用户有该状态   * WAIT_USER_CONFIRM: 等待用户确认训练效果  - 用户驳回，仅NA白名单用户有该状态   * JOB_REJECT: 驳回任务  - 已完成   * JOB_SUCCESS: 训练任务完成（普通用户任务的完成状态，此时用户已经可以使用模型）   * JOB_FINISH: 任务结束，是最终状态，不支持修改此状态(NA用户任务的完成状态，并且此状态表明模型效果已通过用户的验收)  - 挂起，仅NA白名单用户有该状态   * JOB_PENDING: 挂起任务

        :param state: The state of this TrainingJobBasicInfo.
        :type state: str
        """
        self._state = state

    @property
    def asset_id(self):
        r"""Gets the asset_id of this TrainingJobBasicInfo.

        模型资产ID。

        :return: The asset_id of this TrainingJobBasicInfo.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        r"""Sets the asset_id of this TrainingJobBasicInfo.

        模型资产ID。

        :param asset_id: The asset_id of this TrainingJobBasicInfo.
        :type asset_id: str
        """
        self._asset_id = asset_id

    @property
    def project_id(self):
        r"""Gets the project_id of this TrainingJobBasicInfo.

        模型资产所属项目ID。

        :return: The project_id of this TrainingJobBasicInfo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this TrainingJobBasicInfo.

        模型资产所属项目ID。

        :param project_id: The project_id of this TrainingJobBasicInfo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def cover_download_url(self):
        r"""Gets the cover_download_url of this TrainingJobBasicInfo.

        分身数字人模型封面下载URL。URL有效期24小时。

        :return: The cover_download_url of this TrainingJobBasicInfo.
        :rtype: str
        """
        return self._cover_download_url

    @cover_download_url.setter
    def cover_download_url(self, cover_download_url):
        r"""Sets the cover_download_url of this TrainingJobBasicInfo.

        分身数字人模型封面下载URL。URL有效期24小时。

        :param cover_download_url: The cover_download_url of this TrainingJobBasicInfo.
        :type cover_download_url: str
        """
        self._cover_download_url = cover_download_url

    @property
    def last_update_time(self):
        r"""Gets the last_update_time of this TrainingJobBasicInfo.

        用户最近一次更新任务的时间（包括租户创建或者重新提交），格式遵循：RFC 3339。 例 “2020-07-30T10:43:17Z”

        :return: The last_update_time of this TrainingJobBasicInfo.
        :rtype: str
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        r"""Sets the last_update_time of this TrainingJobBasicInfo.

        用户最近一次更新任务的时间（包括租户创建或者重新提交），格式遵循：RFC 3339。 例 “2020-07-30T10:43:17Z”

        :param last_update_time: The last_update_time of this TrainingJobBasicInfo.
        :type last_update_time: str
        """
        self._last_update_time = last_update_time

    @property
    def create_time(self):
        r"""Gets the create_time of this TrainingJobBasicInfo.

        创建时间，格式遵循：RFC 3339。 例 “2020-07-30T10:43:17Z”

        :return: The create_time of this TrainingJobBasicInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this TrainingJobBasicInfo.

        创建时间，格式遵循：RFC 3339。 例 “2020-07-30T10:43:17Z”

        :param create_time: The create_time of this TrainingJobBasicInfo.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def contact(self):
        r"""Gets the contact of this TrainingJobBasicInfo.

        分身数字人训练任务创建者的手机号。

        :return: The contact of this TrainingJobBasicInfo.
        :rtype: str
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        r"""Sets the contact of this TrainingJobBasicInfo.

        分身数字人训练任务创建者的手机号。

        :param contact: The contact of this TrainingJobBasicInfo.
        :type contact: str
        """
        self._contact = contact

    @property
    def batch_name(self):
        r"""Gets the batch_name of this TrainingJobBasicInfo.

        分身数字人训练任务的批次名称。

        :return: The batch_name of this TrainingJobBasicInfo.
        :rtype: str
        """
        return self._batch_name

    @batch_name.setter
    def batch_name(self, batch_name):
        r"""Sets the batch_name of this TrainingJobBasicInfo.

        分身数字人训练任务的批次名称。

        :param batch_name: The batch_name of this TrainingJobBasicInfo.
        :type batch_name: str
        """
        self._batch_name = batch_name

    @property
    def tags(self):
        r"""Gets the tags of this TrainingJobBasicInfo.

        分身数字人训练任务标签。

        :return: The tags of this TrainingJobBasicInfo.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this TrainingJobBasicInfo.

        分身数字人训练任务标签。

        :param tags: The tags of this TrainingJobBasicInfo.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def model_version(self):
        r"""Gets the model_version of this TrainingJobBasicInfo.

        分身数字人模型版本。默认是V3.2版本模型。 * V3.2：V3.2版本模型 > * V3和V2版本已废弃不用

        :return: The model_version of this TrainingJobBasicInfo.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        r"""Sets the model_version of this TrainingJobBasicInfo.

        分身数字人模型版本。默认是V3.2版本模型。 * V3.2：V3.2版本模型 > * V3和V2版本已废弃不用

        :param model_version: The model_version of this TrainingJobBasicInfo.
        :type model_version: str
        """
        self._model_version = model_version

    @property
    def matting_type(self):
        r"""Gets the matting_type of this TrainingJobBasicInfo.

        抠图类型。默认是AI。 * AI：AI抠图 * MANUAL：人工抠图

        :return: The matting_type of this TrainingJobBasicInfo.
        :rtype: str
        """
        return self._matting_type

    @matting_type.setter
    def matting_type(self, matting_type):
        r"""Sets the matting_type of this TrainingJobBasicInfo.

        抠图类型。默认是AI。 * AI：AI抠图 * MANUAL：人工抠图

        :param matting_type: The matting_type of this TrainingJobBasicInfo.
        :type matting_type: str
        """
        self._matting_type = matting_type

    @property
    def model_resolution(self):
        r"""Gets the model_resolution of this TrainingJobBasicInfo.

        分身数字人模型分辨率。默认是1080P。 * 1080P：1080P。支持1080P及720P的视频输出。 * 4K：4K。支持4K、1080P及720P的视频输出。

        :return: The model_resolution of this TrainingJobBasicInfo.
        :rtype: str
        """
        return self._model_resolution

    @model_resolution.setter
    def model_resolution(self, model_resolution):
        r"""Sets the model_resolution of this TrainingJobBasicInfo.

        分身数字人模型分辨率。默认是1080P。 * 1080P：1080P。支持1080P及720P的视频输出。 * 4K：4K。支持4K、1080P及720P的视频输出。

        :param model_resolution: The model_resolution of this TrainingJobBasicInfo.
        :type model_resolution: str
        """
        self._model_resolution = model_resolution

    @property
    def app_user_id(self):
        r"""Gets the app_user_id of this TrainingJobBasicInfo.

        自定义用户id（如创建任务时设置了X-App-UserId则会携带）。

        :return: The app_user_id of this TrainingJobBasicInfo.
        :rtype: str
        """
        return self._app_user_id

    @app_user_id.setter
    def app_user_id(self, app_user_id):
        r"""Sets the app_user_id of this TrainingJobBasicInfo.

        自定义用户id（如创建任务时设置了X-App-UserId则会携带）。

        :param app_user_id: The app_user_id of this TrainingJobBasicInfo.
        :type app_user_id: str
        """
        self._app_user_id = app_user_id

    @property
    def is_flexus(self):
        r"""Gets the is_flexus of this TrainingJobBasicInfo.

        是否是基础版的形象训练

        :return: The is_flexus of this TrainingJobBasicInfo.
        :rtype: bool
        """
        return self._is_flexus

    @is_flexus.setter
    def is_flexus(self, is_flexus):
        r"""Sets the is_flexus of this TrainingJobBasicInfo.

        是否是基础版的形象训练

        :param is_flexus: The is_flexus of this TrainingJobBasicInfo.
        :type is_flexus: bool
        """
        self._is_flexus = is_flexus

    @property
    def is_only_human_model(self):
        r"""Gets the is_only_human_model of this TrainingJobBasicInfo.

        是否只训练形象模型，不训练声音模型。仅Flexus版本时有效，默认false。

        :return: The is_only_human_model of this TrainingJobBasicInfo.
        :rtype: bool
        """
        return self._is_only_human_model

    @is_only_human_model.setter
    def is_only_human_model(self, is_only_human_model):
        r"""Sets the is_only_human_model of this TrainingJobBasicInfo.

        是否只训练形象模型，不训练声音模型。仅Flexus版本时有效，默认false。

        :param is_only_human_model: The is_only_human_model of this TrainingJobBasicInfo.
        :type is_only_human_model: bool
        """
        self._is_only_human_model = is_only_human_model

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
        if not isinstance(other, TrainingJobBasicInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
