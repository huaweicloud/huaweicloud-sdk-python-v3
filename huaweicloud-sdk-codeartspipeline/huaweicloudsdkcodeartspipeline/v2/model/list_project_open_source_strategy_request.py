# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListProjectOpenSourceStrategyRequest:

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
        'name': 'str',
        'creator_name': 'str',
        'include_tenant_rule_set': 'bool',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'project_id': 'project_id',
        'name': 'name',
        'creator_name': 'creator_name',
        'include_tenant_rule_set': 'include_tenant_rule_set',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, project_id=None, name=None, creator_name=None, include_tenant_rule_set=None, limit=None, offset=None):
        """ListProjectOpenSourceStrategyRequest

        The model defined in huaweicloud sdk

        :param project_id: 项目ID
        :type project_id: str
        :param name: 策略名称
        :type name: str
        :param creator_name: 策略创建人名称
        :type creator_name: str
        :param include_tenant_rule_set: 是否包含当前项目所属租户的策略
        :type include_tenant_rule_set: bool
        :param limit: 分页参数，默认15
        :type limit: int
        :param offset: 分页参数，默认0
        :type offset: int
        """
        
        

        self._project_id = None
        self._name = None
        self._creator_name = None
        self._include_tenant_rule_set = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.project_id = project_id
        if name is not None:
            self.name = name
        if creator_name is not None:
            self.creator_name = creator_name
        self.include_tenant_rule_set = include_tenant_rule_set
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def project_id(self):
        """Gets the project_id of this ListProjectOpenSourceStrategyRequest.

        项目ID

        :return: The project_id of this ListProjectOpenSourceStrategyRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ListProjectOpenSourceStrategyRequest.

        项目ID

        :param project_id: The project_id of this ListProjectOpenSourceStrategyRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def name(self):
        """Gets the name of this ListProjectOpenSourceStrategyRequest.

        策略名称

        :return: The name of this ListProjectOpenSourceStrategyRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListProjectOpenSourceStrategyRequest.

        策略名称

        :param name: The name of this ListProjectOpenSourceStrategyRequest.
        :type name: str
        """
        self._name = name

    @property
    def creator_name(self):
        """Gets the creator_name of this ListProjectOpenSourceStrategyRequest.

        策略创建人名称

        :return: The creator_name of this ListProjectOpenSourceStrategyRequest.
        :rtype: str
        """
        return self._creator_name

    @creator_name.setter
    def creator_name(self, creator_name):
        """Sets the creator_name of this ListProjectOpenSourceStrategyRequest.

        策略创建人名称

        :param creator_name: The creator_name of this ListProjectOpenSourceStrategyRequest.
        :type creator_name: str
        """
        self._creator_name = creator_name

    @property
    def include_tenant_rule_set(self):
        """Gets the include_tenant_rule_set of this ListProjectOpenSourceStrategyRequest.

        是否包含当前项目所属租户的策略

        :return: The include_tenant_rule_set of this ListProjectOpenSourceStrategyRequest.
        :rtype: bool
        """
        return self._include_tenant_rule_set

    @include_tenant_rule_set.setter
    def include_tenant_rule_set(self, include_tenant_rule_set):
        """Sets the include_tenant_rule_set of this ListProjectOpenSourceStrategyRequest.

        是否包含当前项目所属租户的策略

        :param include_tenant_rule_set: The include_tenant_rule_set of this ListProjectOpenSourceStrategyRequest.
        :type include_tenant_rule_set: bool
        """
        self._include_tenant_rule_set = include_tenant_rule_set

    @property
    def limit(self):
        """Gets the limit of this ListProjectOpenSourceStrategyRequest.

        分页参数，默认15

        :return: The limit of this ListProjectOpenSourceStrategyRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListProjectOpenSourceStrategyRequest.

        分页参数，默认15

        :param limit: The limit of this ListProjectOpenSourceStrategyRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListProjectOpenSourceStrategyRequest.

        分页参数，默认0

        :return: The offset of this ListProjectOpenSourceStrategyRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListProjectOpenSourceStrategyRequest.

        分页参数，默认0

        :param offset: The offset of this ListProjectOpenSourceStrategyRequest.
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
        if not isinstance(other, ListProjectOpenSourceStrategyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
