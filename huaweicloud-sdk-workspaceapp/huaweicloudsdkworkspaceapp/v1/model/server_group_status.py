# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServerGroupStatus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'aps_status': 'dict(str, int)'
    }

    attribute_map = {
        'aps_status': 'aps_status'
    }

    def __init__(self, aps_status=None):
        r"""ServerGroupStatus

        The model defined in huaweicloud sdk

        :param aps_status: 对应状态的服务器数量，参考ServerStatus。
        :type aps_status: dict(str, int)
        """
        
        

        self._aps_status = None
        self.discriminator = None

        if aps_status is not None:
            self.aps_status = aps_status

    @property
    def aps_status(self):
        r"""Gets the aps_status of this ServerGroupStatus.

        对应状态的服务器数量，参考ServerStatus。

        :return: The aps_status of this ServerGroupStatus.
        :rtype: dict(str, int)
        """
        return self._aps_status

    @aps_status.setter
    def aps_status(self, aps_status):
        r"""Sets the aps_status of this ServerGroupStatus.

        对应状态的服务器数量，参考ServerStatus。

        :param aps_status: The aps_status of this ServerGroupStatus.
        :type aps_status: dict(str, int)
        """
        self._aps_status = aps_status

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
        if not isinstance(other, ServerGroupStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
