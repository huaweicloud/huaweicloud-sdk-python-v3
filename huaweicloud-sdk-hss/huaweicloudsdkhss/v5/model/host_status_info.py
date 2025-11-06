# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HostStatusInfo:

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
        'public_ip': 'list[str]',
        'private_ip': 'list[str]',
        'status': 'str',
        'vpc_id': 'str'
    }

    attribute_map = {
        'host_id': 'host_id',
        'host_name': 'host_name',
        'public_ip': 'public_ip',
        'private_ip': 'private_ip',
        'status': 'status',
        'vpc_id': 'vpc_id'
    }

    def __init__(self, host_id=None, host_name=None, public_ip=None, private_ip=None, status=None, vpc_id=None):
        r"""HostStatusInfo

        The model defined in huaweicloud sdk

        :param host_id: **参数解释**: 服务器ID **取值范围**: 字符长度1-64位 
        :type host_id: str
        :param host_name: **参数解释**: 服务器名称 **取值范围**: 字符长度1-128位 
        :type host_name: str
        :param public_ip: **参数解释**: 弹性公网IP地址 
        :type public_ip: list[str]
        :param private_ip: **参数解释**: 私有IP地址 
        :type private_ip: list[str]
        :param status: **参数解释**: 服务器状态 **取值范围**: 字符长度1-128位 
        :type status: str
        :param vpc_id: **参数解释**: Vpc标识Id **取值范围**: 字符长度1-128位 
        :type vpc_id: str
        """
        
        

        self._host_id = None
        self._host_name = None
        self._public_ip = None
        self._private_ip = None
        self._status = None
        self._vpc_id = None
        self.discriminator = None

        if host_id is not None:
            self.host_id = host_id
        if host_name is not None:
            self.host_name = host_name
        if public_ip is not None:
            self.public_ip = public_ip
        if private_ip is not None:
            self.private_ip = private_ip
        if status is not None:
            self.status = status
        if vpc_id is not None:
            self.vpc_id = vpc_id

    @property
    def host_id(self):
        r"""Gets the host_id of this HostStatusInfo.

        **参数解释**: 服务器ID **取值范围**: 字符长度1-64位 

        :return: The host_id of this HostStatusInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this HostStatusInfo.

        **参数解释**: 服务器ID **取值范围**: 字符长度1-64位 

        :param host_id: The host_id of this HostStatusInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_name(self):
        r"""Gets the host_name of this HostStatusInfo.

        **参数解释**: 服务器名称 **取值范围**: 字符长度1-128位 

        :return: The host_name of this HostStatusInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this HostStatusInfo.

        **参数解释**: 服务器名称 **取值范围**: 字符长度1-128位 

        :param host_name: The host_name of this HostStatusInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def public_ip(self):
        r"""Gets the public_ip of this HostStatusInfo.

        **参数解释**: 弹性公网IP地址 

        :return: The public_ip of this HostStatusInfo.
        :rtype: list[str]
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this HostStatusInfo.

        **参数解释**: 弹性公网IP地址 

        :param public_ip: The public_ip of this HostStatusInfo.
        :type public_ip: list[str]
        """
        self._public_ip = public_ip

    @property
    def private_ip(self):
        r"""Gets the private_ip of this HostStatusInfo.

        **参数解释**: 私有IP地址 

        :return: The private_ip of this HostStatusInfo.
        :rtype: list[str]
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this HostStatusInfo.

        **参数解释**: 私有IP地址 

        :param private_ip: The private_ip of this HostStatusInfo.
        :type private_ip: list[str]
        """
        self._private_ip = private_ip

    @property
    def status(self):
        r"""Gets the status of this HostStatusInfo.

        **参数解释**: 服务器状态 **取值范围**: 字符长度1-128位 

        :return: The status of this HostStatusInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this HostStatusInfo.

        **参数解释**: 服务器状态 **取值范围**: 字符长度1-128位 

        :param status: The status of this HostStatusInfo.
        :type status: str
        """
        self._status = status

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this HostStatusInfo.

        **参数解释**: Vpc标识Id **取值范围**: 字符长度1-128位 

        :return: The vpc_id of this HostStatusInfo.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this HostStatusInfo.

        **参数解释**: Vpc标识Id **取值范围**: 字符长度1-128位 

        :param vpc_id: The vpc_id of this HostStatusInfo.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

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
        if not isinstance(other, HostStatusInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
