# coding: utf-8

import pprint
import re

import six





class ServicePolicyRoleResult:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'catalog': 'str',
        'display_name': 'str',
        'description': 'str',
        'links': 'LinksSelf',
        'policy': 'ServicePolicy',
        'description_cn': 'str',
        'domain_id': 'str',
        'type': 'str',
        'id': 'str',
        'name': 'str',
        'updated_time': 'str',
        'created_time': 'str',
        'references': 'str'
    }

    attribute_map = {
        'catalog': 'catalog',
        'display_name': 'display_name',
        'description': 'description',
        'links': 'links',
        'policy': 'policy',
        'description_cn': 'description_cn',
        'domain_id': 'domain_id',
        'type': 'type',
        'id': 'id',
        'name': 'name',
        'updated_time': 'updated_time',
        'created_time': 'created_time',
        'references': 'references'
    }

    def __init__(self, catalog=None, display_name=None, description=None, links=None, policy=None, description_cn=None, domain_id=None, type=None, id=None, name=None, updated_time=None, created_time=None, references=None):
        """ServicePolicyRoleResult - a model defined in huaweicloud sdk"""
        
        

        self._catalog = None
        self._display_name = None
        self._description = None
        self._links = None
        self._policy = None
        self._description_cn = None
        self._domain_id = None
        self._type = None
        self._id = None
        self._name = None
        self._updated_time = None
        self._created_time = None
        self._references = None
        self.discriminator = None

        self.catalog = catalog
        self.display_name = display_name
        self.description = description
        self.links = links
        self.policy = policy
        if description_cn is not None:
            self.description_cn = description_cn
        self.domain_id = domain_id
        self.type = type
        self.id = id
        self.name = name
        if updated_time is not None:
            self.updated_time = updated_time
        if created_time is not None:
            self.created_time = created_time
        if references is not None:
            self.references = references

    @property
    def catalog(self):
        """Gets the catalog of this ServicePolicyRoleResult.

        自定义策略所在目录。

        :return: The catalog of this ServicePolicyRoleResult.
        :rtype: str
        """
        return self._catalog

    @catalog.setter
    def catalog(self, catalog):
        """Sets the catalog of this ServicePolicyRoleResult.

        自定义策略所在目录。

        :param catalog: The catalog of this ServicePolicyRoleResult.
        :type: str
        """
        self._catalog = catalog

    @property
    def display_name(self):
        """Gets the display_name of this ServicePolicyRoleResult.

        自定义策略展示名。

        :return: The display_name of this ServicePolicyRoleResult.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this ServicePolicyRoleResult.

        自定义策略展示名。

        :param display_name: The display_name of this ServicePolicyRoleResult.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this ServicePolicyRoleResult.

        自定义策略的描述信息。

        :return: The description of this ServicePolicyRoleResult.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ServicePolicyRoleResult.

        自定义策略的描述信息。

        :param description: The description of this ServicePolicyRoleResult.
        :type: str
        """
        self._description = description

    @property
    def links(self):
        """Gets the links of this ServicePolicyRoleResult.


        :return: The links of this ServicePolicyRoleResult.
        :rtype: LinksSelf
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ServicePolicyRoleResult.


        :param links: The links of this ServicePolicyRoleResult.
        :type: LinksSelf
        """
        self._links = links

    @property
    def policy(self):
        """Gets the policy of this ServicePolicyRoleResult.


        :return: The policy of this ServicePolicyRoleResult.
        :rtype: ServicePolicy
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this ServicePolicyRoleResult.


        :param policy: The policy of this ServicePolicyRoleResult.
        :type: ServicePolicy
        """
        self._policy = policy

    @property
    def description_cn(self):
        """Gets the description_cn of this ServicePolicyRoleResult.

        自定义策略的中文描述信息。

        :return: The description_cn of this ServicePolicyRoleResult.
        :rtype: str
        """
        return self._description_cn

    @description_cn.setter
    def description_cn(self, description_cn):
        """Sets the description_cn of this ServicePolicyRoleResult.

        自定义策略的中文描述信息。

        :param description_cn: The description_cn of this ServicePolicyRoleResult.
        :type: str
        """
        self._description_cn = description_cn

    @property
    def domain_id(self):
        """Gets the domain_id of this ServicePolicyRoleResult.

        自定义策略所属账号ID。

        :return: The domain_id of this ServicePolicyRoleResult.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this ServicePolicyRoleResult.

        自定义策略所属账号ID。

        :param domain_id: The domain_id of this ServicePolicyRoleResult.
        :type: str
        """
        self._domain_id = domain_id

    @property
    def type(self):
        """Gets the type of this ServicePolicyRoleResult.

        自定义策略的显示模式。   > - AX表示在domain层显示。   > - XA表示在project层显示。   > - 自定义策略的显示模式只能为AX或者XA，不能在domain层和project层都显示（AA），或者在domain层和project层都不显示（XX）。

        :return: The type of this ServicePolicyRoleResult.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ServicePolicyRoleResult.

        自定义策略的显示模式。   > - AX表示在domain层显示。   > - XA表示在project层显示。   > - 自定义策略的显示模式只能为AX或者XA，不能在domain层和project层都显示（AA），或者在domain层和project层都不显示（XX）。

        :param type: The type of this ServicePolicyRoleResult.
        :type: str
        """
        self._type = type

    @property
    def id(self):
        """Gets the id of this ServicePolicyRoleResult.

        自定义策略ID。

        :return: The id of this ServicePolicyRoleResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ServicePolicyRoleResult.

        自定义策略ID。

        :param id: The id of this ServicePolicyRoleResult.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ServicePolicyRoleResult.

        自定义策略名。

        :return: The name of this ServicePolicyRoleResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ServicePolicyRoleResult.

        自定义策略名。

        :param name: The name of this ServicePolicyRoleResult.
        :type: str
        """
        self._name = name

    @property
    def updated_time(self):
        """Gets the updated_time of this ServicePolicyRoleResult.

        自定义策略更新时间。

        :return: The updated_time of this ServicePolicyRoleResult.
        :rtype: str
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        """Sets the updated_time of this ServicePolicyRoleResult.

        自定义策略更新时间。

        :param updated_time: The updated_time of this ServicePolicyRoleResult.
        :type: str
        """
        self._updated_time = updated_time

    @property
    def created_time(self):
        """Gets the created_time of this ServicePolicyRoleResult.

        自定义策略创建时间。

        :return: The created_time of this ServicePolicyRoleResult.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this ServicePolicyRoleResult.

        自定义策略创建时间。

        :param created_time: The created_time of this ServicePolicyRoleResult.
        :type: str
        """
        self._created_time = created_time

    @property
    def references(self):
        """Gets the references of this ServicePolicyRoleResult.

        自定义策略的引用次数。

        :return: The references of this ServicePolicyRoleResult.
        :rtype: str
        """
        return self._references

    @references.setter
    def references(self, references):
        """Sets the references of this ServicePolicyRoleResult.

        自定义策略的引用次数。

        :param references: The references of this ServicePolicyRoleResult.
        :type: str
        """
        self._references = references

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ServicePolicyRoleResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
