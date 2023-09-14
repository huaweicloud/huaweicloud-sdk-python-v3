# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyVolumeQoSOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'iops': 'int',
        'throughput': 'int'
    }

    attribute_map = {
        'iops': 'iops',
        'throughput': 'throughput'
    }

    def __init__(self, iops=None, throughput=None):
        """ModifyVolumeQoSOption

        The model defined in huaweicloud sdk

        :param iops: 修改后的云硬盘iops，只支持GPSSD2、ESSD2类型的云硬盘。  说明： 了解GPSSD2、ESSD2类型的iops大小范围，请参见 [云硬盘类型及性能介绍里面的云硬盘性能数据表](https://support.huaweicloud.com/productdesc-evs/zh-cn_topic_0044524691.html)。
        :type iops: int
        :param throughput: 修改后的云硬盘吞吐量，单位是MiB/s，GPSSD2类型云盘必须填写，其他类型不能填写。  说明： 了解GPSSD2类型的吞吐量大小范围，请参见 [云硬盘类型及性能介绍里面的云硬盘性能数据表](https://support.huaweicloud.com/productdesc-evs/zh-cn_topic_0044524691.html)。
        :type throughput: int
        """
        
        

        self._iops = None
        self._throughput = None
        self.discriminator = None

        self.iops = iops
        if throughput is not None:
            self.throughput = throughput

    @property
    def iops(self):
        """Gets the iops of this ModifyVolumeQoSOption.

        修改后的云硬盘iops，只支持GPSSD2、ESSD2类型的云硬盘。  说明： 了解GPSSD2、ESSD2类型的iops大小范围，请参见 [云硬盘类型及性能介绍里面的云硬盘性能数据表](https://support.huaweicloud.com/productdesc-evs/zh-cn_topic_0044524691.html)。

        :return: The iops of this ModifyVolumeQoSOption.
        :rtype: int
        """
        return self._iops

    @iops.setter
    def iops(self, iops):
        """Sets the iops of this ModifyVolumeQoSOption.

        修改后的云硬盘iops，只支持GPSSD2、ESSD2类型的云硬盘。  说明： 了解GPSSD2、ESSD2类型的iops大小范围，请参见 [云硬盘类型及性能介绍里面的云硬盘性能数据表](https://support.huaweicloud.com/productdesc-evs/zh-cn_topic_0044524691.html)。

        :param iops: The iops of this ModifyVolumeQoSOption.
        :type iops: int
        """
        self._iops = iops

    @property
    def throughput(self):
        """Gets the throughput of this ModifyVolumeQoSOption.

        修改后的云硬盘吞吐量，单位是MiB/s，GPSSD2类型云盘必须填写，其他类型不能填写。  说明： 了解GPSSD2类型的吞吐量大小范围，请参见 [云硬盘类型及性能介绍里面的云硬盘性能数据表](https://support.huaweicloud.com/productdesc-evs/zh-cn_topic_0044524691.html)。

        :return: The throughput of this ModifyVolumeQoSOption.
        :rtype: int
        """
        return self._throughput

    @throughput.setter
    def throughput(self, throughput):
        """Sets the throughput of this ModifyVolumeQoSOption.

        修改后的云硬盘吞吐量，单位是MiB/s，GPSSD2类型云盘必须填写，其他类型不能填写。  说明： 了解GPSSD2类型的吞吐量大小范围，请参见 [云硬盘类型及性能介绍里面的云硬盘性能数据表](https://support.huaweicloud.com/productdesc-evs/zh-cn_topic_0044524691.html)。

        :param throughput: The throughput of this ModifyVolumeQoSOption.
        :type throughput: int
        """
        self._throughput = throughput

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
        if not isinstance(other, ModifyVolumeQoSOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
