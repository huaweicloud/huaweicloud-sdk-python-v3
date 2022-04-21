# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Attributes:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'cpu_limit': 'str',
        'memory_limit_bytes': 'str',
        'pvc_quantity': 'str'
    }

    attribute_map = {
        'cpu_limit': 'cpu_limit',
        'memory_limit_bytes': 'memory_limit_bytes',
        'pvc_quantity': 'pvc_quantity'
    }

    def __init__(self, cpu_limit=None, memory_limit_bytes=None, pvc_quantity=None):
        """Attributes

        The model defined in huaweicloud sdk

        :param cpu_limit: cpu限制
        :type cpu_limit: str
        :param memory_limit_bytes: 内存限制
        :type memory_limit_bytes: str
        :param pvc_quantity: pvc规格
        :type pvc_quantity: str
        """
        
        

        self._cpu_limit = None
        self._memory_limit_bytes = None
        self._pvc_quantity = None
        self.discriminator = None

        if cpu_limit is not None:
            self.cpu_limit = cpu_limit
        if memory_limit_bytes is not None:
            self.memory_limit_bytes = memory_limit_bytes
        if pvc_quantity is not None:
            self.pvc_quantity = pvc_quantity

    @property
    def cpu_limit(self):
        """Gets the cpu_limit of this Attributes.

        cpu限制

        :return: The cpu_limit of this Attributes.
        :rtype: str
        """
        return self._cpu_limit

    @cpu_limit.setter
    def cpu_limit(self, cpu_limit):
        """Sets the cpu_limit of this Attributes.

        cpu限制

        :param cpu_limit: The cpu_limit of this Attributes.
        :type cpu_limit: str
        """
        self._cpu_limit = cpu_limit

    @property
    def memory_limit_bytes(self):
        """Gets the memory_limit_bytes of this Attributes.

        内存限制

        :return: The memory_limit_bytes of this Attributes.
        :rtype: str
        """
        return self._memory_limit_bytes

    @memory_limit_bytes.setter
    def memory_limit_bytes(self, memory_limit_bytes):
        """Sets the memory_limit_bytes of this Attributes.

        内存限制

        :param memory_limit_bytes: The memory_limit_bytes of this Attributes.
        :type memory_limit_bytes: str
        """
        self._memory_limit_bytes = memory_limit_bytes

    @property
    def pvc_quantity(self):
        """Gets the pvc_quantity of this Attributes.

        pvc规格

        :return: The pvc_quantity of this Attributes.
        :rtype: str
        """
        return self._pvc_quantity

    @pvc_quantity.setter
    def pvc_quantity(self, pvc_quantity):
        """Sets the pvc_quantity of this Attributes.

        pvc规格

        :param pvc_quantity: The pvc_quantity of this Attributes.
        :type pvc_quantity: str
        """
        self._pvc_quantity = pvc_quantity

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
        if not isinstance(other, Attributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
