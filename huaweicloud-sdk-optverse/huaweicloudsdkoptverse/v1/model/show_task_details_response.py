# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTaskDetailsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'description': 'str',
        'user_id': 'str',
        'user_name': 'str',
        'output_path': 'str',
        'algorithm_id': 'str',
        'algorithm_file': 'str',
        'algorithm_func_name': 'str',
        'task_progress': 'float',
        'status': 'str',
        'evaluator_file': 'str',
        'evaluator_func_name': 'str',
        'evaluator_baseline': 'str',
        'evaluator_baseline_func_name': 'str',
        'evaluator_parameter': 'EvaluatorParameter',
        'cluster_id': 'str',
        'meta_create_at': 'int',
        'meta_start_at': 'int',
        'meta_finish_at': 'int',
        'visibility': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'user_id': 'user_id',
        'user_name': 'user_name',
        'output_path': 'output_path',
        'algorithm_id': 'algorithm_id',
        'algorithm_file': 'algorithm_file',
        'algorithm_func_name': 'algorithm_func_name',
        'task_progress': 'task_progress',
        'status': 'status',
        'evaluator_file': 'evaluator_file',
        'evaluator_func_name': 'evaluator_func_name',
        'evaluator_baseline': 'evaluator_baseline',
        'evaluator_baseline_func_name': 'evaluator_baseline_func_name',
        'evaluator_parameter': 'evaluator_parameter',
        'cluster_id': 'cluster_id',
        'meta_create_at': 'meta_create_at',
        'meta_start_at': 'meta_start_at',
        'meta_finish_at': 'meta_finish_at',
        'visibility': 'visibility'
    }

    def __init__(self, id=None, name=None, description=None, user_id=None, user_name=None, output_path=None, algorithm_id=None, algorithm_file=None, algorithm_func_name=None, task_progress=None, status=None, evaluator_file=None, evaluator_func_name=None, evaluator_baseline=None, evaluator_baseline_func_name=None, evaluator_parameter=None, cluster_id=None, meta_create_at=None, meta_start_at=None, meta_finish_at=None, visibility=None):
        r"""ShowTaskDetailsResponse

        The model defined in huaweicloud sdk

        :param id: **参数解释**： 任务标识符。 **约束限制**： 不涉及 **取值范围**： 长度[1-128] **默认取值**： 不涉及 
        :type id: str
        :param name: **参数解释**： 优化任务名称。 **约束限制**： 不涉及 **取值范围**： 取值范围[1,128]。 **默认取值**： 不涉及 
        :type name: str
        :param description: 优化任务描述
        :type description: str
        :param user_id: **参数解释**： 用户标识符。 **约束限制**： 不涉及 **取值范围**： 取值范围[1,128]。 **默认取值**： 不涉及 
        :type user_id: str
        :param user_name: 用户名
        :type user_name: str
        :param output_path: **参数解释**： 优化结果存储路径。 **约束限制**： 不涉及 **取值范围**： 取值范围[1,128]。 **默认取值**： 不涉及 
        :type output_path: str
        :param algorithm_id: **参数解释**： 关联的算法设计项目。 **约束限制**： 不涉及 **取值范围**： 取值范围[1,128]。 **默认取值**： 不涉及 
        :type algorithm_id: str
        :param algorithm_file: **参数解释**： 关联的算法文件路径。 **约束限制**： 不涉及 **取值范围**： 取值范围[1,256]。 **默认取值**： 不涉及 
        :type algorithm_file: str
        :param algorithm_func_name: **参数解释**： 算法函数名。 **约束限制**： 不涉及 **取值范围**： 取值范围[1,256]。 **默认取值**： 不涉及 
        :type algorithm_func_name: str
        :param task_progress: **参数解释**： 算法进度。 **约束限制**： 不涉及 **取值范围**： 取值范围[0,1]。 **默认取值**： 不涉及 
        :type task_progress: float
        :param status: **参数解释**： 算法状态。 **约束限制**： 不涉及 **取值范围**： * DRAFT: 草稿 * PENDING: 初始化 * RUNNING: 运行中 * STOPPED: 已停止 * FINISHED: 已完成 * FAILED: 异常失败 **默认取值**： 不涉及 
        :type status: str
        :param evaluator_file: **参数解释**： 评估器文件路径。 **约束限制**： 不涉及 **取值范围**： 取值范围[1,65536]。 **默认取值**： 不涉及 
        :type evaluator_file: str
        :param evaluator_func_name: **参数解释**： 评估器算法函数名。 **约束限制**： 不涉及 **取值范围**： 取值范围[1,256]。 **默认取值**： 不涉及 
        :type evaluator_func_name: str
        :param evaluator_baseline: **参数解释**： 评估基线文件路径。 **约束限制**： 不涉及 **取值范围**： 取值范围[1,65536]。 **默认取值**： 不涉及 
        :type evaluator_baseline: str
        :param evaluator_baseline_func_name: **参数解释**： 评估基线算法函数名。 **约束限制**： 不涉及 **取值范围**： 取值范围[1,256]。 **默认取值**： 不涉及 
        :type evaluator_baseline_func_name: str
        :param evaluator_parameter: 
        :type evaluator_parameter: :class:`huaweicloudsdkoptverse.v1.EvaluatorParameter`
        :param cluster_id: **参数解释**： 关联CCE集群ID。 **约束限制**： 不涉及 **取值范围**： 取值范围[1,128]。 **默认取值**： 不涉及 
        :type cluster_id: str
        :param meta_create_at: **参数解释**： 演化任务创建时间,单位毫秒。 **约束限制**： 不涉及 **取值范围**： 取值范围[0,9999999999999]。 **默认取值**： 不涉及 
        :type meta_create_at: int
        :param meta_start_at: **参数解释**： 演化任务启动时间,单位毫秒。 **约束限制**： 不涉及 **取值范围**： 取值范围[0,9999999999999]。 **默认取值**： 不涉及 
        :type meta_start_at: int
        :param meta_finish_at: **参数解释**： 演化任务完成时间,单位毫秒。 **约束限制**： 不涉及 **取值范围**： 取值范围[0,9999999999999]。 **默认取值**： 不涉及 
        :type meta_finish_at: int
        :param visibility: **参数解释**： 项目可见性。 **约束限制**： 不涉及 **取值范围**： * 公共: PUBLIC * 私有: PRIVATE **默认取值**： 不涉及 
        :type visibility: str
        """
        
        super().__init__()

        self._id = None
        self._name = None
        self._description = None
        self._user_id = None
        self._user_name = None
        self._output_path = None
        self._algorithm_id = None
        self._algorithm_file = None
        self._algorithm_func_name = None
        self._task_progress = None
        self._status = None
        self._evaluator_file = None
        self._evaluator_func_name = None
        self._evaluator_baseline = None
        self._evaluator_baseline_func_name = None
        self._evaluator_parameter = None
        self._cluster_id = None
        self._meta_create_at = None
        self._meta_start_at = None
        self._meta_finish_at = None
        self._visibility = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if user_id is not None:
            self.user_id = user_id
        if user_name is not None:
            self.user_name = user_name
        if output_path is not None:
            self.output_path = output_path
        if algorithm_id is not None:
            self.algorithm_id = algorithm_id
        if algorithm_file is not None:
            self.algorithm_file = algorithm_file
        if algorithm_func_name is not None:
            self.algorithm_func_name = algorithm_func_name
        if task_progress is not None:
            self.task_progress = task_progress
        if status is not None:
            self.status = status
        if evaluator_file is not None:
            self.evaluator_file = evaluator_file
        if evaluator_func_name is not None:
            self.evaluator_func_name = evaluator_func_name
        if evaluator_baseline is not None:
            self.evaluator_baseline = evaluator_baseline
        if evaluator_baseline_func_name is not None:
            self.evaluator_baseline_func_name = evaluator_baseline_func_name
        if evaluator_parameter is not None:
            self.evaluator_parameter = evaluator_parameter
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if meta_create_at is not None:
            self.meta_create_at = meta_create_at
        if meta_start_at is not None:
            self.meta_start_at = meta_start_at
        if meta_finish_at is not None:
            self.meta_finish_at = meta_finish_at
        if visibility is not None:
            self.visibility = visibility

    @property
    def id(self):
        r"""Gets the id of this ShowTaskDetailsResponse.

        **参数解释**： 任务标识符。 **约束限制**： 不涉及 **取值范围**： 长度[1-128] **默认取值**： 不涉及 

        :return: The id of this ShowTaskDetailsResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowTaskDetailsResponse.

        **参数解释**： 任务标识符。 **约束限制**： 不涉及 **取值范围**： 长度[1-128] **默认取值**： 不涉及 

        :param id: The id of this ShowTaskDetailsResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ShowTaskDetailsResponse.

        **参数解释**： 优化任务名称。 **约束限制**： 不涉及 **取值范围**： 取值范围[1,128]。 **默认取值**： 不涉及 

        :return: The name of this ShowTaskDetailsResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowTaskDetailsResponse.

        **参数解释**： 优化任务名称。 **约束限制**： 不涉及 **取值范围**： 取值范围[1,128]。 **默认取值**： 不涉及 

        :param name: The name of this ShowTaskDetailsResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ShowTaskDetailsResponse.

        优化任务描述

        :return: The description of this ShowTaskDetailsResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowTaskDetailsResponse.

        优化任务描述

        :param description: The description of this ShowTaskDetailsResponse.
        :type description: str
        """
        self._description = description

    @property
    def user_id(self):
        r"""Gets the user_id of this ShowTaskDetailsResponse.

        **参数解释**： 用户标识符。 **约束限制**： 不涉及 **取值范围**： 取值范围[1,128]。 **默认取值**： 不涉及 

        :return: The user_id of this ShowTaskDetailsResponse.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this ShowTaskDetailsResponse.

        **参数解释**： 用户标识符。 **约束限制**： 不涉及 **取值范围**： 取值范围[1,128]。 **默认取值**： 不涉及 

        :param user_id: The user_id of this ShowTaskDetailsResponse.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def user_name(self):
        r"""Gets the user_name of this ShowTaskDetailsResponse.

        用户名

        :return: The user_name of this ShowTaskDetailsResponse.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ShowTaskDetailsResponse.

        用户名

        :param user_name: The user_name of this ShowTaskDetailsResponse.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def output_path(self):
        r"""Gets the output_path of this ShowTaskDetailsResponse.

        **参数解释**： 优化结果存储路径。 **约束限制**： 不涉及 **取值范围**： 取值范围[1,128]。 **默认取值**： 不涉及 

        :return: The output_path of this ShowTaskDetailsResponse.
        :rtype: str
        """
        return self._output_path

    @output_path.setter
    def output_path(self, output_path):
        r"""Sets the output_path of this ShowTaskDetailsResponse.

        **参数解释**： 优化结果存储路径。 **约束限制**： 不涉及 **取值范围**： 取值范围[1,128]。 **默认取值**： 不涉及 

        :param output_path: The output_path of this ShowTaskDetailsResponse.
        :type output_path: str
        """
        self._output_path = output_path

    @property
    def algorithm_id(self):
        r"""Gets the algorithm_id of this ShowTaskDetailsResponse.

        **参数解释**： 关联的算法设计项目。 **约束限制**： 不涉及 **取值范围**： 取值范围[1,128]。 **默认取值**： 不涉及 

        :return: The algorithm_id of this ShowTaskDetailsResponse.
        :rtype: str
        """
        return self._algorithm_id

    @algorithm_id.setter
    def algorithm_id(self, algorithm_id):
        r"""Sets the algorithm_id of this ShowTaskDetailsResponse.

        **参数解释**： 关联的算法设计项目。 **约束限制**： 不涉及 **取值范围**： 取值范围[1,128]。 **默认取值**： 不涉及 

        :param algorithm_id: The algorithm_id of this ShowTaskDetailsResponse.
        :type algorithm_id: str
        """
        self._algorithm_id = algorithm_id

    @property
    def algorithm_file(self):
        r"""Gets the algorithm_file of this ShowTaskDetailsResponse.

        **参数解释**： 关联的算法文件路径。 **约束限制**： 不涉及 **取值范围**： 取值范围[1,256]。 **默认取值**： 不涉及 

        :return: The algorithm_file of this ShowTaskDetailsResponse.
        :rtype: str
        """
        return self._algorithm_file

    @algorithm_file.setter
    def algorithm_file(self, algorithm_file):
        r"""Sets the algorithm_file of this ShowTaskDetailsResponse.

        **参数解释**： 关联的算法文件路径。 **约束限制**： 不涉及 **取值范围**： 取值范围[1,256]。 **默认取值**： 不涉及 

        :param algorithm_file: The algorithm_file of this ShowTaskDetailsResponse.
        :type algorithm_file: str
        """
        self._algorithm_file = algorithm_file

    @property
    def algorithm_func_name(self):
        r"""Gets the algorithm_func_name of this ShowTaskDetailsResponse.

        **参数解释**： 算法函数名。 **约束限制**： 不涉及 **取值范围**： 取值范围[1,256]。 **默认取值**： 不涉及 

        :return: The algorithm_func_name of this ShowTaskDetailsResponse.
        :rtype: str
        """
        return self._algorithm_func_name

    @algorithm_func_name.setter
    def algorithm_func_name(self, algorithm_func_name):
        r"""Sets the algorithm_func_name of this ShowTaskDetailsResponse.

        **参数解释**： 算法函数名。 **约束限制**： 不涉及 **取值范围**： 取值范围[1,256]。 **默认取值**： 不涉及 

        :param algorithm_func_name: The algorithm_func_name of this ShowTaskDetailsResponse.
        :type algorithm_func_name: str
        """
        self._algorithm_func_name = algorithm_func_name

    @property
    def task_progress(self):
        r"""Gets the task_progress of this ShowTaskDetailsResponse.

        **参数解释**： 算法进度。 **约束限制**： 不涉及 **取值范围**： 取值范围[0,1]。 **默认取值**： 不涉及 

        :return: The task_progress of this ShowTaskDetailsResponse.
        :rtype: float
        """
        return self._task_progress

    @task_progress.setter
    def task_progress(self, task_progress):
        r"""Sets the task_progress of this ShowTaskDetailsResponse.

        **参数解释**： 算法进度。 **约束限制**： 不涉及 **取值范围**： 取值范围[0,1]。 **默认取值**： 不涉及 

        :param task_progress: The task_progress of this ShowTaskDetailsResponse.
        :type task_progress: float
        """
        self._task_progress = task_progress

    @property
    def status(self):
        r"""Gets the status of this ShowTaskDetailsResponse.

        **参数解释**： 算法状态。 **约束限制**： 不涉及 **取值范围**： * DRAFT: 草稿 * PENDING: 初始化 * RUNNING: 运行中 * STOPPED: 已停止 * FINISHED: 已完成 * FAILED: 异常失败 **默认取值**： 不涉及 

        :return: The status of this ShowTaskDetailsResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowTaskDetailsResponse.

        **参数解释**： 算法状态。 **约束限制**： 不涉及 **取值范围**： * DRAFT: 草稿 * PENDING: 初始化 * RUNNING: 运行中 * STOPPED: 已停止 * FINISHED: 已完成 * FAILED: 异常失败 **默认取值**： 不涉及 

        :param status: The status of this ShowTaskDetailsResponse.
        :type status: str
        """
        self._status = status

    @property
    def evaluator_file(self):
        r"""Gets the evaluator_file of this ShowTaskDetailsResponse.

        **参数解释**： 评估器文件路径。 **约束限制**： 不涉及 **取值范围**： 取值范围[1,65536]。 **默认取值**： 不涉及 

        :return: The evaluator_file of this ShowTaskDetailsResponse.
        :rtype: str
        """
        return self._evaluator_file

    @evaluator_file.setter
    def evaluator_file(self, evaluator_file):
        r"""Sets the evaluator_file of this ShowTaskDetailsResponse.

        **参数解释**： 评估器文件路径。 **约束限制**： 不涉及 **取值范围**： 取值范围[1,65536]。 **默认取值**： 不涉及 

        :param evaluator_file: The evaluator_file of this ShowTaskDetailsResponse.
        :type evaluator_file: str
        """
        self._evaluator_file = evaluator_file

    @property
    def evaluator_func_name(self):
        r"""Gets the evaluator_func_name of this ShowTaskDetailsResponse.

        **参数解释**： 评估器算法函数名。 **约束限制**： 不涉及 **取值范围**： 取值范围[1,256]。 **默认取值**： 不涉及 

        :return: The evaluator_func_name of this ShowTaskDetailsResponse.
        :rtype: str
        """
        return self._evaluator_func_name

    @evaluator_func_name.setter
    def evaluator_func_name(self, evaluator_func_name):
        r"""Sets the evaluator_func_name of this ShowTaskDetailsResponse.

        **参数解释**： 评估器算法函数名。 **约束限制**： 不涉及 **取值范围**： 取值范围[1,256]。 **默认取值**： 不涉及 

        :param evaluator_func_name: The evaluator_func_name of this ShowTaskDetailsResponse.
        :type evaluator_func_name: str
        """
        self._evaluator_func_name = evaluator_func_name

    @property
    def evaluator_baseline(self):
        r"""Gets the evaluator_baseline of this ShowTaskDetailsResponse.

        **参数解释**： 评估基线文件路径。 **约束限制**： 不涉及 **取值范围**： 取值范围[1,65536]。 **默认取值**： 不涉及 

        :return: The evaluator_baseline of this ShowTaskDetailsResponse.
        :rtype: str
        """
        return self._evaluator_baseline

    @evaluator_baseline.setter
    def evaluator_baseline(self, evaluator_baseline):
        r"""Sets the evaluator_baseline of this ShowTaskDetailsResponse.

        **参数解释**： 评估基线文件路径。 **约束限制**： 不涉及 **取值范围**： 取值范围[1,65536]。 **默认取值**： 不涉及 

        :param evaluator_baseline: The evaluator_baseline of this ShowTaskDetailsResponse.
        :type evaluator_baseline: str
        """
        self._evaluator_baseline = evaluator_baseline

    @property
    def evaluator_baseline_func_name(self):
        r"""Gets the evaluator_baseline_func_name of this ShowTaskDetailsResponse.

        **参数解释**： 评估基线算法函数名。 **约束限制**： 不涉及 **取值范围**： 取值范围[1,256]。 **默认取值**： 不涉及 

        :return: The evaluator_baseline_func_name of this ShowTaskDetailsResponse.
        :rtype: str
        """
        return self._evaluator_baseline_func_name

    @evaluator_baseline_func_name.setter
    def evaluator_baseline_func_name(self, evaluator_baseline_func_name):
        r"""Sets the evaluator_baseline_func_name of this ShowTaskDetailsResponse.

        **参数解释**： 评估基线算法函数名。 **约束限制**： 不涉及 **取值范围**： 取值范围[1,256]。 **默认取值**： 不涉及 

        :param evaluator_baseline_func_name: The evaluator_baseline_func_name of this ShowTaskDetailsResponse.
        :type evaluator_baseline_func_name: str
        """
        self._evaluator_baseline_func_name = evaluator_baseline_func_name

    @property
    def evaluator_parameter(self):
        r"""Gets the evaluator_parameter of this ShowTaskDetailsResponse.

        :return: The evaluator_parameter of this ShowTaskDetailsResponse.
        :rtype: :class:`huaweicloudsdkoptverse.v1.EvaluatorParameter`
        """
        return self._evaluator_parameter

    @evaluator_parameter.setter
    def evaluator_parameter(self, evaluator_parameter):
        r"""Sets the evaluator_parameter of this ShowTaskDetailsResponse.

        :param evaluator_parameter: The evaluator_parameter of this ShowTaskDetailsResponse.
        :type evaluator_parameter: :class:`huaweicloudsdkoptverse.v1.EvaluatorParameter`
        """
        self._evaluator_parameter = evaluator_parameter

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ShowTaskDetailsResponse.

        **参数解释**： 关联CCE集群ID。 **约束限制**： 不涉及 **取值范围**： 取值范围[1,128]。 **默认取值**： 不涉及 

        :return: The cluster_id of this ShowTaskDetailsResponse.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ShowTaskDetailsResponse.

        **参数解释**： 关联CCE集群ID。 **约束限制**： 不涉及 **取值范围**： 取值范围[1,128]。 **默认取值**： 不涉及 

        :param cluster_id: The cluster_id of this ShowTaskDetailsResponse.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def meta_create_at(self):
        r"""Gets the meta_create_at of this ShowTaskDetailsResponse.

        **参数解释**： 演化任务创建时间,单位毫秒。 **约束限制**： 不涉及 **取值范围**： 取值范围[0,9999999999999]。 **默认取值**： 不涉及 

        :return: The meta_create_at of this ShowTaskDetailsResponse.
        :rtype: int
        """
        return self._meta_create_at

    @meta_create_at.setter
    def meta_create_at(self, meta_create_at):
        r"""Sets the meta_create_at of this ShowTaskDetailsResponse.

        **参数解释**： 演化任务创建时间,单位毫秒。 **约束限制**： 不涉及 **取值范围**： 取值范围[0,9999999999999]。 **默认取值**： 不涉及 

        :param meta_create_at: The meta_create_at of this ShowTaskDetailsResponse.
        :type meta_create_at: int
        """
        self._meta_create_at = meta_create_at

    @property
    def meta_start_at(self):
        r"""Gets the meta_start_at of this ShowTaskDetailsResponse.

        **参数解释**： 演化任务启动时间,单位毫秒。 **约束限制**： 不涉及 **取值范围**： 取值范围[0,9999999999999]。 **默认取值**： 不涉及 

        :return: The meta_start_at of this ShowTaskDetailsResponse.
        :rtype: int
        """
        return self._meta_start_at

    @meta_start_at.setter
    def meta_start_at(self, meta_start_at):
        r"""Sets the meta_start_at of this ShowTaskDetailsResponse.

        **参数解释**： 演化任务启动时间,单位毫秒。 **约束限制**： 不涉及 **取值范围**： 取值范围[0,9999999999999]。 **默认取值**： 不涉及 

        :param meta_start_at: The meta_start_at of this ShowTaskDetailsResponse.
        :type meta_start_at: int
        """
        self._meta_start_at = meta_start_at

    @property
    def meta_finish_at(self):
        r"""Gets the meta_finish_at of this ShowTaskDetailsResponse.

        **参数解释**： 演化任务完成时间,单位毫秒。 **约束限制**： 不涉及 **取值范围**： 取值范围[0,9999999999999]。 **默认取值**： 不涉及 

        :return: The meta_finish_at of this ShowTaskDetailsResponse.
        :rtype: int
        """
        return self._meta_finish_at

    @meta_finish_at.setter
    def meta_finish_at(self, meta_finish_at):
        r"""Sets the meta_finish_at of this ShowTaskDetailsResponse.

        **参数解释**： 演化任务完成时间,单位毫秒。 **约束限制**： 不涉及 **取值范围**： 取值范围[0,9999999999999]。 **默认取值**： 不涉及 

        :param meta_finish_at: The meta_finish_at of this ShowTaskDetailsResponse.
        :type meta_finish_at: int
        """
        self._meta_finish_at = meta_finish_at

    @property
    def visibility(self):
        r"""Gets the visibility of this ShowTaskDetailsResponse.

        **参数解释**： 项目可见性。 **约束限制**： 不涉及 **取值范围**： * 公共: PUBLIC * 私有: PRIVATE **默认取值**： 不涉及 

        :return: The visibility of this ShowTaskDetailsResponse.
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        r"""Sets the visibility of this ShowTaskDetailsResponse.

        **参数解释**： 项目可见性。 **约束限制**： 不涉及 **取值范围**： * 公共: PUBLIC * 私有: PRIVATE **默认取值**： 不涉及 

        :param visibility: The visibility of this ShowTaskDetailsResponse.
        :type visibility: str
        """
        self._visibility = visibility

    def to_dict(self):
        import warnings
        warnings.warn("ShowTaskDetailsResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowTaskDetailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
