# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VaultGet:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'billing': 'Billing',
        'description': 'str',
        'id': 'str',
        'name': 'str',
        'project_id': 'str',
        'provider_id': 'str',
        'resources': 'list[ResourceResp]',
        'tags': 'list[TagsResp]',
        'enterprise_project_id': 'str',
        'auto_bind': 'bool',
        'bind_rules': 'VaultBindRules',
        'user_id': 'str',
        'created_at': 'str',
        'auto_expand': 'bool',
        'smn_notify': 'bool',
        'threshold': 'int',
        'updated_at': 'str',
        'version': 'str'
    }

    attribute_map = {
        'billing': 'billing',
        'description': 'description',
        'id': 'id',
        'name': 'name',
        'project_id': 'project_id',
        'provider_id': 'provider_id',
        'resources': 'resources',
        'tags': 'tags',
        'enterprise_project_id': 'enterprise_project_id',
        'auto_bind': 'auto_bind',
        'bind_rules': 'bind_rules',
        'user_id': 'user_id',
        'created_at': 'created_at',
        'auto_expand': 'auto_expand',
        'smn_notify': 'smn_notify',
        'threshold': 'threshold',
        'updated_at': 'updated_at',
        'version': 'version'
    }

    def __init__(self, billing=None, description=None, id=None, name=None, project_id=None, provider_id=None, resources=None, tags=None, enterprise_project_id=None, auto_bind=None, bind_rules=None, user_id=None, created_at=None, auto_expand=None, smn_notify=None, threshold=None, updated_at=None, version=None):
        """VaultGet

        The model defined in huaweicloud sdk

        :param billing: 
        :type billing: :class:`huaweicloudsdkcbr.v1.Billing`
        :param description: 存储库自定义描述信息。
        :type description: str
        :param id: 存储库ID
        :type id: str
        :param name: 存储库名称
        :type name: str
        :param project_id: 项目ID
        :type project_id: str
        :param provider_id: 存储库资源类型id
        :type provider_id: str
        :param resources: 资源
        :type resources: list[:class:`huaweicloudsdkcbr.v1.ResourceResp`]
        :param tags: 标签
        :type tags: list[:class:`huaweicloudsdkcbr.v1.TagsResp`]
        :param enterprise_project_id: 企业项目id，默认为‘0’。
        :type enterprise_project_id: str
        :param auto_bind: 是否自动绑定，默认为false，不支持。
        :type auto_bind: bool
        :param bind_rules: 
        :type bind_rules: :class:`huaweicloudsdkcbr.v1.VaultBindRules`
        :param user_id: 用户id
        :type user_id: str
        :param created_at: 创建时间,例如:\&quot;2020-02-05T10:38:34.209782\&quot;
        :type created_at: str
        :param auto_expand: 是否开启存储库自动扩容能力（只支持按需存储库）。
        :type auto_expand: bool
        :param smn_notify: 存储库smn消息通知开关
        :type smn_notify: bool
        :param threshold: 存储库容量阈值，已用容量占总容量达到此百分比即发送相关通知
        :type threshold: int
        :param updated_at: 更新时间,例如:\&quot;2020-02-05T10:38:34.209782\&quot;
        :type updated_at: str
        :param version: 版本
        :type version: str
        """
        
        

        self._billing = None
        self._description = None
        self._id = None
        self._name = None
        self._project_id = None
        self._provider_id = None
        self._resources = None
        self._tags = None
        self._enterprise_project_id = None
        self._auto_bind = None
        self._bind_rules = None
        self._user_id = None
        self._created_at = None
        self._auto_expand = None
        self._smn_notify = None
        self._threshold = None
        self._updated_at = None
        self._version = None
        self.discriminator = None

        self.billing = billing
        if description is not None:
            self.description = description
        self.id = id
        self.name = name
        self.project_id = project_id
        self.provider_id = provider_id
        self.resources = resources
        if tags is not None:
            self.tags = tags
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if auto_bind is not None:
            self.auto_bind = auto_bind
        if bind_rules is not None:
            self.bind_rules = bind_rules
        if user_id is not None:
            self.user_id = user_id
        if created_at is not None:
            self.created_at = created_at
        if auto_expand is not None:
            self.auto_expand = auto_expand
        if smn_notify is not None:
            self.smn_notify = smn_notify
        if threshold is not None:
            self.threshold = threshold
        self.updated_at = updated_at
        if version is not None:
            self.version = version

    @property
    def billing(self):
        """Gets the billing of this VaultGet.


        :return: The billing of this VaultGet.
        :rtype: :class:`huaweicloudsdkcbr.v1.Billing`
        """
        return self._billing

    @billing.setter
    def billing(self, billing):
        """Sets the billing of this VaultGet.


        :param billing: The billing of this VaultGet.
        :type billing: :class:`huaweicloudsdkcbr.v1.Billing`
        """
        self._billing = billing

    @property
    def description(self):
        """Gets the description of this VaultGet.

        存储库自定义描述信息。

        :return: The description of this VaultGet.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VaultGet.

        存储库自定义描述信息。

        :param description: The description of this VaultGet.
        :type description: str
        """
        self._description = description

    @property
    def id(self):
        """Gets the id of this VaultGet.

        存储库ID

        :return: The id of this VaultGet.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VaultGet.

        存储库ID

        :param id: The id of this VaultGet.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this VaultGet.

        存储库名称

        :return: The name of this VaultGet.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VaultGet.

        存储库名称

        :param name: The name of this VaultGet.
        :type name: str
        """
        self._name = name

    @property
    def project_id(self):
        """Gets the project_id of this VaultGet.

        项目ID

        :return: The project_id of this VaultGet.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this VaultGet.

        项目ID

        :param project_id: The project_id of this VaultGet.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def provider_id(self):
        """Gets the provider_id of this VaultGet.

        存储库资源类型id

        :return: The provider_id of this VaultGet.
        :rtype: str
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        """Sets the provider_id of this VaultGet.

        存储库资源类型id

        :param provider_id: The provider_id of this VaultGet.
        :type provider_id: str
        """
        self._provider_id = provider_id

    @property
    def resources(self):
        """Gets the resources of this VaultGet.

        资源

        :return: The resources of this VaultGet.
        :rtype: list[:class:`huaweicloudsdkcbr.v1.ResourceResp`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this VaultGet.

        资源

        :param resources: The resources of this VaultGet.
        :type resources: list[:class:`huaweicloudsdkcbr.v1.ResourceResp`]
        """
        self._resources = resources

    @property
    def tags(self):
        """Gets the tags of this VaultGet.

        标签

        :return: The tags of this VaultGet.
        :rtype: list[:class:`huaweicloudsdkcbr.v1.TagsResp`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this VaultGet.

        标签

        :param tags: The tags of this VaultGet.
        :type tags: list[:class:`huaweicloudsdkcbr.v1.TagsResp`]
        """
        self._tags = tags

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this VaultGet.

        企业项目id，默认为‘0’。

        :return: The enterprise_project_id of this VaultGet.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this VaultGet.

        企业项目id，默认为‘0’。

        :param enterprise_project_id: The enterprise_project_id of this VaultGet.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def auto_bind(self):
        """Gets the auto_bind of this VaultGet.

        是否自动绑定，默认为false，不支持。

        :return: The auto_bind of this VaultGet.
        :rtype: bool
        """
        return self._auto_bind

    @auto_bind.setter
    def auto_bind(self, auto_bind):
        """Sets the auto_bind of this VaultGet.

        是否自动绑定，默认为false，不支持。

        :param auto_bind: The auto_bind of this VaultGet.
        :type auto_bind: bool
        """
        self._auto_bind = auto_bind

    @property
    def bind_rules(self):
        """Gets the bind_rules of this VaultGet.


        :return: The bind_rules of this VaultGet.
        :rtype: :class:`huaweicloudsdkcbr.v1.VaultBindRules`
        """
        return self._bind_rules

    @bind_rules.setter
    def bind_rules(self, bind_rules):
        """Sets the bind_rules of this VaultGet.


        :param bind_rules: The bind_rules of this VaultGet.
        :type bind_rules: :class:`huaweicloudsdkcbr.v1.VaultBindRules`
        """
        self._bind_rules = bind_rules

    @property
    def user_id(self):
        """Gets the user_id of this VaultGet.

        用户id

        :return: The user_id of this VaultGet.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this VaultGet.

        用户id

        :param user_id: The user_id of this VaultGet.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def created_at(self):
        """Gets the created_at of this VaultGet.

        创建时间,例如:\"2020-02-05T10:38:34.209782\"

        :return: The created_at of this VaultGet.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this VaultGet.

        创建时间,例如:\"2020-02-05T10:38:34.209782\"

        :param created_at: The created_at of this VaultGet.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def auto_expand(self):
        """Gets the auto_expand of this VaultGet.

        是否开启存储库自动扩容能力（只支持按需存储库）。

        :return: The auto_expand of this VaultGet.
        :rtype: bool
        """
        return self._auto_expand

    @auto_expand.setter
    def auto_expand(self, auto_expand):
        """Sets the auto_expand of this VaultGet.

        是否开启存储库自动扩容能力（只支持按需存储库）。

        :param auto_expand: The auto_expand of this VaultGet.
        :type auto_expand: bool
        """
        self._auto_expand = auto_expand

    @property
    def smn_notify(self):
        """Gets the smn_notify of this VaultGet.

        存储库smn消息通知开关

        :return: The smn_notify of this VaultGet.
        :rtype: bool
        """
        return self._smn_notify

    @smn_notify.setter
    def smn_notify(self, smn_notify):
        """Sets the smn_notify of this VaultGet.

        存储库smn消息通知开关

        :param smn_notify: The smn_notify of this VaultGet.
        :type smn_notify: bool
        """
        self._smn_notify = smn_notify

    @property
    def threshold(self):
        """Gets the threshold of this VaultGet.

        存储库容量阈值，已用容量占总容量达到此百分比即发送相关通知

        :return: The threshold of this VaultGet.
        :rtype: int
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        """Sets the threshold of this VaultGet.

        存储库容量阈值，已用容量占总容量达到此百分比即发送相关通知

        :param threshold: The threshold of this VaultGet.
        :type threshold: int
        """
        self._threshold = threshold

    @property
    def updated_at(self):
        """Gets the updated_at of this VaultGet.

        更新时间,例如:\"2020-02-05T10:38:34.209782\"

        :return: The updated_at of this VaultGet.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this VaultGet.

        更新时间,例如:\"2020-02-05T10:38:34.209782\"

        :param updated_at: The updated_at of this VaultGet.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def version(self):
        """Gets the version of this VaultGet.

        版本

        :return: The version of this VaultGet.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this VaultGet.

        版本

        :param version: The version of this VaultGet.
        :type version: str
        """
        self._version = version

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
        if not isinstance(other, VaultGet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
