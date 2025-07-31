# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WeakPwdListInfoResponseInfo:

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
        'private_ip': 'str',
        'public_ip': 'str',
        'update_time': 'int',
        'weak_pwd_accounts': 'list[WeakPwdAccountInfoResponseInfo]'
    }

    attribute_map = {
        'host_id': 'host_id',
        'host_name': 'host_name',
        'host_ip': 'host_ip',
        'private_ip': 'private_ip',
        'public_ip': 'public_ip',
        'update_time': 'update_time',
        'weak_pwd_accounts': 'weak_pwd_accounts'
    }

    def __init__(self, host_id=None, host_name=None, host_ip=None, private_ip=None, public_ip=None, update_time=None, weak_pwd_accounts=None):
        r"""WeakPwdListInfoResponseInfo

        The model defined in huaweicloud sdk

        :param host_id: **参数解释**: 主机ID **取值范围**: 不涉及 
        :type host_id: str
        :param host_name: **参数解释**: 服务器名称 **取值范围**: 不涉及 
        :type host_name: str
        :param host_ip: **参数解释**: 服务器IP（私有IP），为兼容用户使用，不删除此字段 **取值范围**: 不涉及 
        :type host_ip: str
        :param private_ip: **参数解释**: 服务器私有IP **取值范围**: 不涉及 
        :type private_ip: str
        :param public_ip: **参数解释**: 服务器公网IP **取值范围**: 不涉及 
        :type public_ip: str
        :param update_time: **参数解释**: 最近扫描时间，时间戳单位：毫秒 **取值范围**: 不涉及 
        :type update_time: int
        :param weak_pwd_accounts: **参数解释**: 弱口令账号列表 **取值范围**: 不涉及 
        :type weak_pwd_accounts: list[:class:`huaweicloudsdkhss.v5.WeakPwdAccountInfoResponseInfo`]
        """
        
        

        self._host_id = None
        self._host_name = None
        self._host_ip = None
        self._private_ip = None
        self._public_ip = None
        self._update_time = None
        self._weak_pwd_accounts = None
        self.discriminator = None

        if host_id is not None:
            self.host_id = host_id
        if host_name is not None:
            self.host_name = host_name
        if host_ip is not None:
            self.host_ip = host_ip
        if private_ip is not None:
            self.private_ip = private_ip
        if public_ip is not None:
            self.public_ip = public_ip
        if update_time is not None:
            self.update_time = update_time
        if weak_pwd_accounts is not None:
            self.weak_pwd_accounts = weak_pwd_accounts

    @property
    def host_id(self):
        r"""Gets the host_id of this WeakPwdListInfoResponseInfo.

        **参数解释**: 主机ID **取值范围**: 不涉及 

        :return: The host_id of this WeakPwdListInfoResponseInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this WeakPwdListInfoResponseInfo.

        **参数解释**: 主机ID **取值范围**: 不涉及 

        :param host_id: The host_id of this WeakPwdListInfoResponseInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_name(self):
        r"""Gets the host_name of this WeakPwdListInfoResponseInfo.

        **参数解释**: 服务器名称 **取值范围**: 不涉及 

        :return: The host_name of this WeakPwdListInfoResponseInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this WeakPwdListInfoResponseInfo.

        **参数解释**: 服务器名称 **取值范围**: 不涉及 

        :param host_name: The host_name of this WeakPwdListInfoResponseInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_ip(self):
        r"""Gets the host_ip of this WeakPwdListInfoResponseInfo.

        **参数解释**: 服务器IP（私有IP），为兼容用户使用，不删除此字段 **取值范围**: 不涉及 

        :return: The host_ip of this WeakPwdListInfoResponseInfo.
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        r"""Sets the host_ip of this WeakPwdListInfoResponseInfo.

        **参数解释**: 服务器IP（私有IP），为兼容用户使用，不删除此字段 **取值范围**: 不涉及 

        :param host_ip: The host_ip of this WeakPwdListInfoResponseInfo.
        :type host_ip: str
        """
        self._host_ip = host_ip

    @property
    def private_ip(self):
        r"""Gets the private_ip of this WeakPwdListInfoResponseInfo.

        **参数解释**: 服务器私有IP **取值范围**: 不涉及 

        :return: The private_ip of this WeakPwdListInfoResponseInfo.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this WeakPwdListInfoResponseInfo.

        **参数解释**: 服务器私有IP **取值范围**: 不涉及 

        :param private_ip: The private_ip of this WeakPwdListInfoResponseInfo.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def public_ip(self):
        r"""Gets the public_ip of this WeakPwdListInfoResponseInfo.

        **参数解释**: 服务器公网IP **取值范围**: 不涉及 

        :return: The public_ip of this WeakPwdListInfoResponseInfo.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this WeakPwdListInfoResponseInfo.

        **参数解释**: 服务器公网IP **取值范围**: 不涉及 

        :param public_ip: The public_ip of this WeakPwdListInfoResponseInfo.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def update_time(self):
        r"""Gets the update_time of this WeakPwdListInfoResponseInfo.

        **参数解释**: 最近扫描时间，时间戳单位：毫秒 **取值范围**: 不涉及 

        :return: The update_time of this WeakPwdListInfoResponseInfo.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this WeakPwdListInfoResponseInfo.

        **参数解释**: 最近扫描时间，时间戳单位：毫秒 **取值范围**: 不涉及 

        :param update_time: The update_time of this WeakPwdListInfoResponseInfo.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def weak_pwd_accounts(self):
        r"""Gets the weak_pwd_accounts of this WeakPwdListInfoResponseInfo.

        **参数解释**: 弱口令账号列表 **取值范围**: 不涉及 

        :return: The weak_pwd_accounts of this WeakPwdListInfoResponseInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.WeakPwdAccountInfoResponseInfo`]
        """
        return self._weak_pwd_accounts

    @weak_pwd_accounts.setter
    def weak_pwd_accounts(self, weak_pwd_accounts):
        r"""Sets the weak_pwd_accounts of this WeakPwdListInfoResponseInfo.

        **参数解释**: 弱口令账号列表 **取值范围**: 不涉及 

        :param weak_pwd_accounts: The weak_pwd_accounts of this WeakPwdListInfoResponseInfo.
        :type weak_pwd_accounts: list[:class:`huaweicloudsdkhss.v5.WeakPwdAccountInfoResponseInfo`]
        """
        self._weak_pwd_accounts = weak_pwd_accounts

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
        if not isinstance(other, WeakPwdListInfoResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
