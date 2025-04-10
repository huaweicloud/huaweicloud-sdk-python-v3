# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LiveShootScriptItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sequence_no': 'int',
        'title': 'str',
        'text_config': 'TextConfig',
        'audio_config': 'LiveAudioConfig',
        'relation_product': 'RelationProductInfo'
    }

    attribute_map = {
        'sequence_no': 'sequence_no',
        'title': 'title',
        'text_config': 'text_config',
        'audio_config': 'audio_config',
        'relation_product': 'relation_product'
    }

    def __init__(self, sequence_no=None, title=None, text_config=None, audio_config=None, relation_product=None):
        r"""LiveShootScriptItem

        The model defined in huaweicloud sdk

        :param sequence_no: **参数解释**： 剧本序号。 **约束限制**： 不涉及
        :type sequence_no: int
        :param title: **参数解释**： 段落标题。 **约束限制**： 不涉及 **取值范围**： 字符长度0-256位。 **默认取值**： 不涉及。
        :type title: str
        :param text_config: 
        :type text_config: :class:`huaweicloudsdkmetastudio.v1.TextConfig`
        :param audio_config: 
        :type audio_config: :class:`huaweicloudsdkmetastudio.v1.LiveAudioConfig`
        :param relation_product: 
        :type relation_product: :class:`huaweicloudsdkmetastudio.v1.RelationProductInfo`
        """
        
        

        self._sequence_no = None
        self._title = None
        self._text_config = None
        self._audio_config = None
        self._relation_product = None
        self.discriminator = None

        if sequence_no is not None:
            self.sequence_no = sequence_no
        if title is not None:
            self.title = title
        if text_config is not None:
            self.text_config = text_config
        if audio_config is not None:
            self.audio_config = audio_config
        if relation_product is not None:
            self.relation_product = relation_product

    @property
    def sequence_no(self):
        r"""Gets the sequence_no of this LiveShootScriptItem.

        **参数解释**： 剧本序号。 **约束限制**： 不涉及

        :return: The sequence_no of this LiveShootScriptItem.
        :rtype: int
        """
        return self._sequence_no

    @sequence_no.setter
    def sequence_no(self, sequence_no):
        r"""Sets the sequence_no of this LiveShootScriptItem.

        **参数解释**： 剧本序号。 **约束限制**： 不涉及

        :param sequence_no: The sequence_no of this LiveShootScriptItem.
        :type sequence_no: int
        """
        self._sequence_no = sequence_no

    @property
    def title(self):
        r"""Gets the title of this LiveShootScriptItem.

        **参数解释**： 段落标题。 **约束限制**： 不涉及 **取值范围**： 字符长度0-256位。 **默认取值**： 不涉及。

        :return: The title of this LiveShootScriptItem.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this LiveShootScriptItem.

        **参数解释**： 段落标题。 **约束限制**： 不涉及 **取值范围**： 字符长度0-256位。 **默认取值**： 不涉及。

        :param title: The title of this LiveShootScriptItem.
        :type title: str
        """
        self._title = title

    @property
    def text_config(self):
        r"""Gets the text_config of this LiveShootScriptItem.

        :return: The text_config of this LiveShootScriptItem.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.TextConfig`
        """
        return self._text_config

    @text_config.setter
    def text_config(self, text_config):
        r"""Sets the text_config of this LiveShootScriptItem.

        :param text_config: The text_config of this LiveShootScriptItem.
        :type text_config: :class:`huaweicloudsdkmetastudio.v1.TextConfig`
        """
        self._text_config = text_config

    @property
    def audio_config(self):
        r"""Gets the audio_config of this LiveShootScriptItem.

        :return: The audio_config of this LiveShootScriptItem.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.LiveAudioConfig`
        """
        return self._audio_config

    @audio_config.setter
    def audio_config(self, audio_config):
        r"""Sets the audio_config of this LiveShootScriptItem.

        :param audio_config: The audio_config of this LiveShootScriptItem.
        :type audio_config: :class:`huaweicloudsdkmetastudio.v1.LiveAudioConfig`
        """
        self._audio_config = audio_config

    @property
    def relation_product(self):
        r"""Gets the relation_product of this LiveShootScriptItem.

        :return: The relation_product of this LiveShootScriptItem.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.RelationProductInfo`
        """
        return self._relation_product

    @relation_product.setter
    def relation_product(self, relation_product):
        r"""Sets the relation_product of this LiveShootScriptItem.

        :param relation_product: The relation_product of this LiveShootScriptItem.
        :type relation_product: :class:`huaweicloudsdkmetastudio.v1.RelationProductInfo`
        """
        self._relation_product = relation_product

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
        if not isinstance(other, LiveShootScriptItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
