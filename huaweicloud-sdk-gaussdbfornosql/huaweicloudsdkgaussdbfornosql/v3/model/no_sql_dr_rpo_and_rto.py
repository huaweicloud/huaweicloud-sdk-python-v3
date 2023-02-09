# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NoSQLDrRpoAndRto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'scene': 'str',
        'rpo': 'int',
        'rto': 'int'
    }

    attribute_map = {
        'scene': 'scene',
        'rpo': 'rpo',
        'rto': 'rto'
    }

    def __init__(self, scene=None, rpo=None, rto=None):
        """NoSQLDrRpoAndRto

        The model defined in huaweicloud sdk

        :param scene: 场景，枚举值   FAILOVER 强制切换;    SWITCHOVER 主备倒换
        :type scene: str
        :param rpo: 倒换或切换丢失数据时长，单位：秒（s）
        :type rpo: int
        :param rto: 倒换或切换恢复时长，单位：秒（s）
        :type rto: int
        """
        
        

        self._scene = None
        self._rpo = None
        self._rto = None
        self.discriminator = None

        self.scene = scene
        if rpo is not None:
            self.rpo = rpo
        if rto is not None:
            self.rto = rto

    @property
    def scene(self):
        """Gets the scene of this NoSQLDrRpoAndRto.

        场景，枚举值   FAILOVER 强制切换;    SWITCHOVER 主备倒换

        :return: The scene of this NoSQLDrRpoAndRto.
        :rtype: str
        """
        return self._scene

    @scene.setter
    def scene(self, scene):
        """Sets the scene of this NoSQLDrRpoAndRto.

        场景，枚举值   FAILOVER 强制切换;    SWITCHOVER 主备倒换

        :param scene: The scene of this NoSQLDrRpoAndRto.
        :type scene: str
        """
        self._scene = scene

    @property
    def rpo(self):
        """Gets the rpo of this NoSQLDrRpoAndRto.

        倒换或切换丢失数据时长，单位：秒（s）

        :return: The rpo of this NoSQLDrRpoAndRto.
        :rtype: int
        """
        return self._rpo

    @rpo.setter
    def rpo(self, rpo):
        """Sets the rpo of this NoSQLDrRpoAndRto.

        倒换或切换丢失数据时长，单位：秒（s）

        :param rpo: The rpo of this NoSQLDrRpoAndRto.
        :type rpo: int
        """
        self._rpo = rpo

    @property
    def rto(self):
        """Gets the rto of this NoSQLDrRpoAndRto.

        倒换或切换恢复时长，单位：秒（s）

        :return: The rto of this NoSQLDrRpoAndRto.
        :rtype: int
        """
        return self._rto

    @rto.setter
    def rto(self, rto):
        """Sets the rto of this NoSQLDrRpoAndRto.

        倒换或切换恢复时长，单位：秒（s）

        :param rto: The rto of this NoSQLDrRpoAndRto.
        :type rto: int
        """
        self._rto = rto

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
        if not isinstance(other, NoSQLDrRpoAndRto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
