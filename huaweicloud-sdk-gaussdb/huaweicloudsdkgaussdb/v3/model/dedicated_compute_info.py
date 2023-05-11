# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DedicatedComputeInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vcpus_total': 'int',
        'vcpus_used': 'int',
        'ram_total': 'int',
        'ram_used': 'int',
        'spec_code': 'str',
        'host_num': 'int'
    }

    attribute_map = {
        'vcpus_total': 'vcpus_total',
        'vcpus_used': 'vcpus_used',
        'ram_total': 'ram_total',
        'ram_used': 'ram_used',
        'spec_code': 'spec_code',
        'host_num': 'host_num'
    }

    def __init__(self, vcpus_total=None, vcpus_used=None, ram_total=None, ram_used=None, spec_code=None, host_num=None):
        """DedicatedComputeInfo

        The model defined in huaweicloud sdk

        :param vcpus_total: 专属资源池中cpu总数。
        :type vcpus_total: int
        :param vcpus_used: 专属资源池已使用的cpu数。
        :type vcpus_used: int
        :param ram_total: 专属资源池计算内存大小, 单位GB。
        :type ram_total: int
        :param ram_used: 专属资源池已使用的计算内存大小，单位GB。
        :type ram_used: int
        :param spec_code: 专属资源池计算资源规格码。
        :type spec_code: str
        :param host_num: 专属资源池计算主机数量。
        :type host_num: int
        """
        
        

        self._vcpus_total = None
        self._vcpus_used = None
        self._ram_total = None
        self._ram_used = None
        self._spec_code = None
        self._host_num = None
        self.discriminator = None

        self.vcpus_total = vcpus_total
        self.vcpus_used = vcpus_used
        self.ram_total = ram_total
        self.ram_used = ram_used
        self.spec_code = spec_code
        self.host_num = host_num

    @property
    def vcpus_total(self):
        """Gets the vcpus_total of this DedicatedComputeInfo.

        专属资源池中cpu总数。

        :return: The vcpus_total of this DedicatedComputeInfo.
        :rtype: int
        """
        return self._vcpus_total

    @vcpus_total.setter
    def vcpus_total(self, vcpus_total):
        """Sets the vcpus_total of this DedicatedComputeInfo.

        专属资源池中cpu总数。

        :param vcpus_total: The vcpus_total of this DedicatedComputeInfo.
        :type vcpus_total: int
        """
        self._vcpus_total = vcpus_total

    @property
    def vcpus_used(self):
        """Gets the vcpus_used of this DedicatedComputeInfo.

        专属资源池已使用的cpu数。

        :return: The vcpus_used of this DedicatedComputeInfo.
        :rtype: int
        """
        return self._vcpus_used

    @vcpus_used.setter
    def vcpus_used(self, vcpus_used):
        """Sets the vcpus_used of this DedicatedComputeInfo.

        专属资源池已使用的cpu数。

        :param vcpus_used: The vcpus_used of this DedicatedComputeInfo.
        :type vcpus_used: int
        """
        self._vcpus_used = vcpus_used

    @property
    def ram_total(self):
        """Gets the ram_total of this DedicatedComputeInfo.

        专属资源池计算内存大小, 单位GB。

        :return: The ram_total of this DedicatedComputeInfo.
        :rtype: int
        """
        return self._ram_total

    @ram_total.setter
    def ram_total(self, ram_total):
        """Sets the ram_total of this DedicatedComputeInfo.

        专属资源池计算内存大小, 单位GB。

        :param ram_total: The ram_total of this DedicatedComputeInfo.
        :type ram_total: int
        """
        self._ram_total = ram_total

    @property
    def ram_used(self):
        """Gets the ram_used of this DedicatedComputeInfo.

        专属资源池已使用的计算内存大小，单位GB。

        :return: The ram_used of this DedicatedComputeInfo.
        :rtype: int
        """
        return self._ram_used

    @ram_used.setter
    def ram_used(self, ram_used):
        """Sets the ram_used of this DedicatedComputeInfo.

        专属资源池已使用的计算内存大小，单位GB。

        :param ram_used: The ram_used of this DedicatedComputeInfo.
        :type ram_used: int
        """
        self._ram_used = ram_used

    @property
    def spec_code(self):
        """Gets the spec_code of this DedicatedComputeInfo.

        专属资源池计算资源规格码。

        :return: The spec_code of this DedicatedComputeInfo.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        """Sets the spec_code of this DedicatedComputeInfo.

        专属资源池计算资源规格码。

        :param spec_code: The spec_code of this DedicatedComputeInfo.
        :type spec_code: str
        """
        self._spec_code = spec_code

    @property
    def host_num(self):
        """Gets the host_num of this DedicatedComputeInfo.

        专属资源池计算主机数量。

        :return: The host_num of this DedicatedComputeInfo.
        :rtype: int
        """
        return self._host_num

    @host_num.setter
    def host_num(self, host_num):
        """Sets the host_num of this DedicatedComputeInfo.

        专属资源池计算主机数量。

        :param host_num: The host_num of this DedicatedComputeInfo.
        :type host_num: int
        """
        self._host_num = host_num

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
        if not isinstance(other, DedicatedComputeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
