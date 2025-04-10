# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RetypeVolume:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'new_type': 'str',
        'iops': 'int',
        'throughput': 'int'
    }

    attribute_map = {
        'new_type': 'new_type',
        'iops': 'iops',
        'throughput': 'throughput'
    }

    def __init__(self, new_type=None, iops=None, throughput=None):
        r"""RetypeVolume

        The model defined in huaweicloud sdk

        :param new_type: 变更至指定的云硬盘类型
        :type new_type: str
        :param iops: 云硬盘iops大小。
        :type iops: int
        :param throughput: 云硬盘的吞吐量大小。
        :type throughput: int
        """
        
        

        self._new_type = None
        self._iops = None
        self._throughput = None
        self.discriminator = None

        self.new_type = new_type
        if iops is not None:
            self.iops = iops
        if throughput is not None:
            self.throughput = throughput

    @property
    def new_type(self):
        r"""Gets the new_type of this RetypeVolume.

        变更至指定的云硬盘类型

        :return: The new_type of this RetypeVolume.
        :rtype: str
        """
        return self._new_type

    @new_type.setter
    def new_type(self, new_type):
        r"""Sets the new_type of this RetypeVolume.

        变更至指定的云硬盘类型

        :param new_type: The new_type of this RetypeVolume.
        :type new_type: str
        """
        self._new_type = new_type

    @property
    def iops(self):
        r"""Gets the iops of this RetypeVolume.

        云硬盘iops大小。

        :return: The iops of this RetypeVolume.
        :rtype: int
        """
        return self._iops

    @iops.setter
    def iops(self, iops):
        r"""Sets the iops of this RetypeVolume.

        云硬盘iops大小。

        :param iops: The iops of this RetypeVolume.
        :type iops: int
        """
        self._iops = iops

    @property
    def throughput(self):
        r"""Gets the throughput of this RetypeVolume.

        云硬盘的吞吐量大小。

        :return: The throughput of this RetypeVolume.
        :rtype: int
        """
        return self._throughput

    @throughput.setter
    def throughput(self, throughput):
        r"""Sets the throughput of this RetypeVolume.

        云硬盘的吞吐量大小。

        :param throughput: The throughput of this RetypeVolume.
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
        if not isinstance(other, RetypeVolume):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
