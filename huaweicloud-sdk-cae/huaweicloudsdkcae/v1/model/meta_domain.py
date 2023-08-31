# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MetaDomain:

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
        'name': 'str',
        'created_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'created_at': 'created_at'
    }

    def __init__(self, id=None, name=None, created_at=None):
        """MetaDomain

        The model defined in huaweicloud sdk

        :param id: 域名ID。
        :type id: str
        :param name: 域名名称。
        :type name: str
        :param created_at: 创建时间。
        :type created_at: datetime
        """
        
        

        self._id = None
        self._name = None
        self._created_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if created_at is not None:
            self.created_at = created_at

    @property
    def id(self):
        """Gets the id of this MetaDomain.

        域名ID。

        :return: The id of this MetaDomain.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MetaDomain.

        域名ID。

        :param id: The id of this MetaDomain.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this MetaDomain.

        域名名称。

        :return: The name of this MetaDomain.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MetaDomain.

        域名名称。

        :param name: The name of this MetaDomain.
        :type name: str
        """
        self._name = name

    @property
    def created_at(self):
        """Gets the created_at of this MetaDomain.

        创建时间。

        :return: The created_at of this MetaDomain.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this MetaDomain.

        创建时间。

        :param created_at: The created_at of this MetaDomain.
        :type created_at: datetime
        """
        self._created_at = created_at

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
        if not isinstance(other, MetaDomain):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
