# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSystemUserWhiteListRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'host_id': 'str',
        'host_name': 'str',
        'private_ip': 'str',
        'public_ip': 'str',
        'system_user_name': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'host_id': 'host_id',
        'host_name': 'host_name',
        'private_ip': 'private_ip',
        'public_ip': 'public_ip',
        'system_user_name': 'system_user_name',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, enterprise_project_id=None, host_id=None, host_name=None, private_ip=None, public_ip=None, system_user_name=None, offset=None, limit=None):
        r"""ListSystemUserWhiteListRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。
        :type enterprise_project_id: str
        :param host_id: 服务器ID
        :type host_id: str
        :param host_name: 服务器名称
        :type host_name: str
        :param private_ip: 服务器私有IP
        :type private_ip: str
        :param public_ip: 服务器公网IP
        :type public_ip: str
        :param system_user_name: 系统用户名
        :type system_user_name: str
        :param offset: 偏移量：指定返回记录的开始位置
        :type offset: int
        :param limit: 每页显示个数
        :type limit: int
        """
        
        

        self._enterprise_project_id = None
        self._host_id = None
        self._host_name = None
        self._private_ip = None
        self._public_ip = None
        self._system_user_name = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if host_id is not None:
            self.host_id = host_id
        if host_name is not None:
            self.host_name = host_name
        if private_ip is not None:
            self.private_ip = private_ip
        if public_ip is not None:
            self.public_ip = public_ip
        if system_user_name is not None:
            self.system_user_name = system_user_name
        self.offset = offset
        self.limit = limit

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListSystemUserWhiteListRequest.

        主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。

        :return: The enterprise_project_id of this ListSystemUserWhiteListRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListSystemUserWhiteListRequest.

        主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。

        :param enterprise_project_id: The enterprise_project_id of this ListSystemUserWhiteListRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def host_id(self):
        r"""Gets the host_id of this ListSystemUserWhiteListRequest.

        服务器ID

        :return: The host_id of this ListSystemUserWhiteListRequest.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this ListSystemUserWhiteListRequest.

        服务器ID

        :param host_id: The host_id of this ListSystemUserWhiteListRequest.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_name(self):
        r"""Gets the host_name of this ListSystemUserWhiteListRequest.

        服务器名称

        :return: The host_name of this ListSystemUserWhiteListRequest.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this ListSystemUserWhiteListRequest.

        服务器名称

        :param host_name: The host_name of this ListSystemUserWhiteListRequest.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def private_ip(self):
        r"""Gets the private_ip of this ListSystemUserWhiteListRequest.

        服务器私有IP

        :return: The private_ip of this ListSystemUserWhiteListRequest.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this ListSystemUserWhiteListRequest.

        服务器私有IP

        :param private_ip: The private_ip of this ListSystemUserWhiteListRequest.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def public_ip(self):
        r"""Gets the public_ip of this ListSystemUserWhiteListRequest.

        服务器公网IP

        :return: The public_ip of this ListSystemUserWhiteListRequest.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this ListSystemUserWhiteListRequest.

        服务器公网IP

        :param public_ip: The public_ip of this ListSystemUserWhiteListRequest.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def system_user_name(self):
        r"""Gets the system_user_name of this ListSystemUserWhiteListRequest.

        系统用户名

        :return: The system_user_name of this ListSystemUserWhiteListRequest.
        :rtype: str
        """
        return self._system_user_name

    @system_user_name.setter
    def system_user_name(self, system_user_name):
        r"""Sets the system_user_name of this ListSystemUserWhiteListRequest.

        系统用户名

        :param system_user_name: The system_user_name of this ListSystemUserWhiteListRequest.
        :type system_user_name: str
        """
        self._system_user_name = system_user_name

    @property
    def offset(self):
        r"""Gets the offset of this ListSystemUserWhiteListRequest.

        偏移量：指定返回记录的开始位置

        :return: The offset of this ListSystemUserWhiteListRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListSystemUserWhiteListRequest.

        偏移量：指定返回记录的开始位置

        :param offset: The offset of this ListSystemUserWhiteListRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListSystemUserWhiteListRequest.

        每页显示个数

        :return: The limit of this ListSystemUserWhiteListRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSystemUserWhiteListRequest.

        每页显示个数

        :param limit: The limit of this ListSystemUserWhiteListRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListSystemUserWhiteListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
