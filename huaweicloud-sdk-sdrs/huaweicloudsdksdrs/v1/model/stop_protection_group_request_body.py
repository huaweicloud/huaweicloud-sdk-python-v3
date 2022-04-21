# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StopProtectionGroupRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'stop_server_group': 'object'
    }

    attribute_map = {
        'stop_server_group': 'stop-server-group'
    }

    def __init__(self, stop_server_group=None):
        """StopProtectionGroupRequestBody

        The model defined in huaweicloud sdk

        :param stop_server_group: 标识保护组停止保护操作。该参数目前默认值为空。
        :type stop_server_group: object
        """
        
        

        self._stop_server_group = None
        self.discriminator = None

        self.stop_server_group = stop_server_group

    @property
    def stop_server_group(self):
        """Gets the stop_server_group of this StopProtectionGroupRequestBody.

        标识保护组停止保护操作。该参数目前默认值为空。

        :return: The stop_server_group of this StopProtectionGroupRequestBody.
        :rtype: object
        """
        return self._stop_server_group

    @stop_server_group.setter
    def stop_server_group(self, stop_server_group):
        """Sets the stop_server_group of this StopProtectionGroupRequestBody.

        标识保护组停止保护操作。该参数目前默认值为空。

        :param stop_server_group: The stop_server_group of this StopProtectionGroupRequestBody.
        :type stop_server_group: object
        """
        self._stop_server_group = stop_server_group

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
        if not isinstance(other, StopProtectionGroupRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
