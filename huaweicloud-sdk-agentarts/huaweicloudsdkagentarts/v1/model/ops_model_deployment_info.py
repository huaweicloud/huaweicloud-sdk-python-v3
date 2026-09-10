# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsModelDeploymentInfo:

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
        'task_id': 'str',
        'product_id': 'str',
        'task_name': 'str',
        'agent': 'OpsTuningTargetAgent',
        'model_name': 'str',
        'ma_service_id': 'str',
        'model_provider_id': 'str',
        'model_service_id': 'str',
        'model_service_name': 'str',
        'api_url': 'str',
        'status': 'str',
        'created_at': 'int',
        'fail_reason': 'str'
    }

    attribute_map = {
        'id': 'id',
        'task_id': 'task_id',
        'product_id': 'product_id',
        'task_name': 'task_name',
        'agent': 'agent',
        'model_name': 'model_name',
        'ma_service_id': 'ma_service_id',
        'model_provider_id': 'model_provider_id',
        'model_service_id': 'model_service_id',
        'model_service_name': 'model_service_name',
        'api_url': 'api_url',
        'status': 'status',
        'created_at': 'created_at',
        'fail_reason': 'fail_reason'
    }

    def __init__(self, id=None, task_id=None, product_id=None, task_name=None, agent=None, model_name=None, ma_service_id=None, model_provider_id=None, model_service_id=None, model_service_name=None, api_url=None, status=None, created_at=None, fail_reason=None):
        r"""OpsModelDeploymentInfo

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 部署任务ID，标识部署任务的唯一标识符。  **取值范围：** UUID格式字符串。
        :type id: str
        :param task_id: **参数解释：** 关联的模型优化任务ID。  **取值范围：** 任务ID字符串。
        :type task_id: str
        :param product_id: **参数解释：** 模型优化任务产物ID。  **取值范围：** 产物ID字符串。
        :type product_id: str
        :param task_name: **参数解释：** 模型优化任务名称。  **取值范围：** 任务名称字符串。
        :type task_name: str
        :param agent: 
        :type agent: :class:`huaweicloudsdkagentarts.v1.OpsTuningTargetAgent`
        :param model_name: **参数解释：** 被调优的模型名称。  **取值范围：** 模型名称字符串。
        :type model_name: str
        :param ma_service_id: **参数解释：** ModelArts服务ID，关联底层ModelArts平台的服务实例。  **取值范围：** ModelArts侧的服务ID字符串。
        :type ma_service_id: str
        :param model_provider_id: **参数解释：** 模型提供商ID，标识模型来源的服务商。  **取值范围：** 提供商标识字符串。
        :type model_provider_id: str
        :param model_service_id: **参数解释：** 模型服务ID，本平台生成的服务唯一标识。  **取值范围：** 模型服务唯一标识字符串。
        :type model_service_id: str
        :param model_service_name: **参数解释：** 模型服务名称。  **取值范围：** 模型服务显示名称
        :type model_service_name: str
        :param api_url: **参数解释：** 部署服务API地址。  **取值范围：** 合法的URL字符串。
        :type api_url: str
        :param status: **参数解释：** 部署服务状态。  **取值范围：** deploying：部署中，running：运行中，stopping：停止中，stopped：已停止，starting：启动中，fail：部署失败，deleting：删除中，access_fail：接入失败。
        :type status: str
        :param created_at: **参数解释：** 创建时间，单位：毫秒（13位时间戳）。  **取值范围：** 13位毫秒级时间戳。
        :type created_at: int
        :param fail_reason: **参数解释：** 部署错误信息。  **取值范围：** 无。
        :type fail_reason: str
        """
        
        

        self._id = None
        self._task_id = None
        self._product_id = None
        self._task_name = None
        self._agent = None
        self._model_name = None
        self._ma_service_id = None
        self._model_provider_id = None
        self._model_service_id = None
        self._model_service_name = None
        self._api_url = None
        self._status = None
        self._created_at = None
        self._fail_reason = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if task_id is not None:
            self.task_id = task_id
        if product_id is not None:
            self.product_id = product_id
        if task_name is not None:
            self.task_name = task_name
        if agent is not None:
            self.agent = agent
        if model_name is not None:
            self.model_name = model_name
        if ma_service_id is not None:
            self.ma_service_id = ma_service_id
        if model_provider_id is not None:
            self.model_provider_id = model_provider_id
        if model_service_id is not None:
            self.model_service_id = model_service_id
        if model_service_name is not None:
            self.model_service_name = model_service_name
        if api_url is not None:
            self.api_url = api_url
        if status is not None:
            self.status = status
        if created_at is not None:
            self.created_at = created_at
        if fail_reason is not None:
            self.fail_reason = fail_reason

    @property
    def id(self):
        r"""Gets the id of this OpsModelDeploymentInfo.

        **参数解释：** 部署任务ID，标识部署任务的唯一标识符。  **取值范围：** UUID格式字符串。

        :return: The id of this OpsModelDeploymentInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this OpsModelDeploymentInfo.

        **参数解释：** 部署任务ID，标识部署任务的唯一标识符。  **取值范围：** UUID格式字符串。

        :param id: The id of this OpsModelDeploymentInfo.
        :type id: str
        """
        self._id = id

    @property
    def task_id(self):
        r"""Gets the task_id of this OpsModelDeploymentInfo.

        **参数解释：** 关联的模型优化任务ID。  **取值范围：** 任务ID字符串。

        :return: The task_id of this OpsModelDeploymentInfo.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this OpsModelDeploymentInfo.

        **参数解释：** 关联的模型优化任务ID。  **取值范围：** 任务ID字符串。

        :param task_id: The task_id of this OpsModelDeploymentInfo.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def product_id(self):
        r"""Gets the product_id of this OpsModelDeploymentInfo.

        **参数解释：** 模型优化任务产物ID。  **取值范围：** 产物ID字符串。

        :return: The product_id of this OpsModelDeploymentInfo.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this OpsModelDeploymentInfo.

        **参数解释：** 模型优化任务产物ID。  **取值范围：** 产物ID字符串。

        :param product_id: The product_id of this OpsModelDeploymentInfo.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def task_name(self):
        r"""Gets the task_name of this OpsModelDeploymentInfo.

        **参数解释：** 模型优化任务名称。  **取值范围：** 任务名称字符串。

        :return: The task_name of this OpsModelDeploymentInfo.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        r"""Sets the task_name of this OpsModelDeploymentInfo.

        **参数解释：** 模型优化任务名称。  **取值范围：** 任务名称字符串。

        :param task_name: The task_name of this OpsModelDeploymentInfo.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def agent(self):
        r"""Gets the agent of this OpsModelDeploymentInfo.

        :return: The agent of this OpsModelDeploymentInfo.
        :rtype: :class:`huaweicloudsdkagentarts.v1.OpsTuningTargetAgent`
        """
        return self._agent

    @agent.setter
    def agent(self, agent):
        r"""Sets the agent of this OpsModelDeploymentInfo.

        :param agent: The agent of this OpsModelDeploymentInfo.
        :type agent: :class:`huaweicloudsdkagentarts.v1.OpsTuningTargetAgent`
        """
        self._agent = agent

    @property
    def model_name(self):
        r"""Gets the model_name of this OpsModelDeploymentInfo.

        **参数解释：** 被调优的模型名称。  **取值范围：** 模型名称字符串。

        :return: The model_name of this OpsModelDeploymentInfo.
        :rtype: str
        """
        return self._model_name

    @model_name.setter
    def model_name(self, model_name):
        r"""Sets the model_name of this OpsModelDeploymentInfo.

        **参数解释：** 被调优的模型名称。  **取值范围：** 模型名称字符串。

        :param model_name: The model_name of this OpsModelDeploymentInfo.
        :type model_name: str
        """
        self._model_name = model_name

    @property
    def ma_service_id(self):
        r"""Gets the ma_service_id of this OpsModelDeploymentInfo.

        **参数解释：** ModelArts服务ID，关联底层ModelArts平台的服务实例。  **取值范围：** ModelArts侧的服务ID字符串。

        :return: The ma_service_id of this OpsModelDeploymentInfo.
        :rtype: str
        """
        return self._ma_service_id

    @ma_service_id.setter
    def ma_service_id(self, ma_service_id):
        r"""Sets the ma_service_id of this OpsModelDeploymentInfo.

        **参数解释：** ModelArts服务ID，关联底层ModelArts平台的服务实例。  **取值范围：** ModelArts侧的服务ID字符串。

        :param ma_service_id: The ma_service_id of this OpsModelDeploymentInfo.
        :type ma_service_id: str
        """
        self._ma_service_id = ma_service_id

    @property
    def model_provider_id(self):
        r"""Gets the model_provider_id of this OpsModelDeploymentInfo.

        **参数解释：** 模型提供商ID，标识模型来源的服务商。  **取值范围：** 提供商标识字符串。

        :return: The model_provider_id of this OpsModelDeploymentInfo.
        :rtype: str
        """
        return self._model_provider_id

    @model_provider_id.setter
    def model_provider_id(self, model_provider_id):
        r"""Sets the model_provider_id of this OpsModelDeploymentInfo.

        **参数解释：** 模型提供商ID，标识模型来源的服务商。  **取值范围：** 提供商标识字符串。

        :param model_provider_id: The model_provider_id of this OpsModelDeploymentInfo.
        :type model_provider_id: str
        """
        self._model_provider_id = model_provider_id

    @property
    def model_service_id(self):
        r"""Gets the model_service_id of this OpsModelDeploymentInfo.

        **参数解释：** 模型服务ID，本平台生成的服务唯一标识。  **取值范围：** 模型服务唯一标识字符串。

        :return: The model_service_id of this OpsModelDeploymentInfo.
        :rtype: str
        """
        return self._model_service_id

    @model_service_id.setter
    def model_service_id(self, model_service_id):
        r"""Sets the model_service_id of this OpsModelDeploymentInfo.

        **参数解释：** 模型服务ID，本平台生成的服务唯一标识。  **取值范围：** 模型服务唯一标识字符串。

        :param model_service_id: The model_service_id of this OpsModelDeploymentInfo.
        :type model_service_id: str
        """
        self._model_service_id = model_service_id

    @property
    def model_service_name(self):
        r"""Gets the model_service_name of this OpsModelDeploymentInfo.

        **参数解释：** 模型服务名称。  **取值范围：** 模型服务显示名称

        :return: The model_service_name of this OpsModelDeploymentInfo.
        :rtype: str
        """
        return self._model_service_name

    @model_service_name.setter
    def model_service_name(self, model_service_name):
        r"""Sets the model_service_name of this OpsModelDeploymentInfo.

        **参数解释：** 模型服务名称。  **取值范围：** 模型服务显示名称

        :param model_service_name: The model_service_name of this OpsModelDeploymentInfo.
        :type model_service_name: str
        """
        self._model_service_name = model_service_name

    @property
    def api_url(self):
        r"""Gets the api_url of this OpsModelDeploymentInfo.

        **参数解释：** 部署服务API地址。  **取值范围：** 合法的URL字符串。

        :return: The api_url of this OpsModelDeploymentInfo.
        :rtype: str
        """
        return self._api_url

    @api_url.setter
    def api_url(self, api_url):
        r"""Sets the api_url of this OpsModelDeploymentInfo.

        **参数解释：** 部署服务API地址。  **取值范围：** 合法的URL字符串。

        :param api_url: The api_url of this OpsModelDeploymentInfo.
        :type api_url: str
        """
        self._api_url = api_url

    @property
    def status(self):
        r"""Gets the status of this OpsModelDeploymentInfo.

        **参数解释：** 部署服务状态。  **取值范围：** deploying：部署中，running：运行中，stopping：停止中，stopped：已停止，starting：启动中，fail：部署失败，deleting：删除中，access_fail：接入失败。

        :return: The status of this OpsModelDeploymentInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this OpsModelDeploymentInfo.

        **参数解释：** 部署服务状态。  **取值范围：** deploying：部署中，running：运行中，stopping：停止中，stopped：已停止，starting：启动中，fail：部署失败，deleting：删除中，access_fail：接入失败。

        :param status: The status of this OpsModelDeploymentInfo.
        :type status: str
        """
        self._status = status

    @property
    def created_at(self):
        r"""Gets the created_at of this OpsModelDeploymentInfo.

        **参数解释：** 创建时间，单位：毫秒（13位时间戳）。  **取值范围：** 13位毫秒级时间戳。

        :return: The created_at of this OpsModelDeploymentInfo.
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this OpsModelDeploymentInfo.

        **参数解释：** 创建时间，单位：毫秒（13位时间戳）。  **取值范围：** 13位毫秒级时间戳。

        :param created_at: The created_at of this OpsModelDeploymentInfo.
        :type created_at: int
        """
        self._created_at = created_at

    @property
    def fail_reason(self):
        r"""Gets the fail_reason of this OpsModelDeploymentInfo.

        **参数解释：** 部署错误信息。  **取值范围：** 无。

        :return: The fail_reason of this OpsModelDeploymentInfo.
        :rtype: str
        """
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, fail_reason):
        r"""Sets the fail_reason of this OpsModelDeploymentInfo.

        **参数解释：** 部署错误信息。  **取值范围：** 无。

        :param fail_reason: The fail_reason of this OpsModelDeploymentInfo.
        :type fail_reason: str
        """
        self._fail_reason = fail_reason

    def to_dict(self):
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
        if not isinstance(other, OpsModelDeploymentInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
