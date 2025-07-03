# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NovaSimpleServer:

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
        'id': 'str',
        'links': 'list[NovaLink]'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'links': 'links'
    }

    def __init__(self, name=None, id=None, links=None):
        r"""NovaSimpleServer

        The model defined in huaweicloud sdk

        :param name: 云服务器名称。
        :type name: str
        :param id: 云服务器唯一标识。
        :type id: str
        :param links: 云服务器相关快捷链接信息。
        :type links: list[:class:`huaweicloudsdkecs.v2.NovaLink`]
        """
        
        

        self._name = None
        self._id = None
        self._links = None
        self.discriminator = None

        self.name = name
        self.id = id
        self.links = links

    @property
    def name(self):
        r"""Gets the name of this NovaSimpleServer.

        云服务器名称。

        :return: The name of this NovaSimpleServer.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this NovaSimpleServer.

        云服务器名称。

        :param name: The name of this NovaSimpleServer.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        r"""Gets the id of this NovaSimpleServer.

        云服务器唯一标识。

        :return: The id of this NovaSimpleServer.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this NovaSimpleServer.

        云服务器唯一标识。

        :param id: The id of this NovaSimpleServer.
        :type id: str
        """
        self._id = id

    @property
    def links(self):
        r"""Gets the links of this NovaSimpleServer.

        云服务器相关快捷链接信息。

        :return: The links of this NovaSimpleServer.
        :rtype: list[:class:`huaweicloudsdkecs.v2.NovaLink`]
        """
        return self._links

    @links.setter
    def links(self, links):
        r"""Sets the links of this NovaSimpleServer.

        云服务器相关快捷链接信息。

        :param links: The links of this NovaSimpleServer.
        :type links: list[:class:`huaweicloudsdkecs.v2.NovaLink`]
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
        if not isinstance(other, NovaSimpleServer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
