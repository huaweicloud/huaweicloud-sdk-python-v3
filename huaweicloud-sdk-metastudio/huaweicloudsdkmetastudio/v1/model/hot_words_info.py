# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HotWordsInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'hot_words_id': 'str',
        'robot_id': 'str',
        'hot_words_type': 'HotWordsTypeEnum',
        'vocabulary_id': 'str',
        'sis_project_id': 'str',
        'region': 'int',
        'language': 'LanguageEnum',
        'create_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'hot_words_id': 'hot_words_id',
        'robot_id': 'robot_id',
        'hot_words_type': 'hot_words_type',
        'vocabulary_id': 'vocabulary_id',
        'sis_project_id': 'sis_project_id',
        'region': 'region',
        'language': 'language',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, hot_words_id=None, robot_id=None, hot_words_type=None, vocabulary_id=None, sis_project_id=None, region=None, language=None, create_time=None, update_time=None):
        """HotWordsInfo

        The model defined in huaweicloud sdk

        :param hot_words_id: 热词记录ID。
        :type hot_words_id: str
        :param robot_id: 应用ID。
        :type robot_id: str
        :param hot_words_type: 
        :type hot_words_type: :class:`huaweicloudsdkmetastudio.v1.HotWordsTypeEnum`
        :param vocabulary_id: 热词ID(sis中配置)。
        :type vocabulary_id: str
        :param sis_project_id: SIS服务所在区域projectId
        :type sis_project_id: str
        :param region: 对接SIS服务的区域。 &gt; 0：北京四；3：上海一；
        :type region: int
        :param language: 
        :type language: :class:`huaweicloudsdkmetastudio.v1.LanguageEnum`
        :param create_time: 创建时间，格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type create_time: str
        :param update_time: 更新时间，格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type update_time: str
        """
        
        

        self._hot_words_id = None
        self._robot_id = None
        self._hot_words_type = None
        self._vocabulary_id = None
        self._sis_project_id = None
        self._region = None
        self._language = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if hot_words_id is not None:
            self.hot_words_id = hot_words_id
        if robot_id is not None:
            self.robot_id = robot_id
        if hot_words_type is not None:
            self.hot_words_type = hot_words_type
        if vocabulary_id is not None:
            self.vocabulary_id = vocabulary_id
        if sis_project_id is not None:
            self.sis_project_id = sis_project_id
        if region is not None:
            self.region = region
        if language is not None:
            self.language = language
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def hot_words_id(self):
        """Gets the hot_words_id of this HotWordsInfo.

        热词记录ID。

        :return: The hot_words_id of this HotWordsInfo.
        :rtype: str
        """
        return self._hot_words_id

    @hot_words_id.setter
    def hot_words_id(self, hot_words_id):
        """Sets the hot_words_id of this HotWordsInfo.

        热词记录ID。

        :param hot_words_id: The hot_words_id of this HotWordsInfo.
        :type hot_words_id: str
        """
        self._hot_words_id = hot_words_id

    @property
    def robot_id(self):
        """Gets the robot_id of this HotWordsInfo.

        应用ID。

        :return: The robot_id of this HotWordsInfo.
        :rtype: str
        """
        return self._robot_id

    @robot_id.setter
    def robot_id(self, robot_id):
        """Sets the robot_id of this HotWordsInfo.

        应用ID。

        :param robot_id: The robot_id of this HotWordsInfo.
        :type robot_id: str
        """
        self._robot_id = robot_id

    @property
    def hot_words_type(self):
        """Gets the hot_words_type of this HotWordsInfo.

        :return: The hot_words_type of this HotWordsInfo.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.HotWordsTypeEnum`
        """
        return self._hot_words_type

    @hot_words_type.setter
    def hot_words_type(self, hot_words_type):
        """Sets the hot_words_type of this HotWordsInfo.

        :param hot_words_type: The hot_words_type of this HotWordsInfo.
        :type hot_words_type: :class:`huaweicloudsdkmetastudio.v1.HotWordsTypeEnum`
        """
        self._hot_words_type = hot_words_type

    @property
    def vocabulary_id(self):
        """Gets the vocabulary_id of this HotWordsInfo.

        热词ID(sis中配置)。

        :return: The vocabulary_id of this HotWordsInfo.
        :rtype: str
        """
        return self._vocabulary_id

    @vocabulary_id.setter
    def vocabulary_id(self, vocabulary_id):
        """Sets the vocabulary_id of this HotWordsInfo.

        热词ID(sis中配置)。

        :param vocabulary_id: The vocabulary_id of this HotWordsInfo.
        :type vocabulary_id: str
        """
        self._vocabulary_id = vocabulary_id

    @property
    def sis_project_id(self):
        """Gets the sis_project_id of this HotWordsInfo.

        SIS服务所在区域projectId

        :return: The sis_project_id of this HotWordsInfo.
        :rtype: str
        """
        return self._sis_project_id

    @sis_project_id.setter
    def sis_project_id(self, sis_project_id):
        """Sets the sis_project_id of this HotWordsInfo.

        SIS服务所在区域projectId

        :param sis_project_id: The sis_project_id of this HotWordsInfo.
        :type sis_project_id: str
        """
        self._sis_project_id = sis_project_id

    @property
    def region(self):
        """Gets the region of this HotWordsInfo.

        对接SIS服务的区域。 > 0：北京四；3：上海一；

        :return: The region of this HotWordsInfo.
        :rtype: int
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this HotWordsInfo.

        对接SIS服务的区域。 > 0：北京四；3：上海一；

        :param region: The region of this HotWordsInfo.
        :type region: int
        """
        self._region = region

    @property
    def language(self):
        """Gets the language of this HotWordsInfo.

        :return: The language of this HotWordsInfo.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.LanguageEnum`
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this HotWordsInfo.

        :param language: The language of this HotWordsInfo.
        :type language: :class:`huaweicloudsdkmetastudio.v1.LanguageEnum`
        """
        self._language = language

    @property
    def create_time(self):
        """Gets the create_time of this HotWordsInfo.

        创建时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The create_time of this HotWordsInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this HotWordsInfo.

        创建时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param create_time: The create_time of this HotWordsInfo.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this HotWordsInfo.

        更新时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The update_time of this HotWordsInfo.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this HotWordsInfo.

        更新时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param update_time: The update_time of this HotWordsInfo.
        :type update_time: str
        """
        self._update_time = update_time

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
        if not isinstance(other, HotWordsInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
