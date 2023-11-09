# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DocumentQueryResponseResultDetails:

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
        'type': 'str',
        'label': 'str',
        'index': 'int',
        'text': 'str',
        'segments': 'list[DocumentQueryResponseResultSegments]',
        'video_image_details': 'list[DocumentVideoImageDetail]',
        'audio_details': 'list[DocumentAudioDetail]'
    }

    attribute_map = {
        'suggestion': 'suggestion',
        'type': 'type',
        'label': 'label',
        'index': 'index',
        'text': 'text',
        'segments': 'segments',
        'video_image_details': 'video_image_details',
        'audio_details': 'audio_details'
    }

    def __init__(self, suggestion=None, type=None, label=None, index=None, text=None, segments=None, video_image_details=None, audio_details=None):
        """DocumentQueryResponseResultDetails

        The model defined in huaweicloud sdk

        :param suggestion: 当前内容片段的处置建议： block：包含敏感信息，不通过 review：需要人工复检
        :type suggestion: str
        :param type: 当前内容片段的类型，可取值有： text: 文本 image: 图像 video: 视频
        :type type: str
        :param label: 当前内容片段的风险类型： politics：涉政 terrorism：暴恐 porn：色情 sexy：性感 abuse：辱骂 ad：广告 qr_code：二维码 watermark：水印 meaningless：无意义 ban：违禁 bad_scene：不良场景 moan：娇喘
        :type label: str
        :param index: 当前处理的片段索引
        :type index: int
        :param text: 当前内容片段中的文本内容
        :type text: str
        :param segments: 命中的风险片段信息列表，仅在有命中敏感词时才返回
        :type segments: list[:class:`huaweicloudsdkmoderation.v3.DocumentQueryResponseResultSegments`]
        :param video_image_details: 网页视频中截帧部分审核详情
        :type video_image_details: list[:class:`huaweicloudsdkmoderation.v3.DocumentVideoImageDetail`]
        :param audio_details: 网页视频中音频部分审核详情
        :type audio_details: list[:class:`huaweicloudsdkmoderation.v3.DocumentAudioDetail`]
        """
        
        

        self._suggestion = None
        self._type = None
        self._label = None
        self._index = None
        self._text = None
        self._segments = None
        self._video_image_details = None
        self._audio_details = None
        self.discriminator = None

        if suggestion is not None:
            self.suggestion = suggestion
        if type is not None:
            self.type = type
        if label is not None:
            self.label = label
        if index is not None:
            self.index = index
        if text is not None:
            self.text = text
        if segments is not None:
            self.segments = segments
        if video_image_details is not None:
            self.video_image_details = video_image_details
        if audio_details is not None:
            self.audio_details = audio_details

    @property
    def suggestion(self):
        """Gets the suggestion of this DocumentQueryResponseResultDetails.

        当前内容片段的处置建议： block：包含敏感信息，不通过 review：需要人工复检

        :return: The suggestion of this DocumentQueryResponseResultDetails.
        :rtype: str
        """
        return self._suggestion

    @suggestion.setter
    def suggestion(self, suggestion):
        """Sets the suggestion of this DocumentQueryResponseResultDetails.

        当前内容片段的处置建议： block：包含敏感信息，不通过 review：需要人工复检

        :param suggestion: The suggestion of this DocumentQueryResponseResultDetails.
        :type suggestion: str
        """
        self._suggestion = suggestion

    @property
    def type(self):
        """Gets the type of this DocumentQueryResponseResultDetails.

        当前内容片段的类型，可取值有： text: 文本 image: 图像 video: 视频

        :return: The type of this DocumentQueryResponseResultDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DocumentQueryResponseResultDetails.

        当前内容片段的类型，可取值有： text: 文本 image: 图像 video: 视频

        :param type: The type of this DocumentQueryResponseResultDetails.
        :type type: str
        """
        self._type = type

    @property
    def label(self):
        """Gets the label of this DocumentQueryResponseResultDetails.

        当前内容片段的风险类型： politics：涉政 terrorism：暴恐 porn：色情 sexy：性感 abuse：辱骂 ad：广告 qr_code：二维码 watermark：水印 meaningless：无意义 ban：违禁 bad_scene：不良场景 moan：娇喘

        :return: The label of this DocumentQueryResponseResultDetails.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this DocumentQueryResponseResultDetails.

        当前内容片段的风险类型： politics：涉政 terrorism：暴恐 porn：色情 sexy：性感 abuse：辱骂 ad：广告 qr_code：二维码 watermark：水印 meaningless：无意义 ban：违禁 bad_scene：不良场景 moan：娇喘

        :param label: The label of this DocumentQueryResponseResultDetails.
        :type label: str
        """
        self._label = label

    @property
    def index(self):
        """Gets the index of this DocumentQueryResponseResultDetails.

        当前处理的片段索引

        :return: The index of this DocumentQueryResponseResultDetails.
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this DocumentQueryResponseResultDetails.

        当前处理的片段索引

        :param index: The index of this DocumentQueryResponseResultDetails.
        :type index: int
        """
        self._index = index

    @property
    def text(self):
        """Gets the text of this DocumentQueryResponseResultDetails.

        当前内容片段中的文本内容

        :return: The text of this DocumentQueryResponseResultDetails.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this DocumentQueryResponseResultDetails.

        当前内容片段中的文本内容

        :param text: The text of this DocumentQueryResponseResultDetails.
        :type text: str
        """
        self._text = text

    @property
    def segments(self):
        """Gets the segments of this DocumentQueryResponseResultDetails.

        命中的风险片段信息列表，仅在有命中敏感词时才返回

        :return: The segments of this DocumentQueryResponseResultDetails.
        :rtype: list[:class:`huaweicloudsdkmoderation.v3.DocumentQueryResponseResultSegments`]
        """
        return self._segments

    @segments.setter
    def segments(self, segments):
        """Sets the segments of this DocumentQueryResponseResultDetails.

        命中的风险片段信息列表，仅在有命中敏感词时才返回

        :param segments: The segments of this DocumentQueryResponseResultDetails.
        :type segments: list[:class:`huaweicloudsdkmoderation.v3.DocumentQueryResponseResultSegments`]
        """
        self._segments = segments

    @property
    def video_image_details(self):
        """Gets the video_image_details of this DocumentQueryResponseResultDetails.

        网页视频中截帧部分审核详情

        :return: The video_image_details of this DocumentQueryResponseResultDetails.
        :rtype: list[:class:`huaweicloudsdkmoderation.v3.DocumentVideoImageDetail`]
        """
        return self._video_image_details

    @video_image_details.setter
    def video_image_details(self, video_image_details):
        """Sets the video_image_details of this DocumentQueryResponseResultDetails.

        网页视频中截帧部分审核详情

        :param video_image_details: The video_image_details of this DocumentQueryResponseResultDetails.
        :type video_image_details: list[:class:`huaweicloudsdkmoderation.v3.DocumentVideoImageDetail`]
        """
        self._video_image_details = video_image_details

    @property
    def audio_details(self):
        """Gets the audio_details of this DocumentQueryResponseResultDetails.

        网页视频中音频部分审核详情

        :return: The audio_details of this DocumentQueryResponseResultDetails.
        :rtype: list[:class:`huaweicloudsdkmoderation.v3.DocumentAudioDetail`]
        """
        return self._audio_details

    @audio_details.setter
    def audio_details(self, audio_details):
        """Sets the audio_details of this DocumentQueryResponseResultDetails.

        网页视频中音频部分审核详情

        :param audio_details: The audio_details of this DocumentQueryResponseResultDetails.
        :type audio_details: list[:class:`huaweicloudsdkmoderation.v3.DocumentAudioDetail`]
        """
        self._audio_details = audio_details

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
        if not isinstance(other, DocumentQueryResponseResultDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
