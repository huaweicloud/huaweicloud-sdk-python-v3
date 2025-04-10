# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHotQuestionRequest:

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
        'sort_dir': 'str',
        'robot_id': 'str',
        'language': 'str'
    }

    attribute_map = {
        'x_app_user_id': 'X-App-UserId',
        'offset': 'offset',
        'limit': 'limit',
        'sort_dir': 'sort_dir',
        'robot_id': 'robot_id',
        'language': 'language'
    }

    def __init__(self, x_app_user_id=None, offset=None, limit=None, sort_dir=None, robot_id=None, language=None):
        r"""ListHotQuestionRequest

        The model defined in huaweicloud sdk

        :param x_app_user_id: 第三方用户ID。不允许输入中文。
        :type x_app_user_id: str
        :param offset: 偏移量，表示从此偏移量开始查询。
        :type offset: int
        :param limit: 每页显示的条目数量。
        :type limit: int
        :param sort_dir: 排序方式。 * asc：升序 * desc：降序  默认asc升序。
        :type sort_dir: str
        :param robot_id: 机器人ID。
        :type robot_id: str
        :param language: 智能交互语言  * CN:中文  * EN:英文
        :type language: str
        """
        
        

        self._x_app_user_id = None
        self._offset = None
        self._limit = None
        self._sort_dir = None
        self._robot_id = None
        self._language = None
        self.discriminator = None

        if x_app_user_id is not None:
            self.x_app_user_id = x_app_user_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if sort_dir is not None:
            self.sort_dir = sort_dir
        self.robot_id = robot_id
        if language is not None:
            self.language = language

    @property
    def x_app_user_id(self):
        r"""Gets the x_app_user_id of this ListHotQuestionRequest.

        第三方用户ID。不允许输入中文。

        :return: The x_app_user_id of this ListHotQuestionRequest.
        :rtype: str
        """
        return self._x_app_user_id

    @x_app_user_id.setter
    def x_app_user_id(self, x_app_user_id):
        r"""Sets the x_app_user_id of this ListHotQuestionRequest.

        第三方用户ID。不允许输入中文。

        :param x_app_user_id: The x_app_user_id of this ListHotQuestionRequest.
        :type x_app_user_id: str
        """
        self._x_app_user_id = x_app_user_id

    @property
    def offset(self):
        r"""Gets the offset of this ListHotQuestionRequest.

        偏移量，表示从此偏移量开始查询。

        :return: The offset of this ListHotQuestionRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListHotQuestionRequest.

        偏移量，表示从此偏移量开始查询。

        :param offset: The offset of this ListHotQuestionRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListHotQuestionRequest.

        每页显示的条目数量。

        :return: The limit of this ListHotQuestionRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListHotQuestionRequest.

        每页显示的条目数量。

        :param limit: The limit of this ListHotQuestionRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListHotQuestionRequest.

        排序方式。 * asc：升序 * desc：降序  默认asc升序。

        :return: The sort_dir of this ListHotQuestionRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListHotQuestionRequest.

        排序方式。 * asc：升序 * desc：降序  默认asc升序。

        :param sort_dir: The sort_dir of this ListHotQuestionRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def robot_id(self):
        r"""Gets the robot_id of this ListHotQuestionRequest.

        机器人ID。

        :return: The robot_id of this ListHotQuestionRequest.
        :rtype: str
        """
        return self._robot_id

    @robot_id.setter
    def robot_id(self, robot_id):
        r"""Sets the robot_id of this ListHotQuestionRequest.

        机器人ID。

        :param robot_id: The robot_id of this ListHotQuestionRequest.
        :type robot_id: str
        """
        self._robot_id = robot_id

    @property
    def language(self):
        r"""Gets the language of this ListHotQuestionRequest.

        智能交互语言  * CN:中文  * EN:英文

        :return: The language of this ListHotQuestionRequest.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this ListHotQuestionRequest.

        智能交互语言  * CN:中文  * EN:英文

        :param language: The language of this ListHotQuestionRequest.
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
        if not isinstance(other, ListHotQuestionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
