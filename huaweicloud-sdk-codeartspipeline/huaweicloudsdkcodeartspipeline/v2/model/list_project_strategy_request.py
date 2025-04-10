# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListProjectStrategyRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'include_tenant_rule_set': 'bool',
        'name': 'str',
        'is_valid': 'bool',
        'type': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'offset': 'offset',
        'limit': 'limit',
        'include_tenant_rule_set': 'include_tenant_rule_set',
        'name': 'name',
        'is_valid': 'is_valid',
        'type': 'type'
    }

    def __init__(self, project_id=None, offset=None, limit=None, include_tenant_rule_set=None, name=None, is_valid=None, type=None):
        r"""ListProjectStrategyRequest

        The model defined in huaweicloud sdk

        :param project_id: 项目ID
        :type project_id: str
        :param offset: 偏移量，表示从此偏移量开始查询，offset大于等于0
        :type offset: int
        :param limit: 每页显示的条目数量
        :type limit: int
        :param include_tenant_rule_set: 是否包含租户级规则
        :type include_tenant_rule_set: bool
        :param name: 策略名称，用于模糊查询
        :type name: str
        :param is_valid: 是否有效
        :type is_valid: bool
        :param type: 策略类型
        :type type: str
        """
        
        

        self._project_id = None
        self._offset = None
        self._limit = None
        self._include_tenant_rule_set = None
        self._name = None
        self._is_valid = None
        self._type = None
        self.discriminator = None

        self.project_id = project_id
        self.offset = offset
        self.limit = limit
        self.include_tenant_rule_set = include_tenant_rule_set
        if name is not None:
            self.name = name
        if is_valid is not None:
            self.is_valid = is_valid
        if type is not None:
            self.type = type

    @property
    def project_id(self):
        r"""Gets the project_id of this ListProjectStrategyRequest.

        项目ID

        :return: The project_id of this ListProjectStrategyRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListProjectStrategyRequest.

        项目ID

        :param project_id: The project_id of this ListProjectStrategyRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def offset(self):
        r"""Gets the offset of this ListProjectStrategyRequest.

        偏移量，表示从此偏移量开始查询，offset大于等于0

        :return: The offset of this ListProjectStrategyRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListProjectStrategyRequest.

        偏移量，表示从此偏移量开始查询，offset大于等于0

        :param offset: The offset of this ListProjectStrategyRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListProjectStrategyRequest.

        每页显示的条目数量

        :return: The limit of this ListProjectStrategyRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListProjectStrategyRequest.

        每页显示的条目数量

        :param limit: The limit of this ListProjectStrategyRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def include_tenant_rule_set(self):
        r"""Gets the include_tenant_rule_set of this ListProjectStrategyRequest.

        是否包含租户级规则

        :return: The include_tenant_rule_set of this ListProjectStrategyRequest.
        :rtype: bool
        """
        return self._include_tenant_rule_set

    @include_tenant_rule_set.setter
    def include_tenant_rule_set(self, include_tenant_rule_set):
        r"""Sets the include_tenant_rule_set of this ListProjectStrategyRequest.

        是否包含租户级规则

        :param include_tenant_rule_set: The include_tenant_rule_set of this ListProjectStrategyRequest.
        :type include_tenant_rule_set: bool
        """
        self._include_tenant_rule_set = include_tenant_rule_set

    @property
    def name(self):
        r"""Gets the name of this ListProjectStrategyRequest.

        策略名称，用于模糊查询

        :return: The name of this ListProjectStrategyRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListProjectStrategyRequest.

        策略名称，用于模糊查询

        :param name: The name of this ListProjectStrategyRequest.
        :type name: str
        """
        self._name = name

    @property
    def is_valid(self):
        r"""Gets the is_valid of this ListProjectStrategyRequest.

        是否有效

        :return: The is_valid of this ListProjectStrategyRequest.
        :rtype: bool
        """
        return self._is_valid

    @is_valid.setter
    def is_valid(self, is_valid):
        r"""Sets the is_valid of this ListProjectStrategyRequest.

        是否有效

        :param is_valid: The is_valid of this ListProjectStrategyRequest.
        :type is_valid: bool
        """
        self._is_valid = is_valid

    @property
    def type(self):
        r"""Gets the type of this ListProjectStrategyRequest.

        策略类型

        :return: The type of this ListProjectStrategyRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListProjectStrategyRequest.

        策略类型

        :param type: The type of this ListProjectStrategyRequest.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, ListProjectStrategyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
