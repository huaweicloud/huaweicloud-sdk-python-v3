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
        'introduction_text': 'str',
        'voice_asset_id': 'str',
        'video_asset_name': 'str',
        'gender': 'str'
    }

    attribute_map = {
        'business_card_type': 'business_card_type',
        'card_templet_asset_id': 'card_templet_asset_id',
        'card_text_config': 'card_text_config',
        'card_image_config': 'card_image_config',
        'introduction_text': 'introduction_text',
        'voice_asset_id': 'voice_asset_id',
        'video_asset_name': 'video_asset_name',
        'gender': 'gender'
    }

    def __init__(self, business_card_type=None, card_templet_asset_id=None, card_text_config=None, card_image_config=None, introduction_text=None, voice_asset_id=None, video_asset_name=None, gender=None):
        """CreateDigitalHumanBusinessCardReq

        The model defined in huaweicloud sdk

        :param business_card_type: 数字人名片类型。 * 2D_DIGITAL_HUMAN_CARD：分身数字人名片。
        :type business_card_type: str
        :param card_templet_asset_id: 数字人名片模板资产ID。
        :type card_templet_asset_id: str
        :param card_text_config: 
        :type card_text_config: :class:`huaweicloudsdkmetastudio.v1.BusinessCardTextConfig`
        :param card_image_config: 
        :type card_image_config: :class:`huaweicloudsdkmetastudio.v1.BusinessCardImageConfig`
        :param introduction_text: 自我介绍文本，用于驱动数字人口型。
        :type introduction_text: str
        :param voice_asset_id: 音色资产ID。
        :type voice_asset_id: str
        :param video_asset_name: 输出名片视频资产名称。默认取card_name的值
        :type video_asset_name: str
        :param gender: 性别。 * MALE：男性 * FEMALE：女性
        :type gender: str
        """
        
        

        self._business_card_type = None
        self._card_templet_asset_id = None
        self._card_text_config = None
        self._card_image_config = None
        self._introduction_text = None
        self._voice_asset_id = None
        self._video_asset_name = None
        self._gender = None
        self.discriminator = None

        self.business_card_type = business_card_type
        self.card_templet_asset_id = card_templet_asset_id
        self.card_text_config = card_text_config
        self.card_image_config = card_image_config
        self.introduction_text = introduction_text
        self.voice_asset_id = voice_asset_id
        if video_asset_name is not None:
            self.video_asset_name = video_asset_name
        if gender is not None:
            self.gender = gender

    @property
    def business_card_type(self):
        """Gets the business_card_type of this CreateDigitalHumanBusinessCardReq.

        数字人名片类型。 * 2D_DIGITAL_HUMAN_CARD：分身数字人名片。

        :return: The business_card_type of this CreateDigitalHumanBusinessCardReq.
        :rtype: str
        """
        return self._business_card_type

    @business_card_type.setter
    def business_card_type(self, business_card_type):
        """Sets the business_card_type of this CreateDigitalHumanBusinessCardReq.

        数字人名片类型。 * 2D_DIGITAL_HUMAN_CARD：分身数字人名片。

        :param business_card_type: The business_card_type of this CreateDigitalHumanBusinessCardReq.
        :type business_card_type: str
        """
        self._business_card_type = business_card_type

    @property
    def card_templet_asset_id(self):
        """Gets the card_templet_asset_id of this CreateDigitalHumanBusinessCardReq.

        数字人名片模板资产ID。

        :return: The card_templet_asset_id of this CreateDigitalHumanBusinessCardReq.
        :rtype: str
        """
        return self._card_templet_asset_id

    @card_templet_asset_id.setter
    def card_templet_asset_id(self, card_templet_asset_id):
        """Sets the card_templet_asset_id of this CreateDigitalHumanBusinessCardReq.

        数字人名片模板资产ID。

        :param card_templet_asset_id: The card_templet_asset_id of this CreateDigitalHumanBusinessCardReq.
        :type card_templet_asset_id: str
        """
        self._card_templet_asset_id = card_templet_asset_id

    @property
    def card_text_config(self):
        """Gets the card_text_config of this CreateDigitalHumanBusinessCardReq.

        :return: The card_text_config of this CreateDigitalHumanBusinessCardReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.BusinessCardTextConfig`
        """
        return self._card_text_config

    @card_text_config.setter
    def card_text_config(self, card_text_config):
        """Sets the card_text_config of this CreateDigitalHumanBusinessCardReq.

        :param card_text_config: The card_text_config of this CreateDigitalHumanBusinessCardReq.
        :type card_text_config: :class:`huaweicloudsdkmetastudio.v1.BusinessCardTextConfig`
        """
        self._card_text_config = card_text_config

    @property
    def card_image_config(self):
        """Gets the card_image_config of this CreateDigitalHumanBusinessCardReq.

        :return: The card_image_config of this CreateDigitalHumanBusinessCardReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.BusinessCardImageConfig`
        """
        return self._card_image_config

    @card_image_config.setter
    def card_image_config(self, card_image_config):
        """Sets the card_image_config of this CreateDigitalHumanBusinessCardReq.

        :param card_image_config: The card_image_config of this CreateDigitalHumanBusinessCardReq.
        :type card_image_config: :class:`huaweicloudsdkmetastudio.v1.BusinessCardImageConfig`
        """
        self._card_image_config = card_image_config

    @property
    def introduction_text(self):
        """Gets the introduction_text of this CreateDigitalHumanBusinessCardReq.

        自我介绍文本，用于驱动数字人口型。

        :return: The introduction_text of this CreateDigitalHumanBusinessCardReq.
        :rtype: str
        """
        return self._introduction_text

    @introduction_text.setter
    def introduction_text(self, introduction_text):
        """Sets the introduction_text of this CreateDigitalHumanBusinessCardReq.

        自我介绍文本，用于驱动数字人口型。

        :param introduction_text: The introduction_text of this CreateDigitalHumanBusinessCardReq.
        :type introduction_text: str
        """
        self._introduction_text = introduction_text

    @property
    def voice_asset_id(self):
        """Gets the voice_asset_id of this CreateDigitalHumanBusinessCardReq.

        音色资产ID。

        :return: The voice_asset_id of this CreateDigitalHumanBusinessCardReq.
        :rtype: str
        """
        return self._voice_asset_id

    @voice_asset_id.setter
    def voice_asset_id(self, voice_asset_id):
        """Sets the voice_asset_id of this CreateDigitalHumanBusinessCardReq.

        音色资产ID。

        :param voice_asset_id: The voice_asset_id of this CreateDigitalHumanBusinessCardReq.
        :type voice_asset_id: str
        """
        self._voice_asset_id = voice_asset_id

    @property
    def video_asset_name(self):
        """Gets the video_asset_name of this CreateDigitalHumanBusinessCardReq.

        输出名片视频资产名称。默认取card_name的值

        :return: The video_asset_name of this CreateDigitalHumanBusinessCardReq.
        :rtype: str
        """
        return self._video_asset_name

    @video_asset_name.setter
    def video_asset_name(self, video_asset_name):
        """Sets the video_asset_name of this CreateDigitalHumanBusinessCardReq.

        输出名片视频资产名称。默认取card_name的值

        :param video_asset_name: The video_asset_name of this CreateDigitalHumanBusinessCardReq.
        :type video_asset_name: str
        """
        self._video_asset_name = video_asset_name

    @property
    def gender(self):
        """Gets the gender of this CreateDigitalHumanBusinessCardReq.

        性别。 * MALE：男性 * FEMALE：女性

        :return: The gender of this CreateDigitalHumanBusinessCardReq.
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this CreateDigitalHumanBusinessCardReq.

        性别。 * MALE：男性 * FEMALE：女性

        :param gender: The gender of this CreateDigitalHumanBusinessCardReq.
        :type gender: str
        """
        self._gender = gender

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
