# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMergeRequestVotesDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'scores': 'int',
        'merge_request_id': 'int',
        'merge_request_creator': 'str',
        'votes': 'list[MergeRequestVotesDto]'
    }

    attribute_map = {
        'scores': 'scores',
        'merge_request_id': 'merge_request_id',
        'merge_request_creator': 'merge_request_creator',
        'votes': 'votes'
    }

    def __init__(self, scores=None, merge_request_id=None, merge_request_creator=None, votes=None):
        r"""ShowMergeRequestVotesDetailResponse

        The model defined in huaweicloud sdk

        :param scores: **参数解释：** 多人合计总分数。
        :type scores: int
        :param merge_request_id: **参数解释：** 合并请求id。
        :type merge_request_id: int
        :param merge_request_creator: **参数解释：** 合并请求作者名。
        :type merge_request_creator: str
        :param votes: **参数解释：** 个人打分详情。
        :type votes: list[:class:`huaweicloudsdkcodehub.v4.MergeRequestVotesDto`]
        """
        
        super(ShowMergeRequestVotesDetailResponse, self).__init__()

        self._scores = None
        self._merge_request_id = None
        self._merge_request_creator = None
        self._votes = None
        self.discriminator = None

        if scores is not None:
            self.scores = scores
        if merge_request_id is not None:
            self.merge_request_id = merge_request_id
        if merge_request_creator is not None:
            self.merge_request_creator = merge_request_creator
        if votes is not None:
            self.votes = votes

    @property
    def scores(self):
        r"""Gets the scores of this ShowMergeRequestVotesDetailResponse.

        **参数解释：** 多人合计总分数。

        :return: The scores of this ShowMergeRequestVotesDetailResponse.
        :rtype: int
        """
        return self._scores

    @scores.setter
    def scores(self, scores):
        r"""Sets the scores of this ShowMergeRequestVotesDetailResponse.

        **参数解释：** 多人合计总分数。

        :param scores: The scores of this ShowMergeRequestVotesDetailResponse.
        :type scores: int
        """
        self._scores = scores

    @property
    def merge_request_id(self):
        r"""Gets the merge_request_id of this ShowMergeRequestVotesDetailResponse.

        **参数解释：** 合并请求id。

        :return: The merge_request_id of this ShowMergeRequestVotesDetailResponse.
        :rtype: int
        """
        return self._merge_request_id

    @merge_request_id.setter
    def merge_request_id(self, merge_request_id):
        r"""Sets the merge_request_id of this ShowMergeRequestVotesDetailResponse.

        **参数解释：** 合并请求id。

        :param merge_request_id: The merge_request_id of this ShowMergeRequestVotesDetailResponse.
        :type merge_request_id: int
        """
        self._merge_request_id = merge_request_id

    @property
    def merge_request_creator(self):
        r"""Gets the merge_request_creator of this ShowMergeRequestVotesDetailResponse.

        **参数解释：** 合并请求作者名。

        :return: The merge_request_creator of this ShowMergeRequestVotesDetailResponse.
        :rtype: str
        """
        return self._merge_request_creator

    @merge_request_creator.setter
    def merge_request_creator(self, merge_request_creator):
        r"""Sets the merge_request_creator of this ShowMergeRequestVotesDetailResponse.

        **参数解释：** 合并请求作者名。

        :param merge_request_creator: The merge_request_creator of this ShowMergeRequestVotesDetailResponse.
        :type merge_request_creator: str
        """
        self._merge_request_creator = merge_request_creator

    @property
    def votes(self):
        r"""Gets the votes of this ShowMergeRequestVotesDetailResponse.

        **参数解释：** 个人打分详情。

        :return: The votes of this ShowMergeRequestVotesDetailResponse.
        :rtype: list[:class:`huaweicloudsdkcodehub.v4.MergeRequestVotesDto`]
        """
        return self._votes

    @votes.setter
    def votes(self, votes):
        r"""Sets the votes of this ShowMergeRequestVotesDetailResponse.

        **参数解释：** 个人打分详情。

        :param votes: The votes of this ShowMergeRequestVotesDetailResponse.
        :type votes: list[:class:`huaweicloudsdkcodehub.v4.MergeRequestVotesDto`]
        """
        self._votes = votes

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
        if not isinstance(other, ShowMergeRequestVotesDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
