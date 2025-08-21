# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MergeRequestBaseEvaluationDto:

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
        'level': 'int',
        'created_at': 'str',
        'updated_at': 'str',
        'content': 'str',
        'user': 'UserBasicDto'
    }

    attribute_map = {
        'id': 'id',
        'merge_request_id': 'merge_request_id',
        'level': 'level',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'content': 'content',
        'user': 'user'
    }

    def __init__(self, id=None, merge_request_id=None, level=None, created_at=None, updated_at=None, content=None, user=None):
        r"""MergeRequestBaseEvaluationDto

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 评价id。
        :type id: int
        :param merge_request_id: **参数解释：** 合并请求id。
        :type merge_request_id: int
        :param level: **参数解释：** 分数。
        :type level: int
        :param created_at: **参数解释：** 创建时间。
        :type created_at: str
        :param updated_at: **参数解释：** 更新时间。
        :type updated_at: str
        :param content: **参数解释：** 评价文本内容。
        :type content: str
        :param user: 
        :type user: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
        """
        
        

        self._id = None
        self._merge_request_id = None
        self._level = None
        self._created_at = None
        self._updated_at = None
        self._content = None
        self._user = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if merge_request_id is not None:
            self.merge_request_id = merge_request_id
        if level is not None:
            self.level = level
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if content is not None:
            self.content = content
        if user is not None:
            self.user = user

    @property
    def id(self):
        r"""Gets the id of this MergeRequestBaseEvaluationDto.

        **参数解释：** 评价id。

        :return: The id of this MergeRequestBaseEvaluationDto.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this MergeRequestBaseEvaluationDto.

        **参数解释：** 评价id。

        :param id: The id of this MergeRequestBaseEvaluationDto.
        :type id: int
        """
        self._id = id

    @property
    def merge_request_id(self):
        r"""Gets the merge_request_id of this MergeRequestBaseEvaluationDto.

        **参数解释：** 合并请求id。

        :return: The merge_request_id of this MergeRequestBaseEvaluationDto.
        :rtype: int
        """
        return self._merge_request_id

    @merge_request_id.setter
    def merge_request_id(self, merge_request_id):
        r"""Sets the merge_request_id of this MergeRequestBaseEvaluationDto.

        **参数解释：** 合并请求id。

        :param merge_request_id: The merge_request_id of this MergeRequestBaseEvaluationDto.
        :type merge_request_id: int
        """
        self._merge_request_id = merge_request_id

    @property
    def level(self):
        r"""Gets the level of this MergeRequestBaseEvaluationDto.

        **参数解释：** 分数。

        :return: The level of this MergeRequestBaseEvaluationDto.
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this MergeRequestBaseEvaluationDto.

        **参数解释：** 分数。

        :param level: The level of this MergeRequestBaseEvaluationDto.
        :type level: int
        """
        self._level = level

    @property
    def created_at(self):
        r"""Gets the created_at of this MergeRequestBaseEvaluationDto.

        **参数解释：** 创建时间。

        :return: The created_at of this MergeRequestBaseEvaluationDto.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this MergeRequestBaseEvaluationDto.

        **参数解释：** 创建时间。

        :param created_at: The created_at of this MergeRequestBaseEvaluationDto.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this MergeRequestBaseEvaluationDto.

        **参数解释：** 更新时间。

        :return: The updated_at of this MergeRequestBaseEvaluationDto.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this MergeRequestBaseEvaluationDto.

        **参数解释：** 更新时间。

        :param updated_at: The updated_at of this MergeRequestBaseEvaluationDto.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def content(self):
        r"""Gets the content of this MergeRequestBaseEvaluationDto.

        **参数解释：** 评价文本内容。

        :return: The content of this MergeRequestBaseEvaluationDto.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this MergeRequestBaseEvaluationDto.

        **参数解释：** 评价文本内容。

        :param content: The content of this MergeRequestBaseEvaluationDto.
        :type content: str
        """
        self._content = content

    @property
    def user(self):
        r"""Gets the user of this MergeRequestBaseEvaluationDto.

        :return: The user of this MergeRequestBaseEvaluationDto.
        :rtype: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
        """
        return self._user

    @user.setter
    def user(self, user):
        r"""Sets the user of this MergeRequestBaseEvaluationDto.

        :param user: The user of this MergeRequestBaseEvaluationDto.
        :type user: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
        """
        self._user = user

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
        if not isinstance(other, MergeRequestBaseEvaluationDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
