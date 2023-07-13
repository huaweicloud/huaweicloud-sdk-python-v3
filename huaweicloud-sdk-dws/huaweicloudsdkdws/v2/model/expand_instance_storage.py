# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExpandInstanceStorage:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'new_size': 'int'
    }

    attribute_map = {
        'new_size': 'new_size'
    }

    def __init__(self, new_size=None):
        """ExpandInstanceStorage

        The model defined in huaweicloud sdk

        :param new_size: 磁盘扩容后单节点有效存储容量（GB / 节点）。该容量必须大于当前单节点有效容量，小于等于集群规格支持的单节点最大容量，扩容容量为规格支持的步长倍数。集群规格配置详情可根据“查询节点类型”查询。
        :type new_size: int
        """
        
        

        self._new_size = None
        self.discriminator = None

        self.new_size = new_size

    @property
    def new_size(self):
        """Gets the new_size of this ExpandInstanceStorage.

        磁盘扩容后单节点有效存储容量（GB / 节点）。该容量必须大于当前单节点有效容量，小于等于集群规格支持的单节点最大容量，扩容容量为规格支持的步长倍数。集群规格配置详情可根据“查询节点类型”查询。

        :return: The new_size of this ExpandInstanceStorage.
        :rtype: int
        """
        return self._new_size

    @new_size.setter
    def new_size(self, new_size):
        """Sets the new_size of this ExpandInstanceStorage.

        磁盘扩容后单节点有效存储容量（GB / 节点）。该容量必须大于当前单节点有效容量，小于等于集群规格支持的单节点最大容量，扩容容量为规格支持的步长倍数。集群规格配置详情可根据“查询节点类型”查询。

        :param new_size: The new_size of this ExpandInstanceStorage.
        :type new_size: int
        """
        self._new_size = new_size

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
        if not isinstance(other, ExpandInstanceStorage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
