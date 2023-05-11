# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PolicyRoleResult:

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
        'references': 'int',
        'updated_time': 'str',
        'created_time': 'str',
        'description_cn': 'str',
        'catalog': 'str',
        'name': 'str',
        'description': 'str',
        'links': 'LinksSelf',
        'id': 'str',
        'display_name': 'str',
        'type': 'str',
        'policy': 'ServicePolicy'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'references': 'references',
        'updated_time': 'updated_time',
        'created_time': 'created_time',
        'description_cn': 'description_cn',
        'catalog': 'catalog',
        'name': 'name',
        'description': 'description',
        'links': 'links',
        'id': 'id',
        'display_name': 'display_name',
        'type': 'type',
        'policy': 'policy'
    }

    def __init__(self, domain_id=None, references=None, updated_time=None, created_time=None, description_cn=None, catalog=None, name=None, description=None, links=None, id=None, display_name=None, type=None, policy=None):
        """PolicyRoleResult

        The model defined in huaweicloud sdk

        :param domain_id: 自定义策略所属账号ID。
        :type domain_id: str
        :param references: 自定义策略的引用次数。
        :type references: int
        :param updated_time: 自定义策略更新时间。
        :type updated_time: str
        :param created_time: 自定义策略创建时间。
        :type created_time: str
        :param description_cn: 自定义策略的中文描述信息。
        :type description_cn: str
        :param catalog: 自定义策略所在目录。
        :type catalog: str
        :param name: 自定义策略名。
        :type name: str
        :param description: 自定义策略的描述信息。
        :type description: str
        :param links: 
        :type links: :class:`huaweicloudsdkiam.v3.LinksSelf`
        :param id: 自定义策略ID。
        :type id: str
        :param display_name: 自定义策略展示名。
        :type display_name: str
        :param type: 自定义策略的显示模式。 &gt; - AX表示在domain层显示。 &gt; - XA表示在project层显示。 &gt; - 自定义策略的显示模式只能为AX或者XA，不能在domain层和project层都显示（AA），或者在domain层和project层都不显示（XX）。
        :type type: str
        :param policy: 
        :type policy: :class:`huaweicloudsdkiam.v3.ServicePolicy`
        """
        
        

        self._domain_id = None
        self._references = None
        self._updated_time = None
        self._created_time = None
        self._description_cn = None
        self._catalog = None
        self._name = None
        self._description = None
        self._links = None
        self._id = None
        self._display_name = None
        self._type = None
        self._policy = None
        self.discriminator = None

        self.domain_id = domain_id
        if references is not None:
            self.references = references
        if updated_time is not None:
            self.updated_time = updated_time
        if created_time is not None:
            self.created_time = created_time
        if description_cn is not None:
            self.description_cn = description_cn
        self.catalog = catalog
        self.name = name
        self.description = description
        self.links = links
        self.id = id
        self.display_name = display_name
        self.type = type
        self.policy = policy

    @property
    def domain_id(self):
        """Gets the domain_id of this PolicyRoleResult.

        自定义策略所属账号ID。

        :return: The domain_id of this PolicyRoleResult.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this PolicyRoleResult.

        自定义策略所属账号ID。

        :param domain_id: The domain_id of this PolicyRoleResult.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def references(self):
        """Gets the references of this PolicyRoleResult.

        自定义策略的引用次数。

        :return: The references of this PolicyRoleResult.
        :rtype: int
        """
        return self._references

    @references.setter
    def references(self, references):
        """Sets the references of this PolicyRoleResult.

        自定义策略的引用次数。

        :param references: The references of this PolicyRoleResult.
        :type references: int
        """
        self._references = references

    @property
    def updated_time(self):
        """Gets the updated_time of this PolicyRoleResult.

        自定义策略更新时间。

        :return: The updated_time of this PolicyRoleResult.
        :rtype: str
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        """Sets the updated_time of this PolicyRoleResult.

        自定义策略更新时间。

        :param updated_time: The updated_time of this PolicyRoleResult.
        :type updated_time: str
        """
        self._updated_time = updated_time

    @property
    def created_time(self):
        """Gets the created_time of this PolicyRoleResult.

        自定义策略创建时间。

        :return: The created_time of this PolicyRoleResult.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this PolicyRoleResult.

        自定义策略创建时间。

        :param created_time: The created_time of this PolicyRoleResult.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def description_cn(self):
        """Gets the description_cn of this PolicyRoleResult.

        自定义策略的中文描述信息。

        :return: The description_cn of this PolicyRoleResult.
        :rtype: str
        """
        return self._description_cn

    @description_cn.setter
    def description_cn(self, description_cn):
        """Sets the description_cn of this PolicyRoleResult.

        自定义策略的中文描述信息。

        :param description_cn: The description_cn of this PolicyRoleResult.
        :type description_cn: str
        """
        self._description_cn = description_cn

    @property
    def catalog(self):
        """Gets the catalog of this PolicyRoleResult.

        自定义策略所在目录。

        :return: The catalog of this PolicyRoleResult.
        :rtype: str
        """
        return self._catalog

    @catalog.setter
    def catalog(self, catalog):
        """Sets the catalog of this PolicyRoleResult.

        自定义策略所在目录。

        :param catalog: The catalog of this PolicyRoleResult.
        :type catalog: str
        """
        self._catalog = catalog

    @property
    def name(self):
        """Gets the name of this PolicyRoleResult.

        自定义策略名。

        :return: The name of this PolicyRoleResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PolicyRoleResult.

        自定义策略名。

        :param name: The name of this PolicyRoleResult.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this PolicyRoleResult.

        自定义策略的描述信息。

        :return: The description of this PolicyRoleResult.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PolicyRoleResult.

        自定义策略的描述信息。

        :param description: The description of this PolicyRoleResult.
        :type description: str
        """
        self._description = description

    @property
    def links(self):
        """Gets the links of this PolicyRoleResult.

        :return: The links of this PolicyRoleResult.
        :rtype: :class:`huaweicloudsdkiam.v3.LinksSelf`
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this PolicyRoleResult.

        :param links: The links of this PolicyRoleResult.
        :type links: :class:`huaweicloudsdkiam.v3.LinksSelf`
        """
        self._links = links

    @property
    def id(self):
        """Gets the id of this PolicyRoleResult.

        自定义策略ID。

        :return: The id of this PolicyRoleResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PolicyRoleResult.

        自定义策略ID。

        :param id: The id of this PolicyRoleResult.
        :type id: str
        """
        self._id = id

    @property
    def display_name(self):
        """Gets the display_name of this PolicyRoleResult.

        自定义策略展示名。

        :return: The display_name of this PolicyRoleResult.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this PolicyRoleResult.

        自定义策略展示名。

        :param display_name: The display_name of this PolicyRoleResult.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def type(self):
        """Gets the type of this PolicyRoleResult.

        自定义策略的显示模式。 > - AX表示在domain层显示。 > - XA表示在project层显示。 > - 自定义策略的显示模式只能为AX或者XA，不能在domain层和project层都显示（AA），或者在domain层和project层都不显示（XX）。

        :return: The type of this PolicyRoleResult.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PolicyRoleResult.

        自定义策略的显示模式。 > - AX表示在domain层显示。 > - XA表示在project层显示。 > - 自定义策略的显示模式只能为AX或者XA，不能在domain层和project层都显示（AA），或者在domain层和project层都不显示（XX）。

        :param type: The type of this PolicyRoleResult.
        :type type: str
        """
        self._type = type

    @property
    def policy(self):
        """Gets the policy of this PolicyRoleResult.

        :return: The policy of this PolicyRoleResult.
        :rtype: :class:`huaweicloudsdkiam.v3.ServicePolicy`
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this PolicyRoleResult.

        :param policy: The policy of this PolicyRoleResult.
        :type policy: :class:`huaweicloudsdkiam.v3.ServicePolicy`
        """
        self._policy = policy

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
        if not isinstance(other, PolicyRoleResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
