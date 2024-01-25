# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPluginsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'data': 'list[WasmPlugin]'
    }

    attribute_map = {
        'total': 'total',
        'data': 'data'
    }

    def __init__(self, total=None, data=None):
        """ShowPluginsResponse

        The model defined in huaweicloud sdk

        :param total: 插件总数。
        :type total: int
        :param data: 插件列表。
        :type data: list[:class:`huaweicloudsdkcse.v1.WasmPlugin`]
        """
        
        super(ShowPluginsResponse, self).__init__()

        self._total = None
        self._data = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if data is not None:
            self.data = data

    @property
    def total(self):
        """Gets the total of this ShowPluginsResponse.

        插件总数。

        :return: The total of this ShowPluginsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ShowPluginsResponse.

        插件总数。

        :param total: The total of this ShowPluginsResponse.
        :type total: int
        """
        self._total = total

    @property
    def data(self):
        """Gets the data of this ShowPluginsResponse.

        插件列表。

        :return: The data of this ShowPluginsResponse.
        :rtype: list[:class:`huaweicloudsdkcse.v1.WasmPlugin`]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ShowPluginsResponse.

        插件列表。

        :param data: The data of this ShowPluginsResponse.
        :type data: list[:class:`huaweicloudsdkcse.v1.WasmPlugin`]
        """
        self._data = data

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
        if not isinstance(other, ShowPluginsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
