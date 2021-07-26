# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NovaServerImage:


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
        'links': 'list[NovaLink]'
    }

    attribute_map = {
        'id': 'id',
        'links': 'links'
    }

    def __init__(self, id=None, links=None):
        """NovaServerImage - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._links = None
        self.discriminator = None

        self.id = id
        self.links = links

    @property
    def id(self):
        """Gets the id of this NovaServerImage.

        镜像ID。

        :return: The id of this NovaServerImage.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NovaServerImage.

        镜像ID。

        :param id: The id of this NovaServerImage.
        :type: str
        """
        self._id = id

    @property
    def links(self):
        """Gets the links of this NovaServerImage.

        云服务器类型相关标记快捷链接信息。

        :return: The links of this NovaServerImage.
        :rtype: list[NovaLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this NovaServerImage.

        云服务器类型相关标记快捷链接信息。

        :param links: The links of this NovaServerImage.
        :type: list[NovaLink]
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
        import simplejson as json
        return json.dumps(sanitize_for_serialization(self))

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NovaServerImage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
