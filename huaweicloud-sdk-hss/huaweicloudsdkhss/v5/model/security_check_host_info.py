# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecurityCheckHostInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_name': 'str',
        'host_id': 'str',
        'private_ip': 'str',
        'public_ip': 'str',
        'os_type': 'str'
    }

    attribute_map = {
        'host_name': 'host_name',
        'host_id': 'host_id',
        'private_ip': 'private_ip',
        'public_ip': 'public_ip',
        'os_type': 'os_type'
    }

    def __init__(self, host_name=None, host_id=None, private_ip=None, public_ip=None, os_type=None):
        r"""SecurityCheckHostInfo

        The model defined in huaweicloud sdk

        :param host_name: **参数解释**： 服务器名称 **取值范围**： 不涉及 
        :type host_name: str
        :param host_id: **参数解释**： 服务器ID **取值范围**： 不涉及 
        :type host_id: str
        :param private_ip: **参数解释**： 私有IP地址 **取值范围**： 不涉及 
        :type private_ip: str
        :param public_ip: **参数解释**： 公网IP地址 **取值范围**： 不涉及 
        :type public_ip: str
        :param os_type: **参数解释**： 系统类型 **取值范围**： 不涉及 
        :type os_type: str
        """
        
        

        self._host_name = None
        self._host_id = None
        self._private_ip = None
        self._public_ip = None
        self._os_type = None
        self.discriminator = None

        if host_name is not None:
            self.host_name = host_name
        if host_id is not None:
            self.host_id = host_id
        if private_ip is not None:
            self.private_ip = private_ip
        if public_ip is not None:
            self.public_ip = public_ip
        if os_type is not None:
            self.os_type = os_type

    @property
    def host_name(self):
        r"""Gets the host_name of this SecurityCheckHostInfo.

        **参数解释**： 服务器名称 **取值范围**： 不涉及 

        :return: The host_name of this SecurityCheckHostInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this SecurityCheckHostInfo.

        **参数解释**： 服务器名称 **取值范围**： 不涉及 

        :param host_name: The host_name of this SecurityCheckHostInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_id(self):
        r"""Gets the host_id of this SecurityCheckHostInfo.

        **参数解释**： 服务器ID **取值范围**： 不涉及 

        :return: The host_id of this SecurityCheckHostInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this SecurityCheckHostInfo.

        **参数解释**： 服务器ID **取值范围**： 不涉及 

        :param host_id: The host_id of this SecurityCheckHostInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def private_ip(self):
        r"""Gets the private_ip of this SecurityCheckHostInfo.

        **参数解释**： 私有IP地址 **取值范围**： 不涉及 

        :return: The private_ip of this SecurityCheckHostInfo.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this SecurityCheckHostInfo.

        **参数解释**： 私有IP地址 **取值范围**： 不涉及 

        :param private_ip: The private_ip of this SecurityCheckHostInfo.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def public_ip(self):
        r"""Gets the public_ip of this SecurityCheckHostInfo.

        **参数解释**： 公网IP地址 **取值范围**： 不涉及 

        :return: The public_ip of this SecurityCheckHostInfo.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this SecurityCheckHostInfo.

        **参数解释**： 公网IP地址 **取值范围**： 不涉及 

        :param public_ip: The public_ip of this SecurityCheckHostInfo.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def os_type(self):
        r"""Gets the os_type of this SecurityCheckHostInfo.

        **参数解释**： 系统类型 **取值范围**： 不涉及 

        :return: The os_type of this SecurityCheckHostInfo.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this SecurityCheckHostInfo.

        **参数解释**： 系统类型 **取值范围**： 不涉及 

        :param os_type: The os_type of this SecurityCheckHostInfo.
        :type os_type: str
        """
        self._os_type = os_type

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
        if not isinstance(other, SecurityCheckHostInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
