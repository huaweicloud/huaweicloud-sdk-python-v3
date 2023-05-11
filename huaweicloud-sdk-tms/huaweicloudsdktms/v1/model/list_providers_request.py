# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListProvidersRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'locale': 'str',
        'limit': 'int',
        'offset': 'int',
        'provider': 'str'
    }

    attribute_map = {
        'locale': 'locale',
        'limit': 'limit',
        'offset': 'offset',
        'provider': 'provider'
    }

    def __init__(self, locale=None, limit=None, offset=None, provider=None):
        """ListProvidersRequest

        The model defined in huaweicloud sdk

        :param locale: 指定显示语言
        :type locale: str
        :param limit: 查询记录数默认为200，limit最多为200，最小值为1。
        :type limit: int
        :param offset: 索引位置，从offset指定的下一条数据开始查询，必须为数字，不能为负数，默认为0。
        :type offset: int
        :param provider: 云服务名称
        :type provider: str
        """
        
        

        self._locale = None
        self._limit = None
        self._offset = None
        self._provider = None
        self.discriminator = None

        if locale is not None:
            self.locale = locale
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if provider is not None:
            self.provider = provider

    @property
    def locale(self):
        """Gets the locale of this ListProvidersRequest.

        指定显示语言

        :return: The locale of this ListProvidersRequest.
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this ListProvidersRequest.

        指定显示语言

        :param locale: The locale of this ListProvidersRequest.
        :type locale: str
        """
        self._locale = locale

    @property
    def limit(self):
        """Gets the limit of this ListProvidersRequest.

        查询记录数默认为200，limit最多为200，最小值为1。

        :return: The limit of this ListProvidersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListProvidersRequest.

        查询记录数默认为200，limit最多为200，最小值为1。

        :param limit: The limit of this ListProvidersRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListProvidersRequest.

        索引位置，从offset指定的下一条数据开始查询，必须为数字，不能为负数，默认为0。

        :return: The offset of this ListProvidersRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListProvidersRequest.

        索引位置，从offset指定的下一条数据开始查询，必须为数字，不能为负数，默认为0。

        :param offset: The offset of this ListProvidersRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def provider(self):
        """Gets the provider of this ListProvidersRequest.

        云服务名称

        :return: The provider of this ListProvidersRequest.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this ListProvidersRequest.

        云服务名称

        :param provider: The provider of this ListProvidersRequest.
        :type provider: str
        """
        self._provider = provider

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
        if not isinstance(other, ListProvidersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
