# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryResourcesRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'without_any_tag': 'bool',
        'tags': 'list[Tag]',
        'matches': 'list[Match]'
    }

    attribute_map = {
        'without_any_tag': 'without_any_tag',
        'tags': 'tags',
        'matches': 'matches'
    }

    def __init__(self, without_any_tag=None, tags=None, matches=None):
        """QueryResourcesRequestBody

        The model defined in huaweicloud sdk

        :param without_any_tag: 
        :type without_any_tag: bool
        :param tags: 
        :type tags: list[:class:`huaweicloudsdkvpn.v5.Tag`]
        :param matches: 
        :type matches: list[:class:`huaweicloudsdkvpn.v5.Match`]
        """
        
        

        self._without_any_tag = None
        self._tags = None
        self._matches = None
        self.discriminator = None

        if without_any_tag is not None:
            self.without_any_tag = without_any_tag
        if tags is not None:
            self.tags = tags
        if matches is not None:
            self.matches = matches

    @property
    def without_any_tag(self):
        """Gets the without_any_tag of this QueryResourcesRequestBody.

        :return: The without_any_tag of this QueryResourcesRequestBody.
        :rtype: bool
        """
        return self._without_any_tag

    @without_any_tag.setter
    def without_any_tag(self, without_any_tag):
        """Sets the without_any_tag of this QueryResourcesRequestBody.

        :param without_any_tag: The without_any_tag of this QueryResourcesRequestBody.
        :type without_any_tag: bool
        """
        self._without_any_tag = without_any_tag

    @property
    def tags(self):
        """Gets the tags of this QueryResourcesRequestBody.

        :return: The tags of this QueryResourcesRequestBody.
        :rtype: list[:class:`huaweicloudsdkvpn.v5.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this QueryResourcesRequestBody.

        :param tags: The tags of this QueryResourcesRequestBody.
        :type tags: list[:class:`huaweicloudsdkvpn.v5.Tag`]
        """
        self._tags = tags

    @property
    def matches(self):
        """Gets the matches of this QueryResourcesRequestBody.

        :return: The matches of this QueryResourcesRequestBody.
        :rtype: list[:class:`huaweicloudsdkvpn.v5.Match`]
        """
        return self._matches

    @matches.setter
    def matches(self, matches):
        """Sets the matches of this QueryResourcesRequestBody.

        :param matches: The matches of this QueryResourcesRequestBody.
        :type matches: list[:class:`huaweicloudsdkvpn.v5.Match`]
        """
        self._matches = matches

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
        if not isinstance(other, QueryResourcesRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
