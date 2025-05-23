# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TagsVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tag_id': 'str',
        'tag_key': 'str',
        'tag_value': 'str'
    }

    attribute_map = {
        'tag_id': 'tag_id',
        'tag_key': 'tag_key',
        'tag_value': 'tag_value'
    }

    def __init__(self, tag_id=None, tag_key=None, tag_value=None):
        r"""TagsVO

        The model defined in huaweicloud sdk

        :param tag_id: 规则id
        :type tag_id: str
        :param tag_key: 规则标签键
        :type tag_key: str
        :param tag_value: 规则标签值
        :type tag_value: str
        """
        
        

        self._tag_id = None
        self._tag_key = None
        self._tag_value = None
        self.discriminator = None

        if tag_id is not None:
            self.tag_id = tag_id
        if tag_key is not None:
            self.tag_key = tag_key
        if tag_value is not None:
            self.tag_value = tag_value

    @property
    def tag_id(self):
        r"""Gets the tag_id of this TagsVO.

        规则id

        :return: The tag_id of this TagsVO.
        :rtype: str
        """
        return self._tag_id

    @tag_id.setter
    def tag_id(self, tag_id):
        r"""Sets the tag_id of this TagsVO.

        规则id

        :param tag_id: The tag_id of this TagsVO.
        :type tag_id: str
        """
        self._tag_id = tag_id

    @property
    def tag_key(self):
        r"""Gets the tag_key of this TagsVO.

        规则标签键

        :return: The tag_key of this TagsVO.
        :rtype: str
        """
        return self._tag_key

    @tag_key.setter
    def tag_key(self, tag_key):
        r"""Sets the tag_key of this TagsVO.

        规则标签键

        :param tag_key: The tag_key of this TagsVO.
        :type tag_key: str
        """
        self._tag_key = tag_key

    @property
    def tag_value(self):
        r"""Gets the tag_value of this TagsVO.

        规则标签值

        :return: The tag_value of this TagsVO.
        :rtype: str
        """
        return self._tag_value

    @tag_value.setter
    def tag_value(self, tag_value):
        r"""Sets the tag_value of this TagsVO.

        规则标签值

        :param tag_value: The tag_value of this TagsVO.
        :type tag_value: str
        """
        self._tag_value = tag_value

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
        if not isinstance(other, TagsVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
