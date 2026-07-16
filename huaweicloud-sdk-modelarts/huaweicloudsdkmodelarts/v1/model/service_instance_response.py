# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServiceInstanceResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_name': 'str',
        'status': 'str',
        'weight': 'int',
        'pod_count': 'int',
        'running_pod_count': 'int',
        'update_at': 'int'
    }

    attribute_map = {
        'instance_name': 'instance_name',
        'status': 'status',
        'weight': 'weight',
        'pod_count': 'pod_count',
        'running_pod_count': 'running_pod_count',
        'update_at': 'update_at'
    }

    def __init__(self, instance_name=None, status=None, weight=None, pod_count=None, running_pod_count=None, update_at=None):
        r"""ServiceInstanceResponse

        The model defined in huaweicloud sdk

        :param instance_name: **参数解释：** 服务实例名字。 **取值范围：** 不涉及。
        :type instance_name: str
        :param status: **参数解释：** 服务实例状态。 **取值范围：** - RUNNING：运行中 - PENDING：未就绪 - CONCERNING：告警 - FAILED：失败 - UNKNOWN：未知 - DELETED：已删除
        :type status: str
        :param weight: **参数解释：** 服务实例权重。 **取值范围：** [0, 100] 或者为空。
        :type weight: int
        :param pod_count: **参数解释：** 服务实例pod数量。 **取值范围：** 不涉及。
        :type pod_count: int
        :param running_pod_count: **参数解释：** 服务实例运行中pod数量。 **取值范围：** 不涉及。
        :type running_pod_count: int
        :param update_at: **参数解释：** 服务实例最近更新时间。 **取值范围：** 不涉及。
        :type update_at: int
        """
        
        

        self._instance_name = None
        self._status = None
        self._weight = None
        self._pod_count = None
        self._running_pod_count = None
        self._update_at = None
        self.discriminator = None

        if instance_name is not None:
            self.instance_name = instance_name
        if status is not None:
            self.status = status
        if weight is not None:
            self.weight = weight
        if pod_count is not None:
            self.pod_count = pod_count
        if running_pod_count is not None:
            self.running_pod_count = running_pod_count
        if update_at is not None:
            self.update_at = update_at

    @property
    def instance_name(self):
        r"""Gets the instance_name of this ServiceInstanceResponse.

        **参数解释：** 服务实例名字。 **取值范围：** 不涉及。

        :return: The instance_name of this ServiceInstanceResponse.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this ServiceInstanceResponse.

        **参数解释：** 服务实例名字。 **取值范围：** 不涉及。

        :param instance_name: The instance_name of this ServiceInstanceResponse.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def status(self):
        r"""Gets the status of this ServiceInstanceResponse.

        **参数解释：** 服务实例状态。 **取值范围：** - RUNNING：运行中 - PENDING：未就绪 - CONCERNING：告警 - FAILED：失败 - UNKNOWN：未知 - DELETED：已删除

        :return: The status of this ServiceInstanceResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ServiceInstanceResponse.

        **参数解释：** 服务实例状态。 **取值范围：** - RUNNING：运行中 - PENDING：未就绪 - CONCERNING：告警 - FAILED：失败 - UNKNOWN：未知 - DELETED：已删除

        :param status: The status of this ServiceInstanceResponse.
        :type status: str
        """
        self._status = status

    @property
    def weight(self):
        r"""Gets the weight of this ServiceInstanceResponse.

        **参数解释：** 服务实例权重。 **取值范围：** [0, 100] 或者为空。

        :return: The weight of this ServiceInstanceResponse.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        r"""Sets the weight of this ServiceInstanceResponse.

        **参数解释：** 服务实例权重。 **取值范围：** [0, 100] 或者为空。

        :param weight: The weight of this ServiceInstanceResponse.
        :type weight: int
        """
        self._weight = weight

    @property
    def pod_count(self):
        r"""Gets the pod_count of this ServiceInstanceResponse.

        **参数解释：** 服务实例pod数量。 **取值范围：** 不涉及。

        :return: The pod_count of this ServiceInstanceResponse.
        :rtype: int
        """
        return self._pod_count

    @pod_count.setter
    def pod_count(self, pod_count):
        r"""Sets the pod_count of this ServiceInstanceResponse.

        **参数解释：** 服务实例pod数量。 **取值范围：** 不涉及。

        :param pod_count: The pod_count of this ServiceInstanceResponse.
        :type pod_count: int
        """
        self._pod_count = pod_count

    @property
    def running_pod_count(self):
        r"""Gets the running_pod_count of this ServiceInstanceResponse.

        **参数解释：** 服务实例运行中pod数量。 **取值范围：** 不涉及。

        :return: The running_pod_count of this ServiceInstanceResponse.
        :rtype: int
        """
        return self._running_pod_count

    @running_pod_count.setter
    def running_pod_count(self, running_pod_count):
        r"""Sets the running_pod_count of this ServiceInstanceResponse.

        **参数解释：** 服务实例运行中pod数量。 **取值范围：** 不涉及。

        :param running_pod_count: The running_pod_count of this ServiceInstanceResponse.
        :type running_pod_count: int
        """
        self._running_pod_count = running_pod_count

    @property
    def update_at(self):
        r"""Gets the update_at of this ServiceInstanceResponse.

        **参数解释：** 服务实例最近更新时间。 **取值范围：** 不涉及。

        :return: The update_at of this ServiceInstanceResponse.
        :rtype: int
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        r"""Sets the update_at of this ServiceInstanceResponse.

        **参数解释：** 服务实例最近更新时间。 **取值范围：** 不涉及。

        :param update_at: The update_at of this ServiceInstanceResponse.
        :type update_at: int
        """
        self._update_at = update_at

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
        if not isinstance(other, ServiceInstanceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
