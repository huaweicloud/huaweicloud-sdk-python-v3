# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ItemsResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_type': 'str',
        'resource_name': 'str',
        'index': 'str',
        'supported': 'bool',
        'resource_price': 'list[ResourcePriceResponse]'
    }

    attribute_map = {
        'resource_type': 'resource_type',
        'resource_name': 'resource_name',
        'index': 'index',
        'supported': 'supported',
        'resource_price': 'resource_price'
    }

    def __init__(self, resource_type=None, resource_name=None, index=None, supported=None, resource_price=None):
        """ItemsResponse

        The model defined in huaweicloud sdk

        :param resource_type: 执行计划中的资源类型，如：huaweicloud_evs_volume
        :type resource_type: str
        :param resource_name: 执行计划中的用户定义的资源的名字，如：my_volume
        :type resource_name: str
        :param index: 使用count构建的资源时资源对应的index
        :type index: str
        :param supported: 执行计划中的资源是否支持询价
        :type supported: bool
        :param resource_price: 执行计划中的每个资源部署后的总的询价信息，如果该资源询价结果包含不同的period_type，则询价结果根据period_type类型展示总价。 包周期计费和按需计费返回，免费和不支持询价的资源不返回
        :type resource_price: list[:class:`huaweicloudsdkaos.v1.ResourcePriceResponse`]
        """
        
        

        self._resource_type = None
        self._resource_name = None
        self._index = None
        self._supported = None
        self._resource_price = None
        self.discriminator = None

        if resource_type is not None:
            self.resource_type = resource_type
        if resource_name is not None:
            self.resource_name = resource_name
        if index is not None:
            self.index = index
        if supported is not None:
            self.supported = supported
        if resource_price is not None:
            self.resource_price = resource_price

    @property
    def resource_type(self):
        """Gets the resource_type of this ItemsResponse.

        执行计划中的资源类型，如：huaweicloud_evs_volume

        :return: The resource_type of this ItemsResponse.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this ItemsResponse.

        执行计划中的资源类型，如：huaweicloud_evs_volume

        :param resource_type: The resource_type of this ItemsResponse.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_name(self):
        """Gets the resource_name of this ItemsResponse.

        执行计划中的用户定义的资源的名字，如：my_volume

        :return: The resource_name of this ItemsResponse.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this ItemsResponse.

        执行计划中的用户定义的资源的名字，如：my_volume

        :param resource_name: The resource_name of this ItemsResponse.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def index(self):
        """Gets the index of this ItemsResponse.

        使用count构建的资源时资源对应的index

        :return: The index of this ItemsResponse.
        :rtype: str
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this ItemsResponse.

        使用count构建的资源时资源对应的index

        :param index: The index of this ItemsResponse.
        :type index: str
        """
        self._index = index

    @property
    def supported(self):
        """Gets the supported of this ItemsResponse.

        执行计划中的资源是否支持询价

        :return: The supported of this ItemsResponse.
        :rtype: bool
        """
        return self._supported

    @supported.setter
    def supported(self, supported):
        """Sets the supported of this ItemsResponse.

        执行计划中的资源是否支持询价

        :param supported: The supported of this ItemsResponse.
        :type supported: bool
        """
        self._supported = supported

    @property
    def resource_price(self):
        """Gets the resource_price of this ItemsResponse.

        执行计划中的每个资源部署后的总的询价信息，如果该资源询价结果包含不同的period_type，则询价结果根据period_type类型展示总价。 包周期计费和按需计费返回，免费和不支持询价的资源不返回

        :return: The resource_price of this ItemsResponse.
        :rtype: list[:class:`huaweicloudsdkaos.v1.ResourcePriceResponse`]
        """
        return self._resource_price

    @resource_price.setter
    def resource_price(self, resource_price):
        """Sets the resource_price of this ItemsResponse.

        执行计划中的每个资源部署后的总的询价信息，如果该资源询价结果包含不同的period_type，则询价结果根据period_type类型展示总价。 包周期计费和按需计费返回，免费和不支持询价的资源不返回

        :param resource_price: The resource_price of this ItemsResponse.
        :type resource_price: list[:class:`huaweicloudsdkaos.v1.ResourcePriceResponse`]
        """
        self._resource_price = resource_price

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
        if not isinstance(other, ItemsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
