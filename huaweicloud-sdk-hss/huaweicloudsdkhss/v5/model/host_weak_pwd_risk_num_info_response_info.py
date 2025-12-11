# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HostWeakPwdRiskNumInfoResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_id': 'str',
        'host_name': 'str',
        'host_ip': 'str',
        'weak_pwd_num': 'int'
    }

    attribute_map = {
        'host_id': 'host_id',
        'host_name': 'host_name',
        'host_ip': 'host_ip',
        'weak_pwd_num': 'weak_pwd_num'
    }

    def __init__(self, host_id=None, host_name=None, host_ip=None, weak_pwd_num=None):
        r"""HostWeakPwdRiskNumInfoResponseInfo

        The model defined in huaweicloud sdk

        :param host_id: **参数解释**： 服务器（主机）的唯一标识ID **取值范围**： 字符长度1-64位 
        :type host_id: str
        :param host_name: **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 
        :type host_name: str
        :param host_ip: **参数解释**: 服务器IP **取值范围**: 字符长度1-128位 
        :type host_ip: str
        :param weak_pwd_num: **参数解释**: 弱口令数量。 **取值范围**: 取值0-2147483647 
        :type weak_pwd_num: int
        """
        
        

        self._host_id = None
        self._host_name = None
        self._host_ip = None
        self._weak_pwd_num = None
        self.discriminator = None

        if host_id is not None:
            self.host_id = host_id
        if host_name is not None:
            self.host_name = host_name
        if host_ip is not None:
            self.host_ip = host_ip
        if weak_pwd_num is not None:
            self.weak_pwd_num = weak_pwd_num

    @property
    def host_id(self):
        r"""Gets the host_id of this HostWeakPwdRiskNumInfoResponseInfo.

        **参数解释**： 服务器（主机）的唯一标识ID **取值范围**： 字符长度1-64位 

        :return: The host_id of this HostWeakPwdRiskNumInfoResponseInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this HostWeakPwdRiskNumInfoResponseInfo.

        **参数解释**： 服务器（主机）的唯一标识ID **取值范围**： 字符长度1-64位 

        :param host_id: The host_id of this HostWeakPwdRiskNumInfoResponseInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_name(self):
        r"""Gets the host_name of this HostWeakPwdRiskNumInfoResponseInfo.

        **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 

        :return: The host_name of this HostWeakPwdRiskNumInfoResponseInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this HostWeakPwdRiskNumInfoResponseInfo.

        **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 

        :param host_name: The host_name of this HostWeakPwdRiskNumInfoResponseInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_ip(self):
        r"""Gets the host_ip of this HostWeakPwdRiskNumInfoResponseInfo.

        **参数解释**: 服务器IP **取值范围**: 字符长度1-128位 

        :return: The host_ip of this HostWeakPwdRiskNumInfoResponseInfo.
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        r"""Sets the host_ip of this HostWeakPwdRiskNumInfoResponseInfo.

        **参数解释**: 服务器IP **取值范围**: 字符长度1-128位 

        :param host_ip: The host_ip of this HostWeakPwdRiskNumInfoResponseInfo.
        :type host_ip: str
        """
        self._host_ip = host_ip

    @property
    def weak_pwd_num(self):
        r"""Gets the weak_pwd_num of this HostWeakPwdRiskNumInfoResponseInfo.

        **参数解释**: 弱口令数量。 **取值范围**: 取值0-2147483647 

        :return: The weak_pwd_num of this HostWeakPwdRiskNumInfoResponseInfo.
        :rtype: int
        """
        return self._weak_pwd_num

    @weak_pwd_num.setter
    def weak_pwd_num(self, weak_pwd_num):
        r"""Sets the weak_pwd_num of this HostWeakPwdRiskNumInfoResponseInfo.

        **参数解释**: 弱口令数量。 **取值范围**: 取值0-2147483647 

        :param weak_pwd_num: The weak_pwd_num of this HostWeakPwdRiskNumInfoResponseInfo.
        :type weak_pwd_num: int
        """
        self._weak_pwd_num = weak_pwd_num

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
        if not isinstance(other, HostWeakPwdRiskNumInfoResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
