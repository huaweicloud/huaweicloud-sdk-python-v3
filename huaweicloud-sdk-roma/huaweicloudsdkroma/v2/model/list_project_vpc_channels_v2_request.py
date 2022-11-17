# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListProjectVpcChannelsV2Request:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'id': 'str',
        'name': 'str',
        'precise_search': 'str',
        'member_host': 'str',
        'member_port': 'int',
        'member_group_name': 'str',
        'member_group_id': 'str',
        'members_return': 'bool'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'id': 'id',
        'name': 'name',
        'precise_search': 'precise_search',
        'member_host': 'member_host',
        'member_port': 'member_port',
        'member_group_name': 'member_group_name',
        'member_group_id': 'member_group_id',
        'members_return': 'members_return'
    }

    def __init__(self, offset=None, limit=None, id=None, name=None, precise_search=None, member_host=None, member_port=None, member_group_name=None, member_group_id=None, members_return=None):
        """ListProjectVpcChannelsV2Request

        The model defined in huaweicloud sdk

        :param offset: 偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0
        :type offset: int
        :param limit: 每页显示的条目数量
        :type limit: int
        :param id: VPC通道的编号
        :type id: str
        :param name: VPC通道的名称
        :type name: str
        :param precise_search: 指定需要精确匹配查找的参数名称，多个参数需要支持精确匹配时参数之间使用“,”隔开。  目前支持name，member_group_name。
        :type precise_search: str
        :param member_host: 后端服务地址。默认精确查询，不支持模糊查询。
        :type member_host: str
        :param member_port: 后端服务器端口
        :type member_port: int
        :param member_group_name: 后端服务器组名称
        :type member_group_name: str
        :param member_group_id: 后端服务器组编号
        :type member_group_id: str
        :param members_return: 是否返回后端实例列表
        :type members_return: bool
        """
        
        

        self._offset = None
        self._limit = None
        self._id = None
        self._name = None
        self._precise_search = None
        self._member_host = None
        self._member_port = None
        self._member_group_name = None
        self._member_group_id = None
        self._members_return = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if precise_search is not None:
            self.precise_search = precise_search
        if member_host is not None:
            self.member_host = member_host
        if member_port is not None:
            self.member_port = member_port
        if member_group_name is not None:
            self.member_group_name = member_group_name
        if member_group_id is not None:
            self.member_group_id = member_group_id
        if members_return is not None:
            self.members_return = members_return

    @property
    def offset(self):
        """Gets the offset of this ListProjectVpcChannelsV2Request.

        偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0

        :return: The offset of this ListProjectVpcChannelsV2Request.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListProjectVpcChannelsV2Request.

        偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0

        :param offset: The offset of this ListProjectVpcChannelsV2Request.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListProjectVpcChannelsV2Request.

        每页显示的条目数量

        :return: The limit of this ListProjectVpcChannelsV2Request.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListProjectVpcChannelsV2Request.

        每页显示的条目数量

        :param limit: The limit of this ListProjectVpcChannelsV2Request.
        :type limit: int
        """
        self._limit = limit

    @property
    def id(self):
        """Gets the id of this ListProjectVpcChannelsV2Request.

        VPC通道的编号

        :return: The id of this ListProjectVpcChannelsV2Request.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListProjectVpcChannelsV2Request.

        VPC通道的编号

        :param id: The id of this ListProjectVpcChannelsV2Request.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ListProjectVpcChannelsV2Request.

        VPC通道的名称

        :return: The name of this ListProjectVpcChannelsV2Request.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListProjectVpcChannelsV2Request.

        VPC通道的名称

        :param name: The name of this ListProjectVpcChannelsV2Request.
        :type name: str
        """
        self._name = name

    @property
    def precise_search(self):
        """Gets the precise_search of this ListProjectVpcChannelsV2Request.

        指定需要精确匹配查找的参数名称，多个参数需要支持精确匹配时参数之间使用“,”隔开。  目前支持name，member_group_name。

        :return: The precise_search of this ListProjectVpcChannelsV2Request.
        :rtype: str
        """
        return self._precise_search

    @precise_search.setter
    def precise_search(self, precise_search):
        """Sets the precise_search of this ListProjectVpcChannelsV2Request.

        指定需要精确匹配查找的参数名称，多个参数需要支持精确匹配时参数之间使用“,”隔开。  目前支持name，member_group_name。

        :param precise_search: The precise_search of this ListProjectVpcChannelsV2Request.
        :type precise_search: str
        """
        self._precise_search = precise_search

    @property
    def member_host(self):
        """Gets the member_host of this ListProjectVpcChannelsV2Request.

        后端服务地址。默认精确查询，不支持模糊查询。

        :return: The member_host of this ListProjectVpcChannelsV2Request.
        :rtype: str
        """
        return self._member_host

    @member_host.setter
    def member_host(self, member_host):
        """Sets the member_host of this ListProjectVpcChannelsV2Request.

        后端服务地址。默认精确查询，不支持模糊查询。

        :param member_host: The member_host of this ListProjectVpcChannelsV2Request.
        :type member_host: str
        """
        self._member_host = member_host

    @property
    def member_port(self):
        """Gets the member_port of this ListProjectVpcChannelsV2Request.

        后端服务器端口

        :return: The member_port of this ListProjectVpcChannelsV2Request.
        :rtype: int
        """
        return self._member_port

    @member_port.setter
    def member_port(self, member_port):
        """Sets the member_port of this ListProjectVpcChannelsV2Request.

        后端服务器端口

        :param member_port: The member_port of this ListProjectVpcChannelsV2Request.
        :type member_port: int
        """
        self._member_port = member_port

    @property
    def member_group_name(self):
        """Gets the member_group_name of this ListProjectVpcChannelsV2Request.

        后端服务器组名称

        :return: The member_group_name of this ListProjectVpcChannelsV2Request.
        :rtype: str
        """
        return self._member_group_name

    @member_group_name.setter
    def member_group_name(self, member_group_name):
        """Sets the member_group_name of this ListProjectVpcChannelsV2Request.

        后端服务器组名称

        :param member_group_name: The member_group_name of this ListProjectVpcChannelsV2Request.
        :type member_group_name: str
        """
        self._member_group_name = member_group_name

    @property
    def member_group_id(self):
        """Gets the member_group_id of this ListProjectVpcChannelsV2Request.

        后端服务器组编号

        :return: The member_group_id of this ListProjectVpcChannelsV2Request.
        :rtype: str
        """
        return self._member_group_id

    @member_group_id.setter
    def member_group_id(self, member_group_id):
        """Sets the member_group_id of this ListProjectVpcChannelsV2Request.

        后端服务器组编号

        :param member_group_id: The member_group_id of this ListProjectVpcChannelsV2Request.
        :type member_group_id: str
        """
        self._member_group_id = member_group_id

    @property
    def members_return(self):
        """Gets the members_return of this ListProjectVpcChannelsV2Request.

        是否返回后端实例列表

        :return: The members_return of this ListProjectVpcChannelsV2Request.
        :rtype: bool
        """
        return self._members_return

    @members_return.setter
    def members_return(self, members_return):
        """Sets the members_return of this ListProjectVpcChannelsV2Request.

        是否返回后端实例列表

        :param members_return: The members_return of this ListProjectVpcChannelsV2Request.
        :type members_return: bool
        """
        self._members_return = members_return

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
        if not isinstance(other, ListProjectVpcChannelsV2Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
