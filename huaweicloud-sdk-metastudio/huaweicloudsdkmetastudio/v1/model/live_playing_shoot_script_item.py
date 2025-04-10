# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LivePlayingShootScriptItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sequence_no': 'int',
        'title': 'str',
        'text': 'str'
    }

    attribute_map = {
        'sequence_no': 'sequence_no',
        'title': 'title',
        'text': 'text'
    }

    def __init__(self, sequence_no=None, title=None, text=None):
        r"""LivePlayingShootScriptItem

        The model defined in huaweicloud sdk

        :param sequence_no: 剧本序号。
        :type sequence_no: int
        :param title: 段落标题。
        :type title: str
        :param text: 段落话术内容。
        :type text: str
        """
        
        

        self._sequence_no = None
        self._title = None
        self._text = None
        self.discriminator = None

        if sequence_no is not None:
            self.sequence_no = sequence_no
        if title is not None:
            self.title = title
        if text is not None:
            self.text = text

    @property
    def sequence_no(self):
        r"""Gets the sequence_no of this LivePlayingShootScriptItem.

        剧本序号。

        :return: The sequence_no of this LivePlayingShootScriptItem.
        :rtype: int
        """
        return self._sequence_no

    @sequence_no.setter
    def sequence_no(self, sequence_no):
        r"""Sets the sequence_no of this LivePlayingShootScriptItem.

        剧本序号。

        :param sequence_no: The sequence_no of this LivePlayingShootScriptItem.
        :type sequence_no: int
        """
        self._sequence_no = sequence_no

    @property
    def title(self):
        r"""Gets the title of this LivePlayingShootScriptItem.

        段落标题。

        :return: The title of this LivePlayingShootScriptItem.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this LivePlayingShootScriptItem.

        段落标题。

        :param title: The title of this LivePlayingShootScriptItem.
        :type title: str
        """
        self._title = title

    @property
    def text(self):
        r"""Gets the text of this LivePlayingShootScriptItem.

        段落话术内容。

        :return: The text of this LivePlayingShootScriptItem.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        r"""Sets the text of this LivePlayingShootScriptItem.

        段落话术内容。

        :param text: The text of this LivePlayingShootScriptItem.
        :type text: str
        """
        self._text = text

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
        if not isinstance(other, LivePlayingShootScriptItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
