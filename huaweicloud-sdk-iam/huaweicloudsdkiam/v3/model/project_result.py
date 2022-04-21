# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProjectResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'is_domain': 'bool',
        'description': 'str',
        'links': 'Links',
        'enabled': 'bool',
        'id': 'str',
        'parent_id': 'str',
        'domain_id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'is_domain': 'is_domain',
        'description': 'description',
        'links': 'links',
        'enabled': 'enabled',
        'id': 'id',
        'parent_id': 'parent_id',
        'domain_id': 'domain_id',
        'name': 'name'
    }

    def __init__(self, is_domain=None, description=None, links=None, enabled=None, id=None, parent_id=None, domain_id=None, name=None):
        """ProjectResult

        The model defined in huaweicloud sdk

        :param is_domain: false.
        :type is_domain: bool
        :param description: 项目描述信息。
        :type description: str
        :param links: 
        :type links: :class:`huaweicloudsdkiam.v3.Links`
        :param enabled: 项目是否可用。
        :type enabled: bool
        :param id: 项目ID。
        :type id: str
        :param parent_id: 如果查询自己创建的项目，则此处返回所属区域的项目ID。  如果查询的是系统内置项目，如cn-north-4，则此处返回账号ID。
        :type parent_id: str
        :param domain_id: 项目所属账号ID。
        :type domain_id: str
        :param name: 项目名称。
        :type name: str
        """
        
        

        self._is_domain = None
        self._description = None
        self._links = None
        self._enabled = None
        self._id = None
        self._parent_id = None
        self._domain_id = None
        self._name = None
        self.discriminator = None

        self.is_domain = is_domain
        self.description = description
        self.links = links
        self.enabled = enabled
        self.id = id
        self.parent_id = parent_id
        self.domain_id = domain_id
        self.name = name

    @property
    def is_domain(self):
        """Gets the is_domain of this ProjectResult.

        false.

        :return: The is_domain of this ProjectResult.
        :rtype: bool
        """
        return self._is_domain

    @is_domain.setter
    def is_domain(self, is_domain):
        """Sets the is_domain of this ProjectResult.

        false.

        :param is_domain: The is_domain of this ProjectResult.
        :type is_domain: bool
        """
        self._is_domain = is_domain

    @property
    def description(self):
        """Gets the description of this ProjectResult.

        项目描述信息。

        :return: The description of this ProjectResult.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ProjectResult.

        项目描述信息。

        :param description: The description of this ProjectResult.
        :type description: str
        """
        self._description = description

    @property
    def links(self):
        """Gets the links of this ProjectResult.


        :return: The links of this ProjectResult.
        :rtype: :class:`huaweicloudsdkiam.v3.Links`
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ProjectResult.


        :param links: The links of this ProjectResult.
        :type links: :class:`huaweicloudsdkiam.v3.Links`
        """
        self._links = links

    @property
    def enabled(self):
        """Gets the enabled of this ProjectResult.

        项目是否可用。

        :return: The enabled of this ProjectResult.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this ProjectResult.

        项目是否可用。

        :param enabled: The enabled of this ProjectResult.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def id(self):
        """Gets the id of this ProjectResult.

        项目ID。

        :return: The id of this ProjectResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProjectResult.

        项目ID。

        :param id: The id of this ProjectResult.
        :type id: str
        """
        self._id = id

    @property
    def parent_id(self):
        """Gets the parent_id of this ProjectResult.

        如果查询自己创建的项目，则此处返回所属区域的项目ID。  如果查询的是系统内置项目，如cn-north-4，则此处返回账号ID。

        :return: The parent_id of this ProjectResult.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this ProjectResult.

        如果查询自己创建的项目，则此处返回所属区域的项目ID。  如果查询的是系统内置项目，如cn-north-4，则此处返回账号ID。

        :param parent_id: The parent_id of this ProjectResult.
        :type parent_id: str
        """
        self._parent_id = parent_id

    @property
    def domain_id(self):
        """Gets the domain_id of this ProjectResult.

        项目所属账号ID。

        :return: The domain_id of this ProjectResult.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this ProjectResult.

        项目所属账号ID。

        :param domain_id: The domain_id of this ProjectResult.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def name(self):
        """Gets the name of this ProjectResult.

        项目名称。

        :return: The name of this ProjectResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProjectResult.

        项目名称。

        :param name: The name of this ProjectResult.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, ProjectResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
