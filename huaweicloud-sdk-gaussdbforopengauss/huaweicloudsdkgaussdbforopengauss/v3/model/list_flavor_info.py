# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFlavorInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vcpu': 'int',
        'mem': 'int'
    }

    attribute_map = {
        'vcpu': 'vcpu',
        'mem': 'mem'
    }

    def __init__(self, vcpu=None, mem=None):
        r"""ListFlavorInfo

        The model defined in huaweicloud sdk

        :param vcpu: cpu核数。
        :type vcpu: int
        :param mem: 内存大小。
        :type mem: int
        """
        
        

        self._vcpu = None
        self._mem = None
        self.discriminator = None

        self.vcpu = vcpu
        self.mem = mem

    @property
    def vcpu(self):
        r"""Gets the vcpu of this ListFlavorInfo.

        cpu核数。

        :return: The vcpu of this ListFlavorInfo.
        :rtype: int
        """
        return self._vcpu

    @vcpu.setter
    def vcpu(self, vcpu):
        r"""Sets the vcpu of this ListFlavorInfo.

        cpu核数。

        :param vcpu: The vcpu of this ListFlavorInfo.
        :type vcpu: int
        """
        self._vcpu = vcpu

    @property
    def mem(self):
        r"""Gets the mem of this ListFlavorInfo.

        内存大小。

        :return: The mem of this ListFlavorInfo.
        :rtype: int
        """
        return self._mem

    @mem.setter
    def mem(self, mem):
        r"""Sets the mem of this ListFlavorInfo.

        内存大小。

        :param mem: The mem of this ListFlavorInfo.
        :type mem: int
        """
        self._mem = mem

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
        if not isinstance(other, ListFlavorInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
