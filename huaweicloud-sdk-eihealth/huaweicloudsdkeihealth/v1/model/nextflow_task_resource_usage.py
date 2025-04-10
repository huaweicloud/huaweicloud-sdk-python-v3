# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NextflowTaskResourceUsage:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cpu_percent': 'float',
        'mem_percent': 'float',
        'rchar': 'int',
        'wchar': 'int',
        'read_bytes': 'int',
        'write_bytes': 'int',
        'vmem': 'int',
        'rss': 'int',
        'peak_vmem': 'int',
        'peak_rss': 'int',
        'syscr': 'int',
        'syscw': 'int',
        'vol_ctxt': 'int',
        'inv_ctxt': 'int'
    }

    attribute_map = {
        'cpu_percent': 'cpu_percent',
        'mem_percent': 'mem_percent',
        'rchar': 'rchar',
        'wchar': 'wchar',
        'read_bytes': 'read_bytes',
        'write_bytes': 'write_bytes',
        'vmem': 'vmem',
        'rss': 'rss',
        'peak_vmem': 'peak_vmem',
        'peak_rss': 'peak_rss',
        'syscr': 'syscr',
        'syscw': 'syscw',
        'vol_ctxt': 'vol_ctxt',
        'inv_ctxt': 'inv_ctxt'
    }

    def __init__(self, cpu_percent=None, mem_percent=None, rchar=None, wchar=None, read_bytes=None, write_bytes=None, vmem=None, rss=None, peak_vmem=None, peak_rss=None, syscr=None, syscw=None, vol_ctxt=None, inv_ctxt=None):
        r"""NextflowTaskResourceUsage

        The model defined in huaweicloud sdk

        :param cpu_percent: cpu占用率
        :type cpu_percent: float
        :param mem_percent: 内存占用率
        :type mem_percent: float
        :param rchar: 读取字符数
        :type rchar: int
        :param wchar: 写入字符数
        :type wchar: int
        :param read_bytes: 读取字节数
        :type read_bytes: int
        :param write_bytes: 写入字符数
        :type write_bytes: int
        :param vmem: process虚拟内存大小
        :type vmem: int
        :param rss: process实际内存大小
        :type rss: int
        :param peak_vmem: process虚拟内存峰值
        :type peak_vmem: int
        :param peak_rss: process实际内存峰值
        :type peak_rss: int
        :param syscr: 系统调用次数
        :type syscr: int
        :param syscw: 系统调用次数
        :type syscw: int
        :param vol_ctxt: 自愿上下文切换数
        :type vol_ctxt: int
        :param inv_ctxt: 非自愿上下文切换数
        :type inv_ctxt: int
        """
        
        

        self._cpu_percent = None
        self._mem_percent = None
        self._rchar = None
        self._wchar = None
        self._read_bytes = None
        self._write_bytes = None
        self._vmem = None
        self._rss = None
        self._peak_vmem = None
        self._peak_rss = None
        self._syscr = None
        self._syscw = None
        self._vol_ctxt = None
        self._inv_ctxt = None
        self.discriminator = None

        if cpu_percent is not None:
            self.cpu_percent = cpu_percent
        if mem_percent is not None:
            self.mem_percent = mem_percent
        if rchar is not None:
            self.rchar = rchar
        if wchar is not None:
            self.wchar = wchar
        if read_bytes is not None:
            self.read_bytes = read_bytes
        if write_bytes is not None:
            self.write_bytes = write_bytes
        if vmem is not None:
            self.vmem = vmem
        if rss is not None:
            self.rss = rss
        if peak_vmem is not None:
            self.peak_vmem = peak_vmem
        if peak_rss is not None:
            self.peak_rss = peak_rss
        if syscr is not None:
            self.syscr = syscr
        if syscw is not None:
            self.syscw = syscw
        if vol_ctxt is not None:
            self.vol_ctxt = vol_ctxt
        if inv_ctxt is not None:
            self.inv_ctxt = inv_ctxt

    @property
    def cpu_percent(self):
        r"""Gets the cpu_percent of this NextflowTaskResourceUsage.

        cpu占用率

        :return: The cpu_percent of this NextflowTaskResourceUsage.
        :rtype: float
        """
        return self._cpu_percent

    @cpu_percent.setter
    def cpu_percent(self, cpu_percent):
        r"""Sets the cpu_percent of this NextflowTaskResourceUsage.

        cpu占用率

        :param cpu_percent: The cpu_percent of this NextflowTaskResourceUsage.
        :type cpu_percent: float
        """
        self._cpu_percent = cpu_percent

    @property
    def mem_percent(self):
        r"""Gets the mem_percent of this NextflowTaskResourceUsage.

        内存占用率

        :return: The mem_percent of this NextflowTaskResourceUsage.
        :rtype: float
        """
        return self._mem_percent

    @mem_percent.setter
    def mem_percent(self, mem_percent):
        r"""Sets the mem_percent of this NextflowTaskResourceUsage.

        内存占用率

        :param mem_percent: The mem_percent of this NextflowTaskResourceUsage.
        :type mem_percent: float
        """
        self._mem_percent = mem_percent

    @property
    def rchar(self):
        r"""Gets the rchar of this NextflowTaskResourceUsage.

        读取字符数

        :return: The rchar of this NextflowTaskResourceUsage.
        :rtype: int
        """
        return self._rchar

    @rchar.setter
    def rchar(self, rchar):
        r"""Sets the rchar of this NextflowTaskResourceUsage.

        读取字符数

        :param rchar: The rchar of this NextflowTaskResourceUsage.
        :type rchar: int
        """
        self._rchar = rchar

    @property
    def wchar(self):
        r"""Gets the wchar of this NextflowTaskResourceUsage.

        写入字符数

        :return: The wchar of this NextflowTaskResourceUsage.
        :rtype: int
        """
        return self._wchar

    @wchar.setter
    def wchar(self, wchar):
        r"""Sets the wchar of this NextflowTaskResourceUsage.

        写入字符数

        :param wchar: The wchar of this NextflowTaskResourceUsage.
        :type wchar: int
        """
        self._wchar = wchar

    @property
    def read_bytes(self):
        r"""Gets the read_bytes of this NextflowTaskResourceUsage.

        读取字节数

        :return: The read_bytes of this NextflowTaskResourceUsage.
        :rtype: int
        """
        return self._read_bytes

    @read_bytes.setter
    def read_bytes(self, read_bytes):
        r"""Sets the read_bytes of this NextflowTaskResourceUsage.

        读取字节数

        :param read_bytes: The read_bytes of this NextflowTaskResourceUsage.
        :type read_bytes: int
        """
        self._read_bytes = read_bytes

    @property
    def write_bytes(self):
        r"""Gets the write_bytes of this NextflowTaskResourceUsage.

        写入字符数

        :return: The write_bytes of this NextflowTaskResourceUsage.
        :rtype: int
        """
        return self._write_bytes

    @write_bytes.setter
    def write_bytes(self, write_bytes):
        r"""Sets the write_bytes of this NextflowTaskResourceUsage.

        写入字符数

        :param write_bytes: The write_bytes of this NextflowTaskResourceUsage.
        :type write_bytes: int
        """
        self._write_bytes = write_bytes

    @property
    def vmem(self):
        r"""Gets the vmem of this NextflowTaskResourceUsage.

        process虚拟内存大小

        :return: The vmem of this NextflowTaskResourceUsage.
        :rtype: int
        """
        return self._vmem

    @vmem.setter
    def vmem(self, vmem):
        r"""Sets the vmem of this NextflowTaskResourceUsage.

        process虚拟内存大小

        :param vmem: The vmem of this NextflowTaskResourceUsage.
        :type vmem: int
        """
        self._vmem = vmem

    @property
    def rss(self):
        r"""Gets the rss of this NextflowTaskResourceUsage.

        process实际内存大小

        :return: The rss of this NextflowTaskResourceUsage.
        :rtype: int
        """
        return self._rss

    @rss.setter
    def rss(self, rss):
        r"""Sets the rss of this NextflowTaskResourceUsage.

        process实际内存大小

        :param rss: The rss of this NextflowTaskResourceUsage.
        :type rss: int
        """
        self._rss = rss

    @property
    def peak_vmem(self):
        r"""Gets the peak_vmem of this NextflowTaskResourceUsage.

        process虚拟内存峰值

        :return: The peak_vmem of this NextflowTaskResourceUsage.
        :rtype: int
        """
        return self._peak_vmem

    @peak_vmem.setter
    def peak_vmem(self, peak_vmem):
        r"""Sets the peak_vmem of this NextflowTaskResourceUsage.

        process虚拟内存峰值

        :param peak_vmem: The peak_vmem of this NextflowTaskResourceUsage.
        :type peak_vmem: int
        """
        self._peak_vmem = peak_vmem

    @property
    def peak_rss(self):
        r"""Gets the peak_rss of this NextflowTaskResourceUsage.

        process实际内存峰值

        :return: The peak_rss of this NextflowTaskResourceUsage.
        :rtype: int
        """
        return self._peak_rss

    @peak_rss.setter
    def peak_rss(self, peak_rss):
        r"""Sets the peak_rss of this NextflowTaskResourceUsage.

        process实际内存峰值

        :param peak_rss: The peak_rss of this NextflowTaskResourceUsage.
        :type peak_rss: int
        """
        self._peak_rss = peak_rss

    @property
    def syscr(self):
        r"""Gets the syscr of this NextflowTaskResourceUsage.

        系统调用次数

        :return: The syscr of this NextflowTaskResourceUsage.
        :rtype: int
        """
        return self._syscr

    @syscr.setter
    def syscr(self, syscr):
        r"""Sets the syscr of this NextflowTaskResourceUsage.

        系统调用次数

        :param syscr: The syscr of this NextflowTaskResourceUsage.
        :type syscr: int
        """
        self._syscr = syscr

    @property
    def syscw(self):
        r"""Gets the syscw of this NextflowTaskResourceUsage.

        系统调用次数

        :return: The syscw of this NextflowTaskResourceUsage.
        :rtype: int
        """
        return self._syscw

    @syscw.setter
    def syscw(self, syscw):
        r"""Sets the syscw of this NextflowTaskResourceUsage.

        系统调用次数

        :param syscw: The syscw of this NextflowTaskResourceUsage.
        :type syscw: int
        """
        self._syscw = syscw

    @property
    def vol_ctxt(self):
        r"""Gets the vol_ctxt of this NextflowTaskResourceUsage.

        自愿上下文切换数

        :return: The vol_ctxt of this NextflowTaskResourceUsage.
        :rtype: int
        """
        return self._vol_ctxt

    @vol_ctxt.setter
    def vol_ctxt(self, vol_ctxt):
        r"""Sets the vol_ctxt of this NextflowTaskResourceUsage.

        自愿上下文切换数

        :param vol_ctxt: The vol_ctxt of this NextflowTaskResourceUsage.
        :type vol_ctxt: int
        """
        self._vol_ctxt = vol_ctxt

    @property
    def inv_ctxt(self):
        r"""Gets the inv_ctxt of this NextflowTaskResourceUsage.

        非自愿上下文切换数

        :return: The inv_ctxt of this NextflowTaskResourceUsage.
        :rtype: int
        """
        return self._inv_ctxt

    @inv_ctxt.setter
    def inv_ctxt(self, inv_ctxt):
        r"""Sets the inv_ctxt of this NextflowTaskResourceUsage.

        非自愿上下文切换数

        :param inv_ctxt: The inv_ctxt of this NextflowTaskResourceUsage.
        :type inv_ctxt: int
        """
        self._inv_ctxt = inv_ctxt

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
        if not isinstance(other, NextflowTaskResourceUsage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
