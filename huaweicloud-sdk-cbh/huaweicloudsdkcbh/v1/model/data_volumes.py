# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataVolumes:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'volume_type': 'str',
        'size': 'str',
        'extend_param': 'str'
    }

    attribute_map = {
        'volume_type': 'volume_type',
        'size': 'size',
        'extend_param': 'extend_param'
    }

    def __init__(self, volume_type=None, size=None, extend_param=None):
        """DataVolumes

        The model defined in huaweicloud sdk

        :param volume_type: 对应的系统盘类型 SAS SATA SSD
        :type volume_type: str
        :param size: 系统盘大小，容量单位为GB，输入大 小范围为[1-1024]
        :type size: str
        :param extend_param: 磁盘产品信息
        :type extend_param: str
        """
        
        

        self._volume_type = None
        self._size = None
        self._extend_param = None
        self.discriminator = None

        self.volume_type = volume_type
        self.size = size
        self.extend_param = extend_param

    @property
    def volume_type(self):
        """Gets the volume_type of this DataVolumes.

        对应的系统盘类型 SAS SATA SSD

        :return: The volume_type of this DataVolumes.
        :rtype: str
        """
        return self._volume_type

    @volume_type.setter
    def volume_type(self, volume_type):
        """Sets the volume_type of this DataVolumes.

        对应的系统盘类型 SAS SATA SSD

        :param volume_type: The volume_type of this DataVolumes.
        :type volume_type: str
        """
        self._volume_type = volume_type

    @property
    def size(self):
        """Gets the size of this DataVolumes.

        系统盘大小，容量单位为GB，输入大 小范围为[1-1024]

        :return: The size of this DataVolumes.
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this DataVolumes.

        系统盘大小，容量单位为GB，输入大 小范围为[1-1024]

        :param size: The size of this DataVolumes.
        :type size: str
        """
        self._size = size

    @property
    def extend_param(self):
        """Gets the extend_param of this DataVolumes.

        磁盘产品信息

        :return: The extend_param of this DataVolumes.
        :rtype: str
        """
        return self._extend_param

    @extend_param.setter
    def extend_param(self, extend_param):
        """Sets the extend_param of this DataVolumes.

        磁盘产品信息

        :param extend_param: The extend_param of this DataVolumes.
        :type extend_param: str
        """
        self._extend_param = extend_param

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
        if not isinstance(other, DataVolumes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
