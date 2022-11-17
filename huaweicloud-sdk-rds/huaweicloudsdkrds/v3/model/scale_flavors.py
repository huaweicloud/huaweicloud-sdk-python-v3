# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScaleFlavors:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'code': 'str',
        'cpu': 'str',
        'mem': 'str'
    }

    attribute_map = {
        'code': 'code',
        'cpu': 'cpu',
        'mem': 'mem'
    }

    def __init__(self, code=None, cpu=None, mem=None):
        """ScaleFlavors

        The model defined in huaweicloud sdk

        :param code: 规格码。
        :type code: str
        :param cpu: CPU个数。
        :type cpu: str
        :param mem: 内存大小（单位：GB）。
        :type mem: str
        """
        
        

        self._code = None
        self._cpu = None
        self._mem = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if cpu is not None:
            self.cpu = cpu
        if mem is not None:
            self.mem = mem

    @property
    def code(self):
        """Gets the code of this ScaleFlavors.

        规格码。

        :return: The code of this ScaleFlavors.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ScaleFlavors.

        规格码。

        :param code: The code of this ScaleFlavors.
        :type code: str
        """
        self._code = code

    @property
    def cpu(self):
        """Gets the cpu of this ScaleFlavors.

        CPU个数。

        :return: The cpu of this ScaleFlavors.
        :rtype: str
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        """Sets the cpu of this ScaleFlavors.

        CPU个数。

        :param cpu: The cpu of this ScaleFlavors.
        :type cpu: str
        """
        self._cpu = cpu

    @property
    def mem(self):
        """Gets the mem of this ScaleFlavors.

        内存大小（单位：GB）。

        :return: The mem of this ScaleFlavors.
        :rtype: str
        """
        return self._mem

    @mem.setter
    def mem(self, mem):
        """Sets the mem of this ScaleFlavors.

        内存大小（单位：GB）。

        :param mem: The mem of this ScaleFlavors.
        :type mem: str
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
        if not isinstance(other, ScaleFlavors):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
