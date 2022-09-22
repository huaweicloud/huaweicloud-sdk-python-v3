# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubscriptionSource:

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
        'provider_type': 'str',
        'detail': 'object',
        'filter': 'object'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'provider_type': 'provider_type',
        'detail': 'detail',
        'filter': 'filter'
    }

    def __init__(self, id=None, name=None, provider_type=None, detail=None, filter=None):
        """SubscriptionSource

        The model defined in huaweicloud sdk

        :param id: 订阅源ID，需保证全局唯一。指定ID的订阅源存在时则进行更新，否则进行创建；未指定时由系统自动生成。由小写字母、数字、中划线组成，必须字母或数字开头。
        :type id: str
        :param name: 订阅的事件源名称
        :type name: str
        :param provider_type: 订阅的事件源的提供方类型
        :type provider_type: str
        :param detail: 订阅的事件源参数列表, 该字段序列化后总长度不超过1024字节
        :type detail: object
        :param filter: 订阅事件源的匹配过滤规则, 该字段序列化后总长度不超过2048字节
        :type filter: object
        """
        
        

        self._id = None
        self._name = None
        self._provider_type = None
        self._detail = None
        self._filter = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        self.provider_type = provider_type
        if detail is not None:
            self.detail = detail
        self.filter = filter

    @property
    def id(self):
        """Gets the id of this SubscriptionSource.

        订阅源ID，需保证全局唯一。指定ID的订阅源存在时则进行更新，否则进行创建；未指定时由系统自动生成。由小写字母、数字、中划线组成，必须字母或数字开头。

        :return: The id of this SubscriptionSource.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SubscriptionSource.

        订阅源ID，需保证全局唯一。指定ID的订阅源存在时则进行更新，否则进行创建；未指定时由系统自动生成。由小写字母、数字、中划线组成，必须字母或数字开头。

        :param id: The id of this SubscriptionSource.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this SubscriptionSource.

        订阅的事件源名称

        :return: The name of this SubscriptionSource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SubscriptionSource.

        订阅的事件源名称

        :param name: The name of this SubscriptionSource.
        :type name: str
        """
        self._name = name

    @property
    def provider_type(self):
        """Gets the provider_type of this SubscriptionSource.

        订阅的事件源的提供方类型

        :return: The provider_type of this SubscriptionSource.
        :rtype: str
        """
        return self._provider_type

    @provider_type.setter
    def provider_type(self, provider_type):
        """Sets the provider_type of this SubscriptionSource.

        订阅的事件源的提供方类型

        :param provider_type: The provider_type of this SubscriptionSource.
        :type provider_type: str
        """
        self._provider_type = provider_type

    @property
    def detail(self):
        """Gets the detail of this SubscriptionSource.

        订阅的事件源参数列表, 该字段序列化后总长度不超过1024字节

        :return: The detail of this SubscriptionSource.
        :rtype: object
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this SubscriptionSource.

        订阅的事件源参数列表, 该字段序列化后总长度不超过1024字节

        :param detail: The detail of this SubscriptionSource.
        :type detail: object
        """
        self._detail = detail

    @property
    def filter(self):
        """Gets the filter of this SubscriptionSource.

        订阅事件源的匹配过滤规则, 该字段序列化后总长度不超过2048字节

        :return: The filter of this SubscriptionSource.
        :rtype: object
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this SubscriptionSource.

        订阅事件源的匹配过滤规则, 该字段序列化后总长度不超过2048字节

        :param filter: The filter of this SubscriptionSource.
        :type filter: object
        """
        self._filter = filter

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
        if not isinstance(other, SubscriptionSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
