# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RespAddresses:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vpc_id': 'list[RespAddr]'
    }

    attribute_map = {
        'vpc_id': 'vpc_id'
    }

    def __init__(self, vpc_id=None):
        """RespAddresses

        The model defined in huaweicloud sdk

        :param vpc_id: 云服务器的vpc信息。
        :type vpc_id: list[:class:`huaweicloudsdkdeh.v1.RespAddr`]
        """
        
        

        self._vpc_id = None
        self.discriminator = None

        self.vpc_id = vpc_id

    @property
    def vpc_id(self):
        """Gets the vpc_id of this RespAddresses.

        云服务器的vpc信息。

        :return: The vpc_id of this RespAddresses.
        :rtype: list[:class:`huaweicloudsdkdeh.v1.RespAddr`]
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this RespAddresses.

        云服务器的vpc信息。

        :param vpc_id: The vpc_id of this RespAddresses.
        :type vpc_id: list[:class:`huaweicloudsdkdeh.v1.RespAddr`]
        """
        self._vpc_id = vpc_id

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
        if not isinstance(other, RespAddresses):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
