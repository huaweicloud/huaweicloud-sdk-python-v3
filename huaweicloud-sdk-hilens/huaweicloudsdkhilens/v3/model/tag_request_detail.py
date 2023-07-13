# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TagRequestDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tags': 'list[TagObject]'
    }

    attribute_map = {
        'tags': 'tags'
    }

    def __init__(self, tags=None):
        """TagRequestDetail

        The model defined in huaweicloud sdk

        :param tags: 资源标签对列表
        :type tags: list[:class:`huaweicloudsdkhilens.v3.TagObject`]
        """
        
        

        self._tags = None
        self.discriminator = None

        if tags is not None:
            self.tags = tags

    @property
    def tags(self):
        """Gets the tags of this TagRequestDetail.

        资源标签对列表

        :return: The tags of this TagRequestDetail.
        :rtype: list[:class:`huaweicloudsdkhilens.v3.TagObject`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this TagRequestDetail.

        资源标签对列表

        :param tags: The tags of this TagRequestDetail.
        :type tags: list[:class:`huaweicloudsdkhilens.v3.TagObject`]
        """
        self._tags = tags

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
        if not isinstance(other, TagRequestDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
