# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAsrVocabularyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'asr_vocabulary_id': 'str',
        'vocabulary_type': 'AsrVocabularyTypeEnum',
        'name': 'str',
        'content': 'str',
        'language': 'LanguageEnum',
        'create_time': 'str',
        'update_time': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'asr_vocabulary_id': 'asr_vocabulary_id',
        'vocabulary_type': 'vocabulary_type',
        'name': 'name',
        'content': 'content',
        'language': 'language',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, asr_vocabulary_id=None, vocabulary_type=None, name=None, content=None, language=None, create_time=None, update_time=None, x_request_id=None):
        r"""ShowAsrVocabularyResponse

        The model defined in huaweicloud sdk

        :param asr_vocabulary_id: 热词表ID。
        :type asr_vocabulary_id: str
        :param vocabulary_type: 
        :type vocabulary_type: :class:`huaweicloudsdkmetastudio.v1.AsrVocabularyTypeEnum`
        :param name: 奇妙问热词表名
        :type name: str
        :param content: 词表内容
        :type content: str
        :param language: 
        :type language: :class:`huaweicloudsdkmetastudio.v1.LanguageEnum`
        :param create_time: 创建时间，格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type create_time: str
        :param update_time: 更新时间，格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type update_time: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ShowAsrVocabularyResponse, self).__init__()

        self._asr_vocabulary_id = None
        self._vocabulary_type = None
        self._name = None
        self._content = None
        self._language = None
        self._create_time = None
        self._update_time = None
        self._x_request_id = None
        self.discriminator = None

        if asr_vocabulary_id is not None:
            self.asr_vocabulary_id = asr_vocabulary_id
        if vocabulary_type is not None:
            self.vocabulary_type = vocabulary_type
        if name is not None:
            self.name = name
        if content is not None:
            self.content = content
        if language is not None:
            self.language = language
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def asr_vocabulary_id(self):
        r"""Gets the asr_vocabulary_id of this ShowAsrVocabularyResponse.

        热词表ID。

        :return: The asr_vocabulary_id of this ShowAsrVocabularyResponse.
        :rtype: str
        """
        return self._asr_vocabulary_id

    @asr_vocabulary_id.setter
    def asr_vocabulary_id(self, asr_vocabulary_id):
        r"""Sets the asr_vocabulary_id of this ShowAsrVocabularyResponse.

        热词表ID。

        :param asr_vocabulary_id: The asr_vocabulary_id of this ShowAsrVocabularyResponse.
        :type asr_vocabulary_id: str
        """
        self._asr_vocabulary_id = asr_vocabulary_id

    @property
    def vocabulary_type(self):
        r"""Gets the vocabulary_type of this ShowAsrVocabularyResponse.

        :return: The vocabulary_type of this ShowAsrVocabularyResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.AsrVocabularyTypeEnum`
        """
        return self._vocabulary_type

    @vocabulary_type.setter
    def vocabulary_type(self, vocabulary_type):
        r"""Sets the vocabulary_type of this ShowAsrVocabularyResponse.

        :param vocabulary_type: The vocabulary_type of this ShowAsrVocabularyResponse.
        :type vocabulary_type: :class:`huaweicloudsdkmetastudio.v1.AsrVocabularyTypeEnum`
        """
        self._vocabulary_type = vocabulary_type

    @property
    def name(self):
        r"""Gets the name of this ShowAsrVocabularyResponse.

        奇妙问热词表名

        :return: The name of this ShowAsrVocabularyResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowAsrVocabularyResponse.

        奇妙问热词表名

        :param name: The name of this ShowAsrVocabularyResponse.
        :type name: str
        """
        self._name = name

    @property
    def content(self):
        r"""Gets the content of this ShowAsrVocabularyResponse.

        词表内容

        :return: The content of this ShowAsrVocabularyResponse.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this ShowAsrVocabularyResponse.

        词表内容

        :param content: The content of this ShowAsrVocabularyResponse.
        :type content: str
        """
        self._content = content

    @property
    def language(self):
        r"""Gets the language of this ShowAsrVocabularyResponse.

        :return: The language of this ShowAsrVocabularyResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.LanguageEnum`
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this ShowAsrVocabularyResponse.

        :param language: The language of this ShowAsrVocabularyResponse.
        :type language: :class:`huaweicloudsdkmetastudio.v1.LanguageEnum`
        """
        self._language = language

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowAsrVocabularyResponse.

        创建时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The create_time of this ShowAsrVocabularyResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowAsrVocabularyResponse.

        创建时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param create_time: The create_time of this ShowAsrVocabularyResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ShowAsrVocabularyResponse.

        更新时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The update_time of this ShowAsrVocabularyResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ShowAsrVocabularyResponse.

        更新时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param update_time: The update_time of this ShowAsrVocabularyResponse.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ShowAsrVocabularyResponse.

        :return: The x_request_id of this ShowAsrVocabularyResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ShowAsrVocabularyResponse.

        :param x_request_id: The x_request_id of this ShowAsrVocabularyResponse.
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
        if not isinstance(other, ShowAsrVocabularyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
