# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRuleRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_id': 'str',
        'cloud_project_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'type': 'str',
        'name': 'str'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'cloud_project_id': 'cloud_project_id',
        'offset': 'offset',
        'limit': 'limit',
        'type': 'type',
        'name': 'name'
    }

    def __init__(self, domain_id=None, cloud_project_id=None, offset=None, limit=None, type=None, name=None):
        """ListRuleRequest

        The model defined in huaweicloud sdk

        :param domain_id: 租户ID
        :type domain_id: str
        :param cloud_project_id: 项目ID
        :type cloud_project_id: str
        :param offset: 偏移量，表示从此偏移量开始查询，offset大于等于0
        :type offset: int
        :param limit: 每页显示的条目数量
        :type limit: int
        :param type: 类型
        :type type: str
        :param name: 规则名称，用于模糊搜索
        :type name: str
        """
        
        

        self._domain_id = None
        self._cloud_project_id = None
        self._offset = None
        self._limit = None
        self._type = None
        self._name = None
        self.discriminator = None

        self.domain_id = domain_id
        if cloud_project_id is not None:
            self.cloud_project_id = cloud_project_id
        self.offset = offset
        self.limit = limit
        if type is not None:
            self.type = type
        if name is not None:
            self.name = name

    @property
    def domain_id(self):
        """Gets the domain_id of this ListRuleRequest.

        租户ID

        :return: The domain_id of this ListRuleRequest.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this ListRuleRequest.

        租户ID

        :param domain_id: The domain_id of this ListRuleRequest.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def cloud_project_id(self):
        """Gets the cloud_project_id of this ListRuleRequest.

        项目ID

        :return: The cloud_project_id of this ListRuleRequest.
        :rtype: str
        """
        return self._cloud_project_id

    @cloud_project_id.setter
    def cloud_project_id(self, cloud_project_id):
        """Sets the cloud_project_id of this ListRuleRequest.

        项目ID

        :param cloud_project_id: The cloud_project_id of this ListRuleRequest.
        :type cloud_project_id: str
        """
        self._cloud_project_id = cloud_project_id

    @property
    def offset(self):
        """Gets the offset of this ListRuleRequest.

        偏移量，表示从此偏移量开始查询，offset大于等于0

        :return: The offset of this ListRuleRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListRuleRequest.

        偏移量，表示从此偏移量开始查询，offset大于等于0

        :param offset: The offset of this ListRuleRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListRuleRequest.

        每页显示的条目数量

        :return: The limit of this ListRuleRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListRuleRequest.

        每页显示的条目数量

        :param limit: The limit of this ListRuleRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def type(self):
        """Gets the type of this ListRuleRequest.

        类型

        :return: The type of this ListRuleRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListRuleRequest.

        类型

        :param type: The type of this ListRuleRequest.
        :type type: str
        """
        self._type = type

    @property
    def name(self):
        """Gets the name of this ListRuleRequest.

        规则名称，用于模糊搜索

        :return: The name of this ListRuleRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListRuleRequest.

        规则名称，用于模糊搜索

        :param name: The name of this ListRuleRequest.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, ListRuleRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
