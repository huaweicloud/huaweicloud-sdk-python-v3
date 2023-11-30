# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DimensionHierarchiesVO:

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
        'name': 'str',
        'attrs': 'list[HierarchiesAttrVO]',
        'create_time': 'datetime',
        'update_time': 'datetime',
        'create_by': 'str',
        'update_by': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'attrs': 'attrs',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'create_by': 'create_by',
        'update_by': 'update_by'
    }

    def __init__(self, id=None, name=None, attrs=None, create_time=None, update_time=None, create_by=None, update_by=None):
        """DimensionHierarchiesVO

        The model defined in huaweicloud sdk

        :param id: 编码
        :type id: int
        :param name: 层级名称
        :type name: str
        :param attrs: 
        :type attrs: list[:class:`huaweicloudsdkdataartsstudio.v1.HierarchiesAttrVO`]
        :param create_time: 创建时间
        :type create_time: datetime
        :param update_time: 更新时间
        :type update_time: datetime
        :param create_by: 创建人
        :type create_by: str
        :param update_by: 更新人
        :type update_by: str
        """
        
        

        self._id = None
        self._name = None
        self._attrs = None
        self._create_time = None
        self._update_time = None
        self._create_by = None
        self._update_by = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if attrs is not None:
            self.attrs = attrs
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if create_by is not None:
            self.create_by = create_by
        if update_by is not None:
            self.update_by = update_by

    @property
    def id(self):
        """Gets the id of this DimensionHierarchiesVO.

        编码

        :return: The id of this DimensionHierarchiesVO.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DimensionHierarchiesVO.

        编码

        :param id: The id of this DimensionHierarchiesVO.
        :type id: int
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this DimensionHierarchiesVO.

        层级名称

        :return: The name of this DimensionHierarchiesVO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DimensionHierarchiesVO.

        层级名称

        :param name: The name of this DimensionHierarchiesVO.
        :type name: str
        """
        self._name = name

    @property
    def attrs(self):
        """Gets the attrs of this DimensionHierarchiesVO.

        :return: The attrs of this DimensionHierarchiesVO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.HierarchiesAttrVO`]
        """
        return self._attrs

    @attrs.setter
    def attrs(self, attrs):
        """Sets the attrs of this DimensionHierarchiesVO.

        :param attrs: The attrs of this DimensionHierarchiesVO.
        :type attrs: list[:class:`huaweicloudsdkdataartsstudio.v1.HierarchiesAttrVO`]
        """
        self._attrs = attrs

    @property
    def create_time(self):
        """Gets the create_time of this DimensionHierarchiesVO.

        创建时间

        :return: The create_time of this DimensionHierarchiesVO.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this DimensionHierarchiesVO.

        创建时间

        :param create_time: The create_time of this DimensionHierarchiesVO.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this DimensionHierarchiesVO.

        更新时间

        :return: The update_time of this DimensionHierarchiesVO.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this DimensionHierarchiesVO.

        更新时间

        :param update_time: The update_time of this DimensionHierarchiesVO.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def create_by(self):
        """Gets the create_by of this DimensionHierarchiesVO.

        创建人

        :return: The create_by of this DimensionHierarchiesVO.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        """Sets the create_by of this DimensionHierarchiesVO.

        创建人

        :param create_by: The create_by of this DimensionHierarchiesVO.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def update_by(self):
        """Gets the update_by of this DimensionHierarchiesVO.

        更新人

        :return: The update_by of this DimensionHierarchiesVO.
        :rtype: str
        """
        return self._update_by

    @update_by.setter
    def update_by(self, update_by):
        """Sets the update_by of this DimensionHierarchiesVO.

        更新人

        :param update_by: The update_by of this DimensionHierarchiesVO.
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
        if not isinstance(other, DimensionHierarchiesVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
