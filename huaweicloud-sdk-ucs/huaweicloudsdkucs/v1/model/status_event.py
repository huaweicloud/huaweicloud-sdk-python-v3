# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StatusEvent:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'first_timestamp': 'str',
        'resource_kind': 'str',
        'resource_name': 'str',
        'resource_namespace': 'str',
        'message': 'str'
    }

    attribute_map = {
        'first_timestamp': 'firstTimestamp',
        'resource_kind': 'resourceKind',
        'resource_name': 'resourceName',
        'resource_namespace': 'resourceNamespace',
        'message': 'message'
    }

    def __init__(self, first_timestamp=None, resource_kind=None, resource_name=None, resource_namespace=None, message=None):
        r"""StatusEvent

        The model defined in huaweicloud sdk

        :param first_timestamp: 拦截事件首次发生时间
        :type first_timestamp: str
        :param resource_kind: 拦截事件资源类型
        :type resource_kind: str
        :param resource_name: 拦截事件资源名称
        :type resource_name: str
        :param resource_namespace: 拦截事件资源命名空间，如果没有则为空
        :type resource_namespace: str
        :param message: 拦截事件详细信息
        :type message: str
        """
        
        

        self._first_timestamp = None
        self._resource_kind = None
        self._resource_name = None
        self._resource_namespace = None
        self._message = None
        self.discriminator = None

        if first_timestamp is not None:
            self.first_timestamp = first_timestamp
        if resource_kind is not None:
            self.resource_kind = resource_kind
        if resource_name is not None:
            self.resource_name = resource_name
        if resource_namespace is not None:
            self.resource_namespace = resource_namespace
        if message is not None:
            self.message = message

    @property
    def first_timestamp(self):
        r"""Gets the first_timestamp of this StatusEvent.

        拦截事件首次发生时间

        :return: The first_timestamp of this StatusEvent.
        :rtype: str
        """
        return self._first_timestamp

    @first_timestamp.setter
    def first_timestamp(self, first_timestamp):
        r"""Sets the first_timestamp of this StatusEvent.

        拦截事件首次发生时间

        :param first_timestamp: The first_timestamp of this StatusEvent.
        :type first_timestamp: str
        """
        self._first_timestamp = first_timestamp

    @property
    def resource_kind(self):
        r"""Gets the resource_kind of this StatusEvent.

        拦截事件资源类型

        :return: The resource_kind of this StatusEvent.
        :rtype: str
        """
        return self._resource_kind

    @resource_kind.setter
    def resource_kind(self, resource_kind):
        r"""Sets the resource_kind of this StatusEvent.

        拦截事件资源类型

        :param resource_kind: The resource_kind of this StatusEvent.
        :type resource_kind: str
        """
        self._resource_kind = resource_kind

    @property
    def resource_name(self):
        r"""Gets the resource_name of this StatusEvent.

        拦截事件资源名称

        :return: The resource_name of this StatusEvent.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this StatusEvent.

        拦截事件资源名称

        :param resource_name: The resource_name of this StatusEvent.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def resource_namespace(self):
        r"""Gets the resource_namespace of this StatusEvent.

        拦截事件资源命名空间，如果没有则为空

        :return: The resource_namespace of this StatusEvent.
        :rtype: str
        """
        return self._resource_namespace

    @resource_namespace.setter
    def resource_namespace(self, resource_namespace):
        r"""Sets the resource_namespace of this StatusEvent.

        拦截事件资源命名空间，如果没有则为空

        :param resource_namespace: The resource_namespace of this StatusEvent.
        :type resource_namespace: str
        """
        self._resource_namespace = resource_namespace

    @property
    def message(self):
        r"""Gets the message of this StatusEvent.

        拦截事件详细信息

        :return: The message of this StatusEvent.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this StatusEvent.

        拦截事件详细信息

        :param message: The message of this StatusEvent.
        :type message: str
        """
        self._message = message

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
        if not isinstance(other, StatusEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
