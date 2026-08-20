# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StatusEntity:

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
        'belonging': 'str',
        'display_value': 'str',
        'code': 'str',
        'created_by': 'str',
        'created_time': 'str',
        'modified_by': 'str',
        'modified_time': 'str',
        'category_code': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'belonging': 'belonging',
        'display_value': 'display_value',
        'code': 'code',
        'created_by': 'created_by',
        'created_time': 'created_time',
        'modified_by': 'modified_by',
        'modified_time': 'modified_time',
        'category_code': 'category_code'
    }

    def __init__(self, id=None, belonging=None, display_value=None, code=None, created_by=None, created_time=None, modified_by=None, modified_time=None, category_code=None):
        r"""StatusEntity

        The model defined in huaweicloud sdk

        :param id: 状态ID。
        :type id: str
        :param belonging: 工作项的状态属性。
        :type belonging: str
        :param display_value: 状态名。
        :type display_value: str
        :param code: 状态唯一标识。
        :type code: str
        :param created_by: 状态创建人。
        :type created_by: str
        :param created_time: 状态创建时间。
        :type created_time: str
        :param modified_by: 状态修改人。
        :type modified_by: str
        :param modified_time: 状态最近修改时间。
        :type modified_time: str
        :param category_code: 状态被哪些工作项使用。
        :type category_code: list[str]
        """
        
        

        self._id = None
        self._belonging = None
        self._display_value = None
        self._code = None
        self._created_by = None
        self._created_time = None
        self._modified_by = None
        self._modified_time = None
        self._category_code = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if belonging is not None:
            self.belonging = belonging
        if display_value is not None:
            self.display_value = display_value
        if code is not None:
            self.code = code
        if created_by is not None:
            self.created_by = created_by
        if created_time is not None:
            self.created_time = created_time
        if modified_by is not None:
            self.modified_by = modified_by
        if modified_time is not None:
            self.modified_time = modified_time
        if category_code is not None:
            self.category_code = category_code

    @property
    def id(self):
        r"""Gets the id of this StatusEntity.

        状态ID。

        :return: The id of this StatusEntity.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this StatusEntity.

        状态ID。

        :param id: The id of this StatusEntity.
        :type id: str
        """
        self._id = id

    @property
    def belonging(self):
        r"""Gets the belonging of this StatusEntity.

        工作项的状态属性。

        :return: The belonging of this StatusEntity.
        :rtype: str
        """
        return self._belonging

    @belonging.setter
    def belonging(self, belonging):
        r"""Sets the belonging of this StatusEntity.

        工作项的状态属性。

        :param belonging: The belonging of this StatusEntity.
        :type belonging: str
        """
        self._belonging = belonging

    @property
    def display_value(self):
        r"""Gets the display_value of this StatusEntity.

        状态名。

        :return: The display_value of this StatusEntity.
        :rtype: str
        """
        return self._display_value

    @display_value.setter
    def display_value(self, display_value):
        r"""Sets the display_value of this StatusEntity.

        状态名。

        :param display_value: The display_value of this StatusEntity.
        :type display_value: str
        """
        self._display_value = display_value

    @property
    def code(self):
        r"""Gets the code of this StatusEntity.

        状态唯一标识。

        :return: The code of this StatusEntity.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this StatusEntity.

        状态唯一标识。

        :param code: The code of this StatusEntity.
        :type code: str
        """
        self._code = code

    @property
    def created_by(self):
        r"""Gets the created_by of this StatusEntity.

        状态创建人。

        :return: The created_by of this StatusEntity.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        r"""Sets the created_by of this StatusEntity.

        状态创建人。

        :param created_by: The created_by of this StatusEntity.
        :type created_by: str
        """
        self._created_by = created_by

    @property
    def created_time(self):
        r"""Gets the created_time of this StatusEntity.

        状态创建时间。

        :return: The created_time of this StatusEntity.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        r"""Sets the created_time of this StatusEntity.

        状态创建时间。

        :param created_time: The created_time of this StatusEntity.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def modified_by(self):
        r"""Gets the modified_by of this StatusEntity.

        状态修改人。

        :return: The modified_by of this StatusEntity.
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        r"""Sets the modified_by of this StatusEntity.

        状态修改人。

        :param modified_by: The modified_by of this StatusEntity.
        :type modified_by: str
        """
        self._modified_by = modified_by

    @property
    def modified_time(self):
        r"""Gets the modified_time of this StatusEntity.

        状态最近修改时间。

        :return: The modified_time of this StatusEntity.
        :rtype: str
        """
        return self._modified_time

    @modified_time.setter
    def modified_time(self, modified_time):
        r"""Sets the modified_time of this StatusEntity.

        状态最近修改时间。

        :param modified_time: The modified_time of this StatusEntity.
        :type modified_time: str
        """
        self._modified_time = modified_time

    @property
    def category_code(self):
        r"""Gets the category_code of this StatusEntity.

        状态被哪些工作项使用。

        :return: The category_code of this StatusEntity.
        :rtype: list[str]
        """
        return self._category_code

    @category_code.setter
    def category_code(self, category_code):
        r"""Sets the category_code of this StatusEntity.

        状态被哪些工作项使用。

        :param category_code: The category_code of this StatusEntity.
        :type category_code: list[str]
        """
        self._category_code = category_code

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
        if not isinstance(other, StatusEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
