# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FeatureSetOpenApiVO:

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
        'number': 'str',
        'parent_id': 'str',
        'title': 'str',
        'position_float': 'float',
        'created_by': 'UserEntity',
        'modified_by': 'UserEntity',
        'created_date': 'str',
        'modified_date': 'str',
        'child_fs': 'list[FeatureSetOpenApiVO]'
    }

    attribute_map = {
        'id': 'id',
        'number': 'number',
        'parent_id': 'parent_id',
        'title': 'title',
        'position_float': 'position_float',
        'created_by': 'created_by',
        'modified_by': 'modified_by',
        'created_date': 'created_date',
        'modified_date': 'modified_date',
        'child_fs': 'child_fs'
    }

    def __init__(self, id=None, number=None, parent_id=None, title=None, position_float=None, created_by=None, modified_by=None, created_date=None, modified_date=None, child_fs=None):
        r"""FeatureSetOpenApiVO

        The model defined in huaweicloud sdk

        :param id: 特性集ID
        :type id: str
        :param number: 编号
        :type number: str
        :param parent_id: 父特性集ID
        :type parent_id: str
        :param title: 标题
        :type title: str
        :param position_float: 位置信息
        :type position_float: float
        :param created_by: 
        :type created_by: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        :param modified_by: 
        :type modified_by: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        :param created_date: **参数解释**： 特性集创建时间的时间戳。 **取值范围**： 不涉及。
        :type created_date: str
        :param modified_date: **参数解释**： 特性集修改时间的时间戳。 **取值范围**： 不涉及。
        :type modified_date: str
        :param child_fs: 子特性集
        :type child_fs: list[:class:`huaweicloudsdkprojectman.v4.FeatureSetOpenApiVO`]
        """
        
        

        self._id = None
        self._number = None
        self._parent_id = None
        self._title = None
        self._position_float = None
        self._created_by = None
        self._modified_by = None
        self._created_date = None
        self._modified_date = None
        self._child_fs = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if number is not None:
            self.number = number
        if parent_id is not None:
            self.parent_id = parent_id
        if title is not None:
            self.title = title
        if position_float is not None:
            self.position_float = position_float
        if created_by is not None:
            self.created_by = created_by
        if modified_by is not None:
            self.modified_by = modified_by
        if created_date is not None:
            self.created_date = created_date
        if modified_date is not None:
            self.modified_date = modified_date
        if child_fs is not None:
            self.child_fs = child_fs

    @property
    def id(self):
        r"""Gets the id of this FeatureSetOpenApiVO.

        特性集ID

        :return: The id of this FeatureSetOpenApiVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this FeatureSetOpenApiVO.

        特性集ID

        :param id: The id of this FeatureSetOpenApiVO.
        :type id: str
        """
        self._id = id

    @property
    def number(self):
        r"""Gets the number of this FeatureSetOpenApiVO.

        编号

        :return: The number of this FeatureSetOpenApiVO.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        r"""Sets the number of this FeatureSetOpenApiVO.

        编号

        :param number: The number of this FeatureSetOpenApiVO.
        :type number: str
        """
        self._number = number

    @property
    def parent_id(self):
        r"""Gets the parent_id of this FeatureSetOpenApiVO.

        父特性集ID

        :return: The parent_id of this FeatureSetOpenApiVO.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        r"""Sets the parent_id of this FeatureSetOpenApiVO.

        父特性集ID

        :param parent_id: The parent_id of this FeatureSetOpenApiVO.
        :type parent_id: str
        """
        self._parent_id = parent_id

    @property
    def title(self):
        r"""Gets the title of this FeatureSetOpenApiVO.

        标题

        :return: The title of this FeatureSetOpenApiVO.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this FeatureSetOpenApiVO.

        标题

        :param title: The title of this FeatureSetOpenApiVO.
        :type title: str
        """
        self._title = title

    @property
    def position_float(self):
        r"""Gets the position_float of this FeatureSetOpenApiVO.

        位置信息

        :return: The position_float of this FeatureSetOpenApiVO.
        :rtype: float
        """
        return self._position_float

    @position_float.setter
    def position_float(self, position_float):
        r"""Sets the position_float of this FeatureSetOpenApiVO.

        位置信息

        :param position_float: The position_float of this FeatureSetOpenApiVO.
        :type position_float: float
        """
        self._position_float = position_float

    @property
    def created_by(self):
        r"""Gets the created_by of this FeatureSetOpenApiVO.

        :return: The created_by of this FeatureSetOpenApiVO.
        :rtype: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        r"""Sets the created_by of this FeatureSetOpenApiVO.

        :param created_by: The created_by of this FeatureSetOpenApiVO.
        :type created_by: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        """
        self._created_by = created_by

    @property
    def modified_by(self):
        r"""Gets the modified_by of this FeatureSetOpenApiVO.

        :return: The modified_by of this FeatureSetOpenApiVO.
        :rtype: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        r"""Sets the modified_by of this FeatureSetOpenApiVO.

        :param modified_by: The modified_by of this FeatureSetOpenApiVO.
        :type modified_by: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        """
        self._modified_by = modified_by

    @property
    def created_date(self):
        r"""Gets the created_date of this FeatureSetOpenApiVO.

        **参数解释**： 特性集创建时间的时间戳。 **取值范围**： 不涉及。

        :return: The created_date of this FeatureSetOpenApiVO.
        :rtype: str
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        r"""Sets the created_date of this FeatureSetOpenApiVO.

        **参数解释**： 特性集创建时间的时间戳。 **取值范围**： 不涉及。

        :param created_date: The created_date of this FeatureSetOpenApiVO.
        :type created_date: str
        """
        self._created_date = created_date

    @property
    def modified_date(self):
        r"""Gets the modified_date of this FeatureSetOpenApiVO.

        **参数解释**： 特性集修改时间的时间戳。 **取值范围**： 不涉及。

        :return: The modified_date of this FeatureSetOpenApiVO.
        :rtype: str
        """
        return self._modified_date

    @modified_date.setter
    def modified_date(self, modified_date):
        r"""Sets the modified_date of this FeatureSetOpenApiVO.

        **参数解释**： 特性集修改时间的时间戳。 **取值范围**： 不涉及。

        :param modified_date: The modified_date of this FeatureSetOpenApiVO.
        :type modified_date: str
        """
        self._modified_date = modified_date

    @property
    def child_fs(self):
        r"""Gets the child_fs of this FeatureSetOpenApiVO.

        子特性集

        :return: The child_fs of this FeatureSetOpenApiVO.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.FeatureSetOpenApiVO`]
        """
        return self._child_fs

    @child_fs.setter
    def child_fs(self, child_fs):
        r"""Sets the child_fs of this FeatureSetOpenApiVO.

        子特性集

        :param child_fs: The child_fs of this FeatureSetOpenApiVO.
        :type child_fs: list[:class:`huaweicloudsdkprojectman.v4.FeatureSetOpenApiVO`]
        """
        self._child_fs = child_fs

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
        if not isinstance(other, FeatureSetOpenApiVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
