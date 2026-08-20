# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReviewCommentEntity:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'user_id': 'str',
        'other_user_id': 'str',
        'result': 'str',
        'comment': 'str'
    }

    attribute_map = {
        'id': 'id',
        'user_id': 'user_id',
        'other_user_id': 'other_user_id',
        'result': 'result',
        'comment': 'comment'
    }

    def __init__(self, id=None, user_id=None, other_user_id=None, result=None, comment=None):
        r"""ReviewCommentEntity

        The model defined in huaweicloud sdk

        :param id: 评审意见对象ID。
        :type id: str
        :param user_id: 评审用户ID。
        :type user_id: str
        :param other_user_id: 其他用户Id（转他人）。
        :type other_user_id: str
        :param result: 评审结果。
        :type result: str
        :param comment: 评审意见。
        :type comment: str
        """
        
        

        self._id = None
        self._user_id = None
        self._other_user_id = None
        self._result = None
        self._comment = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if user_id is not None:
            self.user_id = user_id
        if other_user_id is not None:
            self.other_user_id = other_user_id
        if result is not None:
            self.result = result
        if comment is not None:
            self.comment = comment

    @property
    def id(self):
        r"""Gets the id of this ReviewCommentEntity.

        评审意见对象ID。

        :return: The id of this ReviewCommentEntity.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ReviewCommentEntity.

        评审意见对象ID。

        :param id: The id of this ReviewCommentEntity.
        :type id: str
        """
        self._id = id

    @property
    def user_id(self):
        r"""Gets the user_id of this ReviewCommentEntity.

        评审用户ID。

        :return: The user_id of this ReviewCommentEntity.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this ReviewCommentEntity.

        评审用户ID。

        :param user_id: The user_id of this ReviewCommentEntity.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def other_user_id(self):
        r"""Gets the other_user_id of this ReviewCommentEntity.

        其他用户Id（转他人）。

        :return: The other_user_id of this ReviewCommentEntity.
        :rtype: str
        """
        return self._other_user_id

    @other_user_id.setter
    def other_user_id(self, other_user_id):
        r"""Sets the other_user_id of this ReviewCommentEntity.

        其他用户Id（转他人）。

        :param other_user_id: The other_user_id of this ReviewCommentEntity.
        :type other_user_id: str
        """
        self._other_user_id = other_user_id

    @property
    def result(self):
        r"""Gets the result of this ReviewCommentEntity.

        评审结果。

        :return: The result of this ReviewCommentEntity.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this ReviewCommentEntity.

        评审结果。

        :param result: The result of this ReviewCommentEntity.
        :type result: str
        """
        self._result = result

    @property
    def comment(self):
        r"""Gets the comment of this ReviewCommentEntity.

        评审意见。

        :return: The comment of this ReviewCommentEntity.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        r"""Sets the comment of this ReviewCommentEntity.

        评审意见。

        :param comment: The comment of this ReviewCommentEntity.
        :type comment: str
        """
        self._comment = comment

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ReviewCommentEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
