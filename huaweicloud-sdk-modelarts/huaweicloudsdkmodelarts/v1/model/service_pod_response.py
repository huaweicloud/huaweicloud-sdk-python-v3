# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServicePodResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pod_id': 'str',
        'pod_name': 'str',
        'pod_node_ip': 'str',
        'pod_node_name': 'str',
        'pod_role': 'str',
        'status': 'str',
        'update_time': 'int'
    }

    attribute_map = {
        'pod_id': 'pod_id',
        'pod_name': 'pod_name',
        'pod_node_ip': 'pod_node_ip',
        'pod_node_name': 'pod_node_name',
        'pod_role': 'pod_role',
        'status': 'status',
        'update_time': 'update_time'
    }

    def __init__(self, pod_id=None, pod_name=None, pod_node_ip=None, pod_node_name=None, pod_role=None, status=None, update_time=None):
        r"""ServicePodResponse

        The model defined in huaweicloud sdk

        :param pod_id: **参数解释：** od ID。 **取值范围：** 不涉及。
        :type pod_id: str
        :param pod_name: **参数解释：** pod名字。 **取值范围：** 不涉及。
        :type pod_name: str
        :param pod_node_ip: **参数解释：** pod所在node的IP。 **取值范围：** 不涉及。
        :type pod_node_ip: str
        :param pod_node_name: **参数解释：** pod所在node的名字。 **取值范围：** 不涉及。
        :type pod_node_name: str
        :param pod_role: **参数解释：** pod角色。 **取值范围：** 不涉及。
        :type pod_role: str
        :param status: **参数解释：** pod服务状态。 **取值范围：** 有7种状态。RUNNING（运行中）、PENDING（未就绪）、SUCCEEDED（成功）、FAILED（失败）、ABNORMAL（异常）、UNKNOWN（未知）、DELETED（已删除）。
        :type status: str
        :param update_time: **参数解释：** 最近更新时间。 **取值范围：** 不涉及。
        :type update_time: int
        """
        
        

        self._pod_id = None
        self._pod_name = None
        self._pod_node_ip = None
        self._pod_node_name = None
        self._pod_role = None
        self._status = None
        self._update_time = None
        self.discriminator = None

        if pod_id is not None:
            self.pod_id = pod_id
        if pod_name is not None:
            self.pod_name = pod_name
        if pod_node_ip is not None:
            self.pod_node_ip = pod_node_ip
        if pod_node_name is not None:
            self.pod_node_name = pod_node_name
        if pod_role is not None:
            self.pod_role = pod_role
        if status is not None:
            self.status = status
        if update_time is not None:
            self.update_time = update_time

    @property
    def pod_id(self):
        r"""Gets the pod_id of this ServicePodResponse.

        **参数解释：** od ID。 **取值范围：** 不涉及。

        :return: The pod_id of this ServicePodResponse.
        :rtype: str
        """
        return self._pod_id

    @pod_id.setter
    def pod_id(self, pod_id):
        r"""Sets the pod_id of this ServicePodResponse.

        **参数解释：** od ID。 **取值范围：** 不涉及。

        :param pod_id: The pod_id of this ServicePodResponse.
        :type pod_id: str
        """
        self._pod_id = pod_id

    @property
    def pod_name(self):
        r"""Gets the pod_name of this ServicePodResponse.

        **参数解释：** pod名字。 **取值范围：** 不涉及。

        :return: The pod_name of this ServicePodResponse.
        :rtype: str
        """
        return self._pod_name

    @pod_name.setter
    def pod_name(self, pod_name):
        r"""Sets the pod_name of this ServicePodResponse.

        **参数解释：** pod名字。 **取值范围：** 不涉及。

        :param pod_name: The pod_name of this ServicePodResponse.
        :type pod_name: str
        """
        self._pod_name = pod_name

    @property
    def pod_node_ip(self):
        r"""Gets the pod_node_ip of this ServicePodResponse.

        **参数解释：** pod所在node的IP。 **取值范围：** 不涉及。

        :return: The pod_node_ip of this ServicePodResponse.
        :rtype: str
        """
        return self._pod_node_ip

    @pod_node_ip.setter
    def pod_node_ip(self, pod_node_ip):
        r"""Sets the pod_node_ip of this ServicePodResponse.

        **参数解释：** pod所在node的IP。 **取值范围：** 不涉及。

        :param pod_node_ip: The pod_node_ip of this ServicePodResponse.
        :type pod_node_ip: str
        """
        self._pod_node_ip = pod_node_ip

    @property
    def pod_node_name(self):
        r"""Gets the pod_node_name of this ServicePodResponse.

        **参数解释：** pod所在node的名字。 **取值范围：** 不涉及。

        :return: The pod_node_name of this ServicePodResponse.
        :rtype: str
        """
        return self._pod_node_name

    @pod_node_name.setter
    def pod_node_name(self, pod_node_name):
        r"""Sets the pod_node_name of this ServicePodResponse.

        **参数解释：** pod所在node的名字。 **取值范围：** 不涉及。

        :param pod_node_name: The pod_node_name of this ServicePodResponse.
        :type pod_node_name: str
        """
        self._pod_node_name = pod_node_name

    @property
    def pod_role(self):
        r"""Gets the pod_role of this ServicePodResponse.

        **参数解释：** pod角色。 **取值范围：** 不涉及。

        :return: The pod_role of this ServicePodResponse.
        :rtype: str
        """
        return self._pod_role

    @pod_role.setter
    def pod_role(self, pod_role):
        r"""Sets the pod_role of this ServicePodResponse.

        **参数解释：** pod角色。 **取值范围：** 不涉及。

        :param pod_role: The pod_role of this ServicePodResponse.
        :type pod_role: str
        """
        self._pod_role = pod_role

    @property
    def status(self):
        r"""Gets the status of this ServicePodResponse.

        **参数解释：** pod服务状态。 **取值范围：** 有7种状态。RUNNING（运行中）、PENDING（未就绪）、SUCCEEDED（成功）、FAILED（失败）、ABNORMAL（异常）、UNKNOWN（未知）、DELETED（已删除）。

        :return: The status of this ServicePodResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ServicePodResponse.

        **参数解释：** pod服务状态。 **取值范围：** 有7种状态。RUNNING（运行中）、PENDING（未就绪）、SUCCEEDED（成功）、FAILED（失败）、ABNORMAL（异常）、UNKNOWN（未知）、DELETED（已删除）。

        :param status: The status of this ServicePodResponse.
        :type status: str
        """
        self._status = status

    @property
    def update_time(self):
        r"""Gets the update_time of this ServicePodResponse.

        **参数解释：** 最近更新时间。 **取值范围：** 不涉及。

        :return: The update_time of this ServicePodResponse.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ServicePodResponse.

        **参数解释：** 最近更新时间。 **取值范围：** 不涉及。

        :param update_time: The update_time of this ServicePodResponse.
        :type update_time: int
        """
        self._update_time = update_time

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
        if not isinstance(other, ServicePodResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
