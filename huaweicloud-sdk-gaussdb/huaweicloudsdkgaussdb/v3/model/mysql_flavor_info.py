# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MysqlFlavorInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vcpus': 'str',
        'ram': 'str'
    }

    attribute_map = {
        'vcpus': 'vcpus',
        'ram': 'ram'
    }

    def __init__(self, vcpus=None, ram=None):
        r"""MysqlFlavorInfo

        The model defined in huaweicloud sdk

        :param vcpus: CPU核数。
        :type vcpus: str
        :param ram: 内存大小，单位GB。
        :type ram: str
        """
        
        

        self._vcpus = None
        self._ram = None
        self.discriminator = None

        self.vcpus = vcpus
        self.ram = ram

    @property
    def vcpus(self):
        r"""Gets the vcpus of this MysqlFlavorInfo.

        CPU核数。

        :return: The vcpus of this MysqlFlavorInfo.
        :rtype: str
        """
        return self._vcpus

    @vcpus.setter
    def vcpus(self, vcpus):
        r"""Sets the vcpus of this MysqlFlavorInfo.

        CPU核数。

        :param vcpus: The vcpus of this MysqlFlavorInfo.
        :type vcpus: str
        """
        self._vcpus = vcpus

    @property
    def ram(self):
        r"""Gets the ram of this MysqlFlavorInfo.

        内存大小，单位GB。

        :return: The ram of this MysqlFlavorInfo.
        :rtype: str
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        r"""Sets the ram of this MysqlFlavorInfo.

        内存大小，单位GB。

        :param ram: The ram of this MysqlFlavorInfo.
        :type ram: str
        """
        self._ram = ram

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
        if not isinstance(other, MysqlFlavorInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
