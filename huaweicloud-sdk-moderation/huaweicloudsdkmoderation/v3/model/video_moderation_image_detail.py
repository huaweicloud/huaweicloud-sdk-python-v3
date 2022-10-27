# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VideoModerationImageDetail:

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
        'ocr_text': 'str',
        'time': 'float',
        'detail': 'list[VideoModerationImageDetailList]'
    }

    attribute_map = {
        'suggestion': 'suggestion',
        'category': 'category',
        'ocr_text': 'ocr_text',
        'time': 'time',
        'detail': 'detail'
    }

    def __init__(self, suggestion=None, category=None, ocr_text=None, time=None, detail=None):
        """VideoModerationImageDetail

        The model defined in huaweicloud sdk

        :param suggestion: 图像审核结果是否通过。 block：包含敏感信息，不通过  review：需要人工复检
        :type suggestion: str
        :param category: 检测结果的一级标签。 支持category列表如下： politics: 涉政  terrorism: 暴恐  porn: 色情  image_text: 图文审核
        :type category: str
        :param ocr_text: 图文审核检测出的文本，只有在category参数配置image_text且检测出文本时展示该字段。
        :type ocr_text: str
        :param time: 截帧在视频文件中的时间，单位为秒
        :type time: float
        :param detail: 图像帧审核详情
        :type detail: list[:class:`huaweicloudsdkmoderation.v3.VideoModerationImageDetailList`]
        """
        
        

        self._suggestion = None
        self._category = None
        self._ocr_text = None
        self._time = None
        self._detail = None
        self.discriminator = None

        if suggestion is not None:
            self.suggestion = suggestion
        if category is not None:
            self.category = category
        if ocr_text is not None:
            self.ocr_text = ocr_text
        if time is not None:
            self.time = time
        if detail is not None:
            self.detail = detail

    @property
    def suggestion(self):
        """Gets the suggestion of this VideoModerationImageDetail.

        图像审核结果是否通过。 block：包含敏感信息，不通过  review：需要人工复检

        :return: The suggestion of this VideoModerationImageDetail.
        :rtype: str
        """
        return self._suggestion

    @suggestion.setter
    def suggestion(self, suggestion):
        """Sets the suggestion of this VideoModerationImageDetail.

        图像审核结果是否通过。 block：包含敏感信息，不通过  review：需要人工复检

        :param suggestion: The suggestion of this VideoModerationImageDetail.
        :type suggestion: str
        """
        self._suggestion = suggestion

    @property
    def category(self):
        """Gets the category of this VideoModerationImageDetail.

        检测结果的一级标签。 支持category列表如下： politics: 涉政  terrorism: 暴恐  porn: 色情  image_text: 图文审核

        :return: The category of this VideoModerationImageDetail.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this VideoModerationImageDetail.

        检测结果的一级标签。 支持category列表如下： politics: 涉政  terrorism: 暴恐  porn: 色情  image_text: 图文审核

        :param category: The category of this VideoModerationImageDetail.
        :type category: str
        """
        self._category = category

    @property
    def ocr_text(self):
        """Gets the ocr_text of this VideoModerationImageDetail.

        图文审核检测出的文本，只有在category参数配置image_text且检测出文本时展示该字段。

        :return: The ocr_text of this VideoModerationImageDetail.
        :rtype: str
        """
        return self._ocr_text

    @ocr_text.setter
    def ocr_text(self, ocr_text):
        """Sets the ocr_text of this VideoModerationImageDetail.

        图文审核检测出的文本，只有在category参数配置image_text且检测出文本时展示该字段。

        :param ocr_text: The ocr_text of this VideoModerationImageDetail.
        :type ocr_text: str
        """
        self._ocr_text = ocr_text

    @property
    def time(self):
        """Gets the time of this VideoModerationImageDetail.

        截帧在视频文件中的时间，单位为秒

        :return: The time of this VideoModerationImageDetail.
        :rtype: float
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this VideoModerationImageDetail.

        截帧在视频文件中的时间，单位为秒

        :param time: The time of this VideoModerationImageDetail.
        :type time: float
        """
        self._time = time

    @property
    def detail(self):
        """Gets the detail of this VideoModerationImageDetail.

        图像帧审核详情

        :return: The detail of this VideoModerationImageDetail.
        :rtype: list[:class:`huaweicloudsdkmoderation.v3.VideoModerationImageDetailList`]
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this VideoModerationImageDetail.

        图像帧审核详情

        :param detail: The detail of this VideoModerationImageDetail.
        :type detail: list[:class:`huaweicloudsdkmoderation.v3.VideoModerationImageDetailList`]
        """
        self._detail = detail

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
        if not isinstance(other, VideoModerationImageDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
