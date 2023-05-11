# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AgencyAllProjectRole:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'links': 'LinksSelf',
        'name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'links': 'links',
        'name': 'name'
    }

    def __init__(self, id=None, links=None, name=None):
        """AgencyAllProjectRole

        The model defined in huaweicloud sdk

        :param id: 权限ID。
        :type id: str
        :param links: 
        :type links: :class:`huaweicloudsdkiam.v3.LinksSelf`
        :param name: 权限名。
        :type name: str
        """
        
        

        self._id = None
        self._links = None
        self._name = None
        self.discriminator = None

        self.id = id
        self.links = links
        self.name = name

    @property
    def id(self):
        """Gets the id of this AgencyAllProjectRole.

        权限ID。

        :return: The id of this AgencyAllProjectRole.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AgencyAllProjectRole.

        权限ID。

        :param id: The id of this AgencyAllProjectRole.
        :type id: str
        """
        self._id = id

    @property
    def links(self):
        """Gets the links of this AgencyAllProjectRole.

        :return: The links of this AgencyAllProjectRole.
        :rtype: :class:`huaweicloudsdkiam.v3.LinksSelf`
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this AgencyAllProjectRole.

        :param links: The links of this AgencyAllProjectRole.
        :type links: :class:`huaweicloudsdkiam.v3.LinksSelf`
        """
        self._links = links

    @property
    def name(self):
        """Gets the name of this AgencyAllProjectRole.

        权限名。

        :return: The name of this AgencyAllProjectRole.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AgencyAllProjectRole.

        权限名。

        :param name: The name of this AgencyAllProjectRole.
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
        if not isinstance(other, AgencyAllProjectRole):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
