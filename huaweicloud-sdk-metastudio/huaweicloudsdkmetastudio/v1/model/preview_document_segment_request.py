# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PreviewDocumentSegmentRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_app_user_id': 'str',
        'document_id': 'str',
        'preview_lines': 'int',
        'body': 'DocumentSegmentParam'
    }

    attribute_map = {
        'x_app_user_id': 'X-App-UserId',
        'document_id': 'document_id',
        'preview_lines': 'preview_lines',
        'body': 'body'
    }

    def __init__(self, x_app_user_id=None, document_id=None, preview_lines=None, body=None):
        r"""PreviewDocumentSegmentRequest

        The model defined in huaweicloud sdk

        :param x_app_user_id: 第三方用户ID。不允许输入中文。
        :type x_app_user_id: str
        :param document_id: 文档ID。
        :type document_id: str
        :param preview_lines: 预览行数。
        :type preview_lines: int
        :param body: Body of the PreviewDocumentSegmentRequest
        :type body: :class:`huaweicloudsdkmetastudio.v1.DocumentSegmentParam`
        """
        
        

        self._x_app_user_id = None
        self._document_id = None
        self._preview_lines = None
        self._body = None
        self.discriminator = None

        if x_app_user_id is not None:
            self.x_app_user_id = x_app_user_id
        self.document_id = document_id
        if preview_lines is not None:
            self.preview_lines = preview_lines
        if body is not None:
            self.body = body

    @property
    def x_app_user_id(self):
        r"""Gets the x_app_user_id of this PreviewDocumentSegmentRequest.

        第三方用户ID。不允许输入中文。

        :return: The x_app_user_id of this PreviewDocumentSegmentRequest.
        :rtype: str
        """
        return self._x_app_user_id

    @x_app_user_id.setter
    def x_app_user_id(self, x_app_user_id):
        r"""Sets the x_app_user_id of this PreviewDocumentSegmentRequest.

        第三方用户ID。不允许输入中文。

        :param x_app_user_id: The x_app_user_id of this PreviewDocumentSegmentRequest.
        :type x_app_user_id: str
        """
        self._x_app_user_id = x_app_user_id

    @property
    def document_id(self):
        r"""Gets the document_id of this PreviewDocumentSegmentRequest.

        文档ID。

        :return: The document_id of this PreviewDocumentSegmentRequest.
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        r"""Sets the document_id of this PreviewDocumentSegmentRequest.

        文档ID。

        :param document_id: The document_id of this PreviewDocumentSegmentRequest.
        :type document_id: str
        """
        self._document_id = document_id

    @property
    def preview_lines(self):
        r"""Gets the preview_lines of this PreviewDocumentSegmentRequest.

        预览行数。

        :return: The preview_lines of this PreviewDocumentSegmentRequest.
        :rtype: int
        """
        return self._preview_lines

    @preview_lines.setter
    def preview_lines(self, preview_lines):
        r"""Sets the preview_lines of this PreviewDocumentSegmentRequest.

        预览行数。

        :param preview_lines: The preview_lines of this PreviewDocumentSegmentRequest.
        :type preview_lines: int
        """
        self._preview_lines = preview_lines

    @property
    def body(self):
        r"""Gets the body of this PreviewDocumentSegmentRequest.

        :return: The body of this PreviewDocumentSegmentRequest.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.DocumentSegmentParam`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this PreviewDocumentSegmentRequest.

        :param body: The body of this PreviewDocumentSegmentRequest.
        :type body: :class:`huaweicloudsdkmetastudio.v1.DocumentSegmentParam`
        """
        self._body = body

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
        if not isinstance(other, PreviewDocumentSegmentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
