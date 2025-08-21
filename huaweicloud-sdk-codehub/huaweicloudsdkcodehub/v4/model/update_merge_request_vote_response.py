# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateMergeRequestVoteResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'merge_request_id': 'int',
        'score': 'int',
        'author': 'UserSafeDto'
    }

    attribute_map = {
        'id': 'id',
        'merge_request_id': 'merge_request_id',
        'score': 'score',
        'author': 'author'
    }

    def __init__(self, id=None, merge_request_id=None, score=None, author=None):
        r"""UpdateMergeRequestVoteResponse

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 打分记录的id。
        :type id: int
        :param merge_request_id: **参数解释：** 合并请求id。
        :type merge_request_id: int
        :param score: **参数解释：** 分数。
        :type score: int
        :param author: 
        :type author: :class:`huaweicloudsdkcodehub.v4.UserSafeDto`
        """
        
        super(UpdateMergeRequestVoteResponse, self).__init__()

        self._id = None
        self._merge_request_id = None
        self._score = None
        self._author = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if merge_request_id is not None:
            self.merge_request_id = merge_request_id
        if score is not None:
            self.score = score
        if author is not None:
            self.author = author

    @property
    def id(self):
        r"""Gets the id of this UpdateMergeRequestVoteResponse.

        **参数解释：** 打分记录的id。

        :return: The id of this UpdateMergeRequestVoteResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UpdateMergeRequestVoteResponse.

        **参数解释：** 打分记录的id。

        :param id: The id of this UpdateMergeRequestVoteResponse.
        :type id: int
        """
        self._id = id

    @property
    def merge_request_id(self):
        r"""Gets the merge_request_id of this UpdateMergeRequestVoteResponse.

        **参数解释：** 合并请求id。

        :return: The merge_request_id of this UpdateMergeRequestVoteResponse.
        :rtype: int
        """
        return self._merge_request_id

    @merge_request_id.setter
    def merge_request_id(self, merge_request_id):
        r"""Sets the merge_request_id of this UpdateMergeRequestVoteResponse.

        **参数解释：** 合并请求id。

        :param merge_request_id: The merge_request_id of this UpdateMergeRequestVoteResponse.
        :type merge_request_id: int
        """
        self._merge_request_id = merge_request_id

    @property
    def score(self):
        r"""Gets the score of this UpdateMergeRequestVoteResponse.

        **参数解释：** 分数。

        :return: The score of this UpdateMergeRequestVoteResponse.
        :rtype: int
        """
        return self._score

    @score.setter
    def score(self, score):
        r"""Sets the score of this UpdateMergeRequestVoteResponse.

        **参数解释：** 分数。

        :param score: The score of this UpdateMergeRequestVoteResponse.
        :type score: int
        """
        self._score = score

    @property
    def author(self):
        r"""Gets the author of this UpdateMergeRequestVoteResponse.

        :return: The author of this UpdateMergeRequestVoteResponse.
        :rtype: :class:`huaweicloudsdkcodehub.v4.UserSafeDto`
        """
        return self._author

    @author.setter
    def author(self, author):
        r"""Sets the author of this UpdateMergeRequestVoteResponse.

        :param author: The author of this UpdateMergeRequestVoteResponse.
        :type author: :class:`huaweicloudsdkcodehub.v4.UserSafeDto`
        """
        self._author = author

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
        if not isinstance(other, UpdateMergeRequestVoteResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
