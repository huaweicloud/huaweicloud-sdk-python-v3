# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterAuthTros:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable': 'bool',
        'auth_type': 'float',
        'expire_time': 'float'
    }

    attribute_map = {
        'enable': 'enable',
        'auth_type': 'auth_type',
        'expire_time': 'expire_time'
    }

    def __init__(self, enable=None, auth_type=None, expire_time=None):
        r"""ClusterAuthTros

        The model defined in huaweicloud sdk

        :param enable: 操作界面授权开启或关闭
        :type enable: bool
        :param auth_type: 0为集群界面授权功能的普通授权
        :type auth_type: float
        :param expire_time: enable为true时配置，即授权截止时间，如不传该值默认为7天授权时间
        :type expire_time: float
        """
        
        

        self._enable = None
        self._auth_type = None
        self._expire_time = None
        self.discriminator = None

        self.enable = enable
        self.auth_type = auth_type
        if expire_time is not None:
            self.expire_time = expire_time

    @property
    def enable(self):
        r"""Gets the enable of this ClusterAuthTros.

        操作界面授权开启或关闭

        :return: The enable of this ClusterAuthTros.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this ClusterAuthTros.

        操作界面授权开启或关闭

        :param enable: The enable of this ClusterAuthTros.
        :type enable: bool
        """
        self._enable = enable

    @property
    def auth_type(self):
        r"""Gets the auth_type of this ClusterAuthTros.

        0为集群界面授权功能的普通授权

        :return: The auth_type of this ClusterAuthTros.
        :rtype: float
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        r"""Sets the auth_type of this ClusterAuthTros.

        0为集群界面授权功能的普通授权

        :param auth_type: The auth_type of this ClusterAuthTros.
        :type auth_type: float
        """
        self._auth_type = auth_type

    @property
    def expire_time(self):
        r"""Gets the expire_time of this ClusterAuthTros.

        enable为true时配置，即授权截止时间，如不传该值默认为7天授权时间

        :return: The expire_time of this ClusterAuthTros.
        :rtype: float
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        r"""Sets the expire_time of this ClusterAuthTros.

        enable为true时配置，即授权截止时间，如不传该值默认为7天授权时间

        :param expire_time: The expire_time of this ClusterAuthTros.
        :type expire_time: float
        """
        self._expire_time = expire_time

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ClusterAuthTros):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
