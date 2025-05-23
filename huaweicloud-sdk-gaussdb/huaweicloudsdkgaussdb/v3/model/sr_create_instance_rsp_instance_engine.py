# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SrCreateInstanceRspInstanceEngine:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'version': 'str'
    }

    attribute_map = {
        'type': 'type',
        'version': 'version'
    }

    def __init__(self, type=None, version=None):
        r"""SrCreateInstanceRspInstanceEngine

        The model defined in huaweicloud sdk

        :param type: 引擎类型。
        :type type: str
        :param version: 引擎大版本号。
        :type version: str
        """
        
        

        self._type = None
        self._version = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if version is not None:
            self.version = version

    @property
    def type(self):
        r"""Gets the type of this SrCreateInstanceRspInstanceEngine.

        引擎类型。

        :return: The type of this SrCreateInstanceRspInstanceEngine.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this SrCreateInstanceRspInstanceEngine.

        引擎类型。

        :param type: The type of this SrCreateInstanceRspInstanceEngine.
        :type type: str
        """
        self._type = type

    @property
    def version(self):
        r"""Gets the version of this SrCreateInstanceRspInstanceEngine.

        引擎大版本号。

        :return: The version of this SrCreateInstanceRspInstanceEngine.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this SrCreateInstanceRspInstanceEngine.

        引擎大版本号。

        :param version: The version of this SrCreateInstanceRspInstanceEngine.
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
        if not isinstance(other, SrCreateInstanceRspInstanceEngine):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
