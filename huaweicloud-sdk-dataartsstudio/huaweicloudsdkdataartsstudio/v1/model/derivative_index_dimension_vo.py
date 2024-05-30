# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DerivativeIndexDimensionVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_id': 'str',
        'role': 'str',
        'dimension_id': 'str',
        'hierarchies_id': 'str',
        'ordinal': 'int',
        'group_name': 'str',
        'group_code': 'str',
        'biz_type': 'BizTypeEnum',
        'hierarchies': 'list[DimensionHierarchiesVO]',
        'l1': 'str',
        'l2': 'str',
        'l3': 'str',
        'l1_id': 'str',
        'l2_id': 'str',
        'l3_id': 'str',
        'dw_type': 'str',
        'id': 'str'
    }

    attribute_map = {
        'group_id': 'group_id',
        'role': 'role',
        'dimension_id': 'dimension_id',
        'hierarchies_id': 'hierarchies_id',
        'ordinal': 'ordinal',
        'group_name': 'group_name',
        'group_code': 'group_code',
        'biz_type': 'biz_type',
        'hierarchies': 'hierarchies',
        'l1': 'l1',
        'l2': 'l2',
        'l3': 'l3',
        'l1_id': 'l1_id',
        'l2_id': 'l2_id',
        'l3_id': 'l3_id',
        'dw_type': 'dw_type',
        'id': 'id'
    }

    def __init__(self, group_id=None, role=None, dimension_id=None, hierarchies_id=None, ordinal=None, group_name=None, group_code=None, biz_type=None, hierarchies=None, l1=None, l2=None, l3=None, l1_id=None, l2_id=None, l3_id=None, dw_type=None, id=None):
        """DerivativeIndexDimensionVO

        The model defined in huaweicloud sdk

        :param group_id: 维度分组ID。
        :type group_id: str
        :param role: 维度角色。
        :type role: str
        :param dimension_id: 维度ID，填写String类型替代Long类型。
        :type dimension_id: str
        :param hierarchies_id: 维度层级ID，填写String类型替代Long类型。
        :type hierarchies_id: str
        :param ordinal: 序号，只读。
        :type ordinal: int
        :param group_name: 维度分组名称。
        :type group_name: str
        :param group_code: 维度分组编码。
        :type group_code: str
        :param biz_type: 
        :type biz_type: :class:`huaweicloudsdkdataartsstudio.v1.BizTypeEnum`
        :param hierarchies: 层级属性，只读。
        :type hierarchies: list[:class:`huaweicloudsdkdataartsstudio.v1.DimensionHierarchiesVO`]
        :param l1: 主题域分组中文名，只读，创建和更新时无需填写。
        :type l1: str
        :param l2: 主题域中文名，只读，创建和更新时无需填写。
        :type l2: str
        :param l3: 业务对象中文名，只读，创建和更新时无需填写。
        :type l3: str
        :param l1_id: 主题域分组ID，只读，填写String类型替代Long类型。
        :type l1_id: str
        :param l2_id: 主题域ID，只读，创建和更新时无需填写。
        :type l2_id: str
        :param l3_id: 业务对象ID，只读，填写String类型替代Long类型。
        :type l3_id: str
        :param dw_type: 数据连接类型。
        :type dw_type: str
        :param id: 层级的ID，只读，填写String类型替代Long类型。
        :type id: str
        """
        
        

        self._group_id = None
        self._role = None
        self._dimension_id = None
        self._hierarchies_id = None
        self._ordinal = None
        self._group_name = None
        self._group_code = None
        self._biz_type = None
        self._hierarchies = None
        self._l1 = None
        self._l2 = None
        self._l3 = None
        self._l1_id = None
        self._l2_id = None
        self._l3_id = None
        self._dw_type = None
        self._id = None
        self.discriminator = None

        self.group_id = group_id
        if role is not None:
            self.role = role
        if dimension_id is not None:
            self.dimension_id = dimension_id
        if hierarchies_id is not None:
            self.hierarchies_id = hierarchies_id
        if ordinal is not None:
            self.ordinal = ordinal
        if group_name is not None:
            self.group_name = group_name
        if group_code is not None:
            self.group_code = group_code
        self.biz_type = biz_type
        if hierarchies is not None:
            self.hierarchies = hierarchies
        if l1 is not None:
            self.l1 = l1
        if l2 is not None:
            self.l2 = l2
        if l3 is not None:
            self.l3 = l3
        if l1_id is not None:
            self.l1_id = l1_id
        if l2_id is not None:
            self.l2_id = l2_id
        if l3_id is not None:
            self.l3_id = l3_id
        if dw_type is not None:
            self.dw_type = dw_type
        if id is not None:
            self.id = id

    @property
    def group_id(self):
        """Gets the group_id of this DerivativeIndexDimensionVO.

        维度分组ID。

        :return: The group_id of this DerivativeIndexDimensionVO.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this DerivativeIndexDimensionVO.

        维度分组ID。

        :param group_id: The group_id of this DerivativeIndexDimensionVO.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def role(self):
        """Gets the role of this DerivativeIndexDimensionVO.

        维度角色。

        :return: The role of this DerivativeIndexDimensionVO.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this DerivativeIndexDimensionVO.

        维度角色。

        :param role: The role of this DerivativeIndexDimensionVO.
        :type role: str
        """
        self._role = role

    @property
    def dimension_id(self):
        """Gets the dimension_id of this DerivativeIndexDimensionVO.

        维度ID，填写String类型替代Long类型。

        :return: The dimension_id of this DerivativeIndexDimensionVO.
        :rtype: str
        """
        return self._dimension_id

    @dimension_id.setter
    def dimension_id(self, dimension_id):
        """Sets the dimension_id of this DerivativeIndexDimensionVO.

        维度ID，填写String类型替代Long类型。

        :param dimension_id: The dimension_id of this DerivativeIndexDimensionVO.
        :type dimension_id: str
        """
        self._dimension_id = dimension_id

    @property
    def hierarchies_id(self):
        """Gets the hierarchies_id of this DerivativeIndexDimensionVO.

        维度层级ID，填写String类型替代Long类型。

        :return: The hierarchies_id of this DerivativeIndexDimensionVO.
        :rtype: str
        """
        return self._hierarchies_id

    @hierarchies_id.setter
    def hierarchies_id(self, hierarchies_id):
        """Sets the hierarchies_id of this DerivativeIndexDimensionVO.

        维度层级ID，填写String类型替代Long类型。

        :param hierarchies_id: The hierarchies_id of this DerivativeIndexDimensionVO.
        :type hierarchies_id: str
        """
        self._hierarchies_id = hierarchies_id

    @property
    def ordinal(self):
        """Gets the ordinal of this DerivativeIndexDimensionVO.

        序号，只读。

        :return: The ordinal of this DerivativeIndexDimensionVO.
        :rtype: int
        """
        return self._ordinal

    @ordinal.setter
    def ordinal(self, ordinal):
        """Sets the ordinal of this DerivativeIndexDimensionVO.

        序号，只读。

        :param ordinal: The ordinal of this DerivativeIndexDimensionVO.
        :type ordinal: int
        """
        self._ordinal = ordinal

    @property
    def group_name(self):
        """Gets the group_name of this DerivativeIndexDimensionVO.

        维度分组名称。

        :return: The group_name of this DerivativeIndexDimensionVO.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this DerivativeIndexDimensionVO.

        维度分组名称。

        :param group_name: The group_name of this DerivativeIndexDimensionVO.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def group_code(self):
        """Gets the group_code of this DerivativeIndexDimensionVO.

        维度分组编码。

        :return: The group_code of this DerivativeIndexDimensionVO.
        :rtype: str
        """
        return self._group_code

    @group_code.setter
    def group_code(self, group_code):
        """Sets the group_code of this DerivativeIndexDimensionVO.

        维度分组编码。

        :param group_code: The group_code of this DerivativeIndexDimensionVO.
        :type group_code: str
        """
        self._group_code = group_code

    @property
    def biz_type(self):
        """Gets the biz_type of this DerivativeIndexDimensionVO.

        :return: The biz_type of this DerivativeIndexDimensionVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.BizTypeEnum`
        """
        return self._biz_type

    @biz_type.setter
    def biz_type(self, biz_type):
        """Sets the biz_type of this DerivativeIndexDimensionVO.

        :param biz_type: The biz_type of this DerivativeIndexDimensionVO.
        :type biz_type: :class:`huaweicloudsdkdataartsstudio.v1.BizTypeEnum`
        """
        self._biz_type = biz_type

    @property
    def hierarchies(self):
        """Gets the hierarchies of this DerivativeIndexDimensionVO.

        层级属性，只读。

        :return: The hierarchies of this DerivativeIndexDimensionVO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.DimensionHierarchiesVO`]
        """
        return self._hierarchies

    @hierarchies.setter
    def hierarchies(self, hierarchies):
        """Sets the hierarchies of this DerivativeIndexDimensionVO.

        层级属性，只读。

        :param hierarchies: The hierarchies of this DerivativeIndexDimensionVO.
        :type hierarchies: list[:class:`huaweicloudsdkdataartsstudio.v1.DimensionHierarchiesVO`]
        """
        self._hierarchies = hierarchies

    @property
    def l1(self):
        """Gets the l1 of this DerivativeIndexDimensionVO.

        主题域分组中文名，只读，创建和更新时无需填写。

        :return: The l1 of this DerivativeIndexDimensionVO.
        :rtype: str
        """
        return self._l1

    @l1.setter
    def l1(self, l1):
        """Sets the l1 of this DerivativeIndexDimensionVO.

        主题域分组中文名，只读，创建和更新时无需填写。

        :param l1: The l1 of this DerivativeIndexDimensionVO.
        :type l1: str
        """
        self._l1 = l1

    @property
    def l2(self):
        """Gets the l2 of this DerivativeIndexDimensionVO.

        主题域中文名，只读，创建和更新时无需填写。

        :return: The l2 of this DerivativeIndexDimensionVO.
        :rtype: str
        """
        return self._l2

    @l2.setter
    def l2(self, l2):
        """Sets the l2 of this DerivativeIndexDimensionVO.

        主题域中文名，只读，创建和更新时无需填写。

        :param l2: The l2 of this DerivativeIndexDimensionVO.
        :type l2: str
        """
        self._l2 = l2

    @property
    def l3(self):
        """Gets the l3 of this DerivativeIndexDimensionVO.

        业务对象中文名，只读，创建和更新时无需填写。

        :return: The l3 of this DerivativeIndexDimensionVO.
        :rtype: str
        """
        return self._l3

    @l3.setter
    def l3(self, l3):
        """Sets the l3 of this DerivativeIndexDimensionVO.

        业务对象中文名，只读，创建和更新时无需填写。

        :param l3: The l3 of this DerivativeIndexDimensionVO.
        :type l3: str
        """
        self._l3 = l3

    @property
    def l1_id(self):
        """Gets the l1_id of this DerivativeIndexDimensionVO.

        主题域分组ID，只读，填写String类型替代Long类型。

        :return: The l1_id of this DerivativeIndexDimensionVO.
        :rtype: str
        """
        return self._l1_id

    @l1_id.setter
    def l1_id(self, l1_id):
        """Sets the l1_id of this DerivativeIndexDimensionVO.

        主题域分组ID，只读，填写String类型替代Long类型。

        :param l1_id: The l1_id of this DerivativeIndexDimensionVO.
        :type l1_id: str
        """
        self._l1_id = l1_id

    @property
    def l2_id(self):
        """Gets the l2_id of this DerivativeIndexDimensionVO.

        主题域ID，只读，创建和更新时无需填写。

        :return: The l2_id of this DerivativeIndexDimensionVO.
        :rtype: str
        """
        return self._l2_id

    @l2_id.setter
    def l2_id(self, l2_id):
        """Sets the l2_id of this DerivativeIndexDimensionVO.

        主题域ID，只读，创建和更新时无需填写。

        :param l2_id: The l2_id of this DerivativeIndexDimensionVO.
        :type l2_id: str
        """
        self._l2_id = l2_id

    @property
    def l3_id(self):
        """Gets the l3_id of this DerivativeIndexDimensionVO.

        业务对象ID，只读，填写String类型替代Long类型。

        :return: The l3_id of this DerivativeIndexDimensionVO.
        :rtype: str
        """
        return self._l3_id

    @l3_id.setter
    def l3_id(self, l3_id):
        """Sets the l3_id of this DerivativeIndexDimensionVO.

        业务对象ID，只读，填写String类型替代Long类型。

        :param l3_id: The l3_id of this DerivativeIndexDimensionVO.
        :type l3_id: str
        """
        self._l3_id = l3_id

    @property
    def dw_type(self):
        """Gets the dw_type of this DerivativeIndexDimensionVO.

        数据连接类型。

        :return: The dw_type of this DerivativeIndexDimensionVO.
        :rtype: str
        """
        return self._dw_type

    @dw_type.setter
    def dw_type(self, dw_type):
        """Sets the dw_type of this DerivativeIndexDimensionVO.

        数据连接类型。

        :param dw_type: The dw_type of this DerivativeIndexDimensionVO.
        :type dw_type: str
        """
        self._dw_type = dw_type

    @property
    def id(self):
        """Gets the id of this DerivativeIndexDimensionVO.

        层级的ID，只读，填写String类型替代Long类型。

        :return: The id of this DerivativeIndexDimensionVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DerivativeIndexDimensionVO.

        层级的ID，只读，填写String类型替代Long类型。

        :param id: The id of this DerivativeIndexDimensionVO.
        :type id: str
        """
        self._id = id

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
        if not isinstance(other, DerivativeIndexDimensionVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
