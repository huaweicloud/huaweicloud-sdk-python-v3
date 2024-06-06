# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PreviewFinding:

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
        'change_type': 'str',
        'condition': 'list[FindingCondition]',
        'created_at': 'datetime',
        'existing_finding_id': 'str',
        'existing_finding_status': 'str',
        'id': 'str',
        'is_public': 'bool',
        'principal': 'FindingPrincipal',
        'resource': 'str',
        'resource_owner_account': 'str',
        'resource_type': 'ResourceType',
        'sources': 'list[FindingSourceType]',
        'status': 'str'
    }

    attribute_map = {
        'action': 'action',
        'change_type': 'change_type',
        'condition': 'condition',
        'created_at': 'created_at',
        'existing_finding_id': 'existing_finding_id',
        'existing_finding_status': 'existing_finding_status',
        'id': 'id',
        'is_public': 'is_public',
        'principal': 'principal',
        'resource': 'resource',
        'resource_owner_account': 'resource_owner_account',
        'resource_type': 'resource_type',
        'sources': 'sources',
        'status': 'status'
    }

    def __init__(self, action=None, change_type=None, condition=None, created_at=None, existing_finding_id=None, existing_finding_status=None, id=None, is_public=None, principal=None, resource=None, resource_owner_account=None, resource_type=None, sources=None, status=None):
        """PreviewFinding

        The model defined in huaweicloud sdk

        :param action: 允许外部主体使用的操作。
        :type action: list[str]
        :param change_type: 结果状态的变化。
        :type change_type: str
        :param condition: 分析的策略语句中导致访问预览分析结果的条件。
        :type condition: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.FindingCondition`]
        :param created_at: 生成访问预览分析结果的时间。
        :type created_at: datetime
        :param existing_finding_id: 访问分析结果的唯一标识符。
        :type existing_finding_id: str
        :param existing_finding_status: 分析结果的当前状态。
        :type existing_finding_status: str
        :param id: 访问分析结果的唯一标识符。
        :type id: str
        :param is_public: 表示生成访问分析结果的策略是否允许公共访问资源。
        :type is_public: bool
        :param principal: 
        :type principal: :class:`huaweicloudsdkiamaccessanalyzer.v1.FindingPrincipal`
        :param resource: 资源的唯一资源标识符。
        :type resource: str
        :param resource_owner_account: 拥有资源的账号ID。
        :type resource_owner_account: str
        :param resource_type: 
        :type resource_type: :class:`huaweicloudsdkiamaccessanalyzer.v1.ResourceType`
        :param sources: 访问分析结果的来源，这指示如何授予生成访问分析结果的访问权限。
        :type sources: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.FindingSourceType`]
        :param status: 变化后的状态。
        :type status: str
        """
        
        

        self._action = None
        self._change_type = None
        self._condition = None
        self._created_at = None
        self._existing_finding_id = None
        self._existing_finding_status = None
        self._id = None
        self._is_public = None
        self._principal = None
        self._resource = None
        self._resource_owner_account = None
        self._resource_type = None
        self._sources = None
        self._status = None
        self.discriminator = None

        self.action = action
        self.change_type = change_type
        self.condition = condition
        self.created_at = created_at
        if existing_finding_id is not None:
            self.existing_finding_id = existing_finding_id
        if existing_finding_status is not None:
            self.existing_finding_status = existing_finding_status
        self.id = id
        self.is_public = is_public
        self.principal = principal
        self.resource = resource
        self.resource_owner_account = resource_owner_account
        self.resource_type = resource_type
        if sources is not None:
            self.sources = sources
        self.status = status

    @property
    def action(self):
        """Gets the action of this PreviewFinding.

        允许外部主体使用的操作。

        :return: The action of this PreviewFinding.
        :rtype: list[str]
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this PreviewFinding.

        允许外部主体使用的操作。

        :param action: The action of this PreviewFinding.
        :type action: list[str]
        """
        self._action = action

    @property
    def change_type(self):
        """Gets the change_type of this PreviewFinding.

        结果状态的变化。

        :return: The change_type of this PreviewFinding.
        :rtype: str
        """
        return self._change_type

    @change_type.setter
    def change_type(self, change_type):
        """Sets the change_type of this PreviewFinding.

        结果状态的变化。

        :param change_type: The change_type of this PreviewFinding.
        :type change_type: str
        """
        self._change_type = change_type

    @property
    def condition(self):
        """Gets the condition of this PreviewFinding.

        分析的策略语句中导致访问预览分析结果的条件。

        :return: The condition of this PreviewFinding.
        :rtype: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.FindingCondition`]
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this PreviewFinding.

        分析的策略语句中导致访问预览分析结果的条件。

        :param condition: The condition of this PreviewFinding.
        :type condition: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.FindingCondition`]
        """
        self._condition = condition

    @property
    def created_at(self):
        """Gets the created_at of this PreviewFinding.

        生成访问预览分析结果的时间。

        :return: The created_at of this PreviewFinding.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this PreviewFinding.

        生成访问预览分析结果的时间。

        :param created_at: The created_at of this PreviewFinding.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def existing_finding_id(self):
        """Gets the existing_finding_id of this PreviewFinding.

        访问分析结果的唯一标识符。

        :return: The existing_finding_id of this PreviewFinding.
        :rtype: str
        """
        return self._existing_finding_id

    @existing_finding_id.setter
    def existing_finding_id(self, existing_finding_id):
        """Sets the existing_finding_id of this PreviewFinding.

        访问分析结果的唯一标识符。

        :param existing_finding_id: The existing_finding_id of this PreviewFinding.
        :type existing_finding_id: str
        """
        self._existing_finding_id = existing_finding_id

    @property
    def existing_finding_status(self):
        """Gets the existing_finding_status of this PreviewFinding.

        分析结果的当前状态。

        :return: The existing_finding_status of this PreviewFinding.
        :rtype: str
        """
        return self._existing_finding_status

    @existing_finding_status.setter
    def existing_finding_status(self, existing_finding_status):
        """Sets the existing_finding_status of this PreviewFinding.

        分析结果的当前状态。

        :param existing_finding_status: The existing_finding_status of this PreviewFinding.
        :type existing_finding_status: str
        """
        self._existing_finding_status = existing_finding_status

    @property
    def id(self):
        """Gets the id of this PreviewFinding.

        访问分析结果的唯一标识符。

        :return: The id of this PreviewFinding.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PreviewFinding.

        访问分析结果的唯一标识符。

        :param id: The id of this PreviewFinding.
        :type id: str
        """
        self._id = id

    @property
    def is_public(self):
        """Gets the is_public of this PreviewFinding.

        表示生成访问分析结果的策略是否允许公共访问资源。

        :return: The is_public of this PreviewFinding.
        :rtype: bool
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        """Sets the is_public of this PreviewFinding.

        表示生成访问分析结果的策略是否允许公共访问资源。

        :param is_public: The is_public of this PreviewFinding.
        :type is_public: bool
        """
        self._is_public = is_public

    @property
    def principal(self):
        """Gets the principal of this PreviewFinding.

        :return: The principal of this PreviewFinding.
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.FindingPrincipal`
        """
        return self._principal

    @principal.setter
    def principal(self, principal):
        """Sets the principal of this PreviewFinding.

        :param principal: The principal of this PreviewFinding.
        :type principal: :class:`huaweicloudsdkiamaccessanalyzer.v1.FindingPrincipal`
        """
        self._principal = principal

    @property
    def resource(self):
        """Gets the resource of this PreviewFinding.

        资源的唯一资源标识符。

        :return: The resource of this PreviewFinding.
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this PreviewFinding.

        资源的唯一资源标识符。

        :param resource: The resource of this PreviewFinding.
        :type resource: str
        """
        self._resource = resource

    @property
    def resource_owner_account(self):
        """Gets the resource_owner_account of this PreviewFinding.

        拥有资源的账号ID。

        :return: The resource_owner_account of this PreviewFinding.
        :rtype: str
        """
        return self._resource_owner_account

    @resource_owner_account.setter
    def resource_owner_account(self, resource_owner_account):
        """Sets the resource_owner_account of this PreviewFinding.

        拥有资源的账号ID。

        :param resource_owner_account: The resource_owner_account of this PreviewFinding.
        :type resource_owner_account: str
        """
        self._resource_owner_account = resource_owner_account

    @property
    def resource_type(self):
        """Gets the resource_type of this PreviewFinding.

        :return: The resource_type of this PreviewFinding.
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.ResourceType`
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this PreviewFinding.

        :param resource_type: The resource_type of this PreviewFinding.
        :type resource_type: :class:`huaweicloudsdkiamaccessanalyzer.v1.ResourceType`
        """
        self._resource_type = resource_type

    @property
    def sources(self):
        """Gets the sources of this PreviewFinding.

        访问分析结果的来源，这指示如何授予生成访问分析结果的访问权限。

        :return: The sources of this PreviewFinding.
        :rtype: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.FindingSourceType`]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        """Sets the sources of this PreviewFinding.

        访问分析结果的来源，这指示如何授予生成访问分析结果的访问权限。

        :param sources: The sources of this PreviewFinding.
        :type sources: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.FindingSourceType`]
        """
        self._sources = sources

    @property
    def status(self):
        """Gets the status of this PreviewFinding.

        变化后的状态。

        :return: The status of this PreviewFinding.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PreviewFinding.

        变化后的状态。

        :param status: The status of this PreviewFinding.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, PreviewFinding):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
