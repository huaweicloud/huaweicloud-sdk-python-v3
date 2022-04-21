# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QuerySessionResponse:

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
        'active': 'bool',
        'operation': 'str',
        'type': 'str',
        'cost_time': 'str',
        'plan_summary': 'str',
        'host': 'str',
        'client': 'str',
        'description': 'str',
        'namespace': 'str'
    }

    attribute_map = {
        'id': 'id',
        'active': 'active',
        'operation': 'operation',
        'type': 'type',
        'cost_time': 'cost_time',
        'plan_summary': 'plan_summary',
        'host': 'host',
        'client': 'client',
        'description': 'description',
        'namespace': 'namespace'
    }

    def __init__(self, id=None, active=None, operation=None, type=None, cost_time=None, plan_summary=None, host=None, client=None, description=None, namespace=None):
        """QuerySessionResponse

        The model defined in huaweicloud sdk

        :param id: 会话ID。
        :type id: str
        :param active: 当前会话是否活跃。 取值为“true”，表示活跃。 取值为“false”，表示不活跃。
        :type active: bool
        :param operation: 操作。
        :type operation: str
        :param type: 操作类型。
        :type type: str
        :param cost_time: 运行时间，单位为 ms。
        :type cost_time: str
        :param plan_summary: 执行计划描述。
        :type plan_summary: str
        :param host: 主机。
        :type host: str
        :param client: 客户端地址。
        :type client: str
        :param description: 连接描述。
        :type description: str
        :param namespace: 命名空间。
        :type namespace: str
        """
        
        

        self._id = None
        self._active = None
        self._operation = None
        self._type = None
        self._cost_time = None
        self._plan_summary = None
        self._host = None
        self._client = None
        self._description = None
        self._namespace = None
        self.discriminator = None

        self.id = id
        self.active = active
        self.operation = operation
        self.type = type
        self.cost_time = cost_time
        self.plan_summary = plan_summary
        self.host = host
        self.client = client
        self.description = description
        self.namespace = namespace

    @property
    def id(self):
        """Gets the id of this QuerySessionResponse.

        会话ID。

        :return: The id of this QuerySessionResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this QuerySessionResponse.

        会话ID。

        :param id: The id of this QuerySessionResponse.
        :type id: str
        """
        self._id = id

    @property
    def active(self):
        """Gets the active of this QuerySessionResponse.

        当前会话是否活跃。 取值为“true”，表示活跃。 取值为“false”，表示不活跃。

        :return: The active of this QuerySessionResponse.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this QuerySessionResponse.

        当前会话是否活跃。 取值为“true”，表示活跃。 取值为“false”，表示不活跃。

        :param active: The active of this QuerySessionResponse.
        :type active: bool
        """
        self._active = active

    @property
    def operation(self):
        """Gets the operation of this QuerySessionResponse.

        操作。

        :return: The operation of this QuerySessionResponse.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """Sets the operation of this QuerySessionResponse.

        操作。

        :param operation: The operation of this QuerySessionResponse.
        :type operation: str
        """
        self._operation = operation

    @property
    def type(self):
        """Gets the type of this QuerySessionResponse.

        操作类型。

        :return: The type of this QuerySessionResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this QuerySessionResponse.

        操作类型。

        :param type: The type of this QuerySessionResponse.
        :type type: str
        """
        self._type = type

    @property
    def cost_time(self):
        """Gets the cost_time of this QuerySessionResponse.

        运行时间，单位为 ms。

        :return: The cost_time of this QuerySessionResponse.
        :rtype: str
        """
        return self._cost_time

    @cost_time.setter
    def cost_time(self, cost_time):
        """Sets the cost_time of this QuerySessionResponse.

        运行时间，单位为 ms。

        :param cost_time: The cost_time of this QuerySessionResponse.
        :type cost_time: str
        """
        self._cost_time = cost_time

    @property
    def plan_summary(self):
        """Gets the plan_summary of this QuerySessionResponse.

        执行计划描述。

        :return: The plan_summary of this QuerySessionResponse.
        :rtype: str
        """
        return self._plan_summary

    @plan_summary.setter
    def plan_summary(self, plan_summary):
        """Sets the plan_summary of this QuerySessionResponse.

        执行计划描述。

        :param plan_summary: The plan_summary of this QuerySessionResponse.
        :type plan_summary: str
        """
        self._plan_summary = plan_summary

    @property
    def host(self):
        """Gets the host of this QuerySessionResponse.

        主机。

        :return: The host of this QuerySessionResponse.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this QuerySessionResponse.

        主机。

        :param host: The host of this QuerySessionResponse.
        :type host: str
        """
        self._host = host

    @property
    def client(self):
        """Gets the client of this QuerySessionResponse.

        客户端地址。

        :return: The client of this QuerySessionResponse.
        :rtype: str
        """
        return self._client

    @client.setter
    def client(self, client):
        """Sets the client of this QuerySessionResponse.

        客户端地址。

        :param client: The client of this QuerySessionResponse.
        :type client: str
        """
        self._client = client

    @property
    def description(self):
        """Gets the description of this QuerySessionResponse.

        连接描述。

        :return: The description of this QuerySessionResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this QuerySessionResponse.

        连接描述。

        :param description: The description of this QuerySessionResponse.
        :type description: str
        """
        self._description = description

    @property
    def namespace(self):
        """Gets the namespace of this QuerySessionResponse.

        命名空间。

        :return: The namespace of this QuerySessionResponse.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this QuerySessionResponse.

        命名空间。

        :param namespace: The namespace of this QuerySessionResponse.
        :type namespace: str
        """
        self._namespace = namespace

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
        if not isinstance(other, QuerySessionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
