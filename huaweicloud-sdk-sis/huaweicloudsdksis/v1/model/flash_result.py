# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FlashResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'channel_id': 'int',
        'sentences': 'list[Sentences]'
    }

    attribute_map = {
        'channel_id': 'channel_id',
        'sentences': 'sentences'
    }

    def __init__(self, channel_id=None, sentences=None):
        """FlashResult

        The model defined in huaweicloud sdk

        :param channel_id: 音频声道id
        :type channel_id: int
        :param sentences: 分句结果
        :type sentences: list[:class:`huaweicloudsdksis.v1.Sentences`]
        """
        
        

        self._channel_id = None
        self._sentences = None
        self.discriminator = None

        if channel_id is not None:
            self.channel_id = channel_id
        if sentences is not None:
            self.sentences = sentences

    @property
    def channel_id(self):
        """Gets the channel_id of this FlashResult.

        音频声道id

        :return: The channel_id of this FlashResult.
        :rtype: int
        """
        return self._channel_id

    @channel_id.setter
    def channel_id(self, channel_id):
        """Sets the channel_id of this FlashResult.

        音频声道id

        :param channel_id: The channel_id of this FlashResult.
        :type channel_id: int
        """
        self._channel_id = channel_id

    @property
    def sentences(self):
        """Gets the sentences of this FlashResult.

        分句结果

        :return: The sentences of this FlashResult.
        :rtype: list[:class:`huaweicloudsdksis.v1.Sentences`]
        """
        return self._sentences

    @sentences.setter
    def sentences(self, sentences):
        """Sets the sentences of this FlashResult.

        分句结果

        :param sentences: The sentences of this FlashResult.
        :type sentences: list[:class:`huaweicloudsdksis.v1.Sentences`]
        """
        self._sentences = sentences

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
        if not isinstance(other, FlashResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
