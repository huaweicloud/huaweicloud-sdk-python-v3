# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VolumeFlavor:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'engine_version': 'str',
        'code': 'str',
        'type': 'str',
        'size': 'str',
        'period': 'list[str]'
    }

    attribute_map = {
        'engine_version': 'engine_version',
        'code': 'code',
        'type': 'type',
        'size': 'size',
        'period': 'period'
    }

    def __init__(self, engine_version=None, code=None, type=None, size=None, period=None):
        """VolumeFlavor

        The model defined in huaweicloud sdk

        :param engine_version: 引擎版本
        :type engine_version: str
        :param code: 磁盘规格码
        :type code: str
        :param type: 磁盘类型
        :type type: str
        :param size: 磁盘大小
        :type size: str
        :param period: 订购周期
        :type period: list[str]
        """
        
        

        self._engine_version = None
        self._code = None
        self._type = None
        self._size = None
        self._period = None
        self.discriminator = None

        self.engine_version = engine_version
        self.code = code
        self.type = type
        self.size = size
        self.period = period

    @property
    def engine_version(self):
        """Gets the engine_version of this VolumeFlavor.

        引擎版本

        :return: The engine_version of this VolumeFlavor.
        :rtype: str
        """
        return self._engine_version

    @engine_version.setter
    def engine_version(self, engine_version):
        """Sets the engine_version of this VolumeFlavor.

        引擎版本

        :param engine_version: The engine_version of this VolumeFlavor.
        :type engine_version: str
        """
        self._engine_version = engine_version

    @property
    def code(self):
        """Gets the code of this VolumeFlavor.

        磁盘规格码

        :return: The code of this VolumeFlavor.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this VolumeFlavor.

        磁盘规格码

        :param code: The code of this VolumeFlavor.
        :type code: str
        """
        self._code = code

    @property
    def type(self):
        """Gets the type of this VolumeFlavor.

        磁盘类型

        :return: The type of this VolumeFlavor.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this VolumeFlavor.

        磁盘类型

        :param type: The type of this VolumeFlavor.
        :type type: str
        """
        self._type = type

    @property
    def size(self):
        """Gets the size of this VolumeFlavor.

        磁盘大小

        :return: The size of this VolumeFlavor.
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this VolumeFlavor.

        磁盘大小

        :param size: The size of this VolumeFlavor.
        :type size: str
        """
        self._size = size

    @property
    def period(self):
        """Gets the period of this VolumeFlavor.

        订购周期

        :return: The period of this VolumeFlavor.
        :rtype: list[str]
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this VolumeFlavor.

        订购周期

        :param period: The period of this VolumeFlavor.
        :type period: list[str]
        """
        self._period = period

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
        if not isinstance(other, VolumeFlavor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
