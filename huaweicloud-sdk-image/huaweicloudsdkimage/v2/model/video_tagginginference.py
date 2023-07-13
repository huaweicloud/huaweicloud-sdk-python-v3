# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VideoTagginginference:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'video_title': 'str',
        'language': 'str',
        'use_celebrity': 'str',
        'use_landmark': 'str',
        'use_logo': 'str',
        'use_ocr': 'str',
        'use_sis': 'str',
        'use_tagging': 'str'
    }

    attribute_map = {
        'video_title': 'video_title',
        'language': 'language',
        'use_celebrity': 'use_celebrity',
        'use_landmark': 'use_landmark',
        'use_logo': 'use_logo',
        'use_ocr': 'use_ocr',
        'use_sis': 'use_sis',
        'use_tagging': 'use_tagging'
    }

    def __init__(self, video_title=None, language=None, use_celebrity=None, use_landmark=None, use_logo=None, use_ocr=None, use_sis=None, use_tagging=None):
        """VideoTagginginference

        The model defined in huaweicloud sdk

        :param video_title: 视频标题
        :type video_title: str
        :param language: 标签语种
        :type language: str
        :param use_celebrity: 名人识别使用开关
        :type use_celebrity: str
        :param use_landmark: 地标识别使用开关
        :type use_landmark: str
        :param use_logo: LOGO识别使用开关
        :type use_logo: str
        :param use_ocr: OCR识别使用开关
        :type use_ocr: str
        :param use_sis: 视频语音识别开关
        :type use_sis: str
        :param use_tagging: 图像标签识别开关
        :type use_tagging: str
        """
        
        

        self._video_title = None
        self._language = None
        self._use_celebrity = None
        self._use_landmark = None
        self._use_logo = None
        self._use_ocr = None
        self._use_sis = None
        self._use_tagging = None
        self.discriminator = None

        if video_title is not None:
            self.video_title = video_title
        if language is not None:
            self.language = language
        if use_celebrity is not None:
            self.use_celebrity = use_celebrity
        if use_landmark is not None:
            self.use_landmark = use_landmark
        if use_logo is not None:
            self.use_logo = use_logo
        if use_ocr is not None:
            self.use_ocr = use_ocr
        if use_sis is not None:
            self.use_sis = use_sis
        if use_tagging is not None:
            self.use_tagging = use_tagging

    @property
    def video_title(self):
        """Gets the video_title of this VideoTagginginference.

        视频标题

        :return: The video_title of this VideoTagginginference.
        :rtype: str
        """
        return self._video_title

    @video_title.setter
    def video_title(self, video_title):
        """Sets the video_title of this VideoTagginginference.

        视频标题

        :param video_title: The video_title of this VideoTagginginference.
        :type video_title: str
        """
        self._video_title = video_title

    @property
    def language(self):
        """Gets the language of this VideoTagginginference.

        标签语种

        :return: The language of this VideoTagginginference.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this VideoTagginginference.

        标签语种

        :param language: The language of this VideoTagginginference.
        :type language: str
        """
        self._language = language

    @property
    def use_celebrity(self):
        """Gets the use_celebrity of this VideoTagginginference.

        名人识别使用开关

        :return: The use_celebrity of this VideoTagginginference.
        :rtype: str
        """
        return self._use_celebrity

    @use_celebrity.setter
    def use_celebrity(self, use_celebrity):
        """Sets the use_celebrity of this VideoTagginginference.

        名人识别使用开关

        :param use_celebrity: The use_celebrity of this VideoTagginginference.
        :type use_celebrity: str
        """
        self._use_celebrity = use_celebrity

    @property
    def use_landmark(self):
        """Gets the use_landmark of this VideoTagginginference.

        地标识别使用开关

        :return: The use_landmark of this VideoTagginginference.
        :rtype: str
        """
        return self._use_landmark

    @use_landmark.setter
    def use_landmark(self, use_landmark):
        """Sets the use_landmark of this VideoTagginginference.

        地标识别使用开关

        :param use_landmark: The use_landmark of this VideoTagginginference.
        :type use_landmark: str
        """
        self._use_landmark = use_landmark

    @property
    def use_logo(self):
        """Gets the use_logo of this VideoTagginginference.

        LOGO识别使用开关

        :return: The use_logo of this VideoTagginginference.
        :rtype: str
        """
        return self._use_logo

    @use_logo.setter
    def use_logo(self, use_logo):
        """Sets the use_logo of this VideoTagginginference.

        LOGO识别使用开关

        :param use_logo: The use_logo of this VideoTagginginference.
        :type use_logo: str
        """
        self._use_logo = use_logo

    @property
    def use_ocr(self):
        """Gets the use_ocr of this VideoTagginginference.

        OCR识别使用开关

        :return: The use_ocr of this VideoTagginginference.
        :rtype: str
        """
        return self._use_ocr

    @use_ocr.setter
    def use_ocr(self, use_ocr):
        """Sets the use_ocr of this VideoTagginginference.

        OCR识别使用开关

        :param use_ocr: The use_ocr of this VideoTagginginference.
        :type use_ocr: str
        """
        self._use_ocr = use_ocr

    @property
    def use_sis(self):
        """Gets the use_sis of this VideoTagginginference.

        视频语音识别开关

        :return: The use_sis of this VideoTagginginference.
        :rtype: str
        """
        return self._use_sis

    @use_sis.setter
    def use_sis(self, use_sis):
        """Sets the use_sis of this VideoTagginginference.

        视频语音识别开关

        :param use_sis: The use_sis of this VideoTagginginference.
        :type use_sis: str
        """
        self._use_sis = use_sis

    @property
    def use_tagging(self):
        """Gets the use_tagging of this VideoTagginginference.

        图像标签识别开关

        :return: The use_tagging of this VideoTagginginference.
        :rtype: str
        """
        return self._use_tagging

    @use_tagging.setter
    def use_tagging(self, use_tagging):
        """Sets the use_tagging of this VideoTagginginference.

        图像标签识别开关

        :param use_tagging: The use_tagging of this VideoTagginginference.
        :type use_tagging: str
        """
        self._use_tagging = use_tagging

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
        if not isinstance(other, VideoTagginginference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
