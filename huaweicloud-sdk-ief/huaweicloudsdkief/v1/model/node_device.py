# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeDevice:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'added': 'DeviceInfos',
        'removed': 'list[str]'
    }

    attribute_map = {
        'added': 'added',
        'removed': 'removed'
    }

    def __init__(self, added=None, removed=None):
        r"""NodeDevice

        The model defined in huaweicloud sdk

        :param added: 
        :type added: :class:`huaweicloudsdkief.v1.DeviceInfos`
        :param removed: 要解绑的终端设备ID
        :type removed: list[str]
        """
        
        

        self._added = None
        self._removed = None
        self.discriminator = None

        if added is not None:
            self.added = added
        if removed is not None:
            self.removed = removed

    @property
    def added(self):
        r"""Gets the added of this NodeDevice.

        :return: The added of this NodeDevice.
        :rtype: :class:`huaweicloudsdkief.v1.DeviceInfos`
        """
        return self._added

    @added.setter
    def added(self, added):
        r"""Sets the added of this NodeDevice.

        :param added: The added of this NodeDevice.
        :type added: :class:`huaweicloudsdkief.v1.DeviceInfos`
        """
        self._added = added

    @property
    def removed(self):
        r"""Gets the removed of this NodeDevice.

        要解绑的终端设备ID

        :return: The removed of this NodeDevice.
        :rtype: list[str]
        """
        return self._removed

    @removed.setter
    def removed(self, removed):
        r"""Sets the removed of this NodeDevice.

        要解绑的终端设备ID

        :param removed: The removed of this NodeDevice.
        :type removed: list[str]
        """
        self._removed = removed

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
        if not isinstance(other, NodeDevice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
