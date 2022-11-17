# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubscriptionTarget:

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
        'connection_id': 'str',
        'detail': 'object',
        'transform': 'SubscriptionTargetTransform'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'provider_type': 'provider_type',
        'connection_id': 'connection_id',
        'detail': 'detail',
        'transform': 'transform'
    }

    def __init__(self, id=None, name=None, provider_type=None, connection_id=None, detail=None, transform=None):
        """SubscriptionTarget

        The model defined in huaweicloud sdk

        :param id: 订阅目标ID，需保证全局唯一，由小写字母、数字、中划线组成，必须字母或数字开头。 更新订阅场景时，指定ID的订阅目标存在时则进行更新，否则进行创建； 创建订阅目标场景时，指定ID作为待创建的订阅目标对象ID，未指定时由系统自动生成。 更新订阅目标时，此字段忽略；
        :type id: str
        :param name: 订阅的事件目标名称
        :type name: str
        :param provider_type: 订阅的事件目标的提供方类型
        :type provider_type: str
        :param connection_id: 订阅的事件目标使用的目标链接ID
        :type connection_id: str
        :param detail: 订阅的事件目标参数列表，该字段序列化后总长度不超过1024字节
        :type detail: object
        :param transform: 
        :type transform: :class:`huaweicloudsdkeg.v1.SubscriptionTargetTransform`
        """
        
        

        self._id = None
        self._name = None
        self._provider_type = None
        self._connection_id = None
        self._detail = None
        self._transform = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        self.provider_type = provider_type
        if connection_id is not None:
            self.connection_id = connection_id
        if detail is not None:
            self.detail = detail
        self.transform = transform

    @property
    def id(self):
        """Gets the id of this SubscriptionTarget.

        订阅目标ID，需保证全局唯一，由小写字母、数字、中划线组成，必须字母或数字开头。 更新订阅场景时，指定ID的订阅目标存在时则进行更新，否则进行创建； 创建订阅目标场景时，指定ID作为待创建的订阅目标对象ID，未指定时由系统自动生成。 更新订阅目标时，此字段忽略；

        :return: The id of this SubscriptionTarget.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SubscriptionTarget.

        订阅目标ID，需保证全局唯一，由小写字母、数字、中划线组成，必须字母或数字开头。 更新订阅场景时，指定ID的订阅目标存在时则进行更新，否则进行创建； 创建订阅目标场景时，指定ID作为待创建的订阅目标对象ID，未指定时由系统自动生成。 更新订阅目标时，此字段忽略；

        :param id: The id of this SubscriptionTarget.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this SubscriptionTarget.

        订阅的事件目标名称

        :return: The name of this SubscriptionTarget.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SubscriptionTarget.

        订阅的事件目标名称

        :param name: The name of this SubscriptionTarget.
        :type name: str
        """
        self._name = name

    @property
    def provider_type(self):
        """Gets the provider_type of this SubscriptionTarget.

        订阅的事件目标的提供方类型

        :return: The provider_type of this SubscriptionTarget.
        :rtype: str
        """
        return self._provider_type

    @provider_type.setter
    def provider_type(self, provider_type):
        """Sets the provider_type of this SubscriptionTarget.

        订阅的事件目标的提供方类型

        :param provider_type: The provider_type of this SubscriptionTarget.
        :type provider_type: str
        """
        self._provider_type = provider_type

    @property
    def connection_id(self):
        """Gets the connection_id of this SubscriptionTarget.

        订阅的事件目标使用的目标链接ID

        :return: The connection_id of this SubscriptionTarget.
        :rtype: str
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        """Sets the connection_id of this SubscriptionTarget.

        订阅的事件目标使用的目标链接ID

        :param connection_id: The connection_id of this SubscriptionTarget.
        :type connection_id: str
        """
        self._connection_id = connection_id

    @property
    def detail(self):
        """Gets the detail of this SubscriptionTarget.

        订阅的事件目标参数列表，该字段序列化后总长度不超过1024字节

        :return: The detail of this SubscriptionTarget.
        :rtype: object
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this SubscriptionTarget.

        订阅的事件目标参数列表，该字段序列化后总长度不超过1024字节

        :param detail: The detail of this SubscriptionTarget.
        :type detail: object
        """
        self._detail = detail

    @property
    def transform(self):
        """Gets the transform of this SubscriptionTarget.

        :return: The transform of this SubscriptionTarget.
        :rtype: :class:`huaweicloudsdkeg.v1.SubscriptionTargetTransform`
        """
        return self._transform

    @transform.setter
    def transform(self, transform):
        """Sets the transform of this SubscriptionTarget.

        :param transform: The transform of this SubscriptionTarget.
        :type transform: :class:`huaweicloudsdkeg.v1.SubscriptionTargetTransform`
        """
        self._transform = transform

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
        if not isinstance(other, SubscriptionTarget):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
