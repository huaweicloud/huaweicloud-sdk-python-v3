# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPacifyWordsRequest:

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
        'robot_id': 'str',
        'language': 'str',
        'pacify_words_type': 'int',
        'intent': 'str'
    }

    attribute_map = {
        'x_app_user_id': 'X-App-UserId',
        'offset': 'offset',
        'limit': 'limit',
        'robot_id': 'robot_id',
        'language': 'language',
        'pacify_words_type': 'pacify_words_type',
        'intent': 'intent'
    }

    def __init__(self, x_app_user_id=None, offset=None, limit=None, robot_id=None, language=None, pacify_words_type=None, intent=None):
        r"""ListPacifyWordsRequest

        The model defined in huaweicloud sdk

        :param x_app_user_id: 第三方用户ID。不允许输入中文。
        :type x_app_user_id: str
        :param offset: 偏移量，表示从此偏移量开始查询。
        :type offset: int
        :param limit: 每页显示的条目数量。
        :type limit: int
        :param robot_id: 应用ID。
        :type robot_id: str
        :param language: 智能交互语言 * CN：中文。 * EN：英文。 * ESP：西班牙语（仅海外站点支持） * por：葡萄牙语（仅海外站点支持） * Arabic：阿拉伯语（仅海外站点支持） * Thai：泰语（仅海外站点支持）
        :type language: str
        :param pacify_words_type: 安抚话术类型 &gt; 0:通用安抚话术, 1:基于意图匹配安抚话术
        :type pacify_words_type: int
        :param intent: 安抚话术意图
        :type intent: str
        """
        
        

        self._x_app_user_id = None
        self._offset = None
        self._limit = None
        self._robot_id = None
        self._language = None
        self._pacify_words_type = None
        self._intent = None
        self.discriminator = None

        if x_app_user_id is not None:
            self.x_app_user_id = x_app_user_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        self.robot_id = robot_id
        if language is not None:
            self.language = language
        if pacify_words_type is not None:
            self.pacify_words_type = pacify_words_type
        if intent is not None:
            self.intent = intent

    @property
    def x_app_user_id(self):
        r"""Gets the x_app_user_id of this ListPacifyWordsRequest.

        第三方用户ID。不允许输入中文。

        :return: The x_app_user_id of this ListPacifyWordsRequest.
        :rtype: str
        """
        return self._x_app_user_id

    @x_app_user_id.setter
    def x_app_user_id(self, x_app_user_id):
        r"""Sets the x_app_user_id of this ListPacifyWordsRequest.

        第三方用户ID。不允许输入中文。

        :param x_app_user_id: The x_app_user_id of this ListPacifyWordsRequest.
        :type x_app_user_id: str
        """
        self._x_app_user_id = x_app_user_id

    @property
    def offset(self):
        r"""Gets the offset of this ListPacifyWordsRequest.

        偏移量，表示从此偏移量开始查询。

        :return: The offset of this ListPacifyWordsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListPacifyWordsRequest.

        偏移量，表示从此偏移量开始查询。

        :param offset: The offset of this ListPacifyWordsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListPacifyWordsRequest.

        每页显示的条目数量。

        :return: The limit of this ListPacifyWordsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListPacifyWordsRequest.

        每页显示的条目数量。

        :param limit: The limit of this ListPacifyWordsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def robot_id(self):
        r"""Gets the robot_id of this ListPacifyWordsRequest.

        应用ID。

        :return: The robot_id of this ListPacifyWordsRequest.
        :rtype: str
        """
        return self._robot_id

    @robot_id.setter
    def robot_id(self, robot_id):
        r"""Sets the robot_id of this ListPacifyWordsRequest.

        应用ID。

        :param robot_id: The robot_id of this ListPacifyWordsRequest.
        :type robot_id: str
        """
        self._robot_id = robot_id

    @property
    def language(self):
        r"""Gets the language of this ListPacifyWordsRequest.

        智能交互语言 * CN：中文。 * EN：英文。 * ESP：西班牙语（仅海外站点支持） * por：葡萄牙语（仅海外站点支持） * Arabic：阿拉伯语（仅海外站点支持） * Thai：泰语（仅海外站点支持）

        :return: The language of this ListPacifyWordsRequest.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this ListPacifyWordsRequest.

        智能交互语言 * CN：中文。 * EN：英文。 * ESP：西班牙语（仅海外站点支持） * por：葡萄牙语（仅海外站点支持） * Arabic：阿拉伯语（仅海外站点支持） * Thai：泰语（仅海外站点支持）

        :param language: The language of this ListPacifyWordsRequest.
        :type language: str
        """
        self._language = language

    @property
    def pacify_words_type(self):
        r"""Gets the pacify_words_type of this ListPacifyWordsRequest.

        安抚话术类型 > 0:通用安抚话术, 1:基于意图匹配安抚话术

        :return: The pacify_words_type of this ListPacifyWordsRequest.
        :rtype: int
        """
        return self._pacify_words_type

    @pacify_words_type.setter
    def pacify_words_type(self, pacify_words_type):
        r"""Sets the pacify_words_type of this ListPacifyWordsRequest.

        安抚话术类型 > 0:通用安抚话术, 1:基于意图匹配安抚话术

        :param pacify_words_type: The pacify_words_type of this ListPacifyWordsRequest.
        :type pacify_words_type: int
        """
        self._pacify_words_type = pacify_words_type

    @property
    def intent(self):
        r"""Gets the intent of this ListPacifyWordsRequest.

        安抚话术意图

        :return: The intent of this ListPacifyWordsRequest.
        :rtype: str
        """
        return self._intent

    @intent.setter
    def intent(self, intent):
        r"""Sets the intent of this ListPacifyWordsRequest.

        安抚话术意图

        :param intent: The intent of this ListPacifyWordsRequest.
        :type intent: str
        """
        self._intent = intent

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
        if not isinstance(other, ListPacifyWordsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
