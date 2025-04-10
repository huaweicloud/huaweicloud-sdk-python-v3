# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ComputingSpecDto:

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
        'name': 'str',
        'ram': 'int',
        'vcpus': 'str',
        'max_rate': 'str',
        'min_rate': 'str',
        'max_pps': 'str'
    }

    attribute_map = {
        'code': 'code',
        'name': 'name',
        'ram': 'ram',
        'vcpus': 'vcpus',
        'max_rate': 'max_rate',
        'min_rate': 'min_rate',
        'max_pps': 'max_pps'
    }

    def __init__(self, code=None, name=None, ram=None, vcpus=None, max_rate=None, min_rate=None, max_pps=None):
        r"""ComputingSpecDto

        The model defined in huaweicloud sdk

        :param code: 规格编号
        :type code: str
        :param name: 规格名称
        :type name: str
        :param ram: 内存
        :type ram: int
        :param vcpus: vcpus
        :type vcpus: str
        :param max_rate: 最大带宽
        :type max_rate: str
        :param min_rate: 基准带宽
        :type min_rate: str
        :param max_pps: 最大收发包能力
        :type max_pps: str
        """
        
        

        self._code = None
        self._name = None
        self._ram = None
        self._vcpus = None
        self._max_rate = None
        self._min_rate = None
        self._max_pps = None
        self.discriminator = None

        self.code = code
        self.name = name
        if ram is not None:
            self.ram = ram
        if vcpus is not None:
            self.vcpus = vcpus
        if max_rate is not None:
            self.max_rate = max_rate
        if min_rate is not None:
            self.min_rate = min_rate
        if max_pps is not None:
            self.max_pps = max_pps

    @property
    def code(self):
        r"""Gets the code of this ComputingSpecDto.

        规格编号

        :return: The code of this ComputingSpecDto.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this ComputingSpecDto.

        规格编号

        :param code: The code of this ComputingSpecDto.
        :type code: str
        """
        self._code = code

    @property
    def name(self):
        r"""Gets the name of this ComputingSpecDto.

        规格名称

        :return: The name of this ComputingSpecDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ComputingSpecDto.

        规格名称

        :param name: The name of this ComputingSpecDto.
        :type name: str
        """
        self._name = name

    @property
    def ram(self):
        r"""Gets the ram of this ComputingSpecDto.

        内存

        :return: The ram of this ComputingSpecDto.
        :rtype: int
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        r"""Sets the ram of this ComputingSpecDto.

        内存

        :param ram: The ram of this ComputingSpecDto.
        :type ram: int
        """
        self._ram = ram

    @property
    def vcpus(self):
        r"""Gets the vcpus of this ComputingSpecDto.

        vcpus

        :return: The vcpus of this ComputingSpecDto.
        :rtype: str
        """
        return self._vcpus

    @vcpus.setter
    def vcpus(self, vcpus):
        r"""Sets the vcpus of this ComputingSpecDto.

        vcpus

        :param vcpus: The vcpus of this ComputingSpecDto.
        :type vcpus: str
        """
        self._vcpus = vcpus

    @property
    def max_rate(self):
        r"""Gets the max_rate of this ComputingSpecDto.

        最大带宽

        :return: The max_rate of this ComputingSpecDto.
        :rtype: str
        """
        return self._max_rate

    @max_rate.setter
    def max_rate(self, max_rate):
        r"""Sets the max_rate of this ComputingSpecDto.

        最大带宽

        :param max_rate: The max_rate of this ComputingSpecDto.
        :type max_rate: str
        """
        self._max_rate = max_rate

    @property
    def min_rate(self):
        r"""Gets the min_rate of this ComputingSpecDto.

        基准带宽

        :return: The min_rate of this ComputingSpecDto.
        :rtype: str
        """
        return self._min_rate

    @min_rate.setter
    def min_rate(self, min_rate):
        r"""Sets the min_rate of this ComputingSpecDto.

        基准带宽

        :param min_rate: The min_rate of this ComputingSpecDto.
        :type min_rate: str
        """
        self._min_rate = min_rate

    @property
    def max_pps(self):
        r"""Gets the max_pps of this ComputingSpecDto.

        最大收发包能力

        :return: The max_pps of this ComputingSpecDto.
        :rtype: str
        """
        return self._max_pps

    @max_pps.setter
    def max_pps(self, max_pps):
        r"""Sets the max_pps of this ComputingSpecDto.

        最大收发包能力

        :param max_pps: The max_pps of this ComputingSpecDto.
        :type max_pps: str
        """
        self._max_pps = max_pps

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
        if not isinstance(other, ComputingSpecDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
