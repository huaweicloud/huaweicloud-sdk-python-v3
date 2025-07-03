# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMgmtSiteStatusRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_schema_type': 'str'
    }

    attribute_map = {
        'x_schema_type': 'X-Schema-Type'
    }

    def __init__(self, x_schema_type=None):
        r"""ShowMgmtSiteStatusRequest

        The model defined in huaweicloud sdk

        :param x_schema_type: 模版类型。
        :type x_schema_type: str
        """
        
        

        self._x_schema_type = None
        self.discriminator = None

        if x_schema_type is not None:
            self.x_schema_type = x_schema_type

    @property
    def x_schema_type(self):
        r"""Gets the x_schema_type of this ShowMgmtSiteStatusRequest.

        模版类型。

        :return: The x_schema_type of this ShowMgmtSiteStatusRequest.
        :rtype: str
        """
        return self._x_schema_type

    @x_schema_type.setter
    def x_schema_type(self, x_schema_type):
        r"""Sets the x_schema_type of this ShowMgmtSiteStatusRequest.

        模版类型。

        :param x_schema_type: The x_schema_type of this ShowMgmtSiteStatusRequest.
        :type x_schema_type: str
        """
        self._x_schema_type = x_schema_type

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
        if not isinstance(other, ShowMgmtSiteStatusRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
