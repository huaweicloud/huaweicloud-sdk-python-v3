# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVpcChannelsV2Request:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'id': 'str',
        'name': 'str',
        'dict_code': 'str',
        'precise_search': 'str',
        'member_host': 'str',
        'member_port': 'int',
        'member_group_name': 'str',
        'member_group_id': 'str',
        'vpc_channel_type': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'offset': 'offset',
        'limit': 'limit',
        'id': 'id',
        'name': 'name',
        'dict_code': 'dict_code',
        'precise_search': 'precise_search',
        'member_host': 'member_host',
        'member_port': 'member_port',
        'member_group_name': 'member_group_name',
        'member_group_id': 'member_group_id',
        'vpc_channel_type': 'vpc_channel_type'
    }

    def __init__(self, instance_id=None, offset=None, limit=None, id=None, name=None, dict_code=None, precise_search=None, member_host=None, member_port=None, member_group_name=None, member_group_id=None, vpc_channel_type=None):
        r"""ListVpcChannelsV2Request

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID，在API网关控制台的“实例信息”中获取。
        :type instance_id: str
        :param offset: 偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0
        :type offset: int
        :param limit: 每页显示的条目数量，条目数量小于等于0时，自动转换为20，条目数量大于500时，自动转换为500
        :type limit: int
        :param id: VPC通道的编号
        :type id: str
        :param name: VPC通道的名称
        :type name: str
        :param dict_code: VPC通道的字典编码  支持英文，数字，特殊字符（-_.）  暂不支持
        :type dict_code: str
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
        :param vpc_channel_type: vpc通道类型： - builtin：服务器类型 - microservice： 微服务类型 - reference：引用负载通道类型
        :type vpc_channel_type: str
        """
        
        

        self._instance_id = None
        self._offset = None
        self._limit = None
        self._id = None
        self._name = None
        self._dict_code = None
        self._precise_search = None
        self._member_host = None
        self._member_port = None
        self._member_group_name = None
        self._member_group_id = None
        self._vpc_channel_type = None
        self.discriminator = None

        self.instance_id = instance_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if dict_code is not None:
            self.dict_code = dict_code
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
        if vpc_channel_type is not None:
            self.vpc_channel_type = vpc_channel_type

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListVpcChannelsV2Request.

        实例ID，在API网关控制台的“实例信息”中获取。

        :return: The instance_id of this ListVpcChannelsV2Request.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListVpcChannelsV2Request.

        实例ID，在API网关控制台的“实例信息”中获取。

        :param instance_id: The instance_id of this ListVpcChannelsV2Request.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def offset(self):
        r"""Gets the offset of this ListVpcChannelsV2Request.

        偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0

        :return: The offset of this ListVpcChannelsV2Request.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListVpcChannelsV2Request.

        偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0

        :param offset: The offset of this ListVpcChannelsV2Request.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListVpcChannelsV2Request.

        每页显示的条目数量，条目数量小于等于0时，自动转换为20，条目数量大于500时，自动转换为500

        :return: The limit of this ListVpcChannelsV2Request.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListVpcChannelsV2Request.

        每页显示的条目数量，条目数量小于等于0时，自动转换为20，条目数量大于500时，自动转换为500

        :param limit: The limit of this ListVpcChannelsV2Request.
        :type limit: int
        """
        self._limit = limit

    @property
    def id(self):
        r"""Gets the id of this ListVpcChannelsV2Request.

        VPC通道的编号

        :return: The id of this ListVpcChannelsV2Request.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListVpcChannelsV2Request.

        VPC通道的编号

        :param id: The id of this ListVpcChannelsV2Request.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ListVpcChannelsV2Request.

        VPC通道的名称

        :return: The name of this ListVpcChannelsV2Request.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListVpcChannelsV2Request.

        VPC通道的名称

        :param name: The name of this ListVpcChannelsV2Request.
        :type name: str
        """
        self._name = name

    @property
    def dict_code(self):
        r"""Gets the dict_code of this ListVpcChannelsV2Request.

        VPC通道的字典编码  支持英文，数字，特殊字符（-_.）  暂不支持

        :return: The dict_code of this ListVpcChannelsV2Request.
        :rtype: str
        """
        return self._dict_code

    @dict_code.setter
    def dict_code(self, dict_code):
        r"""Sets the dict_code of this ListVpcChannelsV2Request.

        VPC通道的字典编码  支持英文，数字，特殊字符（-_.）  暂不支持

        :param dict_code: The dict_code of this ListVpcChannelsV2Request.
        :type dict_code: str
        """
        self._dict_code = dict_code

    @property
    def precise_search(self):
        r"""Gets the precise_search of this ListVpcChannelsV2Request.

        指定需要精确匹配查找的参数名称，多个参数需要支持精确匹配时参数之间使用“,”隔开。  目前支持name，member_group_name。

        :return: The precise_search of this ListVpcChannelsV2Request.
        :rtype: str
        """
        return self._precise_search

    @precise_search.setter
    def precise_search(self, precise_search):
        r"""Sets the precise_search of this ListVpcChannelsV2Request.

        指定需要精确匹配查找的参数名称，多个参数需要支持精确匹配时参数之间使用“,”隔开。  目前支持name，member_group_name。

        :param precise_search: The precise_search of this ListVpcChannelsV2Request.
        :type precise_search: str
        """
        self._precise_search = precise_search

    @property
    def member_host(self):
        r"""Gets the member_host of this ListVpcChannelsV2Request.

        后端服务地址。默认精确查询，不支持模糊查询。

        :return: The member_host of this ListVpcChannelsV2Request.
        :rtype: str
        """
        return self._member_host

    @member_host.setter
    def member_host(self, member_host):
        r"""Sets the member_host of this ListVpcChannelsV2Request.

        后端服务地址。默认精确查询，不支持模糊查询。

        :param member_host: The member_host of this ListVpcChannelsV2Request.
        :type member_host: str
        """
        self._member_host = member_host

    @property
    def member_port(self):
        r"""Gets the member_port of this ListVpcChannelsV2Request.

        后端服务器端口

        :return: The member_port of this ListVpcChannelsV2Request.
        :rtype: int
        """
        return self._member_port

    @member_port.setter
    def member_port(self, member_port):
        r"""Sets the member_port of this ListVpcChannelsV2Request.

        后端服务器端口

        :param member_port: The member_port of this ListVpcChannelsV2Request.
        :type member_port: int
        """
        self._member_port = member_port

    @property
    def member_group_name(self):
        r"""Gets the member_group_name of this ListVpcChannelsV2Request.

        后端服务器组名称

        :return: The member_group_name of this ListVpcChannelsV2Request.
        :rtype: str
        """
        return self._member_group_name

    @member_group_name.setter
    def member_group_name(self, member_group_name):
        r"""Sets the member_group_name of this ListVpcChannelsV2Request.

        后端服务器组名称

        :param member_group_name: The member_group_name of this ListVpcChannelsV2Request.
        :type member_group_name: str
        """
        self._member_group_name = member_group_name

    @property
    def member_group_id(self):
        r"""Gets the member_group_id of this ListVpcChannelsV2Request.

        后端服务器组编号

        :return: The member_group_id of this ListVpcChannelsV2Request.
        :rtype: str
        """
        return self._member_group_id

    @member_group_id.setter
    def member_group_id(self, member_group_id):
        r"""Sets the member_group_id of this ListVpcChannelsV2Request.

        后端服务器组编号

        :param member_group_id: The member_group_id of this ListVpcChannelsV2Request.
        :type member_group_id: str
        """
        self._member_group_id = member_group_id

    @property
    def vpc_channel_type(self):
        r"""Gets the vpc_channel_type of this ListVpcChannelsV2Request.

        vpc通道类型： - builtin：服务器类型 - microservice： 微服务类型 - reference：引用负载通道类型

        :return: The vpc_channel_type of this ListVpcChannelsV2Request.
        :rtype: str
        """
        return self._vpc_channel_type

    @vpc_channel_type.setter
    def vpc_channel_type(self, vpc_channel_type):
        r"""Sets the vpc_channel_type of this ListVpcChannelsV2Request.

        vpc通道类型： - builtin：服务器类型 - microservice： 微服务类型 - reference：引用负载通道类型

        :param vpc_channel_type: The vpc_channel_type of this ListVpcChannelsV2Request.
        :type vpc_channel_type: str
        """
        self._vpc_channel_type = vpc_channel_type

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
        if not isinstance(other, ListVpcChannelsV2Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
