# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDocumentSegmentReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'document_id': 'str',
        'id': 'str',
        'text_index': 'int',
        'text': 'str'
    }

    attribute_map = {
        'document_id': 'document_id',
        'id': 'id',
        'text_index': 'text_index',
        'text': 'text'
    }

    def __init__(self, document_id=None, id=None, text_index=None, text=None):
        r"""UpdateDocumentSegmentReq

        The model defined in huaweicloud sdk

        :param document_id: 文档ID。
        :type document_id: str
        :param id: 文档分段文本ID。
        :type id: str
        :param text_index: 分段序号
        :type text_index: int
        :param text: 文档分段文本。
        :type text: str
        """
        
        

        self._document_id = None
        self._id = None
        self._text_index = None
        self._text = None
        self.discriminator = None

        self.document_id = document_id
        self.id = id
        if text_index is not None:
            self.text_index = text_index
        if text is not None:
            self.text = text

    @property
    def document_id(self):
        r"""Gets the document_id of this UpdateDocumentSegmentReq.

        文档ID。

        :return: The document_id of this UpdateDocumentSegmentReq.
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        r"""Sets the document_id of this UpdateDocumentSegmentReq.

        文档ID。

        :param document_id: The document_id of this UpdateDocumentSegmentReq.
        :type document_id: str
        """
        self._document_id = document_id

    @property
    def id(self):
        r"""Gets the id of this UpdateDocumentSegmentReq.

        文档分段文本ID。

        :return: The id of this UpdateDocumentSegmentReq.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UpdateDocumentSegmentReq.

        文档分段文本ID。

        :param id: The id of this UpdateDocumentSegmentReq.
        :type id: str
        """
        self._id = id

    @property
    def text_index(self):
        r"""Gets the text_index of this UpdateDocumentSegmentReq.

        分段序号

        :return: The text_index of this UpdateDocumentSegmentReq.
        :rtype: int
        """
        return self._text_index

    @text_index.setter
    def text_index(self, text_index):
        r"""Sets the text_index of this UpdateDocumentSegmentReq.

        分段序号

        :param text_index: The text_index of this UpdateDocumentSegmentReq.
        :type text_index: int
        """
        self._text_index = text_index

    @property
    def text(self):
        r"""Gets the text of this UpdateDocumentSegmentReq.

        文档分段文本。

        :return: The text of this UpdateDocumentSegmentReq.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        r"""Sets the text of this UpdateDocumentSegmentReq.

        文档分段文本。

        :param text: The text of this UpdateDocumentSegmentReq.
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
        if not isinstance(other, UpdateDocumentSegmentReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
