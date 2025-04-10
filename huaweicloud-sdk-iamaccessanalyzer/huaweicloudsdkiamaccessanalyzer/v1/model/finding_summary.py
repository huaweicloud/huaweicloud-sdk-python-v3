# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FindingSummary:

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
        'finding_type': 'FindingType',
        'id': 'str',
        'is_public': 'bool',
        'principal': 'FindingPrincipal',
        'resource': 'str',
        'resource_id': 'str',
        'resource_owner_account': 'str',
        'resource_project_id': 'str',
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
        'finding_type': 'finding_type',
        'id': 'id',
        'is_public': 'is_public',
        'principal': 'principal',
        'resource': 'resource',
        'resource_id': 'resource_id',
        'resource_owner_account': 'resource_owner_account',
        'resource_project_id': 'resource_project_id',
        'resource_type': 'resource_type',
        'sources': 'sources',
        'status': 'status',
        'updated_at': 'updated_at'
    }

    def __init__(self, action=None, analyzed_at=None, condition=None, created_at=None, finding_type=None, id=None, is_public=None, principal=None, resource=None, resource_id=None, resource_owner_account=None, resource_project_id=None, resource_type=None, sources=None, status=None, updated_at=None):
        r"""FindingSummary

        The model defined in huaweicloud sdk

        :param action: 允许外部主体使用的操作。
        :type action: list[str]
        :param analyzed_at: 分析资源的时间。
        :type analyzed_at: datetime
        :param condition: 分析的策略语句中导致访问分析结果的条件。
        :type condition: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.FindingCondition`]
        :param created_at: 生成访问分析结果的时间。
        :type created_at: datetime
        :param finding_type: 
        :type finding_type: :class:`huaweicloudsdkiamaccessanalyzer.v1.FindingType`
        :param id: 访问分析结果的唯一标识符。
        :type id: str
        :param is_public: 表示生成访问分析结果的策略是否允许公共访问资源。
        :type is_public: bool
        :param principal: 
        :type principal: :class:`huaweicloudsdkiamaccessanalyzer.v1.FindingPrincipal`
        :param resource: 资源的唯一资源标识符。
        :type resource: str
        :param resource_id: 资源的唯一标识符。
        :type resource_id: str
        :param resource_owner_account: 拥有资源的账号ID。
        :type resource_owner_account: str
        :param resource_project_id: 资源所属的项目标识符
        :type resource_project_id: str
        :param resource_type: 
        :type resource_type: :class:`huaweicloudsdkiamaccessanalyzer.v1.ResourceType`
        :param sources: 访问分析结果的来源，这指示如何授予生成访问分析结果的访问权限。
        :type sources: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.FindingSourceType`]
        :param status: 访问分析结果当前状态。
        :type status: str
        :param updated_at: 更新访问分析结果的时间。
        :type updated_at: datetime
        """
        
        

        self._action = None
        self._analyzed_at = None
        self._condition = None
        self._created_at = None
        self._finding_type = None
        self._id = None
        self._is_public = None
        self._principal = None
        self._resource = None
        self._resource_id = None
        self._resource_owner_account = None
        self._resource_project_id = None
        self._resource_type = None
        self._sources = None
        self._status = None
        self._updated_at = None
        self.discriminator = None

        if action is not None:
            self.action = action
        self.analyzed_at = analyzed_at
        if condition is not None:
            self.condition = condition
        self.created_at = created_at
        self.finding_type = finding_type
        self.id = id
        if is_public is not None:
            self.is_public = is_public
        if principal is not None:
            self.principal = principal
        self.resource = resource
        if resource_id is not None:
            self.resource_id = resource_id
        self.resource_owner_account = resource_owner_account
        if resource_project_id is not None:
            self.resource_project_id = resource_project_id
        self.resource_type = resource_type
        if sources is not None:
            self.sources = sources
        self.status = status
        self.updated_at = updated_at

    @property
    def action(self):
        r"""Gets the action of this FindingSummary.

        允许外部主体使用的操作。

        :return: The action of this FindingSummary.
        :rtype: list[str]
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this FindingSummary.

        允许外部主体使用的操作。

        :param action: The action of this FindingSummary.
        :type action: list[str]
        """
        self._action = action

    @property
    def analyzed_at(self):
        r"""Gets the analyzed_at of this FindingSummary.

        分析资源的时间。

        :return: The analyzed_at of this FindingSummary.
        :rtype: datetime
        """
        return self._analyzed_at

    @analyzed_at.setter
    def analyzed_at(self, analyzed_at):
        r"""Sets the analyzed_at of this FindingSummary.

        分析资源的时间。

        :param analyzed_at: The analyzed_at of this FindingSummary.
        :type analyzed_at: datetime
        """
        self._analyzed_at = analyzed_at

    @property
    def condition(self):
        r"""Gets the condition of this FindingSummary.

        分析的策略语句中导致访问分析结果的条件。

        :return: The condition of this FindingSummary.
        :rtype: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.FindingCondition`]
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        r"""Sets the condition of this FindingSummary.

        分析的策略语句中导致访问分析结果的条件。

        :param condition: The condition of this FindingSummary.
        :type condition: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.FindingCondition`]
        """
        self._condition = condition

    @property
    def created_at(self):
        r"""Gets the created_at of this FindingSummary.

        生成访问分析结果的时间。

        :return: The created_at of this FindingSummary.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this FindingSummary.

        生成访问分析结果的时间。

        :param created_at: The created_at of this FindingSummary.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def finding_type(self):
        r"""Gets the finding_type of this FindingSummary.

        :return: The finding_type of this FindingSummary.
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.FindingType`
        """
        return self._finding_type

    @finding_type.setter
    def finding_type(self, finding_type):
        r"""Sets the finding_type of this FindingSummary.

        :param finding_type: The finding_type of this FindingSummary.
        :type finding_type: :class:`huaweicloudsdkiamaccessanalyzer.v1.FindingType`
        """
        self._finding_type = finding_type

    @property
    def id(self):
        r"""Gets the id of this FindingSummary.

        访问分析结果的唯一标识符。

        :return: The id of this FindingSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this FindingSummary.

        访问分析结果的唯一标识符。

        :param id: The id of this FindingSummary.
        :type id: str
        """
        self._id = id

    @property
    def is_public(self):
        r"""Gets the is_public of this FindingSummary.

        表示生成访问分析结果的策略是否允许公共访问资源。

        :return: The is_public of this FindingSummary.
        :rtype: bool
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        r"""Sets the is_public of this FindingSummary.

        表示生成访问分析结果的策略是否允许公共访问资源。

        :param is_public: The is_public of this FindingSummary.
        :type is_public: bool
        """
        self._is_public = is_public

    @property
    def principal(self):
        r"""Gets the principal of this FindingSummary.

        :return: The principal of this FindingSummary.
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.FindingPrincipal`
        """
        return self._principal

    @principal.setter
    def principal(self, principal):
        r"""Sets the principal of this FindingSummary.

        :param principal: The principal of this FindingSummary.
        :type principal: :class:`huaweicloudsdkiamaccessanalyzer.v1.FindingPrincipal`
        """
        self._principal = principal

    @property
    def resource(self):
        r"""Gets the resource of this FindingSummary.

        资源的唯一资源标识符。

        :return: The resource of this FindingSummary.
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        r"""Sets the resource of this FindingSummary.

        资源的唯一资源标识符。

        :param resource: The resource of this FindingSummary.
        :type resource: str
        """
        self._resource = resource

    @property
    def resource_id(self):
        r"""Gets the resource_id of this FindingSummary.

        资源的唯一标识符。

        :return: The resource_id of this FindingSummary.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this FindingSummary.

        资源的唯一标识符。

        :param resource_id: The resource_id of this FindingSummary.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_owner_account(self):
        r"""Gets the resource_owner_account of this FindingSummary.

        拥有资源的账号ID。

        :return: The resource_owner_account of this FindingSummary.
        :rtype: str
        """
        return self._resource_owner_account

    @resource_owner_account.setter
    def resource_owner_account(self, resource_owner_account):
        r"""Sets the resource_owner_account of this FindingSummary.

        拥有资源的账号ID。

        :param resource_owner_account: The resource_owner_account of this FindingSummary.
        :type resource_owner_account: str
        """
        self._resource_owner_account = resource_owner_account

    @property
    def resource_project_id(self):
        r"""Gets the resource_project_id of this FindingSummary.

        资源所属的项目标识符

        :return: The resource_project_id of this FindingSummary.
        :rtype: str
        """
        return self._resource_project_id

    @resource_project_id.setter
    def resource_project_id(self, resource_project_id):
        r"""Sets the resource_project_id of this FindingSummary.

        资源所属的项目标识符

        :param resource_project_id: The resource_project_id of this FindingSummary.
        :type resource_project_id: str
        """
        self._resource_project_id = resource_project_id

    @property
    def resource_type(self):
        r"""Gets the resource_type of this FindingSummary.

        :return: The resource_type of this FindingSummary.
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.ResourceType`
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this FindingSummary.

        :param resource_type: The resource_type of this FindingSummary.
        :type resource_type: :class:`huaweicloudsdkiamaccessanalyzer.v1.ResourceType`
        """
        self._resource_type = resource_type

    @property
    def sources(self):
        r"""Gets the sources of this FindingSummary.

        访问分析结果的来源，这指示如何授予生成访问分析结果的访问权限。

        :return: The sources of this FindingSummary.
        :rtype: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.FindingSourceType`]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        r"""Sets the sources of this FindingSummary.

        访问分析结果的来源，这指示如何授予生成访问分析结果的访问权限。

        :param sources: The sources of this FindingSummary.
        :type sources: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.FindingSourceType`]
        """
        self._sources = sources

    @property
    def status(self):
        r"""Gets the status of this FindingSummary.

        访问分析结果当前状态。

        :return: The status of this FindingSummary.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this FindingSummary.

        访问分析结果当前状态。

        :param status: The status of this FindingSummary.
        :type status: str
        """
        self._status = status

    @property
    def updated_at(self):
        r"""Gets the updated_at of this FindingSummary.

        更新访问分析结果的时间。

        :return: The updated_at of this FindingSummary.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this FindingSummary.

        更新访问分析结果的时间。

        :param updated_at: The updated_at of this FindingSummary.
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
        if not isinstance(other, FindingSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
