# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSubscriptionSourceResponse(SdkResponse):

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
        'filter': 'object',
        'created_time': 'str',
        'updated_time': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'provider_type': 'provider_type',
        'detail': 'detail',
        'filter': 'filter',
        'created_time': 'created_time',
        'updated_time': 'updated_time',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, id=None, name=None, provider_type=None, detail=None, filter=None, created_time=None, updated_time=None, x_request_id=None):
        """UpdateSubscriptionSourceResponse

        The model defined in huaweicloud sdk

        :param id: 订阅源ID
        :type id: str
        :param name: 订阅的事件源名称
        :type name: str
        :param provider_type: 订阅的事件源的提供方类型
        :type provider_type: str
        :param detail: 订阅的事件源参数列表
        :type detail: object
        :param filter: 订阅事件源的匹配过滤规则
        :type filter: object
        :param created_time: 创建时间
        :type created_time: str
        :param updated_time: 更新时间
        :type updated_time: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(UpdateSubscriptionSourceResponse, self).__init__()

        self._id = None
        self._name = None
        self._provider_type = None
        self._detail = None
        self._filter = None
        self._created_time = None
        self._updated_time = None
        self._x_request_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if provider_type is not None:
            self.provider_type = provider_type
        if detail is not None:
            self.detail = detail
        if filter is not None:
            self.filter = filter
        if created_time is not None:
            self.created_time = created_time
        if updated_time is not None:
            self.updated_time = updated_time
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def id(self):
        """Gets the id of this UpdateSubscriptionSourceResponse.

        订阅源ID

        :return: The id of this UpdateSubscriptionSourceResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdateSubscriptionSourceResponse.

        订阅源ID

        :param id: The id of this UpdateSubscriptionSourceResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this UpdateSubscriptionSourceResponse.

        订阅的事件源名称

        :return: The name of this UpdateSubscriptionSourceResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateSubscriptionSourceResponse.

        订阅的事件源名称

        :param name: The name of this UpdateSubscriptionSourceResponse.
        :type name: str
        """
        self._name = name

    @property
    def provider_type(self):
        """Gets the provider_type of this UpdateSubscriptionSourceResponse.

        订阅的事件源的提供方类型

        :return: The provider_type of this UpdateSubscriptionSourceResponse.
        :rtype: str
        """
        return self._provider_type

    @provider_type.setter
    def provider_type(self, provider_type):
        """Sets the provider_type of this UpdateSubscriptionSourceResponse.

        订阅的事件源的提供方类型

        :param provider_type: The provider_type of this UpdateSubscriptionSourceResponse.
        :type provider_type: str
        """
        self._provider_type = provider_type

    @property
    def detail(self):
        """Gets the detail of this UpdateSubscriptionSourceResponse.

        订阅的事件源参数列表

        :return: The detail of this UpdateSubscriptionSourceResponse.
        :rtype: object
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this UpdateSubscriptionSourceResponse.

        订阅的事件源参数列表

        :param detail: The detail of this UpdateSubscriptionSourceResponse.
        :type detail: object
        """
        self._detail = detail

    @property
    def filter(self):
        """Gets the filter of this UpdateSubscriptionSourceResponse.

        订阅事件源的匹配过滤规则

        :return: The filter of this UpdateSubscriptionSourceResponse.
        :rtype: object
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this UpdateSubscriptionSourceResponse.

        订阅事件源的匹配过滤规则

        :param filter: The filter of this UpdateSubscriptionSourceResponse.
        :type filter: object
        """
        self._filter = filter

    @property
    def created_time(self):
        """Gets the created_time of this UpdateSubscriptionSourceResponse.

        创建时间

        :return: The created_time of this UpdateSubscriptionSourceResponse.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this UpdateSubscriptionSourceResponse.

        创建时间

        :param created_time: The created_time of this UpdateSubscriptionSourceResponse.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def updated_time(self):
        """Gets the updated_time of this UpdateSubscriptionSourceResponse.

        更新时间

        :return: The updated_time of this UpdateSubscriptionSourceResponse.
        :rtype: str
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        """Sets the updated_time of this UpdateSubscriptionSourceResponse.

        更新时间

        :param updated_time: The updated_time of this UpdateSubscriptionSourceResponse.
        :type updated_time: str
        """
        self._updated_time = updated_time

    @property
    def x_request_id(self):
        """Gets the x_request_id of this UpdateSubscriptionSourceResponse.


        :return: The x_request_id of this UpdateSubscriptionSourceResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this UpdateSubscriptionSourceResponse.


        :param x_request_id: The x_request_id of this UpdateSubscriptionSourceResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, UpdateSubscriptionSourceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
