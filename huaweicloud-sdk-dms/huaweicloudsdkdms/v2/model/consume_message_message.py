# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConsumeMessageMessage:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'body': 'object',
        'attributes': 'object',
        'tags': 'list[str]'
    }

    attribute_map = {
        'body': 'body',
        'attributes': 'attributes',
        'tags': 'tags'
    }

    def __init__(self, body=None, attributes=None, tags=None):
        """ConsumeMessageMessage

        The model defined in huaweicloud sdk

        :param body: 消息体的内容。
        :type body: object
        :param attributes: 属性的列表。
        :type attributes: object
        :param tags: 标签值。
        :type tags: list[str]
        """
        
        

        self._body = None
        self._attributes = None
        self._tags = None
        self.discriminator = None

        if body is not None:
            self.body = body
        if attributes is not None:
            self.attributes = attributes
        if tags is not None:
            self.tags = tags

    @property
    def body(self):
        """Gets the body of this ConsumeMessageMessage.

        消息体的内容。

        :return: The body of this ConsumeMessageMessage.
        :rtype: object
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ConsumeMessageMessage.

        消息体的内容。

        :param body: The body of this ConsumeMessageMessage.
        :type body: object
        """
        self._body = body

    @property
    def attributes(self):
        """Gets the attributes of this ConsumeMessageMessage.

        属性的列表。

        :return: The attributes of this ConsumeMessageMessage.
        :rtype: object
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this ConsumeMessageMessage.

        属性的列表。

        :param attributes: The attributes of this ConsumeMessageMessage.
        :type attributes: object
        """
        self._attributes = attributes

    @property
    def tags(self):
        """Gets the tags of this ConsumeMessageMessage.

        标签值。

        :return: The tags of this ConsumeMessageMessage.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ConsumeMessageMessage.

        标签值。

        :param tags: The tags of this ConsumeMessageMessage.
        :type tags: list[str]
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
        if not isinstance(other, ConsumeMessageMessage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
