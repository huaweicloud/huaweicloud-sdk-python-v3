# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StartProtectionGroupRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_server_group': 'object'
    }

    attribute_map = {
        'start_server_group': 'start-server-group'
    }

    def __init__(self, start_server_group=None):
        """StartProtectionGroupRequestBody

        The model defined in huaweicloud sdk

        :param start_server_group: 标识保护组开始保护操作。目前该参数为空。
        :type start_server_group: object
        """
        
        

        self._start_server_group = None
        self.discriminator = None

        self.start_server_group = start_server_group

    @property
    def start_server_group(self):
        """Gets the start_server_group of this StartProtectionGroupRequestBody.

        标识保护组开始保护操作。目前该参数为空。

        :return: The start_server_group of this StartProtectionGroupRequestBody.
        :rtype: object
        """
        return self._start_server_group

    @start_server_group.setter
    def start_server_group(self, start_server_group):
        """Sets the start_server_group of this StartProtectionGroupRequestBody.

        标识保护组开始保护操作。目前该参数为空。

        :param start_server_group: The start_server_group of this StartProtectionGroupRequestBody.
        :type start_server_group: object
        """
        self._start_server_group = start_server_group

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
        if not isinstance(other, StartProtectionGroupRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
