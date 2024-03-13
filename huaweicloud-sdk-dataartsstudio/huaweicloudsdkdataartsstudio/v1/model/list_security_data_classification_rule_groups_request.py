# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSecurityDataClassificationRuleGroupsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace': 'str',
        'limit': 'int',
        'offset': 'int',
        'name': 'str',
        'creator': 'str',
        'order_by': 'str',
        'desc': 'bool'
    }

    attribute_map = {
        'workspace': 'workspace',
        'limit': 'limit',
        'offset': 'offset',
        'name': 'name',
        'creator': 'creator',
        'order_by': 'order_by',
        'desc': 'desc'
    }

    def __init__(self, workspace=None, limit=None, offset=None, name=None, creator=None, order_by=None, desc=None):
        """ListSecurityDataClassificationRuleGroupsRequest

        The model defined in huaweicloud sdk

        :param workspace: DataArts Studio工作空间ID
        :type workspace: str
        :param limit: limit
        :type limit: int
        :param offset: offset
        :type offset: int
        :param name: 规则组名称
        :type name: str
        :param creator: 规则组创建者
        :type creator: str
        :param order_by: 排序字段, createdAt, createdBy, updatedAt, updatedBy, name, description
        :type order_by: str
        :param desc: 是否降序
        :type desc: bool
        """
        
        

        self._workspace = None
        self._limit = None
        self._offset = None
        self._name = None
        self._creator = None
        self._order_by = None
        self._desc = None
        self.discriminator = None

        self.workspace = workspace
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if name is not None:
            self.name = name
        if creator is not None:
            self.creator = creator
        if order_by is not None:
            self.order_by = order_by
        if desc is not None:
            self.desc = desc

    @property
    def workspace(self):
        """Gets the workspace of this ListSecurityDataClassificationRuleGroupsRequest.

        DataArts Studio工作空间ID

        :return: The workspace of this ListSecurityDataClassificationRuleGroupsRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this ListSecurityDataClassificationRuleGroupsRequest.

        DataArts Studio工作空间ID

        :param workspace: The workspace of this ListSecurityDataClassificationRuleGroupsRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def limit(self):
        """Gets the limit of this ListSecurityDataClassificationRuleGroupsRequest.

        limit

        :return: The limit of this ListSecurityDataClassificationRuleGroupsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListSecurityDataClassificationRuleGroupsRequest.

        limit

        :param limit: The limit of this ListSecurityDataClassificationRuleGroupsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListSecurityDataClassificationRuleGroupsRequest.

        offset

        :return: The offset of this ListSecurityDataClassificationRuleGroupsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListSecurityDataClassificationRuleGroupsRequest.

        offset

        :param offset: The offset of this ListSecurityDataClassificationRuleGroupsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def name(self):
        """Gets the name of this ListSecurityDataClassificationRuleGroupsRequest.

        规则组名称

        :return: The name of this ListSecurityDataClassificationRuleGroupsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListSecurityDataClassificationRuleGroupsRequest.

        规则组名称

        :param name: The name of this ListSecurityDataClassificationRuleGroupsRequest.
        :type name: str
        """
        self._name = name

    @property
    def creator(self):
        """Gets the creator of this ListSecurityDataClassificationRuleGroupsRequest.

        规则组创建者

        :return: The creator of this ListSecurityDataClassificationRuleGroupsRequest.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this ListSecurityDataClassificationRuleGroupsRequest.

        规则组创建者

        :param creator: The creator of this ListSecurityDataClassificationRuleGroupsRequest.
        :type creator: str
        """
        self._creator = creator

    @property
    def order_by(self):
        """Gets the order_by of this ListSecurityDataClassificationRuleGroupsRequest.

        排序字段, createdAt, createdBy, updatedAt, updatedBy, name, description

        :return: The order_by of this ListSecurityDataClassificationRuleGroupsRequest.
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        """Sets the order_by of this ListSecurityDataClassificationRuleGroupsRequest.

        排序字段, createdAt, createdBy, updatedAt, updatedBy, name, description

        :param order_by: The order_by of this ListSecurityDataClassificationRuleGroupsRequest.
        :type order_by: str
        """
        self._order_by = order_by

    @property
    def desc(self):
        """Gets the desc of this ListSecurityDataClassificationRuleGroupsRequest.

        是否降序

        :return: The desc of this ListSecurityDataClassificationRuleGroupsRequest.
        :rtype: bool
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """Sets the desc of this ListSecurityDataClassificationRuleGroupsRequest.

        是否降序

        :param desc: The desc of this ListSecurityDataClassificationRuleGroupsRequest.
        :type desc: bool
        """
        self._desc = desc

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
        if not isinstance(other, ListSecurityDataClassificationRuleGroupsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
