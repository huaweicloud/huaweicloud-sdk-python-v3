# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WebTamperHostResponseInfo:

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
        'public_ip': 'str',
        'private_ip': 'str',
        'agent_id': 'str',
        'os_type': 'str',
        'asset_value': 'str',
        'web_app_list': 'list[str]'
    }

    attribute_map = {
        'host_id': 'host_id',
        'host_name': 'host_name',
        'public_ip': 'public_ip',
        'private_ip': 'private_ip',
        'agent_id': 'agent_id',
        'os_type': 'os_type',
        'asset_value': 'asset_value',
        'web_app_list': 'web_app_list'
    }

    def __init__(self, host_id=None, host_name=None, public_ip=None, private_ip=None, agent_id=None, os_type=None, asset_value=None, web_app_list=None):
        r"""WebTamperHostResponseInfo

        The model defined in huaweicloud sdk

        :param host_id: **参数解释**： 主机ID **取值范围**： 字符长度1-64位 
        :type host_id: str
        :param host_name: **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 
        :type host_name: str
        :param public_ip: **参数解释**： 弹性公网IP地址 **取值范围**： 字符长度1-256位 
        :type public_ip: str
        :param private_ip: **参数解释**： 服务器私有IP **取值范围**： 字符长度1-128位 
        :type private_ip: str
        :param agent_id: **参数解释**: Agent ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 
        :type agent_id: str
        :param os_type: **参数解释**： 操作系统类型 **取值范围**： - Linux：Linux。 - Windows：Windows。 
        :type os_type: str
        :param asset_value: 资产重要性，包含如下3种   - important ：重要资产   - common ：一般资产   - test ：测试资产
        :type asset_value: str
        :param web_app_list: web应用列表
        :type web_app_list: list[str]
        """
        
        

        self._host_id = None
        self._host_name = None
        self._public_ip = None
        self._private_ip = None
        self._agent_id = None
        self._os_type = None
        self._asset_value = None
        self._web_app_list = None
        self.discriminator = None

        if host_id is not None:
            self.host_id = host_id
        if host_name is not None:
            self.host_name = host_name
        if public_ip is not None:
            self.public_ip = public_ip
        if private_ip is not None:
            self.private_ip = private_ip
        if agent_id is not None:
            self.agent_id = agent_id
        if os_type is not None:
            self.os_type = os_type
        if asset_value is not None:
            self.asset_value = asset_value
        if web_app_list is not None:
            self.web_app_list = web_app_list

    @property
    def host_id(self):
        r"""Gets the host_id of this WebTamperHostResponseInfo.

        **参数解释**： 主机ID **取值范围**： 字符长度1-64位 

        :return: The host_id of this WebTamperHostResponseInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this WebTamperHostResponseInfo.

        **参数解释**： 主机ID **取值范围**： 字符长度1-64位 

        :param host_id: The host_id of this WebTamperHostResponseInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_name(self):
        r"""Gets the host_name of this WebTamperHostResponseInfo.

        **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 

        :return: The host_name of this WebTamperHostResponseInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this WebTamperHostResponseInfo.

        **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 

        :param host_name: The host_name of this WebTamperHostResponseInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def public_ip(self):
        r"""Gets the public_ip of this WebTamperHostResponseInfo.

        **参数解释**： 弹性公网IP地址 **取值范围**： 字符长度1-256位 

        :return: The public_ip of this WebTamperHostResponseInfo.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this WebTamperHostResponseInfo.

        **参数解释**： 弹性公网IP地址 **取值范围**： 字符长度1-256位 

        :param public_ip: The public_ip of this WebTamperHostResponseInfo.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def private_ip(self):
        r"""Gets the private_ip of this WebTamperHostResponseInfo.

        **参数解释**： 服务器私有IP **取值范围**： 字符长度1-128位 

        :return: The private_ip of this WebTamperHostResponseInfo.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this WebTamperHostResponseInfo.

        **参数解释**： 服务器私有IP **取值范围**： 字符长度1-128位 

        :param private_ip: The private_ip of this WebTamperHostResponseInfo.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def agent_id(self):
        r"""Gets the agent_id of this WebTamperHostResponseInfo.

        **参数解释**: Agent ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :return: The agent_id of this WebTamperHostResponseInfo.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        r"""Sets the agent_id of this WebTamperHostResponseInfo.

        **参数解释**: Agent ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :param agent_id: The agent_id of this WebTamperHostResponseInfo.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def os_type(self):
        r"""Gets the os_type of this WebTamperHostResponseInfo.

        **参数解释**： 操作系统类型 **取值范围**： - Linux：Linux。 - Windows：Windows。 

        :return: The os_type of this WebTamperHostResponseInfo.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this WebTamperHostResponseInfo.

        **参数解释**： 操作系统类型 **取值范围**： - Linux：Linux。 - Windows：Windows。 

        :param os_type: The os_type of this WebTamperHostResponseInfo.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def asset_value(self):
        r"""Gets the asset_value of this WebTamperHostResponseInfo.

        资产重要性，包含如下3种   - important ：重要资产   - common ：一般资产   - test ：测试资产

        :return: The asset_value of this WebTamperHostResponseInfo.
        :rtype: str
        """
        return self._asset_value

    @asset_value.setter
    def asset_value(self, asset_value):
        r"""Sets the asset_value of this WebTamperHostResponseInfo.

        资产重要性，包含如下3种   - important ：重要资产   - common ：一般资产   - test ：测试资产

        :param asset_value: The asset_value of this WebTamperHostResponseInfo.
        :type asset_value: str
        """
        self._asset_value = asset_value

    @property
    def web_app_list(self):
        r"""Gets the web_app_list of this WebTamperHostResponseInfo.

        web应用列表

        :return: The web_app_list of this WebTamperHostResponseInfo.
        :rtype: list[str]
        """
        return self._web_app_list

    @web_app_list.setter
    def web_app_list(self, web_app_list):
        r"""Sets the web_app_list of this WebTamperHostResponseInfo.

        web应用列表

        :param web_app_list: The web_app_list of this WebTamperHostResponseInfo.
        :type web_app_list: list[str]
        """
        self._web_app_list = web_app_list

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
        if not isinstance(other, WebTamperHostResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
