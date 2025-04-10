# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateClusterInstanceVolumeBody:

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
        'size': 'int'
    }

    attribute_map = {
        'volume_type': 'volume_type',
        'size': 'size'
    }

    def __init__(self, volume_type=None, size=None):
        r"""CreateClusterInstanceVolumeBody

        The model defined in huaweicloud sdk

        :param volume_type: 卷类型。  - COMMON：普通I/O。 - HIGH：高I/O。 - ULTRAHIGH：超高I/O。
        :type volume_type: str
        :param size: 卷大小，必须为大于0且为4和10的公倍数，磁盘规格大小可以通过[获取实例规格列表](ListFlavors.xml)中diskrange属性获得。 单位：GB。  &gt;ess-master节点和ess-client节点默认大小为40G，且不可更改。
        :type size: int
        """
        
        

        self._volume_type = None
        self._size = None
        self.discriminator = None

        self.volume_type = volume_type
        self.size = size

    @property
    def volume_type(self):
        r"""Gets the volume_type of this CreateClusterInstanceVolumeBody.

        卷类型。  - COMMON：普通I/O。 - HIGH：高I/O。 - ULTRAHIGH：超高I/O。

        :return: The volume_type of this CreateClusterInstanceVolumeBody.
        :rtype: str
        """
        return self._volume_type

    @volume_type.setter
    def volume_type(self, volume_type):
        r"""Sets the volume_type of this CreateClusterInstanceVolumeBody.

        卷类型。  - COMMON：普通I/O。 - HIGH：高I/O。 - ULTRAHIGH：超高I/O。

        :param volume_type: The volume_type of this CreateClusterInstanceVolumeBody.
        :type volume_type: str
        """
        self._volume_type = volume_type

    @property
    def size(self):
        r"""Gets the size of this CreateClusterInstanceVolumeBody.

        卷大小，必须为大于0且为4和10的公倍数，磁盘规格大小可以通过[获取实例规格列表](ListFlavors.xml)中diskrange属性获得。 单位：GB。  >ess-master节点和ess-client节点默认大小为40G，且不可更改。

        :return: The size of this CreateClusterInstanceVolumeBody.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this CreateClusterInstanceVolumeBody.

        卷大小，必须为大于0且为4和10的公倍数，磁盘规格大小可以通过[获取实例规格列表](ListFlavors.xml)中diskrange属性获得。 单位：GB。  >ess-master节点和ess-client节点默认大小为40G，且不可更改。

        :param size: The size of this CreateClusterInstanceVolumeBody.
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
        if not isinstance(other, CreateClusterInstanceVolumeBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
