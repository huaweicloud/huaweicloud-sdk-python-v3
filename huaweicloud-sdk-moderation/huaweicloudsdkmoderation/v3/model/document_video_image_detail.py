# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DocumentVideoImageDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'time': 'float',
        'suggestion': 'str',
        'ocr_text': 'str',
        'label': 'str',
        'segments': 'list[DocumentVideoImageDetailSegments]'
    }

    attribute_map = {
        'time': 'time',
        'suggestion': 'suggestion',
        'ocr_text': 'ocr_text',
        'label': 'label',
        'segments': 'segments'
    }

    def __init__(self, time=None, suggestion=None, ocr_text=None, label=None, segments=None):
        """DocumentVideoImageDetail

        The model defined in huaweicloud sdk

        :param time: 截帧在视频文件中的时间，单位为秒
        :type time: float
        :param suggestion: 截帧审核结果是否通过。 block：包含敏感信息，不通过 review：需要人工复检
        :type suggestion: str
        :param ocr_text: 截帧检测出的文本
        :type ocr_text: str
        :param label: 识别的详细标签
        :type label: str
        :param segments: 命中的文本风险片段列表
        :type segments: list[:class:`huaweicloudsdkmoderation.v3.DocumentVideoImageDetailSegments`]
        """
        
        

        self._time = None
        self._suggestion = None
        self._ocr_text = None
        self._label = None
        self._segments = None
        self.discriminator = None

        if time is not None:
            self.time = time
        if suggestion is not None:
            self.suggestion = suggestion
        if ocr_text is not None:
            self.ocr_text = ocr_text
        if label is not None:
            self.label = label
        if segments is not None:
            self.segments = segments

    @property
    def time(self):
        """Gets the time of this DocumentVideoImageDetail.

        截帧在视频文件中的时间，单位为秒

        :return: The time of this DocumentVideoImageDetail.
        :rtype: float
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this DocumentVideoImageDetail.

        截帧在视频文件中的时间，单位为秒

        :param time: The time of this DocumentVideoImageDetail.
        :type time: float
        """
        self._time = time

    @property
    def suggestion(self):
        """Gets the suggestion of this DocumentVideoImageDetail.

        截帧审核结果是否通过。 block：包含敏感信息，不通过 review：需要人工复检

        :return: The suggestion of this DocumentVideoImageDetail.
        :rtype: str
        """
        return self._suggestion

    @suggestion.setter
    def suggestion(self, suggestion):
        """Sets the suggestion of this DocumentVideoImageDetail.

        截帧审核结果是否通过。 block：包含敏感信息，不通过 review：需要人工复检

        :param suggestion: The suggestion of this DocumentVideoImageDetail.
        :type suggestion: str
        """
        self._suggestion = suggestion

    @property
    def ocr_text(self):
        """Gets the ocr_text of this DocumentVideoImageDetail.

        截帧检测出的文本

        :return: The ocr_text of this DocumentVideoImageDetail.
        :rtype: str
        """
        return self._ocr_text

    @ocr_text.setter
    def ocr_text(self, ocr_text):
        """Sets the ocr_text of this DocumentVideoImageDetail.

        截帧检测出的文本

        :param ocr_text: The ocr_text of this DocumentVideoImageDetail.
        :type ocr_text: str
        """
        self._ocr_text = ocr_text

    @property
    def label(self):
        """Gets the label of this DocumentVideoImageDetail.

        识别的详细标签

        :return: The label of this DocumentVideoImageDetail.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this DocumentVideoImageDetail.

        识别的详细标签

        :param label: The label of this DocumentVideoImageDetail.
        :type label: str
        """
        self._label = label

    @property
    def segments(self):
        """Gets the segments of this DocumentVideoImageDetail.

        命中的文本风险片段列表

        :return: The segments of this DocumentVideoImageDetail.
        :rtype: list[:class:`huaweicloudsdkmoderation.v3.DocumentVideoImageDetailSegments`]
        """
        return self._segments

    @segments.setter
    def segments(self, segments):
        """Sets the segments of this DocumentVideoImageDetail.

        命中的文本风险片段列表

        :param segments: The segments of this DocumentVideoImageDetail.
        :type segments: list[:class:`huaweicloudsdkmoderation.v3.DocumentVideoImageDetailSegments`]
        """
        self._segments = segments

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
        if not isinstance(other, DocumentVideoImageDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
