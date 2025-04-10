# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RolesItem:

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
        'description_cn': 'str',
        'domain_id': 'str',
        'flag': 'str',
        'id': 'str',
        'name': 'str',
        'policy': 'RolePolicy',
        'type': 'str'
    }

    attribute_map = {
        'catalog': 'catalog',
        'display_name': 'display_name',
        'description': 'description',
        'description_cn': 'description_cn',
        'domain_id': 'domain_id',
        'flag': 'flag',
        'id': 'id',
        'name': 'name',
        'policy': 'policy',
        'type': 'type'
    }

    def __init__(self, catalog=None, display_name=None, description=None, description_cn=None, domain_id=None, flag=None, id=None, name=None, policy=None, type=None):
        r"""RolesItem

        The model defined in huaweicloud sdk

        :param catalog: 权限所在目录。
        :type catalog: str
        :param display_name: 权限展示名称。
        :type display_name: str
        :param description: 权限的英文描述。
        :type description: str
        :param description_cn: 权限的中文描述信息。
        :type description_cn: str
        :param domain_id: 权限所属账号ID。
        :type domain_id: str
        :param flag: 该参数值为fine_grained时，标识此权限为系统内置的策略。
        :type flag: str
        :param id: 权限Id。
        :type id: str
        :param name: 权限名称。
        :type name: str
        :param policy: 
        :type policy: :class:`huaweicloudsdkiam.v3.RolePolicy`
        :param type: 权限的显示模式。 &gt; - AX表示在domain层显示。 &gt; - XA表示在project层显示。 &gt; - AA表示在domain和project层均显示。 &gt; - XX表示在domain和project层均不显示。 &gt; - 自定义策略的显示模式只能为AX或者XA，不能在domain层和project层都显示（AA），或者在domain层和project层都不显示（XX）。
        :type type: str
        """
        
        

        self._catalog = None
        self._display_name = None
        self._description = None
        self._description_cn = None
        self._domain_id = None
        self._flag = None
        self._id = None
        self._name = None
        self._policy = None
        self._type = None
        self.discriminator = None

        self.catalog = catalog
        self.display_name = display_name
        self.description = description
        self.description_cn = description_cn
        self.domain_id = domain_id
        self.flag = flag
        self.id = id
        self.name = name
        self.policy = policy
        self.type = type

    @property
    def catalog(self):
        r"""Gets the catalog of this RolesItem.

        权限所在目录。

        :return: The catalog of this RolesItem.
        :rtype: str
        """
        return self._catalog

    @catalog.setter
    def catalog(self, catalog):
        r"""Sets the catalog of this RolesItem.

        权限所在目录。

        :param catalog: The catalog of this RolesItem.
        :type catalog: str
        """
        self._catalog = catalog

    @property
    def display_name(self):
        r"""Gets the display_name of this RolesItem.

        权限展示名称。

        :return: The display_name of this RolesItem.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this RolesItem.

        权限展示名称。

        :param display_name: The display_name of this RolesItem.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def description(self):
        r"""Gets the description of this RolesItem.

        权限的英文描述。

        :return: The description of this RolesItem.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this RolesItem.

        权限的英文描述。

        :param description: The description of this RolesItem.
        :type description: str
        """
        self._description = description

    @property
    def description_cn(self):
        r"""Gets the description_cn of this RolesItem.

        权限的中文描述信息。

        :return: The description_cn of this RolesItem.
        :rtype: str
        """
        return self._description_cn

    @description_cn.setter
    def description_cn(self, description_cn):
        r"""Sets the description_cn of this RolesItem.

        权限的中文描述信息。

        :param description_cn: The description_cn of this RolesItem.
        :type description_cn: str
        """
        self._description_cn = description_cn

    @property
    def domain_id(self):
        r"""Gets the domain_id of this RolesItem.

        权限所属账号ID。

        :return: The domain_id of this RolesItem.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this RolesItem.

        权限所属账号ID。

        :param domain_id: The domain_id of this RolesItem.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def flag(self):
        r"""Gets the flag of this RolesItem.

        该参数值为fine_grained时，标识此权限为系统内置的策略。

        :return: The flag of this RolesItem.
        :rtype: str
        """
        return self._flag

    @flag.setter
    def flag(self, flag):
        r"""Sets the flag of this RolesItem.

        该参数值为fine_grained时，标识此权限为系统内置的策略。

        :param flag: The flag of this RolesItem.
        :type flag: str
        """
        self._flag = flag

    @property
    def id(self):
        r"""Gets the id of this RolesItem.

        权限Id。

        :return: The id of this RolesItem.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this RolesItem.

        权限Id。

        :param id: The id of this RolesItem.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this RolesItem.

        权限名称。

        :return: The name of this RolesItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this RolesItem.

        权限名称。

        :param name: The name of this RolesItem.
        :type name: str
        """
        self._name = name

    @property
    def policy(self):
        r"""Gets the policy of this RolesItem.

        :return: The policy of this RolesItem.
        :rtype: :class:`huaweicloudsdkiam.v3.RolePolicy`
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        r"""Sets the policy of this RolesItem.

        :param policy: The policy of this RolesItem.
        :type policy: :class:`huaweicloudsdkiam.v3.RolePolicy`
        """
        self._policy = policy

    @property
    def type(self):
        r"""Gets the type of this RolesItem.

        权限的显示模式。 > - AX表示在domain层显示。 > - XA表示在project层显示。 > - AA表示在domain和project层均显示。 > - XX表示在domain和project层均不显示。 > - 自定义策略的显示模式只能为AX或者XA，不能在domain层和project层都显示（AA），或者在domain层和project层都不显示（XX）。

        :return: The type of this RolesItem.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this RolesItem.

        权限的显示模式。 > - AX表示在domain层显示。 > - XA表示在project层显示。 > - AA表示在domain和project层均显示。 > - XX表示在domain和project层均不显示。 > - 自定义策略的显示模式只能为AX或者XA，不能在domain层和project层都显示（AA），或者在domain层和project层都不显示（XX）。

        :param type: The type of this RolesItem.
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
        if not isinstance(other, RolesItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
