# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpenGaussVolume:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'size': 'int'
    }

    attribute_map = {
        'type': 'type',
        'size': 'size'
    }

    def __init__(self, type=None, size=None):
        """OpenGaussVolume

        The model defined in huaweicloud sdk

        :param type: 磁盘类型。  仅支持ULTRAHIGH和ESSD，区分大小写，分别表示SSD和急速云盘。
        :type type: str
        :param size: 磁盘大小。例如：该参数填写为“40”，表示为创建的实例分配40GB的磁盘空间。  取值范围：（分片数*40GB）~（分片数*16TB），且大小只能为分片数*40的整数倍。
        :type size: int
        """
        
        

        self._type = None
        self._size = None
        self.discriminator = None

        self.type = type
        self.size = size

    @property
    def type(self):
        """Gets the type of this OpenGaussVolume.

        磁盘类型。  仅支持ULTRAHIGH和ESSD，区分大小写，分别表示SSD和急速云盘。

        :return: The type of this OpenGaussVolume.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OpenGaussVolume.

        磁盘类型。  仅支持ULTRAHIGH和ESSD，区分大小写，分别表示SSD和急速云盘。

        :param type: The type of this OpenGaussVolume.
        :type type: str
        """
        self._type = type

    @property
    def size(self):
        """Gets the size of this OpenGaussVolume.

        磁盘大小。例如：该参数填写为“40”，表示为创建的实例分配40GB的磁盘空间。  取值范围：（分片数*40GB）~（分片数*16TB），且大小只能为分片数*40的整数倍。

        :return: The size of this OpenGaussVolume.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this OpenGaussVolume.

        磁盘大小。例如：该参数填写为“40”，表示为创建的实例分配40GB的磁盘空间。  取值范围：（分片数*40GB）~（分片数*16TB），且大小只能为分片数*40的整数倍。

        :param size: The size of this OpenGaussVolume.
        :type size: int
        """
        self._size = size

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
        if not isinstance(other, OpenGaussVolume):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
