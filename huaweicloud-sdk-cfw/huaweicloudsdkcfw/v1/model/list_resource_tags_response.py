# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListResourceTagsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data': 'str',
        'sys_tags': 'list[ResourceTag]',
        'tags': 'list[ResourceTag]'
    }

    attribute_map = {
        'data': 'data',
        'sys_tags': 'sys_tags',
        'tags': 'tags'
    }

    def __init__(self, data=None, sys_tags=None, tags=None):
        r"""ListResourceTagsResponse

        The model defined in huaweicloud sdk

        :param data: 
        :type data: str
        :param sys_tags: 
        :type sys_tags: list[:class:`huaweicloudsdkcfw.v1.ResourceTag`]
        :param tags: 
        :type tags: list[:class:`huaweicloudsdkcfw.v1.ResourceTag`]
        """
        
        super(ListResourceTagsResponse, self).__init__()

        self._data = None
        self._sys_tags = None
        self._tags = None
        self.discriminator = None

        if data is not None:
            self.data = data
        if sys_tags is not None:
            self.sys_tags = sys_tags
        if tags is not None:
            self.tags = tags

    @property
    def data(self):
        r"""Gets the data of this ListResourceTagsResponse.

        :return: The data of this ListResourceTagsResponse.
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this ListResourceTagsResponse.

        :param data: The data of this ListResourceTagsResponse.
        :type data: str
        """
        self._data = data

    @property
    def sys_tags(self):
        r"""Gets the sys_tags of this ListResourceTagsResponse.

        :return: The sys_tags of this ListResourceTagsResponse.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.ResourceTag`]
        """
        return self._sys_tags

    @sys_tags.setter
    def sys_tags(self, sys_tags):
        r"""Sets the sys_tags of this ListResourceTagsResponse.

        :param sys_tags: The sys_tags of this ListResourceTagsResponse.
        :type sys_tags: list[:class:`huaweicloudsdkcfw.v1.ResourceTag`]
        """
        self._sys_tags = sys_tags

    @property
    def tags(self):
        r"""Gets the tags of this ListResourceTagsResponse.

        :return: The tags of this ListResourceTagsResponse.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.ResourceTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ListResourceTagsResponse.

        :param tags: The tags of this ListResourceTagsResponse.
        :type tags: list[:class:`huaweicloudsdkcfw.v1.ResourceTag`]
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
        if not isinstance(other, ListResourceTagsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
