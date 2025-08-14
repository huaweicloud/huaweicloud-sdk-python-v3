# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SystemUserWhiteListResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_name': 'str',
        'host_id': 'str',
        'host_name': 'str',
        'private_ip': 'str',
        'public_ip': 'str',
        'system_user_name_list': 'list[str]',
        'update_time': 'int',
        'remarks': 'str'
    }

    attribute_map = {
        'enterprise_project_name': 'enterprise_project_name',
        'host_id': 'host_id',
        'host_name': 'host_name',
        'private_ip': 'private_ip',
        'public_ip': 'public_ip',
        'system_user_name_list': 'system_user_name_list',
        'update_time': 'update_time',
        'remarks': 'remarks'
    }

    def __init__(self, enterprise_project_name=None, host_id=None, host_name=None, private_ip=None, public_ip=None, system_user_name_list=None, update_time=None, remarks=None):
        r"""SystemUserWhiteListResponseInfo

        The model defined in huaweicloud sdk

        :param enterprise_project_name: 企业项目名称
        :type enterprise_project_name: str
        :param host_id: **参数解释**： 主机ID **取值范围**： 字符长度1-64位 
        :type host_id: str
        :param host_name: **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 
        :type host_name: str
        :param private_ip: **参数解释**： 服务器私有IP **取值范围**： 字符长度1-128位 
        :type private_ip: str
        :param public_ip: **参数解释**： 弹性公网IP地址 **取值范围**： 字符长度1-256位 
        :type public_ip: str
        :param system_user_name_list: 系统用户名列表
        :type system_user_name_list: list[str]
        :param update_time: 更新时间，毫秒
        :type update_time: int
        :param remarks: 备注
        :type remarks: str
        """
        
        

        self._enterprise_project_name = None
        self._host_id = None
        self._host_name = None
        self._private_ip = None
        self._public_ip = None
        self._system_user_name_list = None
        self._update_time = None
        self._remarks = None
        self.discriminator = None

        if enterprise_project_name is not None:
            self.enterprise_project_name = enterprise_project_name
        if host_id is not None:
            self.host_id = host_id
        if host_name is not None:
            self.host_name = host_name
        if private_ip is not None:
            self.private_ip = private_ip
        if public_ip is not None:
            self.public_ip = public_ip
        if system_user_name_list is not None:
            self.system_user_name_list = system_user_name_list
        if update_time is not None:
            self.update_time = update_time
        if remarks is not None:
            self.remarks = remarks

    @property
    def enterprise_project_name(self):
        r"""Gets the enterprise_project_name of this SystemUserWhiteListResponseInfo.

        企业项目名称

        :return: The enterprise_project_name of this SystemUserWhiteListResponseInfo.
        :rtype: str
        """
        return self._enterprise_project_name

    @enterprise_project_name.setter
    def enterprise_project_name(self, enterprise_project_name):
        r"""Sets the enterprise_project_name of this SystemUserWhiteListResponseInfo.

        企业项目名称

        :param enterprise_project_name: The enterprise_project_name of this SystemUserWhiteListResponseInfo.
        :type enterprise_project_name: str
        """
        self._enterprise_project_name = enterprise_project_name

    @property
    def host_id(self):
        r"""Gets the host_id of this SystemUserWhiteListResponseInfo.

        **参数解释**： 主机ID **取值范围**： 字符长度1-64位 

        :return: The host_id of this SystemUserWhiteListResponseInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this SystemUserWhiteListResponseInfo.

        **参数解释**： 主机ID **取值范围**： 字符长度1-64位 

        :param host_id: The host_id of this SystemUserWhiteListResponseInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_name(self):
        r"""Gets the host_name of this SystemUserWhiteListResponseInfo.

        **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 

        :return: The host_name of this SystemUserWhiteListResponseInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this SystemUserWhiteListResponseInfo.

        **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 

        :param host_name: The host_name of this SystemUserWhiteListResponseInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def private_ip(self):
        r"""Gets the private_ip of this SystemUserWhiteListResponseInfo.

        **参数解释**： 服务器私有IP **取值范围**： 字符长度1-128位 

        :return: The private_ip of this SystemUserWhiteListResponseInfo.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this SystemUserWhiteListResponseInfo.

        **参数解释**： 服务器私有IP **取值范围**： 字符长度1-128位 

        :param private_ip: The private_ip of this SystemUserWhiteListResponseInfo.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def public_ip(self):
        r"""Gets the public_ip of this SystemUserWhiteListResponseInfo.

        **参数解释**： 弹性公网IP地址 **取值范围**： 字符长度1-256位 

        :return: The public_ip of this SystemUserWhiteListResponseInfo.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this SystemUserWhiteListResponseInfo.

        **参数解释**： 弹性公网IP地址 **取值范围**： 字符长度1-256位 

        :param public_ip: The public_ip of this SystemUserWhiteListResponseInfo.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def system_user_name_list(self):
        r"""Gets the system_user_name_list of this SystemUserWhiteListResponseInfo.

        系统用户名列表

        :return: The system_user_name_list of this SystemUserWhiteListResponseInfo.
        :rtype: list[str]
        """
        return self._system_user_name_list

    @system_user_name_list.setter
    def system_user_name_list(self, system_user_name_list):
        r"""Sets the system_user_name_list of this SystemUserWhiteListResponseInfo.

        系统用户名列表

        :param system_user_name_list: The system_user_name_list of this SystemUserWhiteListResponseInfo.
        :type system_user_name_list: list[str]
        """
        self._system_user_name_list = system_user_name_list

    @property
    def update_time(self):
        r"""Gets the update_time of this SystemUserWhiteListResponseInfo.

        更新时间，毫秒

        :return: The update_time of this SystemUserWhiteListResponseInfo.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this SystemUserWhiteListResponseInfo.

        更新时间，毫秒

        :param update_time: The update_time of this SystemUserWhiteListResponseInfo.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def remarks(self):
        r"""Gets the remarks of this SystemUserWhiteListResponseInfo.

        备注

        :return: The remarks of this SystemUserWhiteListResponseInfo.
        :rtype: str
        """
        return self._remarks

    @remarks.setter
    def remarks(self, remarks):
        r"""Sets the remarks of this SystemUserWhiteListResponseInfo.

        备注

        :param remarks: The remarks of this SystemUserWhiteListResponseInfo.
        :type remarks: str
        """
        self._remarks = remarks

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
        if not isinstance(other, SystemUserWhiteListResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
