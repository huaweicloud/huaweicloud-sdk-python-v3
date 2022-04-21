# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RespAddr:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'addr': 'str',
        'version': 'str'
    }

    attribute_map = {
        'addr': 'addr',
        'version': 'version'
    }

    def __init__(self, addr=None, version=None):
        """RespAddr

        The model defined in huaweicloud sdk

        :param addr: 云服务器的vpc ip。
        :type addr: str
        :param version: 云服务器的vpc版本。
        :type version: str
        """
        
        

        self._addr = None
        self._version = None
        self.discriminator = None

        self.addr = addr
        self.version = version

    @property
    def addr(self):
        """Gets the addr of this RespAddr.

        云服务器的vpc ip。

        :return: The addr of this RespAddr.
        :rtype: str
        """
        return self._addr

    @addr.setter
    def addr(self, addr):
        """Sets the addr of this RespAddr.

        云服务器的vpc ip。

        :param addr: The addr of this RespAddr.
        :type addr: str
        """
        self._addr = addr

    @property
    def version(self):
        """Gets the version of this RespAddr.

        云服务器的vpc版本。

        :return: The version of this RespAddr.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this RespAddr.

        云服务器的vpc版本。

        :param version: The version of this RespAddr.
        :type version: str
        """
        self._version = version

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
        if not isinstance(other, RespAddr):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
