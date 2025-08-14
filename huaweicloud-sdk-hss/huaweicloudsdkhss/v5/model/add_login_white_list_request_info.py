# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddLoginWhiteListRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'private_ip': 'str',
        'login_ip': 'str',
        'login_user_name': 'str',
        'remarks': 'str',
        'handle_event': 'bool'
    }

    attribute_map = {
        'private_ip': 'private_ip',
        'login_ip': 'login_ip',
        'login_user_name': 'login_user_name',
        'remarks': 'remarks',
        'handle_event': 'handle_event'
    }

    def __init__(self, private_ip=None, login_ip=None, login_user_name=None, remarks=None, handle_event=None):
        r"""AddLoginWhiteListRequestInfo

        The model defined in huaweicloud sdk

        :param private_ip: **参数解释**： 服务器私有IP **取值范围**： 字符长度1-128位 
        :type private_ip: str
        :param login_ip: **参数解释**： 登录源IP **取值范围**： 字符长度1-256位 
        :type login_ip: str
        :param login_user_name: **参数解释**： 登录用户名 **取值范围**： 字符长度1-256位 
        :type login_user_name: str
        :param remarks: 备注
        :type remarks: str
        :param handle_event: 是否同时处理相关告警事件
        :type handle_event: bool
        """
        
        

        self._private_ip = None
        self._login_ip = None
        self._login_user_name = None
        self._remarks = None
        self._handle_event = None
        self.discriminator = None

        self.private_ip = private_ip
        self.login_ip = login_ip
        self.login_user_name = login_user_name
        if remarks is not None:
            self.remarks = remarks
        if handle_event is not None:
            self.handle_event = handle_event

    @property
    def private_ip(self):
        r"""Gets the private_ip of this AddLoginWhiteListRequestInfo.

        **参数解释**： 服务器私有IP **取值范围**： 字符长度1-128位 

        :return: The private_ip of this AddLoginWhiteListRequestInfo.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this AddLoginWhiteListRequestInfo.

        **参数解释**： 服务器私有IP **取值范围**： 字符长度1-128位 

        :param private_ip: The private_ip of this AddLoginWhiteListRequestInfo.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def login_ip(self):
        r"""Gets the login_ip of this AddLoginWhiteListRequestInfo.

        **参数解释**： 登录源IP **取值范围**： 字符长度1-256位 

        :return: The login_ip of this AddLoginWhiteListRequestInfo.
        :rtype: str
        """
        return self._login_ip

    @login_ip.setter
    def login_ip(self, login_ip):
        r"""Sets the login_ip of this AddLoginWhiteListRequestInfo.

        **参数解释**： 登录源IP **取值范围**： 字符长度1-256位 

        :param login_ip: The login_ip of this AddLoginWhiteListRequestInfo.
        :type login_ip: str
        """
        self._login_ip = login_ip

    @property
    def login_user_name(self):
        r"""Gets the login_user_name of this AddLoginWhiteListRequestInfo.

        **参数解释**： 登录用户名 **取值范围**： 字符长度1-256位 

        :return: The login_user_name of this AddLoginWhiteListRequestInfo.
        :rtype: str
        """
        return self._login_user_name

    @login_user_name.setter
    def login_user_name(self, login_user_name):
        r"""Sets the login_user_name of this AddLoginWhiteListRequestInfo.

        **参数解释**： 登录用户名 **取值范围**： 字符长度1-256位 

        :param login_user_name: The login_user_name of this AddLoginWhiteListRequestInfo.
        :type login_user_name: str
        """
        self._login_user_name = login_user_name

    @property
    def remarks(self):
        r"""Gets the remarks of this AddLoginWhiteListRequestInfo.

        备注

        :return: The remarks of this AddLoginWhiteListRequestInfo.
        :rtype: str
        """
        return self._remarks

    @remarks.setter
    def remarks(self, remarks):
        r"""Sets the remarks of this AddLoginWhiteListRequestInfo.

        备注

        :param remarks: The remarks of this AddLoginWhiteListRequestInfo.
        :type remarks: str
        """
        self._remarks = remarks

    @property
    def handle_event(self):
        r"""Gets the handle_event of this AddLoginWhiteListRequestInfo.

        是否同时处理相关告警事件

        :return: The handle_event of this AddLoginWhiteListRequestInfo.
        :rtype: bool
        """
        return self._handle_event

    @handle_event.setter
    def handle_event(self, handle_event):
        r"""Sets the handle_event of this AddLoginWhiteListRequestInfo.

        是否同时处理相关告警事件

        :param handle_event: The handle_event of this AddLoginWhiteListRequestInfo.
        :type handle_event: bool
        """
        self._handle_event = handle_event

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
        if not isinstance(other, AddLoginWhiteListRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
