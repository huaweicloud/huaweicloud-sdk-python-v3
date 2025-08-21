# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SimpleMergeRequestDetailDto:

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
        'iid': 'int',
        'title': 'str',
        'description': 'str',
        'source_branch': 'str',
        'target_branch': 'str',
        'state': 'str',
        'created_at': 'str',
        'review_mode': 'str',
        'author': 'UserBasicDto',
        'merge_request_type': 'str',
        'moderation_result': 'bool',
        'moderation_time': 'int',
        'moderation_status': 'int',
        'is_use_temp_branch': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'iid': 'iid',
        'title': 'title',
        'description': 'description',
        'source_branch': 'source_branch',
        'target_branch': 'target_branch',
        'state': 'state',
        'created_at': 'created_at',
        'review_mode': 'review_mode',
        'author': 'author',
        'merge_request_type': 'merge_request_type',
        'moderation_result': 'moderation_result',
        'moderation_time': 'moderation_time',
        'moderation_status': 'moderation_status',
        'is_use_temp_branch': 'is_use_temp_branch'
    }

    def __init__(self, id=None, iid=None, title=None, description=None, source_branch=None, target_branch=None, state=None, created_at=None, review_mode=None, author=None, merge_request_type=None, moderation_result=None, moderation_time=None, moderation_status=None, is_use_temp_branch=None):
        r"""SimpleMergeRequestDetailDto

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 合并请求id。 **取值范围：** 不涉及。
        :type id: int
        :param iid: **参数解释：** 合并请求iid。 **取值范围：** 不涉及。
        :type iid: int
        :param title: **参数解释：** 标题。 **取值范围：** 不涉及。
        :type title: str
        :param description: **参数解释：** 描述。 **取值范围：** 不涉及。
        :type description: str
        :param source_branch: **参数解释：** 源分支。 **取值范围：** 不涉及。
        :type source_branch: str
        :param target_branch: **参数解释：** 目标分支。 **取值范围：** 不涉及。
        :type target_branch: str
        :param state: **参数解释：** 状态。 **取值范围：** 不涉及。
        :type state: str
        :param created_at: **参数解释：** 创建时间。 **取值范围：** 不涉及。
        :type created_at: str
        :param review_mode: **参数解释：** 审核模式。 **取值范围：** 不涉及。
        :type review_mode: str
        :param author: 
        :type author: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
        :param merge_request_type: **参数解释：** 合并请求类型。 **取值范围：** 不涉及。
        :type merge_request_type: str
        :param moderation_result: **参数解释：** 送审结果。 **取值范围：** - true，成功。 - false，失败
        :type moderation_result: bool
        :param moderation_time: **参数解释：** 送审时间时间戳。 **取值范围：** 不涉及。
        :type moderation_time: int
        :param moderation_status: **参数解释：** 送审状态码。 **取值范围：** 不涉及。
        :type moderation_status: int
        :param is_use_temp_branch: **参数解释：** 是否使用临时分支。 **取值范围：** - true，使用。 - false，不使用
        :type is_use_temp_branch: bool
        """
        
        

        self._id = None
        self._iid = None
        self._title = None
        self._description = None
        self._source_branch = None
        self._target_branch = None
        self._state = None
        self._created_at = None
        self._review_mode = None
        self._author = None
        self._merge_request_type = None
        self._moderation_result = None
        self._moderation_time = None
        self._moderation_status = None
        self._is_use_temp_branch = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if iid is not None:
            self.iid = iid
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if source_branch is not None:
            self.source_branch = source_branch
        if target_branch is not None:
            self.target_branch = target_branch
        if state is not None:
            self.state = state
        if created_at is not None:
            self.created_at = created_at
        if review_mode is not None:
            self.review_mode = review_mode
        if author is not None:
            self.author = author
        if merge_request_type is not None:
            self.merge_request_type = merge_request_type
        if moderation_result is not None:
            self.moderation_result = moderation_result
        if moderation_time is not None:
            self.moderation_time = moderation_time
        if moderation_status is not None:
            self.moderation_status = moderation_status
        if is_use_temp_branch is not None:
            self.is_use_temp_branch = is_use_temp_branch

    @property
    def id(self):
        r"""Gets the id of this SimpleMergeRequestDetailDto.

        **参数解释：** 合并请求id。 **取值范围：** 不涉及。

        :return: The id of this SimpleMergeRequestDetailDto.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SimpleMergeRequestDetailDto.

        **参数解释：** 合并请求id。 **取值范围：** 不涉及。

        :param id: The id of this SimpleMergeRequestDetailDto.
        :type id: int
        """
        self._id = id

    @property
    def iid(self):
        r"""Gets the iid of this SimpleMergeRequestDetailDto.

        **参数解释：** 合并请求iid。 **取值范围：** 不涉及。

        :return: The iid of this SimpleMergeRequestDetailDto.
        :rtype: int
        """
        return self._iid

    @iid.setter
    def iid(self, iid):
        r"""Sets the iid of this SimpleMergeRequestDetailDto.

        **参数解释：** 合并请求iid。 **取值范围：** 不涉及。

        :param iid: The iid of this SimpleMergeRequestDetailDto.
        :type iid: int
        """
        self._iid = iid

    @property
    def title(self):
        r"""Gets the title of this SimpleMergeRequestDetailDto.

        **参数解释：** 标题。 **取值范围：** 不涉及。

        :return: The title of this SimpleMergeRequestDetailDto.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this SimpleMergeRequestDetailDto.

        **参数解释：** 标题。 **取值范围：** 不涉及。

        :param title: The title of this SimpleMergeRequestDetailDto.
        :type title: str
        """
        self._title = title

    @property
    def description(self):
        r"""Gets the description of this SimpleMergeRequestDetailDto.

        **参数解释：** 描述。 **取值范围：** 不涉及。

        :return: The description of this SimpleMergeRequestDetailDto.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this SimpleMergeRequestDetailDto.

        **参数解释：** 描述。 **取值范围：** 不涉及。

        :param description: The description of this SimpleMergeRequestDetailDto.
        :type description: str
        """
        self._description = description

    @property
    def source_branch(self):
        r"""Gets the source_branch of this SimpleMergeRequestDetailDto.

        **参数解释：** 源分支。 **取值范围：** 不涉及。

        :return: The source_branch of this SimpleMergeRequestDetailDto.
        :rtype: str
        """
        return self._source_branch

    @source_branch.setter
    def source_branch(self, source_branch):
        r"""Sets the source_branch of this SimpleMergeRequestDetailDto.

        **参数解释：** 源分支。 **取值范围：** 不涉及。

        :param source_branch: The source_branch of this SimpleMergeRequestDetailDto.
        :type source_branch: str
        """
        self._source_branch = source_branch

    @property
    def target_branch(self):
        r"""Gets the target_branch of this SimpleMergeRequestDetailDto.

        **参数解释：** 目标分支。 **取值范围：** 不涉及。

        :return: The target_branch of this SimpleMergeRequestDetailDto.
        :rtype: str
        """
        return self._target_branch

    @target_branch.setter
    def target_branch(self, target_branch):
        r"""Sets the target_branch of this SimpleMergeRequestDetailDto.

        **参数解释：** 目标分支。 **取值范围：** 不涉及。

        :param target_branch: The target_branch of this SimpleMergeRequestDetailDto.
        :type target_branch: str
        """
        self._target_branch = target_branch

    @property
    def state(self):
        r"""Gets the state of this SimpleMergeRequestDetailDto.

        **参数解释：** 状态。 **取值范围：** 不涉及。

        :return: The state of this SimpleMergeRequestDetailDto.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this SimpleMergeRequestDetailDto.

        **参数解释：** 状态。 **取值范围：** 不涉及。

        :param state: The state of this SimpleMergeRequestDetailDto.
        :type state: str
        """
        self._state = state

    @property
    def created_at(self):
        r"""Gets the created_at of this SimpleMergeRequestDetailDto.

        **参数解释：** 创建时间。 **取值范围：** 不涉及。

        :return: The created_at of this SimpleMergeRequestDetailDto.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this SimpleMergeRequestDetailDto.

        **参数解释：** 创建时间。 **取值范围：** 不涉及。

        :param created_at: The created_at of this SimpleMergeRequestDetailDto.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def review_mode(self):
        r"""Gets the review_mode of this SimpleMergeRequestDetailDto.

        **参数解释：** 审核模式。 **取值范围：** 不涉及。

        :return: The review_mode of this SimpleMergeRequestDetailDto.
        :rtype: str
        """
        return self._review_mode

    @review_mode.setter
    def review_mode(self, review_mode):
        r"""Sets the review_mode of this SimpleMergeRequestDetailDto.

        **参数解释：** 审核模式。 **取值范围：** 不涉及。

        :param review_mode: The review_mode of this SimpleMergeRequestDetailDto.
        :type review_mode: str
        """
        self._review_mode = review_mode

    @property
    def author(self):
        r"""Gets the author of this SimpleMergeRequestDetailDto.

        :return: The author of this SimpleMergeRequestDetailDto.
        :rtype: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
        """
        return self._author

    @author.setter
    def author(self, author):
        r"""Sets the author of this SimpleMergeRequestDetailDto.

        :param author: The author of this SimpleMergeRequestDetailDto.
        :type author: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
        """
        self._author = author

    @property
    def merge_request_type(self):
        r"""Gets the merge_request_type of this SimpleMergeRequestDetailDto.

        **参数解释：** 合并请求类型。 **取值范围：** 不涉及。

        :return: The merge_request_type of this SimpleMergeRequestDetailDto.
        :rtype: str
        """
        return self._merge_request_type

    @merge_request_type.setter
    def merge_request_type(self, merge_request_type):
        r"""Sets the merge_request_type of this SimpleMergeRequestDetailDto.

        **参数解释：** 合并请求类型。 **取值范围：** 不涉及。

        :param merge_request_type: The merge_request_type of this SimpleMergeRequestDetailDto.
        :type merge_request_type: str
        """
        self._merge_request_type = merge_request_type

    @property
    def moderation_result(self):
        r"""Gets the moderation_result of this SimpleMergeRequestDetailDto.

        **参数解释：** 送审结果。 **取值范围：** - true，成功。 - false，失败

        :return: The moderation_result of this SimpleMergeRequestDetailDto.
        :rtype: bool
        """
        return self._moderation_result

    @moderation_result.setter
    def moderation_result(self, moderation_result):
        r"""Sets the moderation_result of this SimpleMergeRequestDetailDto.

        **参数解释：** 送审结果。 **取值范围：** - true，成功。 - false，失败

        :param moderation_result: The moderation_result of this SimpleMergeRequestDetailDto.
        :type moderation_result: bool
        """
        self._moderation_result = moderation_result

    @property
    def moderation_time(self):
        r"""Gets the moderation_time of this SimpleMergeRequestDetailDto.

        **参数解释：** 送审时间时间戳。 **取值范围：** 不涉及。

        :return: The moderation_time of this SimpleMergeRequestDetailDto.
        :rtype: int
        """
        return self._moderation_time

    @moderation_time.setter
    def moderation_time(self, moderation_time):
        r"""Sets the moderation_time of this SimpleMergeRequestDetailDto.

        **参数解释：** 送审时间时间戳。 **取值范围：** 不涉及。

        :param moderation_time: The moderation_time of this SimpleMergeRequestDetailDto.
        :type moderation_time: int
        """
        self._moderation_time = moderation_time

    @property
    def moderation_status(self):
        r"""Gets the moderation_status of this SimpleMergeRequestDetailDto.

        **参数解释：** 送审状态码。 **取值范围：** 不涉及。

        :return: The moderation_status of this SimpleMergeRequestDetailDto.
        :rtype: int
        """
        return self._moderation_status

    @moderation_status.setter
    def moderation_status(self, moderation_status):
        r"""Sets the moderation_status of this SimpleMergeRequestDetailDto.

        **参数解释：** 送审状态码。 **取值范围：** 不涉及。

        :param moderation_status: The moderation_status of this SimpleMergeRequestDetailDto.
        :type moderation_status: int
        """
        self._moderation_status = moderation_status

    @property
    def is_use_temp_branch(self):
        r"""Gets the is_use_temp_branch of this SimpleMergeRequestDetailDto.

        **参数解释：** 是否使用临时分支。 **取值范围：** - true，使用。 - false，不使用

        :return: The is_use_temp_branch of this SimpleMergeRequestDetailDto.
        :rtype: bool
        """
        return self._is_use_temp_branch

    @is_use_temp_branch.setter
    def is_use_temp_branch(self, is_use_temp_branch):
        r"""Sets the is_use_temp_branch of this SimpleMergeRequestDetailDto.

        **参数解释：** 是否使用临时分支。 **取值范围：** - true，使用。 - false，不使用

        :param is_use_temp_branch: The is_use_temp_branch of this SimpleMergeRequestDetailDto.
        :type is_use_temp_branch: bool
        """
        self._is_use_temp_branch = is_use_temp_branch

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
        if not isinstance(other, SimpleMergeRequestDetailDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
