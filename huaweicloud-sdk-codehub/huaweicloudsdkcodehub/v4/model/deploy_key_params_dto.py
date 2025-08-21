# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeployKeyParamsDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'title': 'str',
        'key': 'str'
    }

    attribute_map = {
        'title': 'title',
        'key': 'key'
    }

    def __init__(self, title=None, key=None):
        r"""DeployKeyParamsDto

        The model defined in huaweicloud sdk

        :param title: **参数解释：** 标题。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type title: str
        :param key: **参数解释：** key值。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type key: str
        """
        
        

        self._title = None
        self._key = None
        self.discriminator = None

        if title is not None:
            self.title = title
        if key is not None:
            self.key = key

    @property
    def title(self):
        r"""Gets the title of this DeployKeyParamsDto.

        **参数解释：** 标题。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The title of this DeployKeyParamsDto.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this DeployKeyParamsDto.

        **参数解释：** 标题。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param title: The title of this DeployKeyParamsDto.
        :type title: str
        """
        self._title = title

    @property
    def key(self):
        r"""Gets the key of this DeployKeyParamsDto.

        **参数解释：** key值。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The key of this DeployKeyParamsDto.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this DeployKeyParamsDto.

        **参数解释：** key值。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param key: The key of this DeployKeyParamsDto.
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
        if not isinstance(other, DeployKeyParamsDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
