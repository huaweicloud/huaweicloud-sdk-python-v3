# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProjectDetailsAndStatusResult:

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
        'status': 'str'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'is_domain': 'is_domain',
        'parent_id': 'parent_id',
        'name': 'name',
        'description': 'description',
        'id': 'id',
        'enabled': 'enabled',
        'status': 'status'
    }

    def __init__(self, domain_id=None, is_domain=None, parent_id=None, name=None, description=None, id=None, enabled=None, status=None):
        r"""ProjectDetailsAndStatusResult

        The model defined in huaweicloud sdk

        :param domain_id: 项目所属账号ID。
        :type domain_id: str
        :param is_domain: false.
        :type is_domain: bool
        :param parent_id: 如果查询自己创建的项目，则此处返回所属区域的项目ID。  如果查询的是系统内置项目，如cn-north-4，则此处返回账号ID。
        :type parent_id: str
        :param name: 项目名称。
        :type name: str
        :param description: 项目描述信息。
        :type description: str
        :param id: 项目ID。
        :type id: str
        :param enabled: 项目是否可用。
        :type enabled: bool
        :param status: 项目状态。
        :type status: str
        """
        
        

        self._domain_id = None
        self._is_domain = None
        self._parent_id = None
        self._name = None
        self._description = None
        self._id = None
        self._enabled = None
        self._status = None
        self.discriminator = None

        self.domain_id = domain_id
        self.is_domain = is_domain
        self.parent_id = parent_id
        self.name = name
        self.description = description
        self.id = id
        self.enabled = enabled
        self.status = status

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ProjectDetailsAndStatusResult.

        项目所属账号ID。

        :return: The domain_id of this ProjectDetailsAndStatusResult.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ProjectDetailsAndStatusResult.

        项目所属账号ID。

        :param domain_id: The domain_id of this ProjectDetailsAndStatusResult.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def is_domain(self):
        r"""Gets the is_domain of this ProjectDetailsAndStatusResult.

        false.

        :return: The is_domain of this ProjectDetailsAndStatusResult.
        :rtype: bool
        """
        return self._is_domain

    @is_domain.setter
    def is_domain(self, is_domain):
        r"""Sets the is_domain of this ProjectDetailsAndStatusResult.

        false.

        :param is_domain: The is_domain of this ProjectDetailsAndStatusResult.
        :type is_domain: bool
        """
        self._is_domain = is_domain

    @property
    def parent_id(self):
        r"""Gets the parent_id of this ProjectDetailsAndStatusResult.

        如果查询自己创建的项目，则此处返回所属区域的项目ID。  如果查询的是系统内置项目，如cn-north-4，则此处返回账号ID。

        :return: The parent_id of this ProjectDetailsAndStatusResult.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        r"""Sets the parent_id of this ProjectDetailsAndStatusResult.

        如果查询自己创建的项目，则此处返回所属区域的项目ID。  如果查询的是系统内置项目，如cn-north-4，则此处返回账号ID。

        :param parent_id: The parent_id of this ProjectDetailsAndStatusResult.
        :type parent_id: str
        """
        self._parent_id = parent_id

    @property
    def name(self):
        r"""Gets the name of this ProjectDetailsAndStatusResult.

        项目名称。

        :return: The name of this ProjectDetailsAndStatusResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ProjectDetailsAndStatusResult.

        项目名称。

        :param name: The name of this ProjectDetailsAndStatusResult.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ProjectDetailsAndStatusResult.

        项目描述信息。

        :return: The description of this ProjectDetailsAndStatusResult.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ProjectDetailsAndStatusResult.

        项目描述信息。

        :param description: The description of this ProjectDetailsAndStatusResult.
        :type description: str
        """
        self._description = description

    @property
    def id(self):
        r"""Gets the id of this ProjectDetailsAndStatusResult.

        项目ID。

        :return: The id of this ProjectDetailsAndStatusResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ProjectDetailsAndStatusResult.

        项目ID。

        :param id: The id of this ProjectDetailsAndStatusResult.
        :type id: str
        """
        self._id = id

    @property
    def enabled(self):
        r"""Gets the enabled of this ProjectDetailsAndStatusResult.

        项目是否可用。

        :return: The enabled of this ProjectDetailsAndStatusResult.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this ProjectDetailsAndStatusResult.

        项目是否可用。

        :param enabled: The enabled of this ProjectDetailsAndStatusResult.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def status(self):
        r"""Gets the status of this ProjectDetailsAndStatusResult.

        项目状态。

        :return: The status of this ProjectDetailsAndStatusResult.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ProjectDetailsAndStatusResult.

        项目状态。

        :param status: The status of this ProjectDetailsAndStatusResult.
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
        if not isinstance(other, ProjectDetailsAndStatusResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
