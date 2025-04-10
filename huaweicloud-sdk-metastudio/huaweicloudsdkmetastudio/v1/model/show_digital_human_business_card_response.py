# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDigitalHumanBusinessCardResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_info': 'DigitalHumanBusinessCardJobInfo',
        'card_templet_asset_id': 'str',
        'card_text_config': 'BusinessCardTextConfig',
        'card_image_url': 'BusinessCardImageUrl',
        'introduction_type': 'str',
        'introduction_text': 'str',
        'voice_asset_id': 'str',
        'introduction_audio_asset_id': 'str',
        'gender': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'job_info': 'job_info',
        'card_templet_asset_id': 'card_templet_asset_id',
        'card_text_config': 'card_text_config',
        'card_image_url': 'card_image_url',
        'introduction_type': 'introduction_type',
        'introduction_text': 'introduction_text',
        'voice_asset_id': 'voice_asset_id',
        'introduction_audio_asset_id': 'introduction_audio_asset_id',
        'gender': 'gender',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, job_info=None, card_templet_asset_id=None, card_text_config=None, card_image_url=None, introduction_type=None, introduction_text=None, voice_asset_id=None, introduction_audio_asset_id=None, gender=None, x_request_id=None):
        r"""ShowDigitalHumanBusinessCardResponse

        The model defined in huaweicloud sdk

        :param job_info: 
        :type job_info: :class:`huaweicloudsdkmetastudio.v1.DigitalHumanBusinessCardJobInfo`
        :param card_templet_asset_id: 数字人名片模板资产ID，可以从资产库中查询。
        :type card_templet_asset_id: str
        :param card_text_config: 
        :type card_text_config: :class:`huaweicloudsdkmetastudio.v1.BusinessCardTextConfig`
        :param card_image_url: 
        :type card_image_url: :class:`huaweicloudsdkmetastudio.v1.BusinessCardImageUrl`
        :param introduction_type: 自我介绍驱动方式。 * TEXT: 文本驱动，即通过TTS合成语音 * AUDIO: 语音驱动，需要在资产库中先上传语音资产
        :type introduction_type: str
        :param introduction_text: 自我介绍文本，用于驱动数字人口型。
        :type introduction_text: str
        :param voice_asset_id: 音色资产ID，可以从资产库中查询。
        :type voice_asset_id: str
        :param introduction_audio_asset_id: 自我介绍语音资产ID，用于驱动数字人口型。 &gt; * 介绍语音需要作为asset_type&#x3D;AUDIO资产先上传至资产库。 &gt; * 使用时从资产库中查询。
        :type introduction_audio_asset_id: str
        :param gender: 性别。 * MALE：男性 * FEMALE：女性
        :type gender: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ShowDigitalHumanBusinessCardResponse, self).__init__()

        self._job_info = None
        self._card_templet_asset_id = None
        self._card_text_config = None
        self._card_image_url = None
        self._introduction_type = None
        self._introduction_text = None
        self._voice_asset_id = None
        self._introduction_audio_asset_id = None
        self._gender = None
        self._x_request_id = None
        self.discriminator = None

        if job_info is not None:
            self.job_info = job_info
        if card_templet_asset_id is not None:
            self.card_templet_asset_id = card_templet_asset_id
        if card_text_config is not None:
            self.card_text_config = card_text_config
        if card_image_url is not None:
            self.card_image_url = card_image_url
        if introduction_type is not None:
            self.introduction_type = introduction_type
        if introduction_text is not None:
            self.introduction_text = introduction_text
        if voice_asset_id is not None:
            self.voice_asset_id = voice_asset_id
        if introduction_audio_asset_id is not None:
            self.introduction_audio_asset_id = introduction_audio_asset_id
        if gender is not None:
            self.gender = gender
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def job_info(self):
        r"""Gets the job_info of this ShowDigitalHumanBusinessCardResponse.

        :return: The job_info of this ShowDigitalHumanBusinessCardResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.DigitalHumanBusinessCardJobInfo`
        """
        return self._job_info

    @job_info.setter
    def job_info(self, job_info):
        r"""Sets the job_info of this ShowDigitalHumanBusinessCardResponse.

        :param job_info: The job_info of this ShowDigitalHumanBusinessCardResponse.
        :type job_info: :class:`huaweicloudsdkmetastudio.v1.DigitalHumanBusinessCardJobInfo`
        """
        self._job_info = job_info

    @property
    def card_templet_asset_id(self):
        r"""Gets the card_templet_asset_id of this ShowDigitalHumanBusinessCardResponse.

        数字人名片模板资产ID，可以从资产库中查询。

        :return: The card_templet_asset_id of this ShowDigitalHumanBusinessCardResponse.
        :rtype: str
        """
        return self._card_templet_asset_id

    @card_templet_asset_id.setter
    def card_templet_asset_id(self, card_templet_asset_id):
        r"""Sets the card_templet_asset_id of this ShowDigitalHumanBusinessCardResponse.

        数字人名片模板资产ID，可以从资产库中查询。

        :param card_templet_asset_id: The card_templet_asset_id of this ShowDigitalHumanBusinessCardResponse.
        :type card_templet_asset_id: str
        """
        self._card_templet_asset_id = card_templet_asset_id

    @property
    def card_text_config(self):
        r"""Gets the card_text_config of this ShowDigitalHumanBusinessCardResponse.

        :return: The card_text_config of this ShowDigitalHumanBusinessCardResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.BusinessCardTextConfig`
        """
        return self._card_text_config

    @card_text_config.setter
    def card_text_config(self, card_text_config):
        r"""Sets the card_text_config of this ShowDigitalHumanBusinessCardResponse.

        :param card_text_config: The card_text_config of this ShowDigitalHumanBusinessCardResponse.
        :type card_text_config: :class:`huaweicloudsdkmetastudio.v1.BusinessCardTextConfig`
        """
        self._card_text_config = card_text_config

    @property
    def card_image_url(self):
        r"""Gets the card_image_url of this ShowDigitalHumanBusinessCardResponse.

        :return: The card_image_url of this ShowDigitalHumanBusinessCardResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.BusinessCardImageUrl`
        """
        return self._card_image_url

    @card_image_url.setter
    def card_image_url(self, card_image_url):
        r"""Sets the card_image_url of this ShowDigitalHumanBusinessCardResponse.

        :param card_image_url: The card_image_url of this ShowDigitalHumanBusinessCardResponse.
        :type card_image_url: :class:`huaweicloudsdkmetastudio.v1.BusinessCardImageUrl`
        """
        self._card_image_url = card_image_url

    @property
    def introduction_type(self):
        r"""Gets the introduction_type of this ShowDigitalHumanBusinessCardResponse.

        自我介绍驱动方式。 * TEXT: 文本驱动，即通过TTS合成语音 * AUDIO: 语音驱动，需要在资产库中先上传语音资产

        :return: The introduction_type of this ShowDigitalHumanBusinessCardResponse.
        :rtype: str
        """
        return self._introduction_type

    @introduction_type.setter
    def introduction_type(self, introduction_type):
        r"""Sets the introduction_type of this ShowDigitalHumanBusinessCardResponse.

        自我介绍驱动方式。 * TEXT: 文本驱动，即通过TTS合成语音 * AUDIO: 语音驱动，需要在资产库中先上传语音资产

        :param introduction_type: The introduction_type of this ShowDigitalHumanBusinessCardResponse.
        :type introduction_type: str
        """
        self._introduction_type = introduction_type

    @property
    def introduction_text(self):
        r"""Gets the introduction_text of this ShowDigitalHumanBusinessCardResponse.

        自我介绍文本，用于驱动数字人口型。

        :return: The introduction_text of this ShowDigitalHumanBusinessCardResponse.
        :rtype: str
        """
        return self._introduction_text

    @introduction_text.setter
    def introduction_text(self, introduction_text):
        r"""Sets the introduction_text of this ShowDigitalHumanBusinessCardResponse.

        自我介绍文本，用于驱动数字人口型。

        :param introduction_text: The introduction_text of this ShowDigitalHumanBusinessCardResponse.
        :type introduction_text: str
        """
        self._introduction_text = introduction_text

    @property
    def voice_asset_id(self):
        r"""Gets the voice_asset_id of this ShowDigitalHumanBusinessCardResponse.

        音色资产ID，可以从资产库中查询。

        :return: The voice_asset_id of this ShowDigitalHumanBusinessCardResponse.
        :rtype: str
        """
        return self._voice_asset_id

    @voice_asset_id.setter
    def voice_asset_id(self, voice_asset_id):
        r"""Sets the voice_asset_id of this ShowDigitalHumanBusinessCardResponse.

        音色资产ID，可以从资产库中查询。

        :param voice_asset_id: The voice_asset_id of this ShowDigitalHumanBusinessCardResponse.
        :type voice_asset_id: str
        """
        self._voice_asset_id = voice_asset_id

    @property
    def introduction_audio_asset_id(self):
        r"""Gets the introduction_audio_asset_id of this ShowDigitalHumanBusinessCardResponse.

        自我介绍语音资产ID，用于驱动数字人口型。 > * 介绍语音需要作为asset_type=AUDIO资产先上传至资产库。 > * 使用时从资产库中查询。

        :return: The introduction_audio_asset_id of this ShowDigitalHumanBusinessCardResponse.
        :rtype: str
        """
        return self._introduction_audio_asset_id

    @introduction_audio_asset_id.setter
    def introduction_audio_asset_id(self, introduction_audio_asset_id):
        r"""Sets the introduction_audio_asset_id of this ShowDigitalHumanBusinessCardResponse.

        自我介绍语音资产ID，用于驱动数字人口型。 > * 介绍语音需要作为asset_type=AUDIO资产先上传至资产库。 > * 使用时从资产库中查询。

        :param introduction_audio_asset_id: The introduction_audio_asset_id of this ShowDigitalHumanBusinessCardResponse.
        :type introduction_audio_asset_id: str
        """
        self._introduction_audio_asset_id = introduction_audio_asset_id

    @property
    def gender(self):
        r"""Gets the gender of this ShowDigitalHumanBusinessCardResponse.

        性别。 * MALE：男性 * FEMALE：女性

        :return: The gender of this ShowDigitalHumanBusinessCardResponse.
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        r"""Sets the gender of this ShowDigitalHumanBusinessCardResponse.

        性别。 * MALE：男性 * FEMALE：女性

        :param gender: The gender of this ShowDigitalHumanBusinessCardResponse.
        :type gender: str
        """
        self._gender = gender

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ShowDigitalHumanBusinessCardResponse.

        :return: The x_request_id of this ShowDigitalHumanBusinessCardResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ShowDigitalHumanBusinessCardResponse.

        :param x_request_id: The x_request_id of this ShowDigitalHumanBusinessCardResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ShowDigitalHumanBusinessCardResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
