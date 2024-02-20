# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Finding:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action': 'list[str]',
        'analyzed_at': 'datetime',
        'condition': 'list[FindingCondition]',
        'created_at': 'datetime',
        'id': 'str',
        'is_public': 'bool',
        'principal': 'FindingPrincipal',
        'resource': 'str',
        'resource_id': 'str',
        'resource_owner_account': 'str',
        'resource_type': 'ResourceType',
        'sources': 'list[FindingSourceType]',
        'status': 'str',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'action': 'action',
        'analyzed_at': 'analyzed_at',
        'condition': 'condition',
        'created_at': 'created_at',
        'id': 'id',
        'is_public': 'is_public',
        'principal': 'principal',
        'resource': 'resource',
        'resource_id': 'resource_id',
        'resource_owner_account': 'resource_owner_account',
        'resource_type': 'resource_type',
        'sources': 'sources',
        'status': 'status',
        'updated_at': 'updated_at'
    }

    def __init__(self, action=None, analyzed_at=None, condition=None, created_at=None, id=None, is_public=None, principal=None, resource=None, resource_id=None, resource_owner_account=None, resource_type=None, sources=None, status=None, updated_at=None):
        """Finding

        The model defined in huaweicloud sdk

        :param action: 访问信任区域内资源的外部主体。
        :type action: list[str]
        :param analyzed_at: 分析资源的时间。
        :type analyzed_at: datetime
        :param condition: 
        :type condition: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.FindingCondition`]
        :param created_at: 生成查找结果的时间。
        :type created_at: datetime
        :param id: 要检索的结果的ID。
        :type id: str
        :param is_public: 表示生成查找结果的策略是否允许公共访问资源。
        :type is_public: bool
        :param principal: 
        :type principal: :class:`huaweicloudsdkiamaccessanalyzer.v1.FindingPrincipal`
        :param resource: 唯一的资源名称。
        :type resource: str
        :param resource_id: 资源的唯一标识符。
        :type resource_id: str
        :param resource_owner_account: 拥有资源的帐户ID。
        :type resource_owner_account: str
        :param resource_type: 
        :type resource_type: :class:`huaweicloudsdkiamaccessanalyzer.v1.ResourceType`
        :param sources: 
        :type sources: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.FindingSourceType`]
        :param status: 结果的当前状态。
        :type status: str
        :param updated_at: 更新调查结果的时间。
        :type updated_at: datetime
        """
        
        

        self._action = None
        self._analyzed_at = None
        self._condition = None
        self._created_at = None
        self._id = None
        self._is_public = None
        self._principal = None
        self._resource = None
        self._resource_id = None
        self._resource_owner_account = None
        self._resource_type = None
        self._sources = None
        self._status = None
        self._updated_at = None
        self.discriminator = None

        self.action = action
        self.analyzed_at = analyzed_at
        self.condition = condition
        self.created_at = created_at
        self.id = id
        self.is_public = is_public
        self.principal = principal
        self.resource = resource
        if resource_id is not None:
            self.resource_id = resource_id
        self.resource_owner_account = resource_owner_account
        self.resource_type = resource_type
        if sources is not None:
            self.sources = sources
        self.status = status
        self.updated_at = updated_at

    @property
    def action(self):
        """Gets the action of this Finding.

        访问信任区域内资源的外部主体。

        :return: The action of this Finding.
        :rtype: list[str]
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this Finding.

        访问信任区域内资源的外部主体。

        :param action: The action of this Finding.
        :type action: list[str]
        """
        self._action = action

    @property
    def analyzed_at(self):
        """Gets the analyzed_at of this Finding.

        分析资源的时间。

        :return: The analyzed_at of this Finding.
        :rtype: datetime
        """
        return self._analyzed_at

    @analyzed_at.setter
    def analyzed_at(self, analyzed_at):
        """Sets the analyzed_at of this Finding.

        分析资源的时间。

        :param analyzed_at: The analyzed_at of this Finding.
        :type analyzed_at: datetime
        """
        self._analyzed_at = analyzed_at

    @property
    def condition(self):
        """Gets the condition of this Finding.

        :return: The condition of this Finding.
        :rtype: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.FindingCondition`]
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this Finding.

        :param condition: The condition of this Finding.
        :type condition: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.FindingCondition`]
        """
        self._condition = condition

    @property
    def created_at(self):
        """Gets the created_at of this Finding.

        生成查找结果的时间。

        :return: The created_at of this Finding.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Finding.

        生成查找结果的时间。

        :param created_at: The created_at of this Finding.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def id(self):
        """Gets the id of this Finding.

        要检索的结果的ID。

        :return: The id of this Finding.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Finding.

        要检索的结果的ID。

        :param id: The id of this Finding.
        :type id: str
        """
        self._id = id

    @property
    def is_public(self):
        """Gets the is_public of this Finding.

        表示生成查找结果的策略是否允许公共访问资源。

        :return: The is_public of this Finding.
        :rtype: bool
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        """Sets the is_public of this Finding.

        表示生成查找结果的策略是否允许公共访问资源。

        :param is_public: The is_public of this Finding.
        :type is_public: bool
        """
        self._is_public = is_public

    @property
    def principal(self):
        """Gets the principal of this Finding.

        :return: The principal of this Finding.
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.FindingPrincipal`
        """
        return self._principal

    @principal.setter
    def principal(self, principal):
        """Sets the principal of this Finding.

        :param principal: The principal of this Finding.
        :type principal: :class:`huaweicloudsdkiamaccessanalyzer.v1.FindingPrincipal`
        """
        self._principal = principal

    @property
    def resource(self):
        """Gets the resource of this Finding.

        唯一的资源名称。

        :return: The resource of this Finding.
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this Finding.

        唯一的资源名称。

        :param resource: The resource of this Finding.
        :type resource: str
        """
        self._resource = resource

    @property
    def resource_id(self):
        """Gets the resource_id of this Finding.

        资源的唯一标识符。

        :return: The resource_id of this Finding.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this Finding.

        资源的唯一标识符。

        :param resource_id: The resource_id of this Finding.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_owner_account(self):
        """Gets the resource_owner_account of this Finding.

        拥有资源的帐户ID。

        :return: The resource_owner_account of this Finding.
        :rtype: str
        """
        return self._resource_owner_account

    @resource_owner_account.setter
    def resource_owner_account(self, resource_owner_account):
        """Sets the resource_owner_account of this Finding.

        拥有资源的帐户ID。

        :param resource_owner_account: The resource_owner_account of this Finding.
        :type resource_owner_account: str
        """
        self._resource_owner_account = resource_owner_account

    @property
    def resource_type(self):
        """Gets the resource_type of this Finding.

        :return: The resource_type of this Finding.
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.ResourceType`
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this Finding.

        :param resource_type: The resource_type of this Finding.
        :type resource_type: :class:`huaweicloudsdkiamaccessanalyzer.v1.ResourceType`
        """
        self._resource_type = resource_type

    @property
    def sources(self):
        """Gets the sources of this Finding.

        :return: The sources of this Finding.
        :rtype: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.FindingSourceType`]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        """Sets the sources of this Finding.

        :param sources: The sources of this Finding.
        :type sources: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.FindingSourceType`]
        """
        self._sources = sources

    @property
    def status(self):
        """Gets the status of this Finding.

        结果的当前状态。

        :return: The status of this Finding.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Finding.

        结果的当前状态。

        :param status: The status of this Finding.
        :type status: str
        """
        self._status = status

    @property
    def updated_at(self):
        """Gets the updated_at of this Finding.

        更新调查结果的时间。

        :return: The updated_at of this Finding.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Finding.

        更新调查结果的时间。

        :param updated_at: The updated_at of this Finding.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

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
        if not isinstance(other, Finding):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
