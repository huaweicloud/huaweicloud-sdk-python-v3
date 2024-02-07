# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ComputingResourceFlavorsRsp:

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
        'max_pps': 'str',
        'sold_out': 'bool',
        'az': 'str',
        'cpu_detail': 'str',
        'disk_detail': 'str',
        'memory_detail': 'str',
        'netcard_detail': 'str',
        'cpu_arch': 'str',
        'gpu_info': 'str'
    }

    attribute_map = {
        'code': 'code',
        'name': 'name',
        'ram': 'ram',
        'vcpus': 'vcpus',
        'max_rate': 'max_rate',
        'min_rate': 'min_rate',
        'max_pps': 'max_pps',
        'sold_out': 'sold_out',
        'az': 'az',
        'cpu_detail': 'cpu_detail',
        'disk_detail': 'disk_detail',
        'memory_detail': 'memory_detail',
        'netcard_detail': 'netcard_detail',
        'cpu_arch': 'cpu_arch',
        'gpu_info': 'gpu_info'
    }

    def __init__(self, code=None, name=None, ram=None, vcpus=None, max_rate=None, min_rate=None, max_pps=None, sold_out=None, az=None, cpu_detail=None, disk_detail=None, memory_detail=None, netcard_detail=None, cpu_arch=None, gpu_info=None):
        """ComputingResourceFlavorsRsp

        The model defined in huaweicloud sdk

        :param code: 规格编码
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
        :param sold_out: 是否售罄
        :type sold_out: bool
        :param az: 可用区
        :type az: str
        :param cpu_detail: CPU物理规格描述信息
        :type cpu_detail: str
        :param disk_detail: 磁盘物理规格描述信息
        :type disk_detail: str
        :param memory_detail: 内存物理规格描述信息
        :type memory_detail: str
        :param netcard_detail: 网卡物理规格描述信息
        :type netcard_detail: str
        :param cpu_arch: 裸金属服务器的CPU架构类型
        :type cpu_arch: str
        :param gpu_info: GPU信息
        :type gpu_info: str
        """
        
        

        self._code = None
        self._name = None
        self._ram = None
        self._vcpus = None
        self._max_rate = None
        self._min_rate = None
        self._max_pps = None
        self._sold_out = None
        self._az = None
        self._cpu_detail = None
        self._disk_detail = None
        self._memory_detail = None
        self._netcard_detail = None
        self._cpu_arch = None
        self._gpu_info = None
        self.discriminator = None

        self.code = code
        self.name = name
        self.ram = ram
        self.vcpus = vcpus
        if max_rate is not None:
            self.max_rate = max_rate
        if min_rate is not None:
            self.min_rate = min_rate
        if max_pps is not None:
            self.max_pps = max_pps
        self.sold_out = sold_out
        if az is not None:
            self.az = az
        if cpu_detail is not None:
            self.cpu_detail = cpu_detail
        if disk_detail is not None:
            self.disk_detail = disk_detail
        if memory_detail is not None:
            self.memory_detail = memory_detail
        if netcard_detail is not None:
            self.netcard_detail = netcard_detail
        if cpu_arch is not None:
            self.cpu_arch = cpu_arch
        if gpu_info is not None:
            self.gpu_info = gpu_info

    @property
    def code(self):
        """Gets the code of this ComputingResourceFlavorsRsp.

        规格编码

        :return: The code of this ComputingResourceFlavorsRsp.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ComputingResourceFlavorsRsp.

        规格编码

        :param code: The code of this ComputingResourceFlavorsRsp.
        :type code: str
        """
        self._code = code

    @property
    def name(self):
        """Gets the name of this ComputingResourceFlavorsRsp.

        规格名称

        :return: The name of this ComputingResourceFlavorsRsp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ComputingResourceFlavorsRsp.

        规格名称

        :param name: The name of this ComputingResourceFlavorsRsp.
        :type name: str
        """
        self._name = name

    @property
    def ram(self):
        """Gets the ram of this ComputingResourceFlavorsRsp.

        内存

        :return: The ram of this ComputingResourceFlavorsRsp.
        :rtype: int
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        """Sets the ram of this ComputingResourceFlavorsRsp.

        内存

        :param ram: The ram of this ComputingResourceFlavorsRsp.
        :type ram: int
        """
        self._ram = ram

    @property
    def vcpus(self):
        """Gets the vcpus of this ComputingResourceFlavorsRsp.

        vcpus

        :return: The vcpus of this ComputingResourceFlavorsRsp.
        :rtype: str
        """
        return self._vcpus

    @vcpus.setter
    def vcpus(self, vcpus):
        """Sets the vcpus of this ComputingResourceFlavorsRsp.

        vcpus

        :param vcpus: The vcpus of this ComputingResourceFlavorsRsp.
        :type vcpus: str
        """
        self._vcpus = vcpus

    @property
    def max_rate(self):
        """Gets the max_rate of this ComputingResourceFlavorsRsp.

        最大带宽

        :return: The max_rate of this ComputingResourceFlavorsRsp.
        :rtype: str
        """
        return self._max_rate

    @max_rate.setter
    def max_rate(self, max_rate):
        """Sets the max_rate of this ComputingResourceFlavorsRsp.

        最大带宽

        :param max_rate: The max_rate of this ComputingResourceFlavorsRsp.
        :type max_rate: str
        """
        self._max_rate = max_rate

    @property
    def min_rate(self):
        """Gets the min_rate of this ComputingResourceFlavorsRsp.

        基准带宽

        :return: The min_rate of this ComputingResourceFlavorsRsp.
        :rtype: str
        """
        return self._min_rate

    @min_rate.setter
    def min_rate(self, min_rate):
        """Sets the min_rate of this ComputingResourceFlavorsRsp.

        基准带宽

        :param min_rate: The min_rate of this ComputingResourceFlavorsRsp.
        :type min_rate: str
        """
        self._min_rate = min_rate

    @property
    def max_pps(self):
        """Gets the max_pps of this ComputingResourceFlavorsRsp.

        最大收发包能力

        :return: The max_pps of this ComputingResourceFlavorsRsp.
        :rtype: str
        """
        return self._max_pps

    @max_pps.setter
    def max_pps(self, max_pps):
        """Sets the max_pps of this ComputingResourceFlavorsRsp.

        最大收发包能力

        :param max_pps: The max_pps of this ComputingResourceFlavorsRsp.
        :type max_pps: str
        """
        self._max_pps = max_pps

    @property
    def sold_out(self):
        """Gets the sold_out of this ComputingResourceFlavorsRsp.

        是否售罄

        :return: The sold_out of this ComputingResourceFlavorsRsp.
        :rtype: bool
        """
        return self._sold_out

    @sold_out.setter
    def sold_out(self, sold_out):
        """Sets the sold_out of this ComputingResourceFlavorsRsp.

        是否售罄

        :param sold_out: The sold_out of this ComputingResourceFlavorsRsp.
        :type sold_out: bool
        """
        self._sold_out = sold_out

    @property
    def az(self):
        """Gets the az of this ComputingResourceFlavorsRsp.

        可用区

        :return: The az of this ComputingResourceFlavorsRsp.
        :rtype: str
        """
        return self._az

    @az.setter
    def az(self, az):
        """Sets the az of this ComputingResourceFlavorsRsp.

        可用区

        :param az: The az of this ComputingResourceFlavorsRsp.
        :type az: str
        """
        self._az = az

    @property
    def cpu_detail(self):
        """Gets the cpu_detail of this ComputingResourceFlavorsRsp.

        CPU物理规格描述信息

        :return: The cpu_detail of this ComputingResourceFlavorsRsp.
        :rtype: str
        """
        return self._cpu_detail

    @cpu_detail.setter
    def cpu_detail(self, cpu_detail):
        """Sets the cpu_detail of this ComputingResourceFlavorsRsp.

        CPU物理规格描述信息

        :param cpu_detail: The cpu_detail of this ComputingResourceFlavorsRsp.
        :type cpu_detail: str
        """
        self._cpu_detail = cpu_detail

    @property
    def disk_detail(self):
        """Gets the disk_detail of this ComputingResourceFlavorsRsp.

        磁盘物理规格描述信息

        :return: The disk_detail of this ComputingResourceFlavorsRsp.
        :rtype: str
        """
        return self._disk_detail

    @disk_detail.setter
    def disk_detail(self, disk_detail):
        """Sets the disk_detail of this ComputingResourceFlavorsRsp.

        磁盘物理规格描述信息

        :param disk_detail: The disk_detail of this ComputingResourceFlavorsRsp.
        :type disk_detail: str
        """
        self._disk_detail = disk_detail

    @property
    def memory_detail(self):
        """Gets the memory_detail of this ComputingResourceFlavorsRsp.

        内存物理规格描述信息

        :return: The memory_detail of this ComputingResourceFlavorsRsp.
        :rtype: str
        """
        return self._memory_detail

    @memory_detail.setter
    def memory_detail(self, memory_detail):
        """Sets the memory_detail of this ComputingResourceFlavorsRsp.

        内存物理规格描述信息

        :param memory_detail: The memory_detail of this ComputingResourceFlavorsRsp.
        :type memory_detail: str
        """
        self._memory_detail = memory_detail

    @property
    def netcard_detail(self):
        """Gets the netcard_detail of this ComputingResourceFlavorsRsp.

        网卡物理规格描述信息

        :return: The netcard_detail of this ComputingResourceFlavorsRsp.
        :rtype: str
        """
        return self._netcard_detail

    @netcard_detail.setter
    def netcard_detail(self, netcard_detail):
        """Sets the netcard_detail of this ComputingResourceFlavorsRsp.

        网卡物理规格描述信息

        :param netcard_detail: The netcard_detail of this ComputingResourceFlavorsRsp.
        :type netcard_detail: str
        """
        self._netcard_detail = netcard_detail

    @property
    def cpu_arch(self):
        """Gets the cpu_arch of this ComputingResourceFlavorsRsp.

        裸金属服务器的CPU架构类型

        :return: The cpu_arch of this ComputingResourceFlavorsRsp.
        :rtype: str
        """
        return self._cpu_arch

    @cpu_arch.setter
    def cpu_arch(self, cpu_arch):
        """Sets the cpu_arch of this ComputingResourceFlavorsRsp.

        裸金属服务器的CPU架构类型

        :param cpu_arch: The cpu_arch of this ComputingResourceFlavorsRsp.
        :type cpu_arch: str
        """
        self._cpu_arch = cpu_arch

    @property
    def gpu_info(self):
        """Gets the gpu_info of this ComputingResourceFlavorsRsp.

        GPU信息

        :return: The gpu_info of this ComputingResourceFlavorsRsp.
        :rtype: str
        """
        return self._gpu_info

    @gpu_info.setter
    def gpu_info(self, gpu_info):
        """Sets the gpu_info of this ComputingResourceFlavorsRsp.

        GPU信息

        :param gpu_info: The gpu_info of this ComputingResourceFlavorsRsp.
        :type gpu_info: str
        """
        self._gpu_info = gpu_info

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
        if not isinstance(other, ComputingResourceFlavorsRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
