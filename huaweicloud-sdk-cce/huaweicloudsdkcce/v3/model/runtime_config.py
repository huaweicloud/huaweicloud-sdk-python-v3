# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RuntimeConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'lv_type': 'str'
    }

    attribute_map = {
        'lv_type': 'lvType'
    }

    def __init__(self, lv_type=None):
        """RuntimeConfig

        The model defined in huaweicloud sdk

        :param lv_type: LVM写入模式：linear、striped。linear：线性模式；striped：条带模式，使用多块磁盘组成条带模式，能够提升磁盘性能。
        :type lv_type: str
        """
        
        

        self._lv_type = None
        self.discriminator = None

        self.lv_type = lv_type

    @property
    def lv_type(self):
        """Gets the lv_type of this RuntimeConfig.

        LVM写入模式：linear、striped。linear：线性模式；striped：条带模式，使用多块磁盘组成条带模式，能够提升磁盘性能。

        :return: The lv_type of this RuntimeConfig.
        :rtype: str
        """
        return self._lv_type

    @lv_type.setter
    def lv_type(self, lv_type):
        """Sets the lv_type of this RuntimeConfig.

        LVM写入模式：linear、striped。linear：线性模式；striped：条带模式，使用多块磁盘组成条带模式，能够提升磁盘性能。

        :param lv_type: The lv_type of this RuntimeConfig.
        :type lv_type: str
        """
        self._lv_type = lv_type

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
        if not isinstance(other, RuntimeConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
