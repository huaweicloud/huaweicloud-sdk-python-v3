# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDirectConnectRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'direct_connect_id': 'str',
        'fields': 'list[str]'
    }

    attribute_map = {
        'direct_connect_id': 'direct_connect_id',
        'fields': 'fields'
    }

    def __init__(self, direct_connect_id=None, fields=None):
        """ShowDirectConnectRequest

        The model defined in huaweicloud sdk

        :param direct_connect_id: 物理专线连接ID。
        :type direct_connect_id: str
        :param fields: 显示字段列表
        :type fields: list[str]
        """
        
        

        self._direct_connect_id = None
        self._fields = None
        self.discriminator = None

        self.direct_connect_id = direct_connect_id
        if fields is not None:
            self.fields = fields

    @property
    def direct_connect_id(self):
        """Gets the direct_connect_id of this ShowDirectConnectRequest.

        物理专线连接ID。

        :return: The direct_connect_id of this ShowDirectConnectRequest.
        :rtype: str
        """
        return self._direct_connect_id

    @direct_connect_id.setter
    def direct_connect_id(self, direct_connect_id):
        """Sets the direct_connect_id of this ShowDirectConnectRequest.

        物理专线连接ID。

        :param direct_connect_id: The direct_connect_id of this ShowDirectConnectRequest.
        :type direct_connect_id: str
        """
        self._direct_connect_id = direct_connect_id

    @property
    def fields(self):
        """Gets the fields of this ShowDirectConnectRequest.

        显示字段列表

        :return: The fields of this ShowDirectConnectRequest.
        :rtype: list[str]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this ShowDirectConnectRequest.

        显示字段列表

        :param fields: The fields of this ShowDirectConnectRequest.
        :type fields: list[str]
        """
        self._fields = fields

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
        if not isinstance(other, ShowDirectConnectRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
