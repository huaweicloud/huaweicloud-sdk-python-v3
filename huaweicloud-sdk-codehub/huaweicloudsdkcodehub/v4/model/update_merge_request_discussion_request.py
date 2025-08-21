# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateMergeRequestDiscussionRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'repository_id': 'int',
        'merge_request_iid': 'int',
        'discussion_id': 'str',
        'note_id': 'int',
        'body': 'UpdateMergeRequestNoteDto'
    }

    attribute_map = {
        'repository_id': 'repository_id',
        'merge_request_iid': 'merge_request_iid',
        'discussion_id': 'discussion_id',
        'note_id': 'note_id',
        'body': 'body'
    }

    def __init__(self, repository_id=None, merge_request_iid=None, discussion_id=None, note_id=None, body=None):
        r"""UpdateMergeRequestDiscussionRequest

        The model defined in huaweicloud sdk

        :param repository_id: **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。
        :type repository_id: int
        :param merge_request_iid: **参数解释：**  合并请求 iid。
        :type merge_request_iid: int
        :param discussion_id: **参数解释：** 检视意见id(主评和回复共用)。 **取值范围：** 字符串长度40。
        :type discussion_id: str
        :param note_id: **参数解释：** 评论id(主评论和回复不共用)。
        :type note_id: int
        :param body: Body of the UpdateMergeRequestDiscussionRequest
        :type body: :class:`huaweicloudsdkcodehub.v4.UpdateMergeRequestNoteDto`
        """
        
        

        self._repository_id = None
        self._merge_request_iid = None
        self._discussion_id = None
        self._note_id = None
        self._body = None
        self.discriminator = None

        self.repository_id = repository_id
        self.merge_request_iid = merge_request_iid
        self.discussion_id = discussion_id
        self.note_id = note_id
        if body is not None:
            self.body = body

    @property
    def repository_id(self):
        r"""Gets the repository_id of this UpdateMergeRequestDiscussionRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。

        :return: The repository_id of this UpdateMergeRequestDiscussionRequest.
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        r"""Sets the repository_id of this UpdateMergeRequestDiscussionRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。

        :param repository_id: The repository_id of this UpdateMergeRequestDiscussionRequest.
        :type repository_id: int
        """
        self._repository_id = repository_id

    @property
    def merge_request_iid(self):
        r"""Gets the merge_request_iid of this UpdateMergeRequestDiscussionRequest.

        **参数解释：**  合并请求 iid。

        :return: The merge_request_iid of this UpdateMergeRequestDiscussionRequest.
        :rtype: int
        """
        return self._merge_request_iid

    @merge_request_iid.setter
    def merge_request_iid(self, merge_request_iid):
        r"""Sets the merge_request_iid of this UpdateMergeRequestDiscussionRequest.

        **参数解释：**  合并请求 iid。

        :param merge_request_iid: The merge_request_iid of this UpdateMergeRequestDiscussionRequest.
        :type merge_request_iid: int
        """
        self._merge_request_iid = merge_request_iid

    @property
    def discussion_id(self):
        r"""Gets the discussion_id of this UpdateMergeRequestDiscussionRequest.

        **参数解释：** 检视意见id(主评和回复共用)。 **取值范围：** 字符串长度40。

        :return: The discussion_id of this UpdateMergeRequestDiscussionRequest.
        :rtype: str
        """
        return self._discussion_id

    @discussion_id.setter
    def discussion_id(self, discussion_id):
        r"""Sets the discussion_id of this UpdateMergeRequestDiscussionRequest.

        **参数解释：** 检视意见id(主评和回复共用)。 **取值范围：** 字符串长度40。

        :param discussion_id: The discussion_id of this UpdateMergeRequestDiscussionRequest.
        :type discussion_id: str
        """
        self._discussion_id = discussion_id

    @property
    def note_id(self):
        r"""Gets the note_id of this UpdateMergeRequestDiscussionRequest.

        **参数解释：** 评论id(主评论和回复不共用)。

        :return: The note_id of this UpdateMergeRequestDiscussionRequest.
        :rtype: int
        """
        return self._note_id

    @note_id.setter
    def note_id(self, note_id):
        r"""Sets the note_id of this UpdateMergeRequestDiscussionRequest.

        **参数解释：** 评论id(主评论和回复不共用)。

        :param note_id: The note_id of this UpdateMergeRequestDiscussionRequest.
        :type note_id: int
        """
        self._note_id = note_id

    @property
    def body(self):
        r"""Gets the body of this UpdateMergeRequestDiscussionRequest.

        :return: The body of this UpdateMergeRequestDiscussionRequest.
        :rtype: :class:`huaweicloudsdkcodehub.v4.UpdateMergeRequestNoteDto`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateMergeRequestDiscussionRequest.

        :param body: The body of this UpdateMergeRequestDiscussionRequest.
        :type body: :class:`huaweicloudsdkcodehub.v4.UpdateMergeRequestNoteDto`
        """
        self._body = body

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
        if not isinstance(other, UpdateMergeRequestDiscussionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
