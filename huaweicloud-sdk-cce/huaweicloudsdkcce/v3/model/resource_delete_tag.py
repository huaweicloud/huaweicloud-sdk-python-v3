# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceDeleteTag:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key': 'str'
    }

    attribute_map = {
        'key': 'key'
    }

    def __init__(self, key=None):
        r"""ResourceDeleteTag

        The model defined in huaweicloud sdk

        :param key: Key值。 - 不能为空，最多支持128个字符 - 可用UTF-8格式表示的汉字、字母、数字和空格 - 支持部分特殊字符：_.:/&#x3D;+-@ - 不能以\&quot;\\_sys\\_\&quot;开头
        :type key: str
        """
        
        

        self._key = None
        self.discriminator = None

        if key is not None:
            self.key = key

    @property
    def key(self):
        r"""Gets the key of this ResourceDeleteTag.

        Key值。 - 不能为空，最多支持128个字符 - 可用UTF-8格式表示的汉字、字母、数字和空格 - 支持部分特殊字符：_.:/=+-@ - 不能以\"\\_sys\\_\"开头

        :return: The key of this ResourceDeleteTag.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this ResourceDeleteTag.

        Key值。 - 不能为空，最多支持128个字符 - 可用UTF-8格式表示的汉字、字母、数字和空格 - 支持部分特殊字符：_.:/=+-@ - 不能以\"\\_sys\\_\"开头

        :param key: The key of this ResourceDeleteTag.
        :type key: str
        """
        self._key = key

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
        if not isinstance(other, ResourceDeleteTag):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
