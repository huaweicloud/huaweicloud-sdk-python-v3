# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEnvironmentVariablesV2Request:

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
        'group_id': 'str',
        'env_id': 'str',
        'variable_name': 'str',
        'precise_search': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'offset': 'offset',
        'limit': 'limit',
        'group_id': 'group_id',
        'env_id': 'env_id',
        'variable_name': 'variable_name',
        'precise_search': 'precise_search'
    }

    def __init__(self, instance_id=None, offset=None, limit=None, group_id=None, env_id=None, variable_name=None, precise_search=None):
        """ListEnvironmentVariablesV2Request

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param offset: 偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0
        :type offset: int
        :param limit: 每页显示的条目数量，条目数量小于等于0时，自动转换为20，条目数量大于500时，自动转换为500
        :type limit: int
        :param group_id: API分组编号
        :type group_id: str
        :param env_id: 环境编号
        :type env_id: str
        :param variable_name: 变量名
        :type variable_name: str
        :param precise_search: 指定需要精确匹配查找的参数名称，目前仅支持name
        :type precise_search: str
        """
        
        

        self._instance_id = None
        self._offset = None
        self._limit = None
        self._group_id = None
        self._env_id = None
        self._variable_name = None
        self._precise_search = None
        self.discriminator = None

        self.instance_id = instance_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        self.group_id = group_id
        if env_id is not None:
            self.env_id = env_id
        if variable_name is not None:
            self.variable_name = variable_name
        if precise_search is not None:
            self.precise_search = precise_search

    @property
    def instance_id(self):
        """Gets the instance_id of this ListEnvironmentVariablesV2Request.

        实例ID

        :return: The instance_id of this ListEnvironmentVariablesV2Request.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListEnvironmentVariablesV2Request.

        实例ID

        :param instance_id: The instance_id of this ListEnvironmentVariablesV2Request.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def offset(self):
        """Gets the offset of this ListEnvironmentVariablesV2Request.

        偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0

        :return: The offset of this ListEnvironmentVariablesV2Request.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListEnvironmentVariablesV2Request.

        偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0

        :param offset: The offset of this ListEnvironmentVariablesV2Request.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListEnvironmentVariablesV2Request.

        每页显示的条目数量，条目数量小于等于0时，自动转换为20，条目数量大于500时，自动转换为500

        :return: The limit of this ListEnvironmentVariablesV2Request.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListEnvironmentVariablesV2Request.

        每页显示的条目数量，条目数量小于等于0时，自动转换为20，条目数量大于500时，自动转换为500

        :param limit: The limit of this ListEnvironmentVariablesV2Request.
        :type limit: int
        """
        self._limit = limit

    @property
    def group_id(self):
        """Gets the group_id of this ListEnvironmentVariablesV2Request.

        API分组编号

        :return: The group_id of this ListEnvironmentVariablesV2Request.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this ListEnvironmentVariablesV2Request.

        API分组编号

        :param group_id: The group_id of this ListEnvironmentVariablesV2Request.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def env_id(self):
        """Gets the env_id of this ListEnvironmentVariablesV2Request.

        环境编号

        :return: The env_id of this ListEnvironmentVariablesV2Request.
        :rtype: str
        """
        return self._env_id

    @env_id.setter
    def env_id(self, env_id):
        """Sets the env_id of this ListEnvironmentVariablesV2Request.

        环境编号

        :param env_id: The env_id of this ListEnvironmentVariablesV2Request.
        :type env_id: str
        """
        self._env_id = env_id

    @property
    def variable_name(self):
        """Gets the variable_name of this ListEnvironmentVariablesV2Request.

        变量名

        :return: The variable_name of this ListEnvironmentVariablesV2Request.
        :rtype: str
        """
        return self._variable_name

    @variable_name.setter
    def variable_name(self, variable_name):
        """Sets the variable_name of this ListEnvironmentVariablesV2Request.

        变量名

        :param variable_name: The variable_name of this ListEnvironmentVariablesV2Request.
        :type variable_name: str
        """
        self._variable_name = variable_name

    @property
    def precise_search(self):
        """Gets the precise_search of this ListEnvironmentVariablesV2Request.

        指定需要精确匹配查找的参数名称，目前仅支持name

        :return: The precise_search of this ListEnvironmentVariablesV2Request.
        :rtype: str
        """
        return self._precise_search

    @precise_search.setter
    def precise_search(self, precise_search):
        """Sets the precise_search of this ListEnvironmentVariablesV2Request.

        指定需要精确匹配查找的参数名称，目前仅支持name

        :param precise_search: The precise_search of this ListEnvironmentVariablesV2Request.
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
        if not isinstance(other, ListEnvironmentVariablesV2Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
