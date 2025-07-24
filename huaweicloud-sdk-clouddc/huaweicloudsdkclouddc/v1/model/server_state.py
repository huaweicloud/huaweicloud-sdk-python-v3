# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServerState:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'dc_stats': 'dict(str, int)'
    }

    attribute_map = {
        'count': 'count',
        'dc_stats': 'dc_stats'
    }

    def __init__(self, count=None, dc_stats=None):
        r"""ServerState

        The model defined in huaweicloud sdk

        :param count: 数量
        :type count: int
        :param dc_stats: 数据中心名称对应数量映射
        :type dc_stats: dict(str, int)
        """
        
        

        self._count = None
        self._dc_stats = None
        self.discriminator = None

        self.count = count
        self.dc_stats = dc_stats

    @property
    def count(self):
        r"""Gets the count of this ServerState.

        数量

        :return: The count of this ServerState.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ServerState.

        数量

        :param count: The count of this ServerState.
        :type count: int
        """
        self._count = count

    @property
    def dc_stats(self):
        r"""Gets the dc_stats of this ServerState.

        数据中心名称对应数量映射

        :return: The dc_stats of this ServerState.
        :rtype: dict(str, int)
        """
        return self._dc_stats

    @dc_stats.setter
    def dc_stats(self, dc_stats):
        r"""Sets the dc_stats of this ServerState.

        数据中心名称对应数量映射

        :param dc_stats: The dc_stats of this ServerState.
        :type dc_stats: dict(str, int)
        """
        self._dc_stats = dc_stats

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
        if not isinstance(other, ServerState):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
