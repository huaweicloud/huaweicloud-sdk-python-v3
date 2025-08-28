# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DocumentSegmentInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'text_index': 'int',
        'id': 'str',
        'title': 'str',
        'text': 'str'
    }

    attribute_map = {
        'text_index': 'text_index',
        'id': 'id',
        'title': 'title',
        'text': 'text'
    }

    def __init__(self, text_index=None, id=None, title=None, text=None):
        r"""DocumentSegmentInfo

        The model defined in huaweicloud sdk

        :param text_index: 分段序号
        :type text_index: int
        :param id: 分段文本ID
        :type id: str
        :param title: 分段文本标题
        :type title: str
        :param text: 分段文本内容
        :type text: str
        """
        
        

        self._text_index = None
        self._id = None
        self._title = None
        self._text = None
        self.discriminator = None

        if text_index is not None:
            self.text_index = text_index
        if id is not None:
            self.id = id
        if title is not None:
            self.title = title
        if text is not None:
            self.text = text

    @property
    def text_index(self):
        r"""Gets the text_index of this DocumentSegmentInfo.

        分段序号

        :return: The text_index of this DocumentSegmentInfo.
        :rtype: int
        """
        return self._text_index

    @text_index.setter
    def text_index(self, text_index):
        r"""Sets the text_index of this DocumentSegmentInfo.

        分段序号

        :param text_index: The text_index of this DocumentSegmentInfo.
        :type text_index: int
        """
        self._text_index = text_index

    @property
    def id(self):
        r"""Gets the id of this DocumentSegmentInfo.

        分段文本ID

        :return: The id of this DocumentSegmentInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DocumentSegmentInfo.

        分段文本ID

        :param id: The id of this DocumentSegmentInfo.
        :type id: str
        """
        self._id = id

    @property
    def title(self):
        r"""Gets the title of this DocumentSegmentInfo.

        分段文本标题

        :return: The title of this DocumentSegmentInfo.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this DocumentSegmentInfo.

        分段文本标题

        :param title: The title of this DocumentSegmentInfo.
        :type title: str
        """
        self._title = title

    @property
    def text(self):
        r"""Gets the text of this DocumentSegmentInfo.

        分段文本内容

        :return: The text of this DocumentSegmentInfo.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        r"""Sets the text of this DocumentSegmentInfo.

        分段文本内容

        :param text: The text of this DocumentSegmentInfo.
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
        if not isinstance(other, DocumentSegmentInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
