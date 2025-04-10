# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProtectedInstanceAttachment:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'replication': 'str',
        'device': 'str'
    }

    attribute_map = {
        'replication': 'replication',
        'device': 'device'
    }

    def __init__(self, replication=None, device=None):
        r"""ProtectedInstanceAttachment

        The model defined in huaweicloud sdk

        :param replication: 复制对ID。
        :type replication: str
        :param device: 挂载点。
        :type device: str
        """
        
        

        self._replication = None
        self._device = None
        self.discriminator = None

        self.replication = replication
        self.device = device

    @property
    def replication(self):
        r"""Gets the replication of this ProtectedInstanceAttachment.

        复制对ID。

        :return: The replication of this ProtectedInstanceAttachment.
        :rtype: str
        """
        return self._replication

    @replication.setter
    def replication(self, replication):
        r"""Sets the replication of this ProtectedInstanceAttachment.

        复制对ID。

        :param replication: The replication of this ProtectedInstanceAttachment.
        :type replication: str
        """
        self._replication = replication

    @property
    def device(self):
        r"""Gets the device of this ProtectedInstanceAttachment.

        挂载点。

        :return: The device of this ProtectedInstanceAttachment.
        :rtype: str
        """
        return self._device

    @device.setter
    def device(self, device):
        r"""Sets the device of this ProtectedInstanceAttachment.

        挂载点。

        :param device: The device of this ProtectedInstanceAttachment.
        :type device: str
        """
        self._device = device

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
        if not isinstance(other, ProtectedInstanceAttachment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
