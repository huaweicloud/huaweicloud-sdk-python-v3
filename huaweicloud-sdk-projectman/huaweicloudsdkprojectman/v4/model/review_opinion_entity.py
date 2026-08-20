# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReviewOpinionEntity:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'category': 'str',
        'co_id': 'str',
        'created_by': 'UserEntity',
        'created_date': 'str',
        'curr_owner': 'UserEntity',
        'id': 'str',
        'modified_date': 'str',
        'review_comments': 'str'
    }

    attribute_map = {
        'category': 'category',
        'co_id': 'co_id',
        'created_by': 'created_by',
        'created_date': 'created_date',
        'curr_owner': 'curr_owner',
        'id': 'id',
        'modified_date': 'modified_date',
        'review_comments': 'review_comments'
    }

    def __init__(self, category=None, co_id=None, created_by=None, created_date=None, curr_owner=None, id=None, modified_date=None, review_comments=None):
        r"""ReviewOpinionEntity

        The model defined in huaweicloud sdk

        :param category: 评审意见对象类型，固定为Opinion。
        :type category: str
        :param co_id: 评审意见对象关联的变更对象ID。
        :type co_id: str
        :param created_by: 
        :type created_by: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        :param created_date: 评审意见创建时间。
        :type created_date: str
        :param curr_owner: 
        :type curr_owner: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        :param id: 评审意见对象ID。
        :type id: str
        :param modified_date: 评审意见最后修改时间。
        :type modified_date: str
        :param review_comments: 评审意见。
        :type review_comments: str
        """
        
        

        self._category = None
        self._co_id = None
        self._created_by = None
        self._created_date = None
        self._curr_owner = None
        self._id = None
        self._modified_date = None
        self._review_comments = None
        self.discriminator = None

        if category is not None:
            self.category = category
        if co_id is not None:
            self.co_id = co_id
        if created_by is not None:
            self.created_by = created_by
        if created_date is not None:
            self.created_date = created_date
        if curr_owner is not None:
            self.curr_owner = curr_owner
        if id is not None:
            self.id = id
        if modified_date is not None:
            self.modified_date = modified_date
        if review_comments is not None:
            self.review_comments = review_comments

    @property
    def category(self):
        r"""Gets the category of this ReviewOpinionEntity.

        评审意见对象类型，固定为Opinion。

        :return: The category of this ReviewOpinionEntity.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ReviewOpinionEntity.

        评审意见对象类型，固定为Opinion。

        :param category: The category of this ReviewOpinionEntity.
        :type category: str
        """
        self._category = category

    @property
    def co_id(self):
        r"""Gets the co_id of this ReviewOpinionEntity.

        评审意见对象关联的变更对象ID。

        :return: The co_id of this ReviewOpinionEntity.
        :rtype: str
        """
        return self._co_id

    @co_id.setter
    def co_id(self, co_id):
        r"""Sets the co_id of this ReviewOpinionEntity.

        评审意见对象关联的变更对象ID。

        :param co_id: The co_id of this ReviewOpinionEntity.
        :type co_id: str
        """
        self._co_id = co_id

    @property
    def created_by(self):
        r"""Gets the created_by of this ReviewOpinionEntity.

        :return: The created_by of this ReviewOpinionEntity.
        :rtype: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        r"""Sets the created_by of this ReviewOpinionEntity.

        :param created_by: The created_by of this ReviewOpinionEntity.
        :type created_by: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        """
        self._created_by = created_by

    @property
    def created_date(self):
        r"""Gets the created_date of this ReviewOpinionEntity.

        评审意见创建时间。

        :return: The created_date of this ReviewOpinionEntity.
        :rtype: str
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        r"""Sets the created_date of this ReviewOpinionEntity.

        评审意见创建时间。

        :param created_date: The created_date of this ReviewOpinionEntity.
        :type created_date: str
        """
        self._created_date = created_date

    @property
    def curr_owner(self):
        r"""Gets the curr_owner of this ReviewOpinionEntity.

        :return: The curr_owner of this ReviewOpinionEntity.
        :rtype: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        """
        return self._curr_owner

    @curr_owner.setter
    def curr_owner(self, curr_owner):
        r"""Sets the curr_owner of this ReviewOpinionEntity.

        :param curr_owner: The curr_owner of this ReviewOpinionEntity.
        :type curr_owner: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        """
        self._curr_owner = curr_owner

    @property
    def id(self):
        r"""Gets the id of this ReviewOpinionEntity.

        评审意见对象ID。

        :return: The id of this ReviewOpinionEntity.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ReviewOpinionEntity.

        评审意见对象ID。

        :param id: The id of this ReviewOpinionEntity.
        :type id: str
        """
        self._id = id

    @property
    def modified_date(self):
        r"""Gets the modified_date of this ReviewOpinionEntity.

        评审意见最后修改时间。

        :return: The modified_date of this ReviewOpinionEntity.
        :rtype: str
        """
        return self._modified_date

    @modified_date.setter
    def modified_date(self, modified_date):
        r"""Sets the modified_date of this ReviewOpinionEntity.

        评审意见最后修改时间。

        :param modified_date: The modified_date of this ReviewOpinionEntity.
        :type modified_date: str
        """
        self._modified_date = modified_date

    @property
    def review_comments(self):
        r"""Gets the review_comments of this ReviewOpinionEntity.

        评审意见。

        :return: The review_comments of this ReviewOpinionEntity.
        :rtype: str
        """
        return self._review_comments

    @review_comments.setter
    def review_comments(self, review_comments):
        r"""Sets the review_comments of this ReviewOpinionEntity.

        评审意见。

        :param review_comments: The review_comments of this ReviewOpinionEntity.
        :type review_comments: str
        """
        self._review_comments = review_comments

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
        if not isinstance(other, ReviewOpinionEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
