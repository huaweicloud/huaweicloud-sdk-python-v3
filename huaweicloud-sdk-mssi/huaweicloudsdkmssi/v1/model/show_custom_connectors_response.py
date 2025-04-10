# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCustomConnectorsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'connector_infos': 'list[ConnectorInfo0]',
        'count': 'int'
    }

    attribute_map = {
        'connector_infos': 'connector_infos',
        'count': 'count'
    }

    def __init__(self, connector_infos=None, count=None):
        r"""ShowCustomConnectorsResponse

        The model defined in huaweicloud sdk

        :param connector_infos: 连接器列表
        :type connector_infos: list[:class:`huaweicloudsdkmssi.v1.ConnectorInfo0`]
        :param count: 连接器数量
        :type count: int
        """
        
        super(ShowCustomConnectorsResponse, self).__init__()

        self._connector_infos = None
        self._count = None
        self.discriminator = None

        if connector_infos is not None:
            self.connector_infos = connector_infos
        if count is not None:
            self.count = count

    @property
    def connector_infos(self):
        r"""Gets the connector_infos of this ShowCustomConnectorsResponse.

        连接器列表

        :return: The connector_infos of this ShowCustomConnectorsResponse.
        :rtype: list[:class:`huaweicloudsdkmssi.v1.ConnectorInfo0`]
        """
        return self._connector_infos

    @connector_infos.setter
    def connector_infos(self, connector_infos):
        r"""Sets the connector_infos of this ShowCustomConnectorsResponse.

        连接器列表

        :param connector_infos: The connector_infos of this ShowCustomConnectorsResponse.
        :type connector_infos: list[:class:`huaweicloudsdkmssi.v1.ConnectorInfo0`]
        """
        self._connector_infos = connector_infos

    @property
    def count(self):
        r"""Gets the count of this ShowCustomConnectorsResponse.

        连接器数量

        :return: The count of this ShowCustomConnectorsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ShowCustomConnectorsResponse.

        连接器数量

        :param count: The count of this ShowCustomConnectorsResponse.
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
        if not isinstance(other, ShowCustomConnectorsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
