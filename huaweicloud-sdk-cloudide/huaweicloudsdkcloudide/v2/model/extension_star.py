# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExtensionStar:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'extension_id': 'str',
        'comment': 'str',
        'stars': 'int'
    }

    attribute_map = {
        'extension_id': 'extension_id',
        'comment': 'comment',
        'stars': 'stars'
    }

    def __init__(self, extension_id=None, comment=None, stars=None):
        r"""ExtensionStar

        The model defined in huaweicloud sdk

        :param extension_id: 插件id
        :type extension_id: str
        :param comment: 评星内容
        :type comment: str
        :param stars: 评星总数
        :type stars: int
        """
        
        

        self._extension_id = None
        self._comment = None
        self._stars = None
        self.discriminator = None

        self.extension_id = extension_id
        if comment is not None:
            self.comment = comment
        self.stars = stars

    @property
    def extension_id(self):
        r"""Gets the extension_id of this ExtensionStar.

        插件id

        :return: The extension_id of this ExtensionStar.
        :rtype: str
        """
        return self._extension_id

    @extension_id.setter
    def extension_id(self, extension_id):
        r"""Sets the extension_id of this ExtensionStar.

        插件id

        :param extension_id: The extension_id of this ExtensionStar.
        :type extension_id: str
        """
        self._extension_id = extension_id

    @property
    def comment(self):
        r"""Gets the comment of this ExtensionStar.

        评星内容

        :return: The comment of this ExtensionStar.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        r"""Sets the comment of this ExtensionStar.

        评星内容

        :param comment: The comment of this ExtensionStar.
        :type comment: str
        """
        self._comment = comment

    @property
    def stars(self):
        r"""Gets the stars of this ExtensionStar.

        评星总数

        :return: The stars of this ExtensionStar.
        :rtype: int
        """
        return self._stars

    @stars.setter
    def stars(self, stars):
        r"""Sets the stars of this ExtensionStar.

        评星总数

        :param stars: The stars of this ExtensionStar.
        :type stars: int
        """
        self._stars = stars

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
        if not isinstance(other, ExtensionStar):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
