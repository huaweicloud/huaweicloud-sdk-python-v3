# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPortHostRequest:

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
        'host_name': 'str',
        'host_ip': 'str',
        'port': 'int',
        'type': 'str',
        'category': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'host_name': 'host_name',
        'host_ip': 'host_ip',
        'port': 'port',
        'type': 'type',
        'category': 'category',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, enterprise_project_id=None, host_name=None, host_ip=None, port=None, type=None, category=None, limit=None, offset=None):
        r"""ListPortHostRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。
        :type enterprise_project_id: str
        :param host_name: 主机名称
        :type host_name: str
        :param host_ip: 主机ip
        :type host_ip: str
        :param port: 端口号
        :type port: int
        :param type: 端口类型：目前包括TCP，UDP两种
        :type type: str
        :param category: 类别，默认为host，包含如下： - host：主机 - container：容器
        :type category: str
        :param limit: 每页显示数量
        :type limit: int
        :param offset: 偏移量：指定返回记录的开始位置
        :type offset: int
        """
        
        

        self._enterprise_project_id = None
        self._host_name = None
        self._host_ip = None
        self._port = None
        self._type = None
        self._category = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if host_name is not None:
            self.host_name = host_name
        if host_ip is not None:
            self.host_ip = host_ip
        self.port = port
        if type is not None:
            self.type = type
        if category is not None:
            self.category = category
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListPortHostRequest.

        主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。

        :return: The enterprise_project_id of this ListPortHostRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListPortHostRequest.

        主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。

        :param enterprise_project_id: The enterprise_project_id of this ListPortHostRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def host_name(self):
        r"""Gets the host_name of this ListPortHostRequest.

        主机名称

        :return: The host_name of this ListPortHostRequest.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this ListPortHostRequest.

        主机名称

        :param host_name: The host_name of this ListPortHostRequest.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_ip(self):
        r"""Gets the host_ip of this ListPortHostRequest.

        主机ip

        :return: The host_ip of this ListPortHostRequest.
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        r"""Sets the host_ip of this ListPortHostRequest.

        主机ip

        :param host_ip: The host_ip of this ListPortHostRequest.
        :type host_ip: str
        """
        self._host_ip = host_ip

    @property
    def port(self):
        r"""Gets the port of this ListPortHostRequest.

        端口号

        :return: The port of this ListPortHostRequest.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this ListPortHostRequest.

        端口号

        :param port: The port of this ListPortHostRequest.
        :type port: int
        """
        self._port = port

    @property
    def type(self):
        r"""Gets the type of this ListPortHostRequest.

        端口类型：目前包括TCP，UDP两种

        :return: The type of this ListPortHostRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListPortHostRequest.

        端口类型：目前包括TCP，UDP两种

        :param type: The type of this ListPortHostRequest.
        :type type: str
        """
        self._type = type

    @property
    def category(self):
        r"""Gets the category of this ListPortHostRequest.

        类别，默认为host，包含如下： - host：主机 - container：容器

        :return: The category of this ListPortHostRequest.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ListPortHostRequest.

        类别，默认为host，包含如下： - host：主机 - container：容器

        :param category: The category of this ListPortHostRequest.
        :type category: str
        """
        self._category = category

    @property
    def limit(self):
        r"""Gets the limit of this ListPortHostRequest.

        每页显示数量

        :return: The limit of this ListPortHostRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListPortHostRequest.

        每页显示数量

        :param limit: The limit of this ListPortHostRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListPortHostRequest.

        偏移量：指定返回记录的开始位置

        :return: The offset of this ListPortHostRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListPortHostRequest.

        偏移量：指定返回记录的开始位置

        :param offset: The offset of this ListPortHostRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListPortHostRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
