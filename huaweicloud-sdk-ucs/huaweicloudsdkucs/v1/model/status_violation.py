# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StatusViolation:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'kind': 'str',
        'name': 'str',
        'namespace': 'str',
        'message': 'str',
        'enforcement_action': 'str'
    }

    attribute_map = {
        'kind': 'kind',
        'name': 'name',
        'namespace': 'namespace',
        'message': 'message',
        'enforcement_action': 'enforcementAction'
    }

    def __init__(self, kind=None, name=None, namespace=None, message=None, enforcement_action=None):
        r"""StatusViolation

        The model defined in huaweicloud sdk

        :param kind: 违规资源类型
        :type kind: str
        :param name: 违规资源名称
        :type name: str
        :param namespace: 违规资源所在命名空间
        :type namespace: str
        :param message: 详细违规信息
        :type message: str
        :param enforcement_action: 审计行为
        :type enforcement_action: str
        """
        
        

        self._kind = None
        self._name = None
        self._namespace = None
        self._message = None
        self._enforcement_action = None
        self.discriminator = None

        if kind is not None:
            self.kind = kind
        if name is not None:
            self.name = name
        if namespace is not None:
            self.namespace = namespace
        if message is not None:
            self.message = message
        if enforcement_action is not None:
            self.enforcement_action = enforcement_action

    @property
    def kind(self):
        r"""Gets the kind of this StatusViolation.

        违规资源类型

        :return: The kind of this StatusViolation.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        r"""Sets the kind of this StatusViolation.

        违规资源类型

        :param kind: The kind of this StatusViolation.
        :type kind: str
        """
        self._kind = kind

    @property
    def name(self):
        r"""Gets the name of this StatusViolation.

        违规资源名称

        :return: The name of this StatusViolation.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this StatusViolation.

        违规资源名称

        :param name: The name of this StatusViolation.
        :type name: str
        """
        self._name = name

    @property
    def namespace(self):
        r"""Gets the namespace of this StatusViolation.

        违规资源所在命名空间

        :return: The namespace of this StatusViolation.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this StatusViolation.

        违规资源所在命名空间

        :param namespace: The namespace of this StatusViolation.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def message(self):
        r"""Gets the message of this StatusViolation.

        详细违规信息

        :return: The message of this StatusViolation.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this StatusViolation.

        详细违规信息

        :param message: The message of this StatusViolation.
        :type message: str
        """
        self._message = message

    @property
    def enforcement_action(self):
        r"""Gets the enforcement_action of this StatusViolation.

        审计行为

        :return: The enforcement_action of this StatusViolation.
        :rtype: str
        """
        return self._enforcement_action

    @enforcement_action.setter
    def enforcement_action(self, enforcement_action):
        r"""Sets the enforcement_action of this StatusViolation.

        审计行为

        :param enforcement_action: The enforcement_action of this StatusViolation.
        :type enforcement_action: str
        """
        self._enforcement_action = enforcement_action

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
        if not isinstance(other, StatusViolation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
