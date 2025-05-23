# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Service:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'links': 'Links',
        'id': 'str',
        'type': 'str',
        'enabled': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'links': 'links',
        'id': 'id',
        'type': 'type',
        'enabled': 'enabled'
    }

    def __init__(self, name=None, description=None, links=None, id=None, type=None, enabled=None):
        r"""Service

        The model defined in huaweicloud sdk

        :param name: 服务名。
        :type name: str
        :param description: 服务描述信息。
        :type description: str
        :param links: 
        :type links: :class:`huaweicloudsdkiam.v3.Links`
        :param id: 服务ID。
        :type id: str
        :param type: 服务类型。
        :type type: str
        :param enabled: 服务是否可用。
        :type enabled: bool
        """
        
        

        self._name = None
        self._description = None
        self._links = None
        self._id = None
        self._type = None
        self._enabled = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.links = links
        self.id = id
        self.type = type
        self.enabled = enabled

    @property
    def name(self):
        r"""Gets the name of this Service.

        服务名。

        :return: The name of this Service.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Service.

        服务名。

        :param name: The name of this Service.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this Service.

        服务描述信息。

        :return: The description of this Service.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this Service.

        服务描述信息。

        :param description: The description of this Service.
        :type description: str
        """
        self._description = description

    @property
    def links(self):
        r"""Gets the links of this Service.

        :return: The links of this Service.
        :rtype: :class:`huaweicloudsdkiam.v3.Links`
        """
        return self._links

    @links.setter
    def links(self, links):
        r"""Sets the links of this Service.

        :param links: The links of this Service.
        :type links: :class:`huaweicloudsdkiam.v3.Links`
        """
        self._links = links

    @property
    def id(self):
        r"""Gets the id of this Service.

        服务ID。

        :return: The id of this Service.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Service.

        服务ID。

        :param id: The id of this Service.
        :type id: str
        """
        self._id = id

    @property
    def type(self):
        r"""Gets the type of this Service.

        服务类型。

        :return: The type of this Service.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this Service.

        服务类型。

        :param type: The type of this Service.
        :type type: str
        """
        self._type = type

    @property
    def enabled(self):
        r"""Gets the enabled of this Service.

        服务是否可用。

        :return: The enabled of this Service.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this Service.

        服务是否可用。

        :param enabled: The enabled of this Service.
        :type enabled: bool
        """
        self._enabled = enabled

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
        if not isinstance(other, Service):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
