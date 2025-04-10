# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePoem:

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
        'type': 'int',
        'acrostic': 'bool'
    }

    attribute_map = {
        'title': 'title',
        'type': 'type',
        'acrostic': 'acrostic'
    }

    def __init__(self, title=None, type=None, acrostic=None):
        r"""CreatePoem

        The model defined in huaweicloud sdk

        :param title: 诗歌标题，目前仅支持UTF-8编码，仅支持中文，长度为1-10
        :type title: str
        :param type: 诗歌类型，取值如下： 0：五言绝句； 1：七言绝句； 2：五言律诗； 3：七言律诗；
        :type type: int
        :param acrostic: 藏头诗，取值如下： 取值为true，为藏头诗； 取值为false，非藏头诗； 默认取值为false。
        :type acrostic: bool
        """
        
        

        self._title = None
        self._type = None
        self._acrostic = None
        self.discriminator = None

        self.title = title
        self.type = type
        if acrostic is not None:
            self.acrostic = acrostic

    @property
    def title(self):
        r"""Gets the title of this CreatePoem.

        诗歌标题，目前仅支持UTF-8编码，仅支持中文，长度为1-10

        :return: The title of this CreatePoem.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this CreatePoem.

        诗歌标题，目前仅支持UTF-8编码，仅支持中文，长度为1-10

        :param title: The title of this CreatePoem.
        :type title: str
        """
        self._title = title

    @property
    def type(self):
        r"""Gets the type of this CreatePoem.

        诗歌类型，取值如下： 0：五言绝句； 1：七言绝句； 2：五言律诗； 3：七言律诗；

        :return: The type of this CreatePoem.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CreatePoem.

        诗歌类型，取值如下： 0：五言绝句； 1：七言绝句； 2：五言律诗； 3：七言律诗；

        :param type: The type of this CreatePoem.
        :type type: int
        """
        self._type = type

    @property
    def acrostic(self):
        r"""Gets the acrostic of this CreatePoem.

        藏头诗，取值如下： 取值为true，为藏头诗； 取值为false，非藏头诗； 默认取值为false。

        :return: The acrostic of this CreatePoem.
        :rtype: bool
        """
        return self._acrostic

    @acrostic.setter
    def acrostic(self, acrostic):
        r"""Sets the acrostic of this CreatePoem.

        藏头诗，取值如下： 取值为true，为藏头诗； 取值为false，非藏头诗； 默认取值为false。

        :param acrostic: The acrostic of this CreatePoem.
        :type acrostic: bool
        """
        self._acrostic = acrostic

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
        if not isinstance(other, CreatePoem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
