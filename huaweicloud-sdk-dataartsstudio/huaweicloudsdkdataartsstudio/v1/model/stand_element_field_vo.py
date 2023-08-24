# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StandElementFieldVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'fd_name': 'str',
        'description': 'str',
        'id': 'int',
        'actived': 'bool',
        'required': 'bool',
        'searchable': 'bool',
        'displayed_name': 'str',
        'displayed_name_en': 'str',
        'create_time': 'datetime',
        'update_time': 'datetime',
        'create_by': 'str',
        'update_by': 'str'
    }

    attribute_map = {
        'fd_name': 'fd_name',
        'description': 'description',
        'id': 'id',
        'actived': 'actived',
        'required': 'required',
        'searchable': 'searchable',
        'displayed_name': 'displayed_name',
        'displayed_name_en': 'displayed_name_en',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'create_by': 'create_by',
        'update_by': 'update_by'
    }

    def __init__(self, fd_name=None, description=None, id=None, actived=None, required=None, searchable=None, displayed_name=None, displayed_name_en=None, create_time=None, update_time=None, create_by=None, update_by=None):
        """StandElementFieldVO

        The model defined in huaweicloud sdk

        :param fd_name: 属性名称
        :type fd_name: str
        :param description: 属性描述
        :type description: str
        :param id: ID
        :type id: int
        :param actived: 是否显示，系统默认项必然显示不允许修改
        :type actived: bool
        :param required: 是否必填
        :type required: bool
        :param searchable: 是否可搜索
        :type searchable: bool
        :param displayed_name: 前端展示名
        :type displayed_name: str
        :param displayed_name_en: 前端展示名英文
        :type displayed_name_en: str
        :param create_time: 创建时间
        :type create_time: datetime
        :param update_time: 更新时间
        :type update_time: datetime
        :param create_by: 创建人
        :type create_by: str
        :param update_by: 更新人
        :type update_by: str
        """
        
        

        self._fd_name = None
        self._description = None
        self._id = None
        self._actived = None
        self._required = None
        self._searchable = None
        self._displayed_name = None
        self._displayed_name_en = None
        self._create_time = None
        self._update_time = None
        self._create_by = None
        self._update_by = None
        self.discriminator = None

        self.fd_name = fd_name
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        self.actived = actived
        if required is not None:
            self.required = required
        if searchable is not None:
            self.searchable = searchable
        if displayed_name is not None:
            self.displayed_name = displayed_name
        if displayed_name_en is not None:
            self.displayed_name_en = displayed_name_en
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if create_by is not None:
            self.create_by = create_by
        if update_by is not None:
            self.update_by = update_by

    @property
    def fd_name(self):
        """Gets the fd_name of this StandElementFieldVO.

        属性名称

        :return: The fd_name of this StandElementFieldVO.
        :rtype: str
        """
        return self._fd_name

    @fd_name.setter
    def fd_name(self, fd_name):
        """Sets the fd_name of this StandElementFieldVO.

        属性名称

        :param fd_name: The fd_name of this StandElementFieldVO.
        :type fd_name: str
        """
        self._fd_name = fd_name

    @property
    def description(self):
        """Gets the description of this StandElementFieldVO.

        属性描述

        :return: The description of this StandElementFieldVO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this StandElementFieldVO.

        属性描述

        :param description: The description of this StandElementFieldVO.
        :type description: str
        """
        self._description = description

    @property
    def id(self):
        """Gets the id of this StandElementFieldVO.

        ID

        :return: The id of this StandElementFieldVO.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StandElementFieldVO.

        ID

        :param id: The id of this StandElementFieldVO.
        :type id: int
        """
        self._id = id

    @property
    def actived(self):
        """Gets the actived of this StandElementFieldVO.

        是否显示，系统默认项必然显示不允许修改

        :return: The actived of this StandElementFieldVO.
        :rtype: bool
        """
        return self._actived

    @actived.setter
    def actived(self, actived):
        """Sets the actived of this StandElementFieldVO.

        是否显示，系统默认项必然显示不允许修改

        :param actived: The actived of this StandElementFieldVO.
        :type actived: bool
        """
        self._actived = actived

    @property
    def required(self):
        """Gets the required of this StandElementFieldVO.

        是否必填

        :return: The required of this StandElementFieldVO.
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this StandElementFieldVO.

        是否必填

        :param required: The required of this StandElementFieldVO.
        :type required: bool
        """
        self._required = required

    @property
    def searchable(self):
        """Gets the searchable of this StandElementFieldVO.

        是否可搜索

        :return: The searchable of this StandElementFieldVO.
        :rtype: bool
        """
        return self._searchable

    @searchable.setter
    def searchable(self, searchable):
        """Sets the searchable of this StandElementFieldVO.

        是否可搜索

        :param searchable: The searchable of this StandElementFieldVO.
        :type searchable: bool
        """
        self._searchable = searchable

    @property
    def displayed_name(self):
        """Gets the displayed_name of this StandElementFieldVO.

        前端展示名

        :return: The displayed_name of this StandElementFieldVO.
        :rtype: str
        """
        return self._displayed_name

    @displayed_name.setter
    def displayed_name(self, displayed_name):
        """Sets the displayed_name of this StandElementFieldVO.

        前端展示名

        :param displayed_name: The displayed_name of this StandElementFieldVO.
        :type displayed_name: str
        """
        self._displayed_name = displayed_name

    @property
    def displayed_name_en(self):
        """Gets the displayed_name_en of this StandElementFieldVO.

        前端展示名英文

        :return: The displayed_name_en of this StandElementFieldVO.
        :rtype: str
        """
        return self._displayed_name_en

    @displayed_name_en.setter
    def displayed_name_en(self, displayed_name_en):
        """Sets the displayed_name_en of this StandElementFieldVO.

        前端展示名英文

        :param displayed_name_en: The displayed_name_en of this StandElementFieldVO.
        :type displayed_name_en: str
        """
        self._displayed_name_en = displayed_name_en

    @property
    def create_time(self):
        """Gets the create_time of this StandElementFieldVO.

        创建时间

        :return: The create_time of this StandElementFieldVO.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this StandElementFieldVO.

        创建时间

        :param create_time: The create_time of this StandElementFieldVO.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this StandElementFieldVO.

        更新时间

        :return: The update_time of this StandElementFieldVO.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this StandElementFieldVO.

        更新时间

        :param update_time: The update_time of this StandElementFieldVO.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def create_by(self):
        """Gets the create_by of this StandElementFieldVO.

        创建人

        :return: The create_by of this StandElementFieldVO.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        """Sets the create_by of this StandElementFieldVO.

        创建人

        :param create_by: The create_by of this StandElementFieldVO.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def update_by(self):
        """Gets the update_by of this StandElementFieldVO.

        更新人

        :return: The update_by of this StandElementFieldVO.
        :rtype: str
        """
        return self._update_by

    @update_by.setter
    def update_by(self, update_by):
        """Sets the update_by of this StandElementFieldVO.

        更新人

        :param update_by: The update_by of this StandElementFieldVO.
        :type update_by: str
        """
        self._update_by = update_by

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
        if not isinstance(other, StandElementFieldVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
