# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SpecsConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offline': 'str',
        'nearline': 'str',
        'rank': 'str',
        'online_tps': 'int'
    }

    attribute_map = {
        'offline': 'offline',
        'nearline': 'nearline',
        'rank': 'rank',
        'online_tps': 'online_tps'
    }

    def __init__(self, offline=None, nearline=None, rank=None, online_tps=None):
        """SpecsConfig

        The model defined in huaweicloud sdk

        :param offline: 离线计算规格。
        :type offline: str
        :param nearline: 实时计算规格。
        :type nearline: str
        :param rank: 深度学习计算规格。
        :type rank: str
        :param online_tps: 在线服务最大并发数。
        :type online_tps: int
        """
        
        

        self._offline = None
        self._nearline = None
        self._rank = None
        self._online_tps = None
        self.discriminator = None

        self.offline = offline
        if nearline is not None:
            self.nearline = nearline
        if rank is not None:
            self.rank = rank
        if online_tps is not None:
            self.online_tps = online_tps

    @property
    def offline(self):
        """Gets the offline of this SpecsConfig.

        离线计算规格。

        :return: The offline of this SpecsConfig.
        :rtype: str
        """
        return self._offline

    @offline.setter
    def offline(self, offline):
        """Sets the offline of this SpecsConfig.

        离线计算规格。

        :param offline: The offline of this SpecsConfig.
        :type offline: str
        """
        self._offline = offline

    @property
    def nearline(self):
        """Gets the nearline of this SpecsConfig.

        实时计算规格。

        :return: The nearline of this SpecsConfig.
        :rtype: str
        """
        return self._nearline

    @nearline.setter
    def nearline(self, nearline):
        """Sets the nearline of this SpecsConfig.

        实时计算规格。

        :param nearline: The nearline of this SpecsConfig.
        :type nearline: str
        """
        self._nearline = nearline

    @property
    def rank(self):
        """Gets the rank of this SpecsConfig.

        深度学习计算规格。

        :return: The rank of this SpecsConfig.
        :rtype: str
        """
        return self._rank

    @rank.setter
    def rank(self, rank):
        """Sets the rank of this SpecsConfig.

        深度学习计算规格。

        :param rank: The rank of this SpecsConfig.
        :type rank: str
        """
        self._rank = rank

    @property
    def online_tps(self):
        """Gets the online_tps of this SpecsConfig.

        在线服务最大并发数。

        :return: The online_tps of this SpecsConfig.
        :rtype: int
        """
        return self._online_tps

    @online_tps.setter
    def online_tps(self, online_tps):
        """Sets the online_tps of this SpecsConfig.

        在线服务最大并发数。

        :param online_tps: The online_tps of this SpecsConfig.
        :type online_tps: int
        """
        self._online_tps = online_tps

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
        if not isinstance(other, SpecsConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
