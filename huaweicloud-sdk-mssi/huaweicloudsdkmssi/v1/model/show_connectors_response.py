# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowConnectorsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'connectors': 'list[ConnectorInfo]',
        'count': 'int'
    }

    attribute_map = {
        'connectors': 'connectors',
        'count': 'count'
    }

    def __init__(self, connectors=None, count=None):
        """ShowConnectorsResponse

        The model defined in huaweicloud sdk

        :param connectors: 连接器列表
        :type connectors: list[:class:`huaweicloudsdkmssi.v1.ConnectorInfo`]
        :param count: 连接器数量
        :type count: int
        """
        
        super(ShowConnectorsResponse, self).__init__()

        self._connectors = None
        self._count = None
        self.discriminator = None

        if connectors is not None:
            self.connectors = connectors
        if count is not None:
            self.count = count

    @property
    def connectors(self):
        """Gets the connectors of this ShowConnectorsResponse.

        连接器列表

        :return: The connectors of this ShowConnectorsResponse.
        :rtype: list[:class:`huaweicloudsdkmssi.v1.ConnectorInfo`]
        """
        return self._connectors

    @connectors.setter
    def connectors(self, connectors):
        """Sets the connectors of this ShowConnectorsResponse.

        连接器列表

        :param connectors: The connectors of this ShowConnectorsResponse.
        :type connectors: list[:class:`huaweicloudsdkmssi.v1.ConnectorInfo`]
        """
        self._connectors = connectors

    @property
    def count(self):
        """Gets the count of this ShowConnectorsResponse.

        连接器数量

        :return: The count of this ShowConnectorsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ShowConnectorsResponse.

        连接器数量

        :param count: The count of this ShowConnectorsResponse.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, ShowConnectorsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
