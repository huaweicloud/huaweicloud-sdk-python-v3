# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RoleResult:

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
        'flag': 'str',
        'description_cn': 'str',
        'catalog': 'str',
        'name': 'str',
        'description': 'str',
        'links': 'Links',
        'id': 'str',
        'display_name': 'str',
        'type': 'str',
        'policy': 'RolePolicy',
        'updated_time': 'str',
        'created_time': 'str'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'flag': 'flag',
        'description_cn': 'description_cn',
        'catalog': 'catalog',
        'name': 'name',
        'description': 'description',
        'links': 'links',
        'id': 'id',
        'display_name': 'display_name',
        'type': 'type',
        'policy': 'policy',
        'updated_time': 'updated_time',
        'created_time': 'created_time'
    }

    def __init__(self, domain_id=None, flag=None, description_cn=None, catalog=None, name=None, description=None, links=None, id=None, display_name=None, type=None, policy=None, updated_time=None, created_time=None):
        r"""RoleResult

        The model defined in huaweicloud sdk

        :param domain_id: 权限所属账号ID。
        :type domain_id: str
        :param flag: 该参数值为fine_grained时，标识此权限为系统内置的策略。
        :type flag: str
        :param description_cn: 权限的中文描述信息。
        :type description_cn: str
        :param catalog: 权限所在目录。
        :type catalog: str
        :param name: 权限名。携带在用户的token中，云服务根据该名称来判断用户是否有权限访问。
        :type name: str
        :param description: 权限描述信息。
        :type description: str
        :param links: 
        :type links: :class:`huaweicloudsdkiam.v3.Links`
        :param id: 权限ID。
        :type id: str
        :param display_name: 权限展示名。
        :type display_name: str
        :param type: 权限的显示模式。 &gt; - AX表示在domain层显示。 &gt; - XA表示在project层显示。 &gt; - AA表示在domain和project层均显示。 &gt; - XX表示在domain和project层均不显示。 &gt; - 自定义策略的显示模式只能为AX或者XA，不能在domain层和project层都显示（AA），或者在domain层和project层都不显示（XX）。
        :type type: str
        :param policy: 
        :type policy: :class:`huaweicloudsdkiam.v3.RolePolicy`
        :param updated_time: 权限更新时间。
        :type updated_time: str
        :param created_time: 权限创建时间。
        :type created_time: str
        """
        
        

        self._domain_id = None
        self._flag = None
        self._description_cn = None
        self._catalog = None
        self._name = None
        self._description = None
        self._links = None
        self._id = None
        self._display_name = None
        self._type = None
        self._policy = None
        self._updated_time = None
        self._created_time = None
        self.discriminator = None

        if domain_id is not None:
            self.domain_id = domain_id
        if flag is not None:
            self.flag = flag
        if description_cn is not None:
            self.description_cn = description_cn
        if catalog is not None:
            self.catalog = catalog
        self.name = name
        if description is not None:
            self.description = description
        if links is not None:
            self.links = links
        self.id = id
        if display_name is not None:
            self.display_name = display_name
        self.type = type
        self.policy = policy
        if updated_time is not None:
            self.updated_time = updated_time
        if created_time is not None:
            self.created_time = created_time

    @property
    def domain_id(self):
        r"""Gets the domain_id of this RoleResult.

        权限所属账号ID。

        :return: The domain_id of this RoleResult.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this RoleResult.

        权限所属账号ID。

        :param domain_id: The domain_id of this RoleResult.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def flag(self):
        r"""Gets the flag of this RoleResult.

        该参数值为fine_grained时，标识此权限为系统内置的策略。

        :return: The flag of this RoleResult.
        :rtype: str
        """
        return self._flag

    @flag.setter
    def flag(self, flag):
        r"""Sets the flag of this RoleResult.

        该参数值为fine_grained时，标识此权限为系统内置的策略。

        :param flag: The flag of this RoleResult.
        :type flag: str
        """
        self._flag = flag

    @property
    def description_cn(self):
        r"""Gets the description_cn of this RoleResult.

        权限的中文描述信息。

        :return: The description_cn of this RoleResult.
        :rtype: str
        """
        return self._description_cn

    @description_cn.setter
    def description_cn(self, description_cn):
        r"""Sets the description_cn of this RoleResult.

        权限的中文描述信息。

        :param description_cn: The description_cn of this RoleResult.
        :type description_cn: str
        """
        self._description_cn = description_cn

    @property
    def catalog(self):
        r"""Gets the catalog of this RoleResult.

        权限所在目录。

        :return: The catalog of this RoleResult.
        :rtype: str
        """
        return self._catalog

    @catalog.setter
    def catalog(self, catalog):
        r"""Sets the catalog of this RoleResult.

        权限所在目录。

        :param catalog: The catalog of this RoleResult.
        :type catalog: str
        """
        self._catalog = catalog

    @property
    def name(self):
        r"""Gets the name of this RoleResult.

        权限名。携带在用户的token中，云服务根据该名称来判断用户是否有权限访问。

        :return: The name of this RoleResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this RoleResult.

        权限名。携带在用户的token中，云服务根据该名称来判断用户是否有权限访问。

        :param name: The name of this RoleResult.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this RoleResult.

        权限描述信息。

        :return: The description of this RoleResult.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this RoleResult.

        权限描述信息。

        :param description: The description of this RoleResult.
        :type description: str
        """
        self._description = description

    @property
    def links(self):
        r"""Gets the links of this RoleResult.

        :return: The links of this RoleResult.
        :rtype: :class:`huaweicloudsdkiam.v3.Links`
        """
        return self._links

    @links.setter
    def links(self, links):
        r"""Sets the links of this RoleResult.

        :param links: The links of this RoleResult.
        :type links: :class:`huaweicloudsdkiam.v3.Links`
        """
        self._links = links

    @property
    def id(self):
        r"""Gets the id of this RoleResult.

        权限ID。

        :return: The id of this RoleResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this RoleResult.

        权限ID。

        :param id: The id of this RoleResult.
        :type id: str
        """
        self._id = id

    @property
    def display_name(self):
        r"""Gets the display_name of this RoleResult.

        权限展示名。

        :return: The display_name of this RoleResult.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this RoleResult.

        权限展示名。

        :param display_name: The display_name of this RoleResult.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def type(self):
        r"""Gets the type of this RoleResult.

        权限的显示模式。 > - AX表示在domain层显示。 > - XA表示在project层显示。 > - AA表示在domain和project层均显示。 > - XX表示在domain和project层均不显示。 > - 自定义策略的显示模式只能为AX或者XA，不能在domain层和project层都显示（AA），或者在domain层和project层都不显示（XX）。

        :return: The type of this RoleResult.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this RoleResult.

        权限的显示模式。 > - AX表示在domain层显示。 > - XA表示在project层显示。 > - AA表示在domain和project层均显示。 > - XX表示在domain和project层均不显示。 > - 自定义策略的显示模式只能为AX或者XA，不能在domain层和project层都显示（AA），或者在domain层和project层都不显示（XX）。

        :param type: The type of this RoleResult.
        :type type: str
        """
        self._type = type

    @property
    def policy(self):
        r"""Gets the policy of this RoleResult.

        :return: The policy of this RoleResult.
        :rtype: :class:`huaweicloudsdkiam.v3.RolePolicy`
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        r"""Sets the policy of this RoleResult.

        :param policy: The policy of this RoleResult.
        :type policy: :class:`huaweicloudsdkiam.v3.RolePolicy`
        """
        self._policy = policy

    @property
    def updated_time(self):
        r"""Gets the updated_time of this RoleResult.

        权限更新时间。

        :return: The updated_time of this RoleResult.
        :rtype: str
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        r"""Sets the updated_time of this RoleResult.

        权限更新时间。

        :param updated_time: The updated_time of this RoleResult.
        :type updated_time: str
        """
        self._updated_time = updated_time

    @property
    def created_time(self):
        r"""Gets the created_time of this RoleResult.

        权限创建时间。

        :return: The created_time of this RoleResult.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        r"""Sets the created_time of this RoleResult.

        权限创建时间。

        :param created_time: The created_time of this RoleResult.
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
        if not isinstance(other, RoleResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
