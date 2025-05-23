# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SimpleFlavor:

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
        'links': 'list[Link]'
    }

    attribute_map = {
        'id': 'id',
        'links': 'links'
    }

    def __init__(self, id=None, links=None):
        r"""SimpleFlavor

        The model defined in huaweicloud sdk

        :param id: 云服务器规格的ID。
        :type id: str
        :param links: 规格相关快捷链接地址。
        :type links: list[:class:`huaweicloudsdkecs.v2.Link`]
        """
        
        

        self._id = None
        self._links = None
        self.discriminator = None

        self.id = id
        self.links = links

    @property
    def id(self):
        r"""Gets the id of this SimpleFlavor.

        云服务器规格的ID。

        :return: The id of this SimpleFlavor.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SimpleFlavor.

        云服务器规格的ID。

        :param id: The id of this SimpleFlavor.
        :type id: str
        """
        self._id = id

    @property
    def links(self):
        r"""Gets the links of this SimpleFlavor.

        规格相关快捷链接地址。

        :return: The links of this SimpleFlavor.
        :rtype: list[:class:`huaweicloudsdkecs.v2.Link`]
        """
        return self._links

    @links.setter
    def links(self, links):
        r"""Sets the links of this SimpleFlavor.

        规格相关快捷链接地址。

        :param links: The links of this SimpleFlavor.
        :type links: list[:class:`huaweicloudsdkecs.v2.Link`]
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
        if not isinstance(other, SimpleFlavor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
