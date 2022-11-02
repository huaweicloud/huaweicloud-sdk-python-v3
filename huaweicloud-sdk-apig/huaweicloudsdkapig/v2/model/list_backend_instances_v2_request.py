# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBackendInstancesV2Request:

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
        'vpc_channel_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'name': 'str',
        'member_group_name': 'str',
        'member_group_id': 'str',
        'precise_search': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'vpc_channel_id': 'vpc_channel_id',
        'offset': 'offset',
        'limit': 'limit',
        'name': 'name',
        'member_group_name': 'member_group_name',
        'member_group_id': 'member_group_id',
        'precise_search': 'precise_search'
    }

    def __init__(self, instance_id=None, vpc_channel_id=None, offset=None, limit=None, name=None, member_group_name=None, member_group_id=None, precise_search=None):
        """ListBackendInstancesV2Request

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param vpc_channel_id: VPC通道的编号
        :type vpc_channel_id: str
        :param offset: 偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0
        :type offset: int
        :param limit: 每页显示的条目数量，条目数量小于等于0时，自动转换为20，条目数量大于500时，自动转换为500
        :type limit: int
        :param name: 云服务器的名称
        :type name: str
        :param member_group_name: 后端服务器组名称。
        :type member_group_name: str
        :param member_group_id: 后端服务器组编号
        :type member_group_id: str
        :param precise_search: 指定需要精确匹配查找的参数名称，多个参数需要支持精确匹配时参数之间使用“,”隔开。  目前支持name，member_group_name。
        :type precise_search: str
        """
        
        

        self._instance_id = None
        self._vpc_channel_id = None
        self._offset = None
        self._limit = None
        self._name = None
        self._member_group_name = None
        self._member_group_id = None
        self._precise_search = None
        self.discriminator = None

        self.instance_id = instance_id
        self.vpc_channel_id = vpc_channel_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if name is not None:
            self.name = name
        if member_group_name is not None:
            self.member_group_name = member_group_name
        if member_group_id is not None:
            self.member_group_id = member_group_id
        if precise_search is not None:
            self.precise_search = precise_search

    @property
    def instance_id(self):
        """Gets the instance_id of this ListBackendInstancesV2Request.

        实例ID

        :return: The instance_id of this ListBackendInstancesV2Request.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListBackendInstancesV2Request.

        实例ID

        :param instance_id: The instance_id of this ListBackendInstancesV2Request.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def vpc_channel_id(self):
        """Gets the vpc_channel_id of this ListBackendInstancesV2Request.

        VPC通道的编号

        :return: The vpc_channel_id of this ListBackendInstancesV2Request.
        :rtype: str
        """
        return self._vpc_channel_id

    @vpc_channel_id.setter
    def vpc_channel_id(self, vpc_channel_id):
        """Sets the vpc_channel_id of this ListBackendInstancesV2Request.

        VPC通道的编号

        :param vpc_channel_id: The vpc_channel_id of this ListBackendInstancesV2Request.
        :type vpc_channel_id: str
        """
        self._vpc_channel_id = vpc_channel_id

    @property
    def offset(self):
        """Gets the offset of this ListBackendInstancesV2Request.

        偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0

        :return: The offset of this ListBackendInstancesV2Request.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListBackendInstancesV2Request.

        偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0

        :param offset: The offset of this ListBackendInstancesV2Request.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListBackendInstancesV2Request.

        每页显示的条目数量，条目数量小于等于0时，自动转换为20，条目数量大于500时，自动转换为500

        :return: The limit of this ListBackendInstancesV2Request.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListBackendInstancesV2Request.

        每页显示的条目数量，条目数量小于等于0时，自动转换为20，条目数量大于500时，自动转换为500

        :param limit: The limit of this ListBackendInstancesV2Request.
        :type limit: int
        """
        self._limit = limit

    @property
    def name(self):
        """Gets the name of this ListBackendInstancesV2Request.

        云服务器的名称

        :return: The name of this ListBackendInstancesV2Request.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListBackendInstancesV2Request.

        云服务器的名称

        :param name: The name of this ListBackendInstancesV2Request.
        :type name: str
        """
        self._name = name

    @property
    def member_group_name(self):
        """Gets the member_group_name of this ListBackendInstancesV2Request.

        后端服务器组名称。

        :return: The member_group_name of this ListBackendInstancesV2Request.
        :rtype: str
        """
        return self._member_group_name

    @member_group_name.setter
    def member_group_name(self, member_group_name):
        """Sets the member_group_name of this ListBackendInstancesV2Request.

        后端服务器组名称。

        :param member_group_name: The member_group_name of this ListBackendInstancesV2Request.
        :type member_group_name: str
        """
        self._member_group_name = member_group_name

    @property
    def member_group_id(self):
        """Gets the member_group_id of this ListBackendInstancesV2Request.

        后端服务器组编号

        :return: The member_group_id of this ListBackendInstancesV2Request.
        :rtype: str
        """
        return self._member_group_id

    @member_group_id.setter
    def member_group_id(self, member_group_id):
        """Sets the member_group_id of this ListBackendInstancesV2Request.

        后端服务器组编号

        :param member_group_id: The member_group_id of this ListBackendInstancesV2Request.
        :type member_group_id: str
        """
        self._member_group_id = member_group_id

    @property
    def precise_search(self):
        """Gets the precise_search of this ListBackendInstancesV2Request.

        指定需要精确匹配查找的参数名称，多个参数需要支持精确匹配时参数之间使用“,”隔开。  目前支持name，member_group_name。

        :return: The precise_search of this ListBackendInstancesV2Request.
        :rtype: str
        """
        return self._precise_search

    @precise_search.setter
    def precise_search(self, precise_search):
        """Sets the precise_search of this ListBackendInstancesV2Request.

        指定需要精确匹配查找的参数名称，多个参数需要支持精确匹配时参数之间使用“,”隔开。  目前支持name，member_group_name。

        :param precise_search: The precise_search of this ListBackendInstancesV2Request.
        :type precise_search: str
        """
        self._precise_search = precise_search

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
        if not isinstance(other, ListBackendInstancesV2Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
