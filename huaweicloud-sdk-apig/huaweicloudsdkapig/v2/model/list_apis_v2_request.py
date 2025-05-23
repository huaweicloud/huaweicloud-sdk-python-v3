# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListApisV2Request:

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
        'group_id': 'str',
        'req_protocol': 'str',
        'req_method': 'str',
        'req_uri': 'str',
        'auth_type': 'str',
        'env_id': 'str',
        'type': 'int',
        'precise_search': 'str',
        'vpc_channel_name': 'str',
        'return_data_mode': 'str',
        'tags': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'offset': 'offset',
        'limit': 'limit',
        'id': 'id',
        'name': 'name',
        'group_id': 'group_id',
        'req_protocol': 'req_protocol',
        'req_method': 'req_method',
        'req_uri': 'req_uri',
        'auth_type': 'auth_type',
        'env_id': 'env_id',
        'type': 'type',
        'precise_search': 'precise_search',
        'vpc_channel_name': 'vpc_channel_name',
        'return_data_mode': 'return_data_mode',
        'tags': 'tags'
    }

    def __init__(self, instance_id=None, offset=None, limit=None, id=None, name=None, group_id=None, req_protocol=None, req_method=None, req_uri=None, auth_type=None, env_id=None, type=None, precise_search=None, vpc_channel_name=None, return_data_mode=None, tags=None):
        r"""ListApisV2Request

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID，在API网关控制台的“实例信息”中获取。
        :type instance_id: str
        :param offset: 偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0
        :type offset: int
        :param limit: 每页显示的条目数量，条目数量小于等于0时，自动转换为20，条目数量大于500时，自动转换为500
        :type limit: int
        :param id: API编号
        :type id: str
        :param name: API名称
        :type name: str
        :param group_id: API分组编号
        :type group_id: str
        :param req_protocol: 请求协议
        :type req_protocol: str
        :param req_method: 请求方法
        :type req_method: str
        :param req_uri: 请求路径
        :type req_uri: str
        :param auth_type: 授权类型
        :type auth_type: str
        :param env_id: 发布的环境编号
        :type env_id: str
        :param type: API类型
        :type type: int
        :param precise_search: 指定需要精确匹配查找的参数名称，目前仅支持name、req_uri
        :type precise_search: str
        :param vpc_channel_name: 负载通道名称
        :type vpc_channel_name: str
        :param return_data_mode: 指定API详情中需要包含的额外返回结果，多个参数之间使用“,”隔开，当brief和其他include参数共同使用时，brief不生效。 目前仅支持brief，include_group，include_group_backend。 brief：默认值，不包含额外信息。 include_group：返回结果中包含api_group_info。 include_group_backend：返回结果中包含backend_api。
        :type return_data_mode: str
        :param tags: API标签，该参数可指定多个，多个不同的参数值为或关系；不指定或为空时，表示不筛选标签；指定为#no_tags#时，表示筛选无标签API。
        :type tags: str
        """
        
        

        self._instance_id = None
        self._offset = None
        self._limit = None
        self._id = None
        self._name = None
        self._group_id = None
        self._req_protocol = None
        self._req_method = None
        self._req_uri = None
        self._auth_type = None
        self._env_id = None
        self._type = None
        self._precise_search = None
        self._vpc_channel_name = None
        self._return_data_mode = None
        self._tags = None
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
        if group_id is not None:
            self.group_id = group_id
        if req_protocol is not None:
            self.req_protocol = req_protocol
        if req_method is not None:
            self.req_method = req_method
        if req_uri is not None:
            self.req_uri = req_uri
        if auth_type is not None:
            self.auth_type = auth_type
        if env_id is not None:
            self.env_id = env_id
        if type is not None:
            self.type = type
        if precise_search is not None:
            self.precise_search = precise_search
        if vpc_channel_name is not None:
            self.vpc_channel_name = vpc_channel_name
        if return_data_mode is not None:
            self.return_data_mode = return_data_mode
        if tags is not None:
            self.tags = tags

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListApisV2Request.

        实例ID，在API网关控制台的“实例信息”中获取。

        :return: The instance_id of this ListApisV2Request.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListApisV2Request.

        实例ID，在API网关控制台的“实例信息”中获取。

        :param instance_id: The instance_id of this ListApisV2Request.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def offset(self):
        r"""Gets the offset of this ListApisV2Request.

        偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0

        :return: The offset of this ListApisV2Request.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListApisV2Request.

        偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0

        :param offset: The offset of this ListApisV2Request.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListApisV2Request.

        每页显示的条目数量，条目数量小于等于0时，自动转换为20，条目数量大于500时，自动转换为500

        :return: The limit of this ListApisV2Request.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListApisV2Request.

        每页显示的条目数量，条目数量小于等于0时，自动转换为20，条目数量大于500时，自动转换为500

        :param limit: The limit of this ListApisV2Request.
        :type limit: int
        """
        self._limit = limit

    @property
    def id(self):
        r"""Gets the id of this ListApisV2Request.

        API编号

        :return: The id of this ListApisV2Request.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListApisV2Request.

        API编号

        :param id: The id of this ListApisV2Request.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ListApisV2Request.

        API名称

        :return: The name of this ListApisV2Request.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListApisV2Request.

        API名称

        :param name: The name of this ListApisV2Request.
        :type name: str
        """
        self._name = name

    @property
    def group_id(self):
        r"""Gets the group_id of this ListApisV2Request.

        API分组编号

        :return: The group_id of this ListApisV2Request.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this ListApisV2Request.

        API分组编号

        :param group_id: The group_id of this ListApisV2Request.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def req_protocol(self):
        r"""Gets the req_protocol of this ListApisV2Request.

        请求协议

        :return: The req_protocol of this ListApisV2Request.
        :rtype: str
        """
        return self._req_protocol

    @req_protocol.setter
    def req_protocol(self, req_protocol):
        r"""Sets the req_protocol of this ListApisV2Request.

        请求协议

        :param req_protocol: The req_protocol of this ListApisV2Request.
        :type req_protocol: str
        """
        self._req_protocol = req_protocol

    @property
    def req_method(self):
        r"""Gets the req_method of this ListApisV2Request.

        请求方法

        :return: The req_method of this ListApisV2Request.
        :rtype: str
        """
        return self._req_method

    @req_method.setter
    def req_method(self, req_method):
        r"""Sets the req_method of this ListApisV2Request.

        请求方法

        :param req_method: The req_method of this ListApisV2Request.
        :type req_method: str
        """
        self._req_method = req_method

    @property
    def req_uri(self):
        r"""Gets the req_uri of this ListApisV2Request.

        请求路径

        :return: The req_uri of this ListApisV2Request.
        :rtype: str
        """
        return self._req_uri

    @req_uri.setter
    def req_uri(self, req_uri):
        r"""Sets the req_uri of this ListApisV2Request.

        请求路径

        :param req_uri: The req_uri of this ListApisV2Request.
        :type req_uri: str
        """
        self._req_uri = req_uri

    @property
    def auth_type(self):
        r"""Gets the auth_type of this ListApisV2Request.

        授权类型

        :return: The auth_type of this ListApisV2Request.
        :rtype: str
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        r"""Sets the auth_type of this ListApisV2Request.

        授权类型

        :param auth_type: The auth_type of this ListApisV2Request.
        :type auth_type: str
        """
        self._auth_type = auth_type

    @property
    def env_id(self):
        r"""Gets the env_id of this ListApisV2Request.

        发布的环境编号

        :return: The env_id of this ListApisV2Request.
        :rtype: str
        """
        return self._env_id

    @env_id.setter
    def env_id(self, env_id):
        r"""Sets the env_id of this ListApisV2Request.

        发布的环境编号

        :param env_id: The env_id of this ListApisV2Request.
        :type env_id: str
        """
        self._env_id = env_id

    @property
    def type(self):
        r"""Gets the type of this ListApisV2Request.

        API类型

        :return: The type of this ListApisV2Request.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListApisV2Request.

        API类型

        :param type: The type of this ListApisV2Request.
        :type type: int
        """
        self._type = type

    @property
    def precise_search(self):
        r"""Gets the precise_search of this ListApisV2Request.

        指定需要精确匹配查找的参数名称，目前仅支持name、req_uri

        :return: The precise_search of this ListApisV2Request.
        :rtype: str
        """
        return self._precise_search

    @precise_search.setter
    def precise_search(self, precise_search):
        r"""Sets the precise_search of this ListApisV2Request.

        指定需要精确匹配查找的参数名称，目前仅支持name、req_uri

        :param precise_search: The precise_search of this ListApisV2Request.
        :type precise_search: str
        """
        self._precise_search = precise_search

    @property
    def vpc_channel_name(self):
        r"""Gets the vpc_channel_name of this ListApisV2Request.

        负载通道名称

        :return: The vpc_channel_name of this ListApisV2Request.
        :rtype: str
        """
        return self._vpc_channel_name

    @vpc_channel_name.setter
    def vpc_channel_name(self, vpc_channel_name):
        r"""Sets the vpc_channel_name of this ListApisV2Request.

        负载通道名称

        :param vpc_channel_name: The vpc_channel_name of this ListApisV2Request.
        :type vpc_channel_name: str
        """
        self._vpc_channel_name = vpc_channel_name

    @property
    def return_data_mode(self):
        r"""Gets the return_data_mode of this ListApisV2Request.

        指定API详情中需要包含的额外返回结果，多个参数之间使用“,”隔开，当brief和其他include参数共同使用时，brief不生效。 目前仅支持brief，include_group，include_group_backend。 brief：默认值，不包含额外信息。 include_group：返回结果中包含api_group_info。 include_group_backend：返回结果中包含backend_api。

        :return: The return_data_mode of this ListApisV2Request.
        :rtype: str
        """
        return self._return_data_mode

    @return_data_mode.setter
    def return_data_mode(self, return_data_mode):
        r"""Sets the return_data_mode of this ListApisV2Request.

        指定API详情中需要包含的额外返回结果，多个参数之间使用“,”隔开，当brief和其他include参数共同使用时，brief不生效。 目前仅支持brief，include_group，include_group_backend。 brief：默认值，不包含额外信息。 include_group：返回结果中包含api_group_info。 include_group_backend：返回结果中包含backend_api。

        :param return_data_mode: The return_data_mode of this ListApisV2Request.
        :type return_data_mode: str
        """
        self._return_data_mode = return_data_mode

    @property
    def tags(self):
        r"""Gets the tags of this ListApisV2Request.

        API标签，该参数可指定多个，多个不同的参数值为或关系；不指定或为空时，表示不筛选标签；指定为#no_tags#时，表示筛选无标签API。

        :return: The tags of this ListApisV2Request.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ListApisV2Request.

        API标签，该参数可指定多个，多个不同的参数值为或关系；不指定或为空时，表示不筛选标签；指定为#no_tags#时，表示筛选无标签API。

        :param tags: The tags of this ListApisV2Request.
        :type tags: str
        """
        self._tags = tags

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
        if not isinstance(other, ListApisV2Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
