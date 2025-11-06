# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateRouteRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'configtype': 'str',
        'configkey': 'str',
        'configvalue': 'str'
    }

    attribute_map = {
        'configtype': 'configtype',
        'configkey': 'configkey',
        'configvalue': 'configvalue'
    }

    def __init__(self, configtype=None, configkey=None, configvalue=None):
        r"""UpdateRouteRequestBody

        The model defined in huaweicloud sdk

        :param configtype: 操作类型。add_ip为增加集群路由，del_ip为删除集群路由。
        :type configtype: str
        :param configkey: 路由ip地址，公网源数据所在的服务器ip。不能以0开头。
        :type configkey: str
        :param configvalue: 路由子网掩码。如果上面ip取的是16位，子网掩码可以填255.255.0.0，24位的话子网掩码填255.255.255.0
        :type configvalue: str
        """
        
        

        self._configtype = None
        self._configkey = None
        self._configvalue = None
        self.discriminator = None

        self.configtype = configtype
        self.configkey = configkey
        self.configvalue = configvalue

    @property
    def configtype(self):
        r"""Gets the configtype of this UpdateRouteRequestBody.

        操作类型。add_ip为增加集群路由，del_ip为删除集群路由。

        :return: The configtype of this UpdateRouteRequestBody.
        :rtype: str
        """
        return self._configtype

    @configtype.setter
    def configtype(self, configtype):
        r"""Sets the configtype of this UpdateRouteRequestBody.

        操作类型。add_ip为增加集群路由，del_ip为删除集群路由。

        :param configtype: The configtype of this UpdateRouteRequestBody.
        :type configtype: str
        """
        self._configtype = configtype

    @property
    def configkey(self):
        r"""Gets the configkey of this UpdateRouteRequestBody.

        路由ip地址，公网源数据所在的服务器ip。不能以0开头。

        :return: The configkey of this UpdateRouteRequestBody.
        :rtype: str
        """
        return self._configkey

    @configkey.setter
    def configkey(self, configkey):
        r"""Sets the configkey of this UpdateRouteRequestBody.

        路由ip地址，公网源数据所在的服务器ip。不能以0开头。

        :param configkey: The configkey of this UpdateRouteRequestBody.
        :type configkey: str
        """
        self._configkey = configkey

    @property
    def configvalue(self):
        r"""Gets the configvalue of this UpdateRouteRequestBody.

        路由子网掩码。如果上面ip取的是16位，子网掩码可以填255.255.0.0，24位的话子网掩码填255.255.255.0

        :return: The configvalue of this UpdateRouteRequestBody.
        :rtype: str
        """
        return self._configvalue

    @configvalue.setter
    def configvalue(self, configvalue):
        r"""Sets the configvalue of this UpdateRouteRequestBody.

        路由子网掩码。如果上面ip取的是16位，子网掩码可以填255.255.0.0，24位的话子网掩码填255.255.255.0

        :param configvalue: The configvalue of this UpdateRouteRequestBody.
        :type configvalue: str
        """
        self._configvalue = configvalue

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
        if not isinstance(other, UpdateRouteRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
