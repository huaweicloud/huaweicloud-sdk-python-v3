# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CpuOptions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'hwcpu_threads': 'int'
    }

    attribute_map = {
        'hwcpu_threads': 'hw:cpu_threads'
    }

    def __init__(self, hwcpu_threads=None):
        """CpuOptions

        The model defined in huaweicloud sdk

        :param hwcpu_threads: CPU超线程数， 决定CPU是否开启超线程
        :type hwcpu_threads: int
        """
        
        

        self._hwcpu_threads = None
        self.discriminator = None

        if hwcpu_threads is not None:
            self.hwcpu_threads = hwcpu_threads

    @property
    def hwcpu_threads(self):
        """Gets the hwcpu_threads of this CpuOptions.

        CPU超线程数， 决定CPU是否开启超线程

        :return: The hwcpu_threads of this CpuOptions.
        :rtype: int
        """
        return self._hwcpu_threads

    @hwcpu_threads.setter
    def hwcpu_threads(self, hwcpu_threads):
        """Sets the hwcpu_threads of this CpuOptions.

        CPU超线程数， 决定CPU是否开启超线程

        :param hwcpu_threads: The hwcpu_threads of this CpuOptions.
        :type hwcpu_threads: int
        """
        self._hwcpu_threads = hwcpu_threads

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
        if not isinstance(other, CpuOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
