# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FailoverProtectionGroupRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'failover_server_group': 'object'
    }

    attribute_map = {
        'failover_server_group': 'failover-server-group'
    }

    def __init__(self, failover_server_group=None):
        """FailoverProtectionGroupRequestBody

        The model defined in huaweicloud sdk

        :param failover_server_group: 标识保护组故障切换操作。该参数目前默认值为空。
        :type failover_server_group: object
        """
        
        

        self._failover_server_group = None
        self.discriminator = None

        self.failover_server_group = failover_server_group

    @property
    def failover_server_group(self):
        """Gets the failover_server_group of this FailoverProtectionGroupRequestBody.

        标识保护组故障切换操作。该参数目前默认值为空。

        :return: The failover_server_group of this FailoverProtectionGroupRequestBody.
        :rtype: object
        """
        return self._failover_server_group

    @failover_server_group.setter
    def failover_server_group(self, failover_server_group):
        """Sets the failover_server_group of this FailoverProtectionGroupRequestBody.

        标识保护组故障切换操作。该参数目前默认值为空。

        :param failover_server_group: The failover_server_group of this FailoverProtectionGroupRequestBody.
        :type failover_server_group: object
        """
        self._failover_server_group = failover_server_group

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
        if not isinstance(other, FailoverProtectionGroupRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
