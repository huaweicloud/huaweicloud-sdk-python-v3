# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListUserQuotaDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'modeling_count_2d_model': 'int',
        'modeling_count_2d_model_flexus': 'int',
        'video_time_2d_model': 'float',
        'video_time_flexus_2d_model': 'float',
        'voice_clone_basic': 'int',
        'voice_clone_middle': 'int',
        'voice_clone_advance': 'int',
        'voice_clone_flexus': 'int'
    }

    attribute_map = {
        'modeling_count_2d_model': 'modeling_count_2d_model',
        'modeling_count_2d_model_flexus': 'modeling_count_2d_model_flexus',
        'video_time_2d_model': 'video_time_2d_model',
        'video_time_flexus_2d_model': 'video_time_flexus_2d_model',
        'voice_clone_basic': 'voice_clone_basic',
        'voice_clone_middle': 'voice_clone_middle',
        'voice_clone_advance': 'voice_clone_advance',
        'voice_clone_flexus': 'voice_clone_flexus'
    }

    def __init__(self, modeling_count_2d_model=None, modeling_count_2d_model_flexus=None, video_time_2d_model=None, video_time_flexus_2d_model=None, voice_clone_basic=None, voice_clone_middle=None, voice_clone_advance=None, voice_clone_flexus=None):
        r"""ListUserQuotaDetail

        The model defined in huaweicloud sdk

        :param modeling_count_2d_model: 分身数字人训练模型数量。-1表示无限制。
        :type modeling_count_2d_model: int
        :param modeling_count_2d_model_flexus: 分身数字人flexus版训练模型数量。-1表示无限制。
        :type modeling_count_2d_model_flexus: int
        :param video_time_2d_model: 分身数字人视频制作内容时间，单位分钟。-1表示无限制。
        :type video_time_2d_model: float
        :param video_time_flexus_2d_model: 分身数字人视频制作flexus版内容时间，单位分钟。-1表示无限制。
        :type video_time_flexus_2d_model: float
        :param voice_clone_basic: 声音克隆基础版。-1表示无限制。
        :type voice_clone_basic: int
        :param voice_clone_middle: 声音克隆进阶版。-1表示无限制。
        :type voice_clone_middle: int
        :param voice_clone_advance: 声音克隆高级版。-1表示无限制。
        :type voice_clone_advance: int
        :param voice_clone_flexus: 声音克隆flexus版。-1表示无限制。
        :type voice_clone_flexus: int
        """
        
        

        self._modeling_count_2d_model = None
        self._modeling_count_2d_model_flexus = None
        self._video_time_2d_model = None
        self._video_time_flexus_2d_model = None
        self._voice_clone_basic = None
        self._voice_clone_middle = None
        self._voice_clone_advance = None
        self._voice_clone_flexus = None
        self.discriminator = None

        if modeling_count_2d_model is not None:
            self.modeling_count_2d_model = modeling_count_2d_model
        if modeling_count_2d_model_flexus is not None:
            self.modeling_count_2d_model_flexus = modeling_count_2d_model_flexus
        if video_time_2d_model is not None:
            self.video_time_2d_model = video_time_2d_model
        if video_time_flexus_2d_model is not None:
            self.video_time_flexus_2d_model = video_time_flexus_2d_model
        if voice_clone_basic is not None:
            self.voice_clone_basic = voice_clone_basic
        if voice_clone_middle is not None:
            self.voice_clone_middle = voice_clone_middle
        if voice_clone_advance is not None:
            self.voice_clone_advance = voice_clone_advance
        if voice_clone_flexus is not None:
            self.voice_clone_flexus = voice_clone_flexus

    @property
    def modeling_count_2d_model(self):
        r"""Gets the modeling_count_2d_model of this ListUserQuotaDetail.

        分身数字人训练模型数量。-1表示无限制。

        :return: The modeling_count_2d_model of this ListUserQuotaDetail.
        :rtype: int
        """
        return self._modeling_count_2d_model

    @modeling_count_2d_model.setter
    def modeling_count_2d_model(self, modeling_count_2d_model):
        r"""Sets the modeling_count_2d_model of this ListUserQuotaDetail.

        分身数字人训练模型数量。-1表示无限制。

        :param modeling_count_2d_model: The modeling_count_2d_model of this ListUserQuotaDetail.
        :type modeling_count_2d_model: int
        """
        self._modeling_count_2d_model = modeling_count_2d_model

    @property
    def modeling_count_2d_model_flexus(self):
        r"""Gets the modeling_count_2d_model_flexus of this ListUserQuotaDetail.

        分身数字人flexus版训练模型数量。-1表示无限制。

        :return: The modeling_count_2d_model_flexus of this ListUserQuotaDetail.
        :rtype: int
        """
        return self._modeling_count_2d_model_flexus

    @modeling_count_2d_model_flexus.setter
    def modeling_count_2d_model_flexus(self, modeling_count_2d_model_flexus):
        r"""Sets the modeling_count_2d_model_flexus of this ListUserQuotaDetail.

        分身数字人flexus版训练模型数量。-1表示无限制。

        :param modeling_count_2d_model_flexus: The modeling_count_2d_model_flexus of this ListUserQuotaDetail.
        :type modeling_count_2d_model_flexus: int
        """
        self._modeling_count_2d_model_flexus = modeling_count_2d_model_flexus

    @property
    def video_time_2d_model(self):
        r"""Gets the video_time_2d_model of this ListUserQuotaDetail.

        分身数字人视频制作内容时间，单位分钟。-1表示无限制。

        :return: The video_time_2d_model of this ListUserQuotaDetail.
        :rtype: float
        """
        return self._video_time_2d_model

    @video_time_2d_model.setter
    def video_time_2d_model(self, video_time_2d_model):
        r"""Sets the video_time_2d_model of this ListUserQuotaDetail.

        分身数字人视频制作内容时间，单位分钟。-1表示无限制。

        :param video_time_2d_model: The video_time_2d_model of this ListUserQuotaDetail.
        :type video_time_2d_model: float
        """
        self._video_time_2d_model = video_time_2d_model

    @property
    def video_time_flexus_2d_model(self):
        r"""Gets the video_time_flexus_2d_model of this ListUserQuotaDetail.

        分身数字人视频制作flexus版内容时间，单位分钟。-1表示无限制。

        :return: The video_time_flexus_2d_model of this ListUserQuotaDetail.
        :rtype: float
        """
        return self._video_time_flexus_2d_model

    @video_time_flexus_2d_model.setter
    def video_time_flexus_2d_model(self, video_time_flexus_2d_model):
        r"""Sets the video_time_flexus_2d_model of this ListUserQuotaDetail.

        分身数字人视频制作flexus版内容时间，单位分钟。-1表示无限制。

        :param video_time_flexus_2d_model: The video_time_flexus_2d_model of this ListUserQuotaDetail.
        :type video_time_flexus_2d_model: float
        """
        self._video_time_flexus_2d_model = video_time_flexus_2d_model

    @property
    def voice_clone_basic(self):
        r"""Gets the voice_clone_basic of this ListUserQuotaDetail.

        声音克隆基础版。-1表示无限制。

        :return: The voice_clone_basic of this ListUserQuotaDetail.
        :rtype: int
        """
        return self._voice_clone_basic

    @voice_clone_basic.setter
    def voice_clone_basic(self, voice_clone_basic):
        r"""Sets the voice_clone_basic of this ListUserQuotaDetail.

        声音克隆基础版。-1表示无限制。

        :param voice_clone_basic: The voice_clone_basic of this ListUserQuotaDetail.
        :type voice_clone_basic: int
        """
        self._voice_clone_basic = voice_clone_basic

    @property
    def voice_clone_middle(self):
        r"""Gets the voice_clone_middle of this ListUserQuotaDetail.

        声音克隆进阶版。-1表示无限制。

        :return: The voice_clone_middle of this ListUserQuotaDetail.
        :rtype: int
        """
        return self._voice_clone_middle

    @voice_clone_middle.setter
    def voice_clone_middle(self, voice_clone_middle):
        r"""Sets the voice_clone_middle of this ListUserQuotaDetail.

        声音克隆进阶版。-1表示无限制。

        :param voice_clone_middle: The voice_clone_middle of this ListUserQuotaDetail.
        :type voice_clone_middle: int
        """
        self._voice_clone_middle = voice_clone_middle

    @property
    def voice_clone_advance(self):
        r"""Gets the voice_clone_advance of this ListUserQuotaDetail.

        声音克隆高级版。-1表示无限制。

        :return: The voice_clone_advance of this ListUserQuotaDetail.
        :rtype: int
        """
        return self._voice_clone_advance

    @voice_clone_advance.setter
    def voice_clone_advance(self, voice_clone_advance):
        r"""Sets the voice_clone_advance of this ListUserQuotaDetail.

        声音克隆高级版。-1表示无限制。

        :param voice_clone_advance: The voice_clone_advance of this ListUserQuotaDetail.
        :type voice_clone_advance: int
        """
        self._voice_clone_advance = voice_clone_advance

    @property
    def voice_clone_flexus(self):
        r"""Gets the voice_clone_flexus of this ListUserQuotaDetail.

        声音克隆flexus版。-1表示无限制。

        :return: The voice_clone_flexus of this ListUserQuotaDetail.
        :rtype: int
        """
        return self._voice_clone_flexus

    @voice_clone_flexus.setter
    def voice_clone_flexus(self, voice_clone_flexus):
        r"""Sets the voice_clone_flexus of this ListUserQuotaDetail.

        声音克隆flexus版。-1表示无限制。

        :param voice_clone_flexus: The voice_clone_flexus of this ListUserQuotaDetail.
        :type voice_clone_flexus: int
        """
        self._voice_clone_flexus = voice_clone_flexus

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListUserQuotaDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
