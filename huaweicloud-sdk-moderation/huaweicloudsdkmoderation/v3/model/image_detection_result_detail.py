# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageDetectionResultDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'suggestion': 'str',
        'category': 'str',
        'confidence': 'float',
        'face_location': 'FaceLocationDetail',
        'qr_location': 'QRLocationDetail',
        'qr_content': 'str',
        'segments': 'list[OCRTextDetail]',
        'label': 'str'
    }

    attribute_map = {
        'suggestion': 'suggestion',
        'category': 'category',
        'confidence': 'confidence',
        'face_location': 'face_location',
        'qr_location': 'qr_location',
        'qr_content': 'qr_content',
        'segments': 'segments',
        'label': 'label'
    }

    def __init__(self, suggestion=None, category=None, confidence=None, face_location=None, qr_location=None, qr_content=None, segments=None, label=None):
        """ImageDetectionResultDetail

        The model defined in huaweicloud sdk

        :param suggestion: 审核结果是否通过。 block：包含敏感信息，不通过 review：需要人工复检
        :type suggestion: str
        :param category: 检测结果的一级标签。 支持category列表如下： terrorism: 暴恐 porn: 色情 image_text: 图文审核
        :type category: str
        :param confidence: 置信度，可选值在0-1之间，值越大，可信度越高。
        :type confidence: float
        :param face_location: 
        :type face_location: :class:`huaweicloudsdkmoderation.v3.FaceLocationDetail`
        :param qr_location: 
        :type qr_location: :class:`huaweicloudsdkmoderation.v3.QRLocationDetail`
        :param qr_content: 图片中二维码指向的链接，当请求参数categories中包含image_text时存在。
        :type qr_content: str
        :param segments: image_text场景下命中的文本片段。
        :type segments: list[:class:`huaweicloudsdkmoderation.v3.OCRTextDetail`]
        :param label: 识别的详细标签。
        :type label: str
        """
        
        

        self._suggestion = None
        self._category = None
        self._confidence = None
        self._face_location = None
        self._qr_location = None
        self._qr_content = None
        self._segments = None
        self._label = None
        self.discriminator = None

        self.suggestion = suggestion
        self.category = category
        self.confidence = confidence
        if face_location is not None:
            self.face_location = face_location
        if qr_location is not None:
            self.qr_location = qr_location
        if qr_content is not None:
            self.qr_content = qr_content
        if segments is not None:
            self.segments = segments
        if label is not None:
            self.label = label

    @property
    def suggestion(self):
        """Gets the suggestion of this ImageDetectionResultDetail.

        审核结果是否通过。 block：包含敏感信息，不通过 review：需要人工复检

        :return: The suggestion of this ImageDetectionResultDetail.
        :rtype: str
        """
        return self._suggestion

    @suggestion.setter
    def suggestion(self, suggestion):
        """Sets the suggestion of this ImageDetectionResultDetail.

        审核结果是否通过。 block：包含敏感信息，不通过 review：需要人工复检

        :param suggestion: The suggestion of this ImageDetectionResultDetail.
        :type suggestion: str
        """
        self._suggestion = suggestion

    @property
    def category(self):
        """Gets the category of this ImageDetectionResultDetail.

        检测结果的一级标签。 支持category列表如下： terrorism: 暴恐 porn: 色情 image_text: 图文审核

        :return: The category of this ImageDetectionResultDetail.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this ImageDetectionResultDetail.

        检测结果的一级标签。 支持category列表如下： terrorism: 暴恐 porn: 色情 image_text: 图文审核

        :param category: The category of this ImageDetectionResultDetail.
        :type category: str
        """
        self._category = category

    @property
    def confidence(self):
        """Gets the confidence of this ImageDetectionResultDetail.

        置信度，可选值在0-1之间，值越大，可信度越高。

        :return: The confidence of this ImageDetectionResultDetail.
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this ImageDetectionResultDetail.

        置信度，可选值在0-1之间，值越大，可信度越高。

        :param confidence: The confidence of this ImageDetectionResultDetail.
        :type confidence: float
        """
        self._confidence = confidence

    @property
    def face_location(self):
        """Gets the face_location of this ImageDetectionResultDetail.

        :return: The face_location of this ImageDetectionResultDetail.
        :rtype: :class:`huaweicloudsdkmoderation.v3.FaceLocationDetail`
        """
        return self._face_location

    @face_location.setter
    def face_location(self, face_location):
        """Sets the face_location of this ImageDetectionResultDetail.

        :param face_location: The face_location of this ImageDetectionResultDetail.
        :type face_location: :class:`huaweicloudsdkmoderation.v3.FaceLocationDetail`
        """
        self._face_location = face_location

    @property
    def qr_location(self):
        """Gets the qr_location of this ImageDetectionResultDetail.

        :return: The qr_location of this ImageDetectionResultDetail.
        :rtype: :class:`huaweicloudsdkmoderation.v3.QRLocationDetail`
        """
        return self._qr_location

    @qr_location.setter
    def qr_location(self, qr_location):
        """Sets the qr_location of this ImageDetectionResultDetail.

        :param qr_location: The qr_location of this ImageDetectionResultDetail.
        :type qr_location: :class:`huaweicloudsdkmoderation.v3.QRLocationDetail`
        """
        self._qr_location = qr_location

    @property
    def qr_content(self):
        """Gets the qr_content of this ImageDetectionResultDetail.

        图片中二维码指向的链接，当请求参数categories中包含image_text时存在。

        :return: The qr_content of this ImageDetectionResultDetail.
        :rtype: str
        """
        return self._qr_content

    @qr_content.setter
    def qr_content(self, qr_content):
        """Sets the qr_content of this ImageDetectionResultDetail.

        图片中二维码指向的链接，当请求参数categories中包含image_text时存在。

        :param qr_content: The qr_content of this ImageDetectionResultDetail.
        :type qr_content: str
        """
        self._qr_content = qr_content

    @property
    def segments(self):
        """Gets the segments of this ImageDetectionResultDetail.

        image_text场景下命中的文本片段。

        :return: The segments of this ImageDetectionResultDetail.
        :rtype: list[:class:`huaweicloudsdkmoderation.v3.OCRTextDetail`]
        """
        return self._segments

    @segments.setter
    def segments(self, segments):
        """Sets the segments of this ImageDetectionResultDetail.

        image_text场景下命中的文本片段。

        :param segments: The segments of this ImageDetectionResultDetail.
        :type segments: list[:class:`huaweicloudsdkmoderation.v3.OCRTextDetail`]
        """
        self._segments = segments

    @property
    def label(self):
        """Gets the label of this ImageDetectionResultDetail.

        识别的详细标签。

        :return: The label of this ImageDetectionResultDetail.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this ImageDetectionResultDetail.

        识别的详细标签。

        :param label: The label of this ImageDetectionResultDetail.
        :type label: str
        """
        self._label = label

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
        if not isinstance(other, ImageDetectionResultDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
