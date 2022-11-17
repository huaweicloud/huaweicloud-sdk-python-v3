# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCreateOrDeleteTagsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tags': 'list[TagItem]',
        'action': 'str',
        'sequence': 'str'
    }

    attribute_map = {
        'tags': 'tags',
        'action': 'action',
        'sequence': 'sequence'
    }

    def __init__(self, tags=None, action=None, sequence=None):
        """BatchCreateOrDeleteTagsRequestBody

        The model defined in huaweicloud sdk

        :param tags: 标签列表，key和value键值对的集合。
        :type tags: list[:class:`huaweicloudsdkcsms.v1.TagItem`]
        :param action: 操作标识： 仅限于“create”和“delete”。
        :type action: str
        :param sequence: 请求消息序列号，36字节序列号。 例如：919c82d4-8046-4722-9094-35c3c6524cff
        :type sequence: str
        """
        
        

        self._tags = None
        self._action = None
        self._sequence = None
        self.discriminator = None

        if tags is not None:
            self.tags = tags
        if action is not None:
            self.action = action
        if sequence is not None:
            self.sequence = sequence

    @property
    def tags(self):
        """Gets the tags of this BatchCreateOrDeleteTagsRequestBody.

        标签列表，key和value键值对的集合。

        :return: The tags of this BatchCreateOrDeleteTagsRequestBody.
        :rtype: list[:class:`huaweicloudsdkcsms.v1.TagItem`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this BatchCreateOrDeleteTagsRequestBody.

        标签列表，key和value键值对的集合。

        :param tags: The tags of this BatchCreateOrDeleteTagsRequestBody.
        :type tags: list[:class:`huaweicloudsdkcsms.v1.TagItem`]
        """
        self._tags = tags

    @property
    def action(self):
        """Gets the action of this BatchCreateOrDeleteTagsRequestBody.

        操作标识： 仅限于“create”和“delete”。

        :return: The action of this BatchCreateOrDeleteTagsRequestBody.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this BatchCreateOrDeleteTagsRequestBody.

        操作标识： 仅限于“create”和“delete”。

        :param action: The action of this BatchCreateOrDeleteTagsRequestBody.
        :type action: str
        """
        self._action = action

    @property
    def sequence(self):
        """Gets the sequence of this BatchCreateOrDeleteTagsRequestBody.

        请求消息序列号，36字节序列号。 例如：919c82d4-8046-4722-9094-35c3c6524cff

        :return: The sequence of this BatchCreateOrDeleteTagsRequestBody.
        :rtype: str
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        """Sets the sequence of this BatchCreateOrDeleteTagsRequestBody.

        请求消息序列号，36字节序列号。 例如：919c82d4-8046-4722-9094-35c3c6524cff

        :param sequence: The sequence of this BatchCreateOrDeleteTagsRequestBody.
        :type sequence: str
        """
        self._sequence = sequence

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
        if not isinstance(other, BatchCreateOrDeleteTagsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
