# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOpsModelDeploymentsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'task_id': 'str',
        'status': 'str',
        'model_service_name': 'str',
        'model_name': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'task_id': 'task_id',
        'status': 'status',
        'model_service_name': 'model_service_name',
        'model_name': 'model_name'
    }

    def __init__(self, offset=None, limit=None, task_id=None, status=None, model_service_name=None, model_name=None):
        r"""ListOpsModelDeploymentsRequest

        The model defined in huaweicloud sdk

        :param offset: **参数解释：** 返回结果偏移量。 **约束限制：** 必须为非负整数。 **取值范围：** 0-100000。 **默认取值：** 0。 
        :type offset: int
        :param limit: **参数解释：** 限制数量。 **约束限制：** 不涉及。 **取值范围：** 正整数，最大值100。 **默认取值：** 100。
        :type limit: int
        :param task_id: **参数解释：** 模型优化任务ID，标识任务的唯一标识符。获取方法请参考查询模型优化任务列表。  **约束限制：** 不涉及  **取值范围：** 真实存在的模型优化任务ID字符串。  **默认取值：** 无
        :type task_id: str
        :param status: **参数解释：** 部署状态，用于根据状态筛选任务。  **约束限制：** 不涉及  **取值范围：** deploying：部署中，running：运行中，stopping：停止中，stopped：已停止，starting：启动中，fail：部署失败，deleting：删除中，access_fail：接入失败。  **默认取值：** 无
        :type status: str
        :param model_service_name: **参数解释：** 模型服务名称。  **约束限制：** 选填参数，支持模糊匹配。  **取值范围：** 模型服务名称字符串。  **默认取值：** 无
        :type model_service_name: str
        :param model_name: **参数解释：** 模型名称。  **约束限制：** 选填参数，支持模糊匹配。  **取值范围：** 模型名称字符串。  **默认取值：** 无
        :type model_name: str
        """
        
        

        self._offset = None
        self._limit = None
        self._task_id = None
        self._status = None
        self._model_service_name = None
        self._model_name = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if task_id is not None:
            self.task_id = task_id
        if status is not None:
            self.status = status
        if model_service_name is not None:
            self.model_service_name = model_service_name
        if model_name is not None:
            self.model_name = model_name

    @property
    def offset(self):
        r"""Gets the offset of this ListOpsModelDeploymentsRequest.

        **参数解释：** 返回结果偏移量。 **约束限制：** 必须为非负整数。 **取值范围：** 0-100000。 **默认取值：** 0。 

        :return: The offset of this ListOpsModelDeploymentsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListOpsModelDeploymentsRequest.

        **参数解释：** 返回结果偏移量。 **约束限制：** 必须为非负整数。 **取值范围：** 0-100000。 **默认取值：** 0。 

        :param offset: The offset of this ListOpsModelDeploymentsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListOpsModelDeploymentsRequest.

        **参数解释：** 限制数量。 **约束限制：** 不涉及。 **取值范围：** 正整数，最大值100。 **默认取值：** 100。

        :return: The limit of this ListOpsModelDeploymentsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListOpsModelDeploymentsRequest.

        **参数解释：** 限制数量。 **约束限制：** 不涉及。 **取值范围：** 正整数，最大值100。 **默认取值：** 100。

        :param limit: The limit of this ListOpsModelDeploymentsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def task_id(self):
        r"""Gets the task_id of this ListOpsModelDeploymentsRequest.

        **参数解释：** 模型优化任务ID，标识任务的唯一标识符。获取方法请参考查询模型优化任务列表。  **约束限制：** 不涉及  **取值范围：** 真实存在的模型优化任务ID字符串。  **默认取值：** 无

        :return: The task_id of this ListOpsModelDeploymentsRequest.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ListOpsModelDeploymentsRequest.

        **参数解释：** 模型优化任务ID，标识任务的唯一标识符。获取方法请参考查询模型优化任务列表。  **约束限制：** 不涉及  **取值范围：** 真实存在的模型优化任务ID字符串。  **默认取值：** 无

        :param task_id: The task_id of this ListOpsModelDeploymentsRequest.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def status(self):
        r"""Gets the status of this ListOpsModelDeploymentsRequest.

        **参数解释：** 部署状态，用于根据状态筛选任务。  **约束限制：** 不涉及  **取值范围：** deploying：部署中，running：运行中，stopping：停止中，stopped：已停止，starting：启动中，fail：部署失败，deleting：删除中，access_fail：接入失败。  **默认取值：** 无

        :return: The status of this ListOpsModelDeploymentsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListOpsModelDeploymentsRequest.

        **参数解释：** 部署状态，用于根据状态筛选任务。  **约束限制：** 不涉及  **取值范围：** deploying：部署中，running：运行中，stopping：停止中，stopped：已停止，starting：启动中，fail：部署失败，deleting：删除中，access_fail：接入失败。  **默认取值：** 无

        :param status: The status of this ListOpsModelDeploymentsRequest.
        :type status: str
        """
        self._status = status

    @property
    def model_service_name(self):
        r"""Gets the model_service_name of this ListOpsModelDeploymentsRequest.

        **参数解释：** 模型服务名称。  **约束限制：** 选填参数，支持模糊匹配。  **取值范围：** 模型服务名称字符串。  **默认取值：** 无

        :return: The model_service_name of this ListOpsModelDeploymentsRequest.
        :rtype: str
        """
        return self._model_service_name

    @model_service_name.setter
    def model_service_name(self, model_service_name):
        r"""Sets the model_service_name of this ListOpsModelDeploymentsRequest.

        **参数解释：** 模型服务名称。  **约束限制：** 选填参数，支持模糊匹配。  **取值范围：** 模型服务名称字符串。  **默认取值：** 无

        :param model_service_name: The model_service_name of this ListOpsModelDeploymentsRequest.
        :type model_service_name: str
        """
        self._model_service_name = model_service_name

    @property
    def model_name(self):
        r"""Gets the model_name of this ListOpsModelDeploymentsRequest.

        **参数解释：** 模型名称。  **约束限制：** 选填参数，支持模糊匹配。  **取值范围：** 模型名称字符串。  **默认取值：** 无

        :return: The model_name of this ListOpsModelDeploymentsRequest.
        :rtype: str
        """
        return self._model_name

    @model_name.setter
    def model_name(self, model_name):
        r"""Sets the model_name of this ListOpsModelDeploymentsRequest.

        **参数解释：** 模型名称。  **约束限制：** 选填参数，支持模糊匹配。  **取值范围：** 模型名称字符串。  **默认取值：** 无

        :param model_name: The model_name of this ListOpsModelDeploymentsRequest.
        :type model_name: str
        """
        self._model_name = model_name

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
        if not isinstance(other, ListOpsModelDeploymentsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
