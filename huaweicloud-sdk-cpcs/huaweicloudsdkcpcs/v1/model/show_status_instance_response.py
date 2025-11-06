# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowStatusInstanceResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cpu_utils': 'list[ShowStatusInstanceItem]',
        'mem_utils': 'list[ShowStatusInstanceItem]',
        'disk_utils': 'list[ShowStatusInstanceItem]',
        'cpu_util_instance_names': 'list[str]',
        'mem_util_instance_names': 'list[str]',
        'disk_util_instance_names': 'list[str]',
        'cpu_util_averages': 'list[float]',
        'mem_util_averages': 'list[float]',
        'disk_util_averages': 'list[float]'
    }

    attribute_map = {
        'cpu_utils': 'cpu_utils',
        'mem_utils': 'mem_utils',
        'disk_utils': 'disk_utils',
        'cpu_util_instance_names': 'cpu_util_instance_names',
        'mem_util_instance_names': 'mem_util_instance_names',
        'disk_util_instance_names': 'disk_util_instance_names',
        'cpu_util_averages': 'cpu_util_averages',
        'mem_util_averages': 'mem_util_averages',
        'disk_util_averages': 'disk_util_averages'
    }

    def __init__(self, cpu_utils=None, mem_utils=None, disk_utils=None, cpu_util_instance_names=None, mem_util_instance_names=None, disk_util_instance_names=None, cpu_util_averages=None, mem_util_averages=None, disk_util_averages=None):
        r"""ShowStatusInstanceResponse

        The model defined in huaweicloud sdk

        :param cpu_utils: CPU使用率
        :type cpu_utils: list[:class:`huaweicloudsdkcpcs.v1.ShowStatusInstanceItem`]
        :param mem_utils: 内存使用率
        :type mem_utils: list[:class:`huaweicloudsdkcpcs.v1.ShowStatusInstanceItem`]
        :param disk_utils: 磁盘使用率
        :type disk_utils: list[:class:`huaweicloudsdkcpcs.v1.ShowStatusInstanceItem`]
        :param cpu_util_instance_names: CPU使用率对应实例名称
        :type cpu_util_instance_names: list[str]
        :param mem_util_instance_names: 内存使用率对应实例名称
        :type mem_util_instance_names: list[str]
        :param disk_util_instance_names: 磁盘使用率对应实例名称
        :type disk_util_instance_names: list[str]
        :param cpu_util_averages: CPU使用率平均值
        :type cpu_util_averages: list[float]
        :param mem_util_averages: 内存使用率平均值
        :type mem_util_averages: list[float]
        :param disk_util_averages: 磁盘使用率平均值
        :type disk_util_averages: list[float]
        """
        
        super().__init__()

        self._cpu_utils = None
        self._mem_utils = None
        self._disk_utils = None
        self._cpu_util_instance_names = None
        self._mem_util_instance_names = None
        self._disk_util_instance_names = None
        self._cpu_util_averages = None
        self._mem_util_averages = None
        self._disk_util_averages = None
        self.discriminator = None

        if cpu_utils is not None:
            self.cpu_utils = cpu_utils
        if mem_utils is not None:
            self.mem_utils = mem_utils
        if disk_utils is not None:
            self.disk_utils = disk_utils
        if cpu_util_instance_names is not None:
            self.cpu_util_instance_names = cpu_util_instance_names
        if mem_util_instance_names is not None:
            self.mem_util_instance_names = mem_util_instance_names
        if disk_util_instance_names is not None:
            self.disk_util_instance_names = disk_util_instance_names
        if cpu_util_averages is not None:
            self.cpu_util_averages = cpu_util_averages
        if mem_util_averages is not None:
            self.mem_util_averages = mem_util_averages
        if disk_util_averages is not None:
            self.disk_util_averages = disk_util_averages

    @property
    def cpu_utils(self):
        r"""Gets the cpu_utils of this ShowStatusInstanceResponse.

        CPU使用率

        :return: The cpu_utils of this ShowStatusInstanceResponse.
        :rtype: list[:class:`huaweicloudsdkcpcs.v1.ShowStatusInstanceItem`]
        """
        return self._cpu_utils

    @cpu_utils.setter
    def cpu_utils(self, cpu_utils):
        r"""Sets the cpu_utils of this ShowStatusInstanceResponse.

        CPU使用率

        :param cpu_utils: The cpu_utils of this ShowStatusInstanceResponse.
        :type cpu_utils: list[:class:`huaweicloudsdkcpcs.v1.ShowStatusInstanceItem`]
        """
        self._cpu_utils = cpu_utils

    @property
    def mem_utils(self):
        r"""Gets the mem_utils of this ShowStatusInstanceResponse.

        内存使用率

        :return: The mem_utils of this ShowStatusInstanceResponse.
        :rtype: list[:class:`huaweicloudsdkcpcs.v1.ShowStatusInstanceItem`]
        """
        return self._mem_utils

    @mem_utils.setter
    def mem_utils(self, mem_utils):
        r"""Sets the mem_utils of this ShowStatusInstanceResponse.

        内存使用率

        :param mem_utils: The mem_utils of this ShowStatusInstanceResponse.
        :type mem_utils: list[:class:`huaweicloudsdkcpcs.v1.ShowStatusInstanceItem`]
        """
        self._mem_utils = mem_utils

    @property
    def disk_utils(self):
        r"""Gets the disk_utils of this ShowStatusInstanceResponse.

        磁盘使用率

        :return: The disk_utils of this ShowStatusInstanceResponse.
        :rtype: list[:class:`huaweicloudsdkcpcs.v1.ShowStatusInstanceItem`]
        """
        return self._disk_utils

    @disk_utils.setter
    def disk_utils(self, disk_utils):
        r"""Sets the disk_utils of this ShowStatusInstanceResponse.

        磁盘使用率

        :param disk_utils: The disk_utils of this ShowStatusInstanceResponse.
        :type disk_utils: list[:class:`huaweicloudsdkcpcs.v1.ShowStatusInstanceItem`]
        """
        self._disk_utils = disk_utils

    @property
    def cpu_util_instance_names(self):
        r"""Gets the cpu_util_instance_names of this ShowStatusInstanceResponse.

        CPU使用率对应实例名称

        :return: The cpu_util_instance_names of this ShowStatusInstanceResponse.
        :rtype: list[str]
        """
        return self._cpu_util_instance_names

    @cpu_util_instance_names.setter
    def cpu_util_instance_names(self, cpu_util_instance_names):
        r"""Sets the cpu_util_instance_names of this ShowStatusInstanceResponse.

        CPU使用率对应实例名称

        :param cpu_util_instance_names: The cpu_util_instance_names of this ShowStatusInstanceResponse.
        :type cpu_util_instance_names: list[str]
        """
        self._cpu_util_instance_names = cpu_util_instance_names

    @property
    def mem_util_instance_names(self):
        r"""Gets the mem_util_instance_names of this ShowStatusInstanceResponse.

        内存使用率对应实例名称

        :return: The mem_util_instance_names of this ShowStatusInstanceResponse.
        :rtype: list[str]
        """
        return self._mem_util_instance_names

    @mem_util_instance_names.setter
    def mem_util_instance_names(self, mem_util_instance_names):
        r"""Sets the mem_util_instance_names of this ShowStatusInstanceResponse.

        内存使用率对应实例名称

        :param mem_util_instance_names: The mem_util_instance_names of this ShowStatusInstanceResponse.
        :type mem_util_instance_names: list[str]
        """
        self._mem_util_instance_names = mem_util_instance_names

    @property
    def disk_util_instance_names(self):
        r"""Gets the disk_util_instance_names of this ShowStatusInstanceResponse.

        磁盘使用率对应实例名称

        :return: The disk_util_instance_names of this ShowStatusInstanceResponse.
        :rtype: list[str]
        """
        return self._disk_util_instance_names

    @disk_util_instance_names.setter
    def disk_util_instance_names(self, disk_util_instance_names):
        r"""Sets the disk_util_instance_names of this ShowStatusInstanceResponse.

        磁盘使用率对应实例名称

        :param disk_util_instance_names: The disk_util_instance_names of this ShowStatusInstanceResponse.
        :type disk_util_instance_names: list[str]
        """
        self._disk_util_instance_names = disk_util_instance_names

    @property
    def cpu_util_averages(self):
        r"""Gets the cpu_util_averages of this ShowStatusInstanceResponse.

        CPU使用率平均值

        :return: The cpu_util_averages of this ShowStatusInstanceResponse.
        :rtype: list[float]
        """
        return self._cpu_util_averages

    @cpu_util_averages.setter
    def cpu_util_averages(self, cpu_util_averages):
        r"""Sets the cpu_util_averages of this ShowStatusInstanceResponse.

        CPU使用率平均值

        :param cpu_util_averages: The cpu_util_averages of this ShowStatusInstanceResponse.
        :type cpu_util_averages: list[float]
        """
        self._cpu_util_averages = cpu_util_averages

    @property
    def mem_util_averages(self):
        r"""Gets the mem_util_averages of this ShowStatusInstanceResponse.

        内存使用率平均值

        :return: The mem_util_averages of this ShowStatusInstanceResponse.
        :rtype: list[float]
        """
        return self._mem_util_averages

    @mem_util_averages.setter
    def mem_util_averages(self, mem_util_averages):
        r"""Sets the mem_util_averages of this ShowStatusInstanceResponse.

        内存使用率平均值

        :param mem_util_averages: The mem_util_averages of this ShowStatusInstanceResponse.
        :type mem_util_averages: list[float]
        """
        self._mem_util_averages = mem_util_averages

    @property
    def disk_util_averages(self):
        r"""Gets the disk_util_averages of this ShowStatusInstanceResponse.

        磁盘使用率平均值

        :return: The disk_util_averages of this ShowStatusInstanceResponse.
        :rtype: list[float]
        """
        return self._disk_util_averages

    @disk_util_averages.setter
    def disk_util_averages(self, disk_util_averages):
        r"""Sets the disk_util_averages of this ShowStatusInstanceResponse.

        磁盘使用率平均值

        :param disk_util_averages: The disk_util_averages of this ShowStatusInstanceResponse.
        :type disk_util_averages: list[float]
        """
        self._disk_util_averages = disk_util_averages

    def to_dict(self):
        import warnings
        warnings.warn("ShowStatusInstanceResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowStatusInstanceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
