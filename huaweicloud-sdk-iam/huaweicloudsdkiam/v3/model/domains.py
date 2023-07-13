# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Domains:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enabled': 'bool',
        'id': 'str',
        'name': 'str',
        'links': 'LinksSelf',
        'description': 'str'
    }

    attribute_map = {
        'enabled': 'enabled',
        'id': 'id',
        'name': 'name',
        'links': 'links',
        'description': 'description'
    }

    def __init__(self, enabled=None, id=None, name=None, links=None, description=None):
        """Domains

        The model defined in huaweicloud sdk

        :param enabled: 是否启用账号，true为启用，false为停用，默认为true。
        :type enabled: bool
        :param id: 账号ID。
        :type id: str
        :param name: 账号名。
        :type name: str
        :param links: 
        :type links: :class:`huaweicloudsdkiam.v3.LinksSelf`
        :param description: 账号的描述信息。
        :type description: str
        """
        
        

        self._enabled = None
        self._id = None
        self._name = None
        self._links = None
        self._description = None
        self.discriminator = None

        self.enabled = enabled
        self.id = id
        self.name = name
        self.links = links
        self.description = description

    @property
    def enabled(self):
        """Gets the enabled of this Domains.

        是否启用账号，true为启用，false为停用，默认为true。

        :return: The enabled of this Domains.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this Domains.

        是否启用账号，true为启用，false为停用，默认为true。

        :param enabled: The enabled of this Domains.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def id(self):
        """Gets the id of this Domains.

        账号ID。

        :return: The id of this Domains.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Domains.

        账号ID。

        :param id: The id of this Domains.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this Domains.

        账号名。

        :return: The name of this Domains.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Domains.

        账号名。

        :param name: The name of this Domains.
        :type name: str
        """
        self._name = name

    @property
    def links(self):
        """Gets the links of this Domains.

        :return: The links of this Domains.
        :rtype: :class:`huaweicloudsdkiam.v3.LinksSelf`
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Domains.

        :param links: The links of this Domains.
        :type links: :class:`huaweicloudsdkiam.v3.LinksSelf`
        """
        self._links = links

    @property
    def description(self):
        """Gets the description of this Domains.

        账号的描述信息。

        :return: The description of this Domains.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Domains.

        账号的描述信息。

        :param description: The description of this Domains.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, Domains):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
