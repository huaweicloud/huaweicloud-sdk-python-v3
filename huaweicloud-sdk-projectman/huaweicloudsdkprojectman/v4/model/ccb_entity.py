# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CcbEntity:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'approval_time': 'str',
        'category': 'str',
        'ccb2review': 'str',
        'co_id': 'str',
        'id': 'str',
        'owner': 'UserEntity',
        'approval_comments': 'str'
    }

    attribute_map = {
        'approval_time': 'approval_time',
        'category': 'category',
        'ccb2review': 'ccb2review',
        'co_id': 'co_id',
        'id': 'id',
        'owner': 'owner',
        'approval_comments': 'approval_comments'
    }

    def __init__(self, approval_time=None, category=None, ccb2review=None, co_id=None, id=None, owner=None, approval_comments=None):
        r"""CcbEntity

        The model defined in huaweicloud sdk

        :param approval_time: 审批时间。
        :type approval_time: str
        :param category: 工作项类型，审批对象固定为CCB。
        :type category: str
        :param ccb2review: 审批对象关联的评审单ID。
        :type ccb2review: str
        :param co_id: 关联的变更对象ID。
        :type co_id: str
        :param id: 审批对象ID。
        :type id: str
        :param owner: 
        :type owner: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        :param approval_comments: 审批意见。
        :type approval_comments: str
        """
        
        

        self._approval_time = None
        self._category = None
        self._ccb2review = None
        self._co_id = None
        self._id = None
        self._owner = None
        self._approval_comments = None
        self.discriminator = None

        if approval_time is not None:
            self.approval_time = approval_time
        if category is not None:
            self.category = category
        if ccb2review is not None:
            self.ccb2review = ccb2review
        if co_id is not None:
            self.co_id = co_id
        if id is not None:
            self.id = id
        if owner is not None:
            self.owner = owner
        if approval_comments is not None:
            self.approval_comments = approval_comments

    @property
    def approval_time(self):
        r"""Gets the approval_time of this CcbEntity.

        审批时间。

        :return: The approval_time of this CcbEntity.
        :rtype: str
        """
        return self._approval_time

    @approval_time.setter
    def approval_time(self, approval_time):
        r"""Sets the approval_time of this CcbEntity.

        审批时间。

        :param approval_time: The approval_time of this CcbEntity.
        :type approval_time: str
        """
        self._approval_time = approval_time

    @property
    def category(self):
        r"""Gets the category of this CcbEntity.

        工作项类型，审批对象固定为CCB。

        :return: The category of this CcbEntity.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this CcbEntity.

        工作项类型，审批对象固定为CCB。

        :param category: The category of this CcbEntity.
        :type category: str
        """
        self._category = category

    @property
    def ccb2review(self):
        r"""Gets the ccb2review of this CcbEntity.

        审批对象关联的评审单ID。

        :return: The ccb2review of this CcbEntity.
        :rtype: str
        """
        return self._ccb2review

    @ccb2review.setter
    def ccb2review(self, ccb2review):
        r"""Sets the ccb2review of this CcbEntity.

        审批对象关联的评审单ID。

        :param ccb2review: The ccb2review of this CcbEntity.
        :type ccb2review: str
        """
        self._ccb2review = ccb2review

    @property
    def co_id(self):
        r"""Gets the co_id of this CcbEntity.

        关联的变更对象ID。

        :return: The co_id of this CcbEntity.
        :rtype: str
        """
        return self._co_id

    @co_id.setter
    def co_id(self, co_id):
        r"""Sets the co_id of this CcbEntity.

        关联的变更对象ID。

        :param co_id: The co_id of this CcbEntity.
        :type co_id: str
        """
        self._co_id = co_id

    @property
    def id(self):
        r"""Gets the id of this CcbEntity.

        审批对象ID。

        :return: The id of this CcbEntity.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CcbEntity.

        审批对象ID。

        :param id: The id of this CcbEntity.
        :type id: str
        """
        self._id = id

    @property
    def owner(self):
        r"""Gets the owner of this CcbEntity.

        :return: The owner of this CcbEntity.
        :rtype: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this CcbEntity.

        :param owner: The owner of this CcbEntity.
        :type owner: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        """
        self._owner = owner

    @property
    def approval_comments(self):
        r"""Gets the approval_comments of this CcbEntity.

        审批意见。

        :return: The approval_comments of this CcbEntity.
        :rtype: str
        """
        return self._approval_comments

    @approval_comments.setter
    def approval_comments(self, approval_comments):
        r"""Sets the approval_comments of this CcbEntity.

        审批意见。

        :param approval_comments: The approval_comments of this CcbEntity.
        :type approval_comments: str
        """
        self._approval_comments = approval_comments

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
        if not isinstance(other, CcbEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
