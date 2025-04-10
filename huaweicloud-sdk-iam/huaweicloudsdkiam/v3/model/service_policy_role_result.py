# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        'created_time': 'str'
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
        'created_time': 'created_time'
    }

    def __init__(self, catalog=None, display_name=None, description=None, links=None, policy=None, description_cn=None, domain_id=None, type=None, id=None, name=None, updated_time=None, created_time=None):
        r"""ServicePolicyRoleResult

        The model defined in huaweicloud sdk

        :param catalog: 自定义策略所在目录。
        :type catalog: str
        :param display_name: 自定义策略展示名。
        :type display_name: str
        :param description: 自定义策略的描述信息。
        :type description: str
        :param links: 
        :type links: :class:`huaweicloudsdkiam.v3.LinksSelf`
        :param policy: 
        :type policy: :class:`huaweicloudsdkiam.v3.ServicePolicy`
        :param description_cn: 自定义策略的中文描述信息。
        :type description_cn: str
        :param domain_id: 自定义策略所属账号ID。
        :type domain_id: str
        :param type: 自定义策略的显示模式。 &gt; - AX表示在domain层显示。 &gt; - XA表示在project层显示。 &gt; - 自定义策略的显示模式只能为AX或者XA，不能在domain层和project层都显示（AA），或者在domain层和project层都不显示（XX）。
        :type type: str
        :param id: 自定义策略ID。
        :type id: str
        :param name: 自定义策略名。
        :type name: str
        :param updated_time: 自定义策略更新时间。
        :type updated_time: str
        :param created_time: 自定义策略创建时间。
        :type created_time: str
        """
        
        

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

    @property
    def catalog(self):
        r"""Gets the catalog of this ServicePolicyRoleResult.

        自定义策略所在目录。

        :return: The catalog of this ServicePolicyRoleResult.
        :rtype: str
        """
        return self._catalog

    @catalog.setter
    def catalog(self, catalog):
        r"""Sets the catalog of this ServicePolicyRoleResult.

        自定义策略所在目录。

        :param catalog: The catalog of this ServicePolicyRoleResult.
        :type catalog: str
        """
        self._catalog = catalog

    @property
    def display_name(self):
        r"""Gets the display_name of this ServicePolicyRoleResult.

        自定义策略展示名。

        :return: The display_name of this ServicePolicyRoleResult.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this ServicePolicyRoleResult.

        自定义策略展示名。

        :param display_name: The display_name of this ServicePolicyRoleResult.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def description(self):
        r"""Gets the description of this ServicePolicyRoleResult.

        自定义策略的描述信息。

        :return: The description of this ServicePolicyRoleResult.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ServicePolicyRoleResult.

        自定义策略的描述信息。

        :param description: The description of this ServicePolicyRoleResult.
        :type description: str
        """
        self._description = description

    @property
    def links(self):
        r"""Gets the links of this ServicePolicyRoleResult.

        :return: The links of this ServicePolicyRoleResult.
        :rtype: :class:`huaweicloudsdkiam.v3.LinksSelf`
        """
        return self._links

    @links.setter
    def links(self, links):
        r"""Sets the links of this ServicePolicyRoleResult.

        :param links: The links of this ServicePolicyRoleResult.
        :type links: :class:`huaweicloudsdkiam.v3.LinksSelf`
        """
        self._links = links

    @property
    def policy(self):
        r"""Gets the policy of this ServicePolicyRoleResult.

        :return: The policy of this ServicePolicyRoleResult.
        :rtype: :class:`huaweicloudsdkiam.v3.ServicePolicy`
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        r"""Sets the policy of this ServicePolicyRoleResult.

        :param policy: The policy of this ServicePolicyRoleResult.
        :type policy: :class:`huaweicloudsdkiam.v3.ServicePolicy`
        """
        self._policy = policy

    @property
    def description_cn(self):
        r"""Gets the description_cn of this ServicePolicyRoleResult.

        自定义策略的中文描述信息。

        :return: The description_cn of this ServicePolicyRoleResult.
        :rtype: str
        """
        return self._description_cn

    @description_cn.setter
    def description_cn(self, description_cn):
        r"""Sets the description_cn of this ServicePolicyRoleResult.

        自定义策略的中文描述信息。

        :param description_cn: The description_cn of this ServicePolicyRoleResult.
        :type description_cn: str
        """
        self._description_cn = description_cn

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ServicePolicyRoleResult.

        自定义策略所属账号ID。

        :return: The domain_id of this ServicePolicyRoleResult.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ServicePolicyRoleResult.

        自定义策略所属账号ID。

        :param domain_id: The domain_id of this ServicePolicyRoleResult.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def type(self):
        r"""Gets the type of this ServicePolicyRoleResult.

        自定义策略的显示模式。 > - AX表示在domain层显示。 > - XA表示在project层显示。 > - 自定义策略的显示模式只能为AX或者XA，不能在domain层和project层都显示（AA），或者在domain层和project层都不显示（XX）。

        :return: The type of this ServicePolicyRoleResult.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ServicePolicyRoleResult.

        自定义策略的显示模式。 > - AX表示在domain层显示。 > - XA表示在project层显示。 > - 自定义策略的显示模式只能为AX或者XA，不能在domain层和project层都显示（AA），或者在domain层和project层都不显示（XX）。

        :param type: The type of this ServicePolicyRoleResult.
        :type type: str
        """
        self._type = type

    @property
    def id(self):
        r"""Gets the id of this ServicePolicyRoleResult.

        自定义策略ID。

        :return: The id of this ServicePolicyRoleResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ServicePolicyRoleResult.

        自定义策略ID。

        :param id: The id of this ServicePolicyRoleResult.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ServicePolicyRoleResult.

        自定义策略名。

        :return: The name of this ServicePolicyRoleResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ServicePolicyRoleResult.

        自定义策略名。

        :param name: The name of this ServicePolicyRoleResult.
        :type name: str
        """
        self._name = name

    @property
    def updated_time(self):
        r"""Gets the updated_time of this ServicePolicyRoleResult.

        自定义策略更新时间。

        :return: The updated_time of this ServicePolicyRoleResult.
        :rtype: str
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        r"""Sets the updated_time of this ServicePolicyRoleResult.

        自定义策略更新时间。

        :param updated_time: The updated_time of this ServicePolicyRoleResult.
        :type updated_time: str
        """
        self._updated_time = updated_time

    @property
    def created_time(self):
        r"""Gets the created_time of this ServicePolicyRoleResult.

        自定义策略创建时间。

        :return: The created_time of this ServicePolicyRoleResult.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        r"""Sets the created_time of this ServicePolicyRoleResult.

        自定义策略创建时间。

        :param created_time: The created_time of this ServicePolicyRoleResult.
        :type created_time: str
        """
        self._created_time = created_time

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
        if not isinstance(other, ServicePolicyRoleResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
