# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProjectsListInfo:

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
        'is_domain': 'bool',
        'parent_id': 'str',
        'name': 'str',
        'description': 'str',
        'id': 'str',
        'enabled': 'bool',
        'links': 'SelfLinksInfo'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'is_domain': 'is_domain',
        'parent_id': 'parent_id',
        'name': 'name',
        'description': 'description',
        'id': 'id',
        'enabled': 'enabled',
        'links': 'links'
    }

    def __init__(self, domain_id=None, is_domain=None, parent_id=None, name=None, description=None, id=None, enabled=None, links=None):
        """ProjectsListInfo

        The model defined in huaweicloud sdk

        :param domain_id: 域 ID
        :type domain_id: str
        :param is_domain: 是否是域级
        :type is_domain: bool
        :param parent_id: 父项目 ID
        :type parent_id: str
        :param name: 名称
        :type name: str
        :param description: 描述信息
        :type description: str
        :param id: 项目ID
        :type id: str
        :param enabled: 是否开启
        :type enabled: bool
        :param links: 
        :type links: :class:`huaweicloudsdkcbr.v1.SelfLinksInfo`
        """
        
        

        self._domain_id = None
        self._is_domain = None
        self._parent_id = None
        self._name = None
        self._description = None
        self._id = None
        self._enabled = None
        self._links = None
        self.discriminator = None

        if domain_id is not None:
            self.domain_id = domain_id
        if is_domain is not None:
            self.is_domain = is_domain
        if parent_id is not None:
            self.parent_id = parent_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if enabled is not None:
            self.enabled = enabled
        if links is not None:
            self.links = links

    @property
    def domain_id(self):
        """Gets the domain_id of this ProjectsListInfo.

        域 ID

        :return: The domain_id of this ProjectsListInfo.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this ProjectsListInfo.

        域 ID

        :param domain_id: The domain_id of this ProjectsListInfo.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def is_domain(self):
        """Gets the is_domain of this ProjectsListInfo.

        是否是域级

        :return: The is_domain of this ProjectsListInfo.
        :rtype: bool
        """
        return self._is_domain

    @is_domain.setter
    def is_domain(self, is_domain):
        """Sets the is_domain of this ProjectsListInfo.

        是否是域级

        :param is_domain: The is_domain of this ProjectsListInfo.
        :type is_domain: bool
        """
        self._is_domain = is_domain

    @property
    def parent_id(self):
        """Gets the parent_id of this ProjectsListInfo.

        父项目 ID

        :return: The parent_id of this ProjectsListInfo.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this ProjectsListInfo.

        父项目 ID

        :param parent_id: The parent_id of this ProjectsListInfo.
        :type parent_id: str
        """
        self._parent_id = parent_id

    @property
    def name(self):
        """Gets the name of this ProjectsListInfo.

        名称

        :return: The name of this ProjectsListInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProjectsListInfo.

        名称

        :param name: The name of this ProjectsListInfo.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ProjectsListInfo.

        描述信息

        :return: The description of this ProjectsListInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ProjectsListInfo.

        描述信息

        :param description: The description of this ProjectsListInfo.
        :type description: str
        """
        self._description = description

    @property
    def id(self):
        """Gets the id of this ProjectsListInfo.

        项目ID

        :return: The id of this ProjectsListInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProjectsListInfo.

        项目ID

        :param id: The id of this ProjectsListInfo.
        :type id: str
        """
        self._id = id

    @property
    def enabled(self):
        """Gets the enabled of this ProjectsListInfo.

        是否开启

        :return: The enabled of this ProjectsListInfo.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this ProjectsListInfo.

        是否开启

        :param enabled: The enabled of this ProjectsListInfo.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def links(self):
        """Gets the links of this ProjectsListInfo.

        :return: The links of this ProjectsListInfo.
        :rtype: :class:`huaweicloudsdkcbr.v1.SelfLinksInfo`
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ProjectsListInfo.

        :param links: The links of this ProjectsListInfo.
        :type links: :class:`huaweicloudsdkcbr.v1.SelfLinksInfo`
        """
        self._links = links

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
        if not isinstance(other, ProjectsListInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
