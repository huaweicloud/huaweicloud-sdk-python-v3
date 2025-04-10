# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UntagResourceReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tags': 'list[Untag]'
    }

    attribute_map = {
        'tags': 'tags'
    }

    def __init__(self, tags=None):
        r"""UntagResourceReqBody

        The model defined in huaweicloud sdk

        :param tags: 一个或多个标签键值对的列表。标签键必须存在，而不是空字符串。标签值必须存在，但可以是空字符串。
        :type tags: list[:class:`huaweicloudsdkram.v1.Untag`]
        """
        
        

        self._tags = None
        self.discriminator = None

        self.tags = tags

    @property
    def tags(self):
        r"""Gets the tags of this UntagResourceReqBody.

        一个或多个标签键值对的列表。标签键必须存在，而不是空字符串。标签值必须存在，但可以是空字符串。

        :return: The tags of this UntagResourceReqBody.
        :rtype: list[:class:`huaweicloudsdkram.v1.Untag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this UntagResourceReqBody.

        一个或多个标签键值对的列表。标签键必须存在，而不是空字符串。标签值必须存在，但可以是空字符串。

        :param tags: The tags of this UntagResourceReqBody.
        :type tags: list[:class:`huaweicloudsdkram.v1.Untag`]
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
        if not isinstance(other, UntagResourceReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
