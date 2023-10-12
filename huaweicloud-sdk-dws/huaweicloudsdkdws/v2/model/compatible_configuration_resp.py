# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CompatibleConfigurationResp:

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
        'links': 'list[LinkResp]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'links': 'links'
    }

    def __init__(self, id=None, name=None, links=None):
        """CompatibleConfigurationResp

        The model defined in huaweicloud sdk

        :param id: ID
        :type id: str
        :param name: 名称
        :type name: str
        :param links: 连接
        :type links: list[:class:`huaweicloudsdkdws.v2.LinkResp`]
        """
        
        

        self._id = None
        self._name = None
        self._links = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if links is not None:
            self.links = links

    @property
    def id(self):
        """Gets the id of this CompatibleConfigurationResp.

        ID

        :return: The id of this CompatibleConfigurationResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CompatibleConfigurationResp.

        ID

        :param id: The id of this CompatibleConfigurationResp.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this CompatibleConfigurationResp.

        名称

        :return: The name of this CompatibleConfigurationResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CompatibleConfigurationResp.

        名称

        :param name: The name of this CompatibleConfigurationResp.
        :type name: str
        """
        self._name = name

    @property
    def links(self):
        """Gets the links of this CompatibleConfigurationResp.

        连接

        :return: The links of this CompatibleConfigurationResp.
        :rtype: list[:class:`huaweicloudsdkdws.v2.LinkResp`]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this CompatibleConfigurationResp.

        连接

        :param links: The links of this CompatibleConfigurationResp.
        :type links: list[:class:`huaweicloudsdkdws.v2.LinkResp`]
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
        if not isinstance(other, CompatibleConfigurationResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
