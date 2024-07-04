# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAutoLaunchsRequest:

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
        'name': 'str',
        'host_ip': 'str',
        'type': 'str',
        'enterprise_project_id': 'str',
        'limit': 'int',
        'offset': 'int',
        'part_match': 'bool'
    }

    attribute_map = {
        'host_id': 'host_id',
        'host_name': 'host_name',
        'name': 'name',
        'host_ip': 'host_ip',
        'type': 'type',
        'enterprise_project_id': 'enterprise_project_id',
        'limit': 'limit',
        'offset': 'offset',
        'part_match': 'part_match'
    }

    def __init__(self, host_id=None, host_name=None, name=None, host_ip=None, type=None, enterprise_project_id=None, limit=None, offset=None, part_match=None):
        """ListAutoLaunchsRequest

        The model defined in huaweicloud sdk

        :param host_id: 主机id
        :type host_id: str
        :param host_name: 主机名称
        :type host_name: str
        :param name: 自启动项名称
        :type name: str
        :param host_ip: 主机ip
        :type host_ip: str
        :param type: 自启动项类型   - 0 ：自启动服务   - 1 ：定时任务   - 2 ：预加载动态库   - 3 ：Run注册表键   - 4 ：开机启动文件夹
        :type type: str
        :param enterprise_project_id: 企业项目ID，查询所有企业项目时填写：all_granted_eps
        :type enterprise_project_id: str
        :param limit: 每页显示数量
        :type limit: int
        :param offset: 偏移量：指定返回记录的开始位置
        :type offset: int
        :param part_match: 是否模糊匹配，默认false表示精确匹配
        :type part_match: bool
        """
        
        

        self._host_id = None
        self._host_name = None
        self._name = None
        self._host_ip = None
        self._type = None
        self._enterprise_project_id = None
        self._limit = None
        self._offset = None
        self._part_match = None
        self.discriminator = None

        if host_id is not None:
            self.host_id = host_id
        if host_name is not None:
            self.host_name = host_name
        if name is not None:
            self.name = name
        if host_ip is not None:
            self.host_ip = host_ip
        if type is not None:
            self.type = type
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if part_match is not None:
            self.part_match = part_match

    @property
    def host_id(self):
        """Gets the host_id of this ListAutoLaunchsRequest.

        主机id

        :return: The host_id of this ListAutoLaunchsRequest.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this ListAutoLaunchsRequest.

        主机id

        :param host_id: The host_id of this ListAutoLaunchsRequest.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_name(self):
        """Gets the host_name of this ListAutoLaunchsRequest.

        主机名称

        :return: The host_name of this ListAutoLaunchsRequest.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this ListAutoLaunchsRequest.

        主机名称

        :param host_name: The host_name of this ListAutoLaunchsRequest.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def name(self):
        """Gets the name of this ListAutoLaunchsRequest.

        自启动项名称

        :return: The name of this ListAutoLaunchsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListAutoLaunchsRequest.

        自启动项名称

        :param name: The name of this ListAutoLaunchsRequest.
        :type name: str
        """
        self._name = name

    @property
    def host_ip(self):
        """Gets the host_ip of this ListAutoLaunchsRequest.

        主机ip

        :return: The host_ip of this ListAutoLaunchsRequest.
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        """Sets the host_ip of this ListAutoLaunchsRequest.

        主机ip

        :param host_ip: The host_ip of this ListAutoLaunchsRequest.
        :type host_ip: str
        """
        self._host_ip = host_ip

    @property
    def type(self):
        """Gets the type of this ListAutoLaunchsRequest.

        自启动项类型   - 0 ：自启动服务   - 1 ：定时任务   - 2 ：预加载动态库   - 3 ：Run注册表键   - 4 ：开机启动文件夹

        :return: The type of this ListAutoLaunchsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListAutoLaunchsRequest.

        自启动项类型   - 0 ：自启动服务   - 1 ：定时任务   - 2 ：预加载动态库   - 3 ：Run注册表键   - 4 ：开机启动文件夹

        :param type: The type of this ListAutoLaunchsRequest.
        :type type: str
        """
        self._type = type

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListAutoLaunchsRequest.

        企业项目ID，查询所有企业项目时填写：all_granted_eps

        :return: The enterprise_project_id of this ListAutoLaunchsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListAutoLaunchsRequest.

        企业项目ID，查询所有企业项目时填写：all_granted_eps

        :param enterprise_project_id: The enterprise_project_id of this ListAutoLaunchsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def limit(self):
        """Gets the limit of this ListAutoLaunchsRequest.

        每页显示数量

        :return: The limit of this ListAutoLaunchsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListAutoLaunchsRequest.

        每页显示数量

        :param limit: The limit of this ListAutoLaunchsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListAutoLaunchsRequest.

        偏移量：指定返回记录的开始位置

        :return: The offset of this ListAutoLaunchsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListAutoLaunchsRequest.

        偏移量：指定返回记录的开始位置

        :param offset: The offset of this ListAutoLaunchsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def part_match(self):
        """Gets the part_match of this ListAutoLaunchsRequest.

        是否模糊匹配，默认false表示精确匹配

        :return: The part_match of this ListAutoLaunchsRequest.
        :rtype: bool
        """
        return self._part_match

    @part_match.setter
    def part_match(self, part_match):
        """Sets the part_match of this ListAutoLaunchsRequest.

        是否模糊匹配，默认false表示精确匹配

        :param part_match: The part_match of this ListAutoLaunchsRequest.
        :type part_match: bool
        """
        self._part_match = part_match

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
        if not isinstance(other, ListAutoLaunchsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
