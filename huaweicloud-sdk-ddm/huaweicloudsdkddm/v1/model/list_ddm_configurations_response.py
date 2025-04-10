# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDdmConfigurationsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'configurations': 'list[ConfigurationInfo]',
        'total': 'int',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'configurations': 'configurations',
        'total': 'total',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, configurations=None, total=None, offset=None, limit=None):
        r"""ListDdmConfigurationsResponse

        The model defined in huaweicloud sdk

        :param configurations: 参数配置列表
        :type configurations: list[:class:`huaweicloudsdkddm.v1.ConfigurationInfo`]
        :param total: 参数模板总数。
        :type total: int
        :param offset: 分页参数: 起始值。
        :type offset: int
        :param limit: 分页参数：每页多少条。
        :type limit: int
        """
        
        super(ListDdmConfigurationsResponse, self).__init__()

        self._configurations = None
        self._total = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if configurations is not None:
            self.configurations = configurations
        if total is not None:
            self.total = total
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def configurations(self):
        r"""Gets the configurations of this ListDdmConfigurationsResponse.

        参数配置列表

        :return: The configurations of this ListDdmConfigurationsResponse.
        :rtype: list[:class:`huaweicloudsdkddm.v1.ConfigurationInfo`]
        """
        return self._configurations

    @configurations.setter
    def configurations(self, configurations):
        r"""Sets the configurations of this ListDdmConfigurationsResponse.

        参数配置列表

        :param configurations: The configurations of this ListDdmConfigurationsResponse.
        :type configurations: list[:class:`huaweicloudsdkddm.v1.ConfigurationInfo`]
        """
        self._configurations = configurations

    @property
    def total(self):
        r"""Gets the total of this ListDdmConfigurationsResponse.

        参数模板总数。

        :return: The total of this ListDdmConfigurationsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListDdmConfigurationsResponse.

        参数模板总数。

        :param total: The total of this ListDdmConfigurationsResponse.
        :type total: int
        """
        self._total = total

    @property
    def offset(self):
        r"""Gets the offset of this ListDdmConfigurationsResponse.

        分页参数: 起始值。

        :return: The offset of this ListDdmConfigurationsResponse.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListDdmConfigurationsResponse.

        分页参数: 起始值。

        :param offset: The offset of this ListDdmConfigurationsResponse.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListDdmConfigurationsResponse.

        分页参数：每页多少条。

        :return: The limit of this ListDdmConfigurationsResponse.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListDdmConfigurationsResponse.

        分页参数：每页多少条。

        :param limit: The limit of this ListDdmConfigurationsResponse.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListDdmConfigurationsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
