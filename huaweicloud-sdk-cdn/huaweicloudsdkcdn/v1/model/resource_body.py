# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sources': 'list[SourceWithPort]'
    }

    attribute_map = {
        'sources': 'sources'
    }

    def __init__(self, sources=None):
        r"""ResourceBody

        The model defined in huaweicloud sdk

        :param sources: 源站配置。
        :type sources: list[:class:`huaweicloudsdkcdn.v1.SourceWithPort`]
        """
        
        

        self._sources = None
        self.discriminator = None

        self.sources = sources

    @property
    def sources(self):
        r"""Gets the sources of this ResourceBody.

        源站配置。

        :return: The sources of this ResourceBody.
        :rtype: list[:class:`huaweicloudsdkcdn.v1.SourceWithPort`]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        r"""Sets the sources of this ResourceBody.

        源站配置。

        :param sources: The sources of this ResourceBody.
        :type sources: list[:class:`huaweicloudsdkcdn.v1.SourceWithPort`]
        """
        self._sources = sources

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
        if not isinstance(other, ResourceBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
