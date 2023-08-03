# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDataConnectorResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_count': 'int',
        'data_connectors': 'list[DataConnectorDetail]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'data_connectors': 'data_connectors'
    }

    def __init__(self, total_count=None, data_connectors=None):
        """ListDataConnectorResponse

        The model defined in huaweicloud sdk

        :param total_count: 数据连接总数
        :type total_count: int
        :param data_connectors: 数据连接详情列表
        :type data_connectors: list[:class:`huaweicloudsdkmrs.v2.DataConnectorDetail`]
        """
        
        super(ListDataConnectorResponse, self).__init__()

        self._total_count = None
        self._data_connectors = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if data_connectors is not None:
            self.data_connectors = data_connectors

    @property
    def total_count(self):
        """Gets the total_count of this ListDataConnectorResponse.

        数据连接总数

        :return: The total_count of this ListDataConnectorResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListDataConnectorResponse.

        数据连接总数

        :param total_count: The total_count of this ListDataConnectorResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def data_connectors(self):
        """Gets the data_connectors of this ListDataConnectorResponse.

        数据连接详情列表

        :return: The data_connectors of this ListDataConnectorResponse.
        :rtype: list[:class:`huaweicloudsdkmrs.v2.DataConnectorDetail`]
        """
        return self._data_connectors

    @data_connectors.setter
    def data_connectors(self, data_connectors):
        """Sets the data_connectors of this ListDataConnectorResponse.

        数据连接详情列表

        :param data_connectors: The data_connectors of this ListDataConnectorResponse.
        :type data_connectors: list[:class:`huaweicloudsdkmrs.v2.DataConnectorDetail`]
        """
        self._data_connectors = data_connectors

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
        if not isinstance(other, ListDataConnectorResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
