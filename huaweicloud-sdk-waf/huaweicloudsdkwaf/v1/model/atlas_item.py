# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AtlasItem:

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
        'name': 'str',
        'type': 'int',
        'description': 'str',
        'create_time': 'int',
        'update_time': 'int',
        'image_count': 'int',
        'referenced_rules': 'list[ReferencedRule]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'description': 'description',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'image_count': 'image_count',
        'referenced_rules': 'referenced_rules'
    }

    def __init__(self, id=None, name=None, type=None, description=None, create_time=None, update_time=None, image_count=None, referenced_rules=None):
        r"""AtlasItem

        The model defined in huaweicloud sdk

        :param id: 图库ID
        :type id: str
        :param name: 图库名称
        :type name: str
        :param type: 图库类型 0&#x3D;白库（豁免/可信样本） / 1&#x3D;黑库（敏感/拦截样本）
        :type type: int
        :param description: 图库描述
        :type description: str
        :param create_time: 创建时间（毫秒）
        :type create_time: int
        :param update_time: 更新时间（毫秒）
        :type update_time: int
        :param image_count: 图库下已加入（status≥0）且未删除的图片数量；创建返回 0
        :type image_count: int
        :param referenced_rules: 引用此图库的规则列表
        :type referenced_rules: list[:class:`huaweicloudsdkwaf.v1.ReferencedRule`]
        """
        
        

        self._id = None
        self._name = None
        self._type = None
        self._description = None
        self._create_time = None
        self._update_time = None
        self._image_count = None
        self._referenced_rules = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if description is not None:
            self.description = description
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if image_count is not None:
            self.image_count = image_count
        if referenced_rules is not None:
            self.referenced_rules = referenced_rules

    @property
    def id(self):
        r"""Gets the id of this AtlasItem.

        图库ID

        :return: The id of this AtlasItem.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AtlasItem.

        图库ID

        :param id: The id of this AtlasItem.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this AtlasItem.

        图库名称

        :return: The name of this AtlasItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AtlasItem.

        图库名称

        :param name: The name of this AtlasItem.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this AtlasItem.

        图库类型 0=白库（豁免/可信样本） / 1=黑库（敏感/拦截样本）

        :return: The type of this AtlasItem.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this AtlasItem.

        图库类型 0=白库（豁免/可信样本） / 1=黑库（敏感/拦截样本）

        :param type: The type of this AtlasItem.
        :type type: int
        """
        self._type = type

    @property
    def description(self):
        r"""Gets the description of this AtlasItem.

        图库描述

        :return: The description of this AtlasItem.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this AtlasItem.

        图库描述

        :param description: The description of this AtlasItem.
        :type description: str
        """
        self._description = description

    @property
    def create_time(self):
        r"""Gets the create_time of this AtlasItem.

        创建时间（毫秒）

        :return: The create_time of this AtlasItem.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this AtlasItem.

        创建时间（毫秒）

        :param create_time: The create_time of this AtlasItem.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this AtlasItem.

        更新时间（毫秒）

        :return: The update_time of this AtlasItem.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this AtlasItem.

        更新时间（毫秒）

        :param update_time: The update_time of this AtlasItem.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def image_count(self):
        r"""Gets the image_count of this AtlasItem.

        图库下已加入（status≥0）且未删除的图片数量；创建返回 0

        :return: The image_count of this AtlasItem.
        :rtype: int
        """
        return self._image_count

    @image_count.setter
    def image_count(self, image_count):
        r"""Sets the image_count of this AtlasItem.

        图库下已加入（status≥0）且未删除的图片数量；创建返回 0

        :param image_count: The image_count of this AtlasItem.
        :type image_count: int
        """
        self._image_count = image_count

    @property
    def referenced_rules(self):
        r"""Gets the referenced_rules of this AtlasItem.

        引用此图库的规则列表

        :return: The referenced_rules of this AtlasItem.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.ReferencedRule`]
        """
        return self._referenced_rules

    @referenced_rules.setter
    def referenced_rules(self, referenced_rules):
        r"""Sets the referenced_rules of this AtlasItem.

        引用此图库的规则列表

        :param referenced_rules: The referenced_rules of this AtlasItem.
        :type referenced_rules: list[:class:`huaweicloudsdkwaf.v1.ReferencedRule`]
        """
        self._referenced_rules = referenced_rules

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
        if not isinstance(other, AtlasItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
