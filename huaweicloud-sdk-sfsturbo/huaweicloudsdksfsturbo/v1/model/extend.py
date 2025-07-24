# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Extend:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'new_size': 'int',
        'new_bandwidth': 'int',
        'bss_param': 'BssInfoExtend'
    }

    attribute_map = {
        'new_size': 'new_size',
        'new_bandwidth': 'new_bandwidth',
        'bss_param': 'bss_param'
    }

    def __init__(self, new_size=None, new_bandwidth=None, bss_param=None):
        r"""Extend

        The model defined in huaweicloud sdk

        :param new_size: 扩容后文件系统的新容量，以GiB为单位。  SFS Turbo上一代文件系统规格类型-标准型和性能型，取值范围500~32768 GiB，扩容步长大于等于100 GiB。  SFS Turbo上一代文件系统规格类型-标准型增强版和性能型增强版。容量范围是10240~327680 GiB。扩容步长大于等于100 GiB。  20MB/s/TiB，容量范围是3686~1048576 GiB。容量必须为1.2TiB的倍数，扩容步长需要大于等于1.2TiB，需要将目标容量换算为GiB后需要向下取整。如4.8TiB-&gt;4915GiB，8.4TiB-&gt;8601GiB。  40MB/s/TiB，容量范围是1228~1048576 GiB。容量必须为1.2TiB的倍数，扩容步长需要大于等于1.2TiB，需要将目标容量换算为GiB后需要向下取整。如4.8TiB-&gt;4915GiB，8.4TiB-&gt;8601GiB。  125MB/s/TiB、250MB/s/TiB、500MB/s/TiB、1000MB/s/TiB与40MB/s/TiB的容量范围，扩容步长相同。  HPC缓存型文件系统，容量范围是4096~1048576 GiB。扩容步长均为1TiB。需要将目标容量换算为GiB。 
        :type new_size: int
        :param new_bandwidth: 带宽的目标值，单位：GB。仅HPC缓存型支持带宽扩缩。 支持的带宽值为：2、4、8、16、24、32、48。 
        :type new_bandwidth: int
        :param bss_param: 
        :type bss_param: :class:`huaweicloudsdksfsturbo.v1.BssInfoExtend`
        """
        
        

        self._new_size = None
        self._new_bandwidth = None
        self._bss_param = None
        self.discriminator = None

        self.new_size = new_size
        if new_bandwidth is not None:
            self.new_bandwidth = new_bandwidth
        if bss_param is not None:
            self.bss_param = bss_param

    @property
    def new_size(self):
        r"""Gets the new_size of this Extend.

        扩容后文件系统的新容量，以GiB为单位。  SFS Turbo上一代文件系统规格类型-标准型和性能型，取值范围500~32768 GiB，扩容步长大于等于100 GiB。  SFS Turbo上一代文件系统规格类型-标准型增强版和性能型增强版。容量范围是10240~327680 GiB。扩容步长大于等于100 GiB。  20MB/s/TiB，容量范围是3686~1048576 GiB。容量必须为1.2TiB的倍数，扩容步长需要大于等于1.2TiB，需要将目标容量换算为GiB后需要向下取整。如4.8TiB->4915GiB，8.4TiB->8601GiB。  40MB/s/TiB，容量范围是1228~1048576 GiB。容量必须为1.2TiB的倍数，扩容步长需要大于等于1.2TiB，需要将目标容量换算为GiB后需要向下取整。如4.8TiB->4915GiB，8.4TiB->8601GiB。  125MB/s/TiB、250MB/s/TiB、500MB/s/TiB、1000MB/s/TiB与40MB/s/TiB的容量范围，扩容步长相同。  HPC缓存型文件系统，容量范围是4096~1048576 GiB。扩容步长均为1TiB。需要将目标容量换算为GiB。 

        :return: The new_size of this Extend.
        :rtype: int
        """
        return self._new_size

    @new_size.setter
    def new_size(self, new_size):
        r"""Sets the new_size of this Extend.

        扩容后文件系统的新容量，以GiB为单位。  SFS Turbo上一代文件系统规格类型-标准型和性能型，取值范围500~32768 GiB，扩容步长大于等于100 GiB。  SFS Turbo上一代文件系统规格类型-标准型增强版和性能型增强版。容量范围是10240~327680 GiB。扩容步长大于等于100 GiB。  20MB/s/TiB，容量范围是3686~1048576 GiB。容量必须为1.2TiB的倍数，扩容步长需要大于等于1.2TiB，需要将目标容量换算为GiB后需要向下取整。如4.8TiB->4915GiB，8.4TiB->8601GiB。  40MB/s/TiB，容量范围是1228~1048576 GiB。容量必须为1.2TiB的倍数，扩容步长需要大于等于1.2TiB，需要将目标容量换算为GiB后需要向下取整。如4.8TiB->4915GiB，8.4TiB->8601GiB。  125MB/s/TiB、250MB/s/TiB、500MB/s/TiB、1000MB/s/TiB与40MB/s/TiB的容量范围，扩容步长相同。  HPC缓存型文件系统，容量范围是4096~1048576 GiB。扩容步长均为1TiB。需要将目标容量换算为GiB。 

        :param new_size: The new_size of this Extend.
        :type new_size: int
        """
        self._new_size = new_size

    @property
    def new_bandwidth(self):
        r"""Gets the new_bandwidth of this Extend.

        带宽的目标值，单位：GB。仅HPC缓存型支持带宽扩缩。 支持的带宽值为：2、4、8、16、24、32、48。 

        :return: The new_bandwidth of this Extend.
        :rtype: int
        """
        return self._new_bandwidth

    @new_bandwidth.setter
    def new_bandwidth(self, new_bandwidth):
        r"""Sets the new_bandwidth of this Extend.

        带宽的目标值，单位：GB。仅HPC缓存型支持带宽扩缩。 支持的带宽值为：2、4、8、16、24、32、48。 

        :param new_bandwidth: The new_bandwidth of this Extend.
        :type new_bandwidth: int
        """
        self._new_bandwidth = new_bandwidth

    @property
    def bss_param(self):
        r"""Gets the bss_param of this Extend.

        :return: The bss_param of this Extend.
        :rtype: :class:`huaweicloudsdksfsturbo.v1.BssInfoExtend`
        """
        return self._bss_param

    @bss_param.setter
    def bss_param(self, bss_param):
        r"""Sets the bss_param of this Extend.

        :param bss_param: The bss_param of this Extend.
        :type bss_param: :class:`huaweicloudsdksfsturbo.v1.BssInfoExtend`
        """
        self._bss_param = bss_param

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
        if not isinstance(other, Extend):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
