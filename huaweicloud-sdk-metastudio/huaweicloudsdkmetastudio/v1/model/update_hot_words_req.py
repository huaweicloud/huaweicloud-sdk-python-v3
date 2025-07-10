# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateHotWordsReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'hot_words_type': 'HotWordsTypeEnum',
        'sis_hot_words': 'UpdateSisHotWords',
        'mobvoi_hot_words': 'UpdateMobvoiHotWords'
    }

    attribute_map = {
        'hot_words_type': 'hot_words_type',
        'sis_hot_words': 'sis_hot_words',
        'mobvoi_hot_words': 'mobvoi_hot_words'
    }

    def __init__(self, hot_words_type=None, sis_hot_words=None, mobvoi_hot_words=None):
        r"""UpdateHotWordsReq

        The model defined in huaweicloud sdk

        :param hot_words_type: 
        :type hot_words_type: :class:`huaweicloudsdkmetastudio.v1.HotWordsTypeEnum`
        :param sis_hot_words: 
        :type sis_hot_words: :class:`huaweicloudsdkmetastudio.v1.UpdateSisHotWords`
        :param mobvoi_hot_words: 
        :type mobvoi_hot_words: :class:`huaweicloudsdkmetastudio.v1.UpdateMobvoiHotWords`
        """
        
        

        self._hot_words_type = None
        self._sis_hot_words = None
        self._mobvoi_hot_words = None
        self.discriminator = None

        self.hot_words_type = hot_words_type
        if sis_hot_words is not None:
            self.sis_hot_words = sis_hot_words
        if mobvoi_hot_words is not None:
            self.mobvoi_hot_words = mobvoi_hot_words

    @property
    def hot_words_type(self):
        r"""Gets the hot_words_type of this UpdateHotWordsReq.

        :return: The hot_words_type of this UpdateHotWordsReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.HotWordsTypeEnum`
        """
        return self._hot_words_type

    @hot_words_type.setter
    def hot_words_type(self, hot_words_type):
        r"""Sets the hot_words_type of this UpdateHotWordsReq.

        :param hot_words_type: The hot_words_type of this UpdateHotWordsReq.
        :type hot_words_type: :class:`huaweicloudsdkmetastudio.v1.HotWordsTypeEnum`
        """
        self._hot_words_type = hot_words_type

    @property
    def sis_hot_words(self):
        r"""Gets the sis_hot_words of this UpdateHotWordsReq.

        :return: The sis_hot_words of this UpdateHotWordsReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.UpdateSisHotWords`
        """
        return self._sis_hot_words

    @sis_hot_words.setter
    def sis_hot_words(self, sis_hot_words):
        r"""Sets the sis_hot_words of this UpdateHotWordsReq.

        :param sis_hot_words: The sis_hot_words of this UpdateHotWordsReq.
        :type sis_hot_words: :class:`huaweicloudsdkmetastudio.v1.UpdateSisHotWords`
        """
        self._sis_hot_words = sis_hot_words

    @property
    def mobvoi_hot_words(self):
        r"""Gets the mobvoi_hot_words of this UpdateHotWordsReq.

        :return: The mobvoi_hot_words of this UpdateHotWordsReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.UpdateMobvoiHotWords`
        """
        return self._mobvoi_hot_words

    @mobvoi_hot_words.setter
    def mobvoi_hot_words(self, mobvoi_hot_words):
        r"""Sets the mobvoi_hot_words of this UpdateHotWordsReq.

        :param mobvoi_hot_words: The mobvoi_hot_words of this UpdateHotWordsReq.
        :type mobvoi_hot_words: :class:`huaweicloudsdkmetastudio.v1.UpdateMobvoiHotWords`
        """
        self._mobvoi_hot_words = mobvoi_hot_words

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
        if not isinstance(other, UpdateHotWordsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
