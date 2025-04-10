# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListServerAzInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'availability_zone_id': 'str',
        'type': 'str',
        'mode': 'str',
        'public_border_group': 'str',
        'alias': 'str',
        'az_group_ids': 'list[str]',
        'category': 'int'
    }

    attribute_map = {
        'availability_zone_id': 'availability_zone_id',
        'type': 'type',
        'mode': 'mode',
        'public_border_group': 'public_border_group',
        'alias': 'alias',
        'az_group_ids': 'az_group_ids',
        'category': 'category'
    }

    def __init__(self, availability_zone_id=None, type=None, mode=None, public_border_group=None, alias=None, az_group_ids=None, category=None):
        r"""ListServerAzInfo

        The model defined in huaweicloud sdk

        :param availability_zone_id: 可用区ID
        :type availability_zone_id: str
        :param type: 可用区类型
        :type type: str
        :param mode: 可用区模式
        :type mode: str
        :param public_border_group: 公网边界组，网络eip类别标识，用于查找az可用的eip池
        :type public_border_group: str
        :param alias: 可用区别名
        :type alias: str
        :param az_group_ids: 可用区所属的AZGroup列表
        :type az_group_ids: list[str]
        :param category: 可用区类型对应的子类型
        :type category: int
        """
        
        

        self._availability_zone_id = None
        self._type = None
        self._mode = None
        self._public_border_group = None
        self._alias = None
        self._az_group_ids = None
        self._category = None
        self.discriminator = None

        self.availability_zone_id = availability_zone_id
        if type is not None:
            self.type = type
        if mode is not None:
            self.mode = mode
        if public_border_group is not None:
            self.public_border_group = public_border_group
        if alias is not None:
            self.alias = alias
        if az_group_ids is not None:
            self.az_group_ids = az_group_ids
        if category is not None:
            self.category = category

    @property
    def availability_zone_id(self):
        r"""Gets the availability_zone_id of this ListServerAzInfo.

        可用区ID

        :return: The availability_zone_id of this ListServerAzInfo.
        :rtype: str
        """
        return self._availability_zone_id

    @availability_zone_id.setter
    def availability_zone_id(self, availability_zone_id):
        r"""Sets the availability_zone_id of this ListServerAzInfo.

        可用区ID

        :param availability_zone_id: The availability_zone_id of this ListServerAzInfo.
        :type availability_zone_id: str
        """
        self._availability_zone_id = availability_zone_id

    @property
    def type(self):
        r"""Gets the type of this ListServerAzInfo.

        可用区类型

        :return: The type of this ListServerAzInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListServerAzInfo.

        可用区类型

        :param type: The type of this ListServerAzInfo.
        :type type: str
        """
        self._type = type

    @property
    def mode(self):
        r"""Gets the mode of this ListServerAzInfo.

        可用区模式

        :return: The mode of this ListServerAzInfo.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this ListServerAzInfo.

        可用区模式

        :param mode: The mode of this ListServerAzInfo.
        :type mode: str
        """
        self._mode = mode

    @property
    def public_border_group(self):
        r"""Gets the public_border_group of this ListServerAzInfo.

        公网边界组，网络eip类别标识，用于查找az可用的eip池

        :return: The public_border_group of this ListServerAzInfo.
        :rtype: str
        """
        return self._public_border_group

    @public_border_group.setter
    def public_border_group(self, public_border_group):
        r"""Sets the public_border_group of this ListServerAzInfo.

        公网边界组，网络eip类别标识，用于查找az可用的eip池

        :param public_border_group: The public_border_group of this ListServerAzInfo.
        :type public_border_group: str
        """
        self._public_border_group = public_border_group

    @property
    def alias(self):
        r"""Gets the alias of this ListServerAzInfo.

        可用区别名

        :return: The alias of this ListServerAzInfo.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        r"""Sets the alias of this ListServerAzInfo.

        可用区别名

        :param alias: The alias of this ListServerAzInfo.
        :type alias: str
        """
        self._alias = alias

    @property
    def az_group_ids(self):
        r"""Gets the az_group_ids of this ListServerAzInfo.

        可用区所属的AZGroup列表

        :return: The az_group_ids of this ListServerAzInfo.
        :rtype: list[str]
        """
        return self._az_group_ids

    @az_group_ids.setter
    def az_group_ids(self, az_group_ids):
        r"""Sets the az_group_ids of this ListServerAzInfo.

        可用区所属的AZGroup列表

        :param az_group_ids: The az_group_ids of this ListServerAzInfo.
        :type az_group_ids: list[str]
        """
        self._az_group_ids = az_group_ids

    @property
    def category(self):
        r"""Gets the category of this ListServerAzInfo.

        可用区类型对应的子类型

        :return: The category of this ListServerAzInfo.
        :rtype: int
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ListServerAzInfo.

        可用区类型对应的子类型

        :param category: The category of this ListServerAzInfo.
        :type category: int
        """
        self._category = category

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
        if not isinstance(other, ListServerAzInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
