# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDigitalHumanBusinessCardReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'business_card_type': 'str',
        'card_templet_asset_id': 'str',
        'card_text_config': 'BusinessCardTextConfig',
        'card_image_config': 'BusinessCardImageConfig',
        'introduction_type': 'str',
        'introduction_text': 'str',
        'voice_asset_id': 'str',
        'introduction_audio_asset_id': 'str',
        'video_asset_name': 'str',
        'gender': 'str',
        'review_config': 'ReviewConfig',
        'callback_config': 'CallBackConfig'
    }

    attribute_map = {
        'business_card_type': 'business_card_type',
        'card_templet_asset_id': 'card_templet_asset_id',
        'card_text_config': 'card_text_config',
        'card_image_config': 'card_image_config',
        'introduction_type': 'introduction_type',
        'introduction_text': 'introduction_text',
        'voice_asset_id': 'voice_asset_id',
        'introduction_audio_asset_id': 'introduction_audio_asset_id',
        'video_asset_name': 'video_asset_name',
        'gender': 'gender',
        'review_config': 'review_config',
        'callback_config': 'callback_config'
    }

    def __init__(self, business_card_type=None, card_templet_asset_id=None, card_text_config=None, card_image_config=None, introduction_type=None, introduction_text=None, voice_asset_id=None, introduction_audio_asset_id=None, video_asset_name=None, gender=None, review_config=None, callback_config=None):
        r"""CreateDigitalHumanBusinessCardReq

        The model defined in huaweicloud sdk

        :param business_card_type: 数字人名片类型。 * 2D_DIGITAL_HUMAN_CARD：分身数字人名片。
        :type business_card_type: str
        :param card_templet_asset_id: 数字人名片模板资产ID，可以从资产库中查询。
        :type card_templet_asset_id: str
        :param card_text_config: 
        :type card_text_config: :class:`huaweicloudsdkmetastudio.v1.BusinessCardTextConfig`
        :param card_image_config: 
        :type card_image_config: :class:`huaweicloudsdkmetastudio.v1.BusinessCardImageConfig`
        :param introduction_type: 自我介绍驱动方式。 * TEXT: 文本驱动，即通过TTS合成语音。文本驱动需要填写introduction_text和voice_asset_id参数。 * AUDIO: 语音驱动，需要在资产库中先上传语音资产。语音驱动需要填写introduction_audio_asset_id参数。
        :type introduction_type: str
        :param introduction_text: 自我介绍文本，用于驱动数字人口型。
        :type introduction_text: str
        :param voice_asset_id: 音色资产ID，可以从资产库中查询。
        :type voice_asset_id: str
        :param introduction_audio_asset_id: 自我介绍语音资产ID，用于驱动数字人口型。 &gt; * 介绍语音需要作为asset_type&#x3D;AUDIO资产先上传至资产库。 &gt; * 使用时从资产库中查询。
        :type introduction_audio_asset_id: str
        :param video_asset_name: 输出名片视频资产名称。默认取card_name的值
        :type video_asset_name: str
        :param gender: 性别。 * MALE：男性 * FEMALE：女性
        :type gender: str
        :param review_config: 
        :type review_config: :class:`huaweicloudsdkmetastudio.v1.ReviewConfig`
        :param callback_config: 
        :type callback_config: :class:`huaweicloudsdkmetastudio.v1.CallBackConfig`
        """
        
        

        self._business_card_type = None
        self._card_templet_asset_id = None
        self._card_text_config = None
        self._card_image_config = None
        self._introduction_type = None
        self._introduction_text = None
        self._voice_asset_id = None
        self._introduction_audio_asset_id = None
        self._video_asset_name = None
        self._gender = None
        self._review_config = None
        self._callback_config = None
        self.discriminator = None

        self.business_card_type = business_card_type
        self.card_templet_asset_id = card_templet_asset_id
        self.card_text_config = card_text_config
        self.card_image_config = card_image_config
        if introduction_type is not None:
            self.introduction_type = introduction_type
        if introduction_text is not None:
            self.introduction_text = introduction_text
        if voice_asset_id is not None:
            self.voice_asset_id = voice_asset_id
        if introduction_audio_asset_id is not None:
            self.introduction_audio_asset_id = introduction_audio_asset_id
        if video_asset_name is not None:
            self.video_asset_name = video_asset_name
        if gender is not None:
            self.gender = gender
        if review_config is not None:
            self.review_config = review_config
        if callback_config is not None:
            self.callback_config = callback_config

    @property
    def business_card_type(self):
        r"""Gets the business_card_type of this CreateDigitalHumanBusinessCardReq.

        数字人名片类型。 * 2D_DIGITAL_HUMAN_CARD：分身数字人名片。

        :return: The business_card_type of this CreateDigitalHumanBusinessCardReq.
        :rtype: str
        """
        return self._business_card_type

    @business_card_type.setter
    def business_card_type(self, business_card_type):
        r"""Sets the business_card_type of this CreateDigitalHumanBusinessCardReq.

        数字人名片类型。 * 2D_DIGITAL_HUMAN_CARD：分身数字人名片。

        :param business_card_type: The business_card_type of this CreateDigitalHumanBusinessCardReq.
        :type business_card_type: str
        """
        self._business_card_type = business_card_type

    @property
    def card_templet_asset_id(self):
        r"""Gets the card_templet_asset_id of this CreateDigitalHumanBusinessCardReq.

        数字人名片模板资产ID，可以从资产库中查询。

        :return: The card_templet_asset_id of this CreateDigitalHumanBusinessCardReq.
        :rtype: str
        """
        return self._card_templet_asset_id

    @card_templet_asset_id.setter
    def card_templet_asset_id(self, card_templet_asset_id):
        r"""Sets the card_templet_asset_id of this CreateDigitalHumanBusinessCardReq.

        数字人名片模板资产ID，可以从资产库中查询。

        :param card_templet_asset_id: The card_templet_asset_id of this CreateDigitalHumanBusinessCardReq.
        :type card_templet_asset_id: str
        """
        self._card_templet_asset_id = card_templet_asset_id

    @property
    def card_text_config(self):
        r"""Gets the card_text_config of this CreateDigitalHumanBusinessCardReq.

        :return: The card_text_config of this CreateDigitalHumanBusinessCardReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.BusinessCardTextConfig`
        """
        return self._card_text_config

    @card_text_config.setter
    def card_text_config(self, card_text_config):
        r"""Sets the card_text_config of this CreateDigitalHumanBusinessCardReq.

        :param card_text_config: The card_text_config of this CreateDigitalHumanBusinessCardReq.
        :type card_text_config: :class:`huaweicloudsdkmetastudio.v1.BusinessCardTextConfig`
        """
        self._card_text_config = card_text_config

    @property
    def card_image_config(self):
        r"""Gets the card_image_config of this CreateDigitalHumanBusinessCardReq.

        :return: The card_image_config of this CreateDigitalHumanBusinessCardReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.BusinessCardImageConfig`
        """
        return self._card_image_config

    @card_image_config.setter
    def card_image_config(self, card_image_config):
        r"""Sets the card_image_config of this CreateDigitalHumanBusinessCardReq.

        :param card_image_config: The card_image_config of this CreateDigitalHumanBusinessCardReq.
        :type card_image_config: :class:`huaweicloudsdkmetastudio.v1.BusinessCardImageConfig`
        """
        self._card_image_config = card_image_config

    @property
    def introduction_type(self):
        r"""Gets the introduction_type of this CreateDigitalHumanBusinessCardReq.

        自我介绍驱动方式。 * TEXT: 文本驱动，即通过TTS合成语音。文本驱动需要填写introduction_text和voice_asset_id参数。 * AUDIO: 语音驱动，需要在资产库中先上传语音资产。语音驱动需要填写introduction_audio_asset_id参数。

        :return: The introduction_type of this CreateDigitalHumanBusinessCardReq.
        :rtype: str
        """
        return self._introduction_type

    @introduction_type.setter
    def introduction_type(self, introduction_type):
        r"""Sets the introduction_type of this CreateDigitalHumanBusinessCardReq.

        自我介绍驱动方式。 * TEXT: 文本驱动，即通过TTS合成语音。文本驱动需要填写introduction_text和voice_asset_id参数。 * AUDIO: 语音驱动，需要在资产库中先上传语音资产。语音驱动需要填写introduction_audio_asset_id参数。

        :param introduction_type: The introduction_type of this CreateDigitalHumanBusinessCardReq.
        :type introduction_type: str
        """
        self._introduction_type = introduction_type

    @property
    def introduction_text(self):
        r"""Gets the introduction_text of this CreateDigitalHumanBusinessCardReq.

        自我介绍文本，用于驱动数字人口型。

        :return: The introduction_text of this CreateDigitalHumanBusinessCardReq.
        :rtype: str
        """
        return self._introduction_text

    @introduction_text.setter
    def introduction_text(self, introduction_text):
        r"""Sets the introduction_text of this CreateDigitalHumanBusinessCardReq.

        自我介绍文本，用于驱动数字人口型。

        :param introduction_text: The introduction_text of this CreateDigitalHumanBusinessCardReq.
        :type introduction_text: str
        """
        self._introduction_text = introduction_text

    @property
    def voice_asset_id(self):
        r"""Gets the voice_asset_id of this CreateDigitalHumanBusinessCardReq.

        音色资产ID，可以从资产库中查询。

        :return: The voice_asset_id of this CreateDigitalHumanBusinessCardReq.
        :rtype: str
        """
        return self._voice_asset_id

    @voice_asset_id.setter
    def voice_asset_id(self, voice_asset_id):
        r"""Sets the voice_asset_id of this CreateDigitalHumanBusinessCardReq.

        音色资产ID，可以从资产库中查询。

        :param voice_asset_id: The voice_asset_id of this CreateDigitalHumanBusinessCardReq.
        :type voice_asset_id: str
        """
        self._voice_asset_id = voice_asset_id

    @property
    def introduction_audio_asset_id(self):
        r"""Gets the introduction_audio_asset_id of this CreateDigitalHumanBusinessCardReq.

        自我介绍语音资产ID，用于驱动数字人口型。 > * 介绍语音需要作为asset_type=AUDIO资产先上传至资产库。 > * 使用时从资产库中查询。

        :return: The introduction_audio_asset_id of this CreateDigitalHumanBusinessCardReq.
        :rtype: str
        """
        return self._introduction_audio_asset_id

    @introduction_audio_asset_id.setter
    def introduction_audio_asset_id(self, introduction_audio_asset_id):
        r"""Sets the introduction_audio_asset_id of this CreateDigitalHumanBusinessCardReq.

        自我介绍语音资产ID，用于驱动数字人口型。 > * 介绍语音需要作为asset_type=AUDIO资产先上传至资产库。 > * 使用时从资产库中查询。

        :param introduction_audio_asset_id: The introduction_audio_asset_id of this CreateDigitalHumanBusinessCardReq.
        :type introduction_audio_asset_id: str
        """
        self._introduction_audio_asset_id = introduction_audio_asset_id

    @property
    def video_asset_name(self):
        r"""Gets the video_asset_name of this CreateDigitalHumanBusinessCardReq.

        输出名片视频资产名称。默认取card_name的值

        :return: The video_asset_name of this CreateDigitalHumanBusinessCardReq.
        :rtype: str
        """
        return self._video_asset_name

    @video_asset_name.setter
    def video_asset_name(self, video_asset_name):
        r"""Sets the video_asset_name of this CreateDigitalHumanBusinessCardReq.

        输出名片视频资产名称。默认取card_name的值

        :param video_asset_name: The video_asset_name of this CreateDigitalHumanBusinessCardReq.
        :type video_asset_name: str
        """
        self._video_asset_name = video_asset_name

    @property
    def gender(self):
        r"""Gets the gender of this CreateDigitalHumanBusinessCardReq.

        性别。 * MALE：男性 * FEMALE：女性

        :return: The gender of this CreateDigitalHumanBusinessCardReq.
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        r"""Sets the gender of this CreateDigitalHumanBusinessCardReq.

        性别。 * MALE：男性 * FEMALE：女性

        :param gender: The gender of this CreateDigitalHumanBusinessCardReq.
        :type gender: str
        """
        self._gender = gender

    @property
    def review_config(self):
        r"""Gets the review_config of this CreateDigitalHumanBusinessCardReq.

        :return: The review_config of this CreateDigitalHumanBusinessCardReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ReviewConfig`
        """
        return self._review_config

    @review_config.setter
    def review_config(self, review_config):
        r"""Sets the review_config of this CreateDigitalHumanBusinessCardReq.

        :param review_config: The review_config of this CreateDigitalHumanBusinessCardReq.
        :type review_config: :class:`huaweicloudsdkmetastudio.v1.ReviewConfig`
        """
        self._review_config = review_config

    @property
    def callback_config(self):
        r"""Gets the callback_config of this CreateDigitalHumanBusinessCardReq.

        :return: The callback_config of this CreateDigitalHumanBusinessCardReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CallBackConfig`
        """
        return self._callback_config

    @callback_config.setter
    def callback_config(self, callback_config):
        r"""Sets the callback_config of this CreateDigitalHumanBusinessCardReq.

        :param callback_config: The callback_config of this CreateDigitalHumanBusinessCardReq.
        :type callback_config: :class:`huaweicloudsdkmetastudio.v1.CallBackConfig`
        """
        self._callback_config = callback_config

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
        if not isinstance(other, CreateDigitalHumanBusinessCardReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
