# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAsrVocabularyRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_app_user_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'vocabulary_type': 'str',
        'language': 'str'
    }

    attribute_map = {
        'x_app_user_id': 'X-App-UserId',
        'offset': 'offset',
        'limit': 'limit',
        'vocabulary_type': 'vocabulary_type',
        'language': 'language'
    }

    def __init__(self, x_app_user_id=None, offset=None, limit=None, vocabulary_type=None, language=None):
        r"""ListAsrVocabularyRequest

        The model defined in huaweicloud sdk

        :param x_app_user_id: 第三方用户ID。不允许输入中文。
        :type x_app_user_id: str
        :param offset: 偏移量，表示从此偏移量开始查询。
        :type offset: int
        :param limit: 每页显示的条目数量。
        :type limit: int
        :param vocabulary_type: 词表类型。 &gt; MOBVOI:使用的语音识别服务为MOBVOI时选择此类型
        :type vocabulary_type: str
        :param language: 智能交互语言 * CN：中文。 * EN：英文。 * ESP：西班牙语（仅海外站点支持） * por：葡萄牙语（仅海外站点支持） * Arabic：阿拉伯语（仅海外站点支持） * Thai：泰语（仅海外站点支持）
        :type language: str
        """
        
        

        self._x_app_user_id = None
        self._offset = None
        self._limit = None
        self._vocabulary_type = None
        self._language = None
        self.discriminator = None

        if x_app_user_id is not None:
            self.x_app_user_id = x_app_user_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if vocabulary_type is not None:
            self.vocabulary_type = vocabulary_type
        if language is not None:
            self.language = language

    @property
    def x_app_user_id(self):
        r"""Gets the x_app_user_id of this ListAsrVocabularyRequest.

        第三方用户ID。不允许输入中文。

        :return: The x_app_user_id of this ListAsrVocabularyRequest.
        :rtype: str
        """
        return self._x_app_user_id

    @x_app_user_id.setter
    def x_app_user_id(self, x_app_user_id):
        r"""Sets the x_app_user_id of this ListAsrVocabularyRequest.

        第三方用户ID。不允许输入中文。

        :param x_app_user_id: The x_app_user_id of this ListAsrVocabularyRequest.
        :type x_app_user_id: str
        """
        self._x_app_user_id = x_app_user_id

    @property
    def offset(self):
        r"""Gets the offset of this ListAsrVocabularyRequest.

        偏移量，表示从此偏移量开始查询。

        :return: The offset of this ListAsrVocabularyRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListAsrVocabularyRequest.

        偏移量，表示从此偏移量开始查询。

        :param offset: The offset of this ListAsrVocabularyRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListAsrVocabularyRequest.

        每页显示的条目数量。

        :return: The limit of this ListAsrVocabularyRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAsrVocabularyRequest.

        每页显示的条目数量。

        :param limit: The limit of this ListAsrVocabularyRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def vocabulary_type(self):
        r"""Gets the vocabulary_type of this ListAsrVocabularyRequest.

        词表类型。 > MOBVOI:使用的语音识别服务为MOBVOI时选择此类型

        :return: The vocabulary_type of this ListAsrVocabularyRequest.
        :rtype: str
        """
        return self._vocabulary_type

    @vocabulary_type.setter
    def vocabulary_type(self, vocabulary_type):
        r"""Sets the vocabulary_type of this ListAsrVocabularyRequest.

        词表类型。 > MOBVOI:使用的语音识别服务为MOBVOI时选择此类型

        :param vocabulary_type: The vocabulary_type of this ListAsrVocabularyRequest.
        :type vocabulary_type: str
        """
        self._vocabulary_type = vocabulary_type

    @property
    def language(self):
        r"""Gets the language of this ListAsrVocabularyRequest.

        智能交互语言 * CN：中文。 * EN：英文。 * ESP：西班牙语（仅海外站点支持） * por：葡萄牙语（仅海外站点支持） * Arabic：阿拉伯语（仅海外站点支持） * Thai：泰语（仅海外站点支持）

        :return: The language of this ListAsrVocabularyRequest.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this ListAsrVocabularyRequest.

        智能交互语言 * CN：中文。 * EN：英文。 * ESP：西班牙语（仅海外站点支持） * por：葡萄牙语（仅海外站点支持） * Arabic：阿拉伯语（仅海外站点支持） * Thai：泰语（仅海外站点支持）

        :param language: The language of this ListAsrVocabularyRequest.
        :type language: str
        """
        self._language = language

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
        if not isinstance(other, ListAsrVocabularyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
