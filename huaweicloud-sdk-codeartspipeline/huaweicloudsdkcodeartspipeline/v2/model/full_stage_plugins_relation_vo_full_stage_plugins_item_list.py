# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FullStagePluginsRelationVOFullStagePluginsItemList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'plugins_list': 'list[FullStagePluginsRelationVOPluginsList]',
        'display_name': 'str',
        'business_type': 'str',
        'unique_id': 'str',
        'conditions': 'list[str]',
        'addables': 'list[FullStagePluginsRelationVOAddables]',
        'editable': 'bool',
        'removable': 'bool',
        'cloneable': 'bool',
        'disabled': 'bool'
    }

    attribute_map = {
        'plugins_list': 'plugins_list',
        'display_name': 'display_name',
        'business_type': 'business_type',
        'unique_id': 'unique_id',
        'conditions': 'conditions',
        'addables': 'addables',
        'editable': 'editable',
        'removable': 'removable',
        'cloneable': 'cloneable',
        'disabled': 'disabled'
    }

    def __init__(self, plugins_list=None, display_name=None, business_type=None, unique_id=None, conditions=None, addables=None, editable=None, removable=None, cloneable=None, disabled=None):
        r"""FullStagePluginsRelationVOFullStagePluginsItemList

        The model defined in huaweicloud sdk

        :param plugins_list: 插件列表
        :type plugins_list: list[:class:`huaweicloudsdkcodeartspipeline.v2.FullStagePluginsRelationVOPluginsList`]
        :param display_name: 展示名
        :type display_name: str
        :param business_type: 业务类型
        :type business_type: str
        :param unique_id: 唯一ID
        :type unique_id: str
        :param conditions: 条件
        :type conditions: list[str]
        :param addables: 额外属性
        :type addables: list[:class:`huaweicloudsdkcodeartspipeline.v2.FullStagePluginsRelationVOAddables`]
        :param editable: 是否可编辑
        :type editable: bool
        :param removable: 是否可移除
        :type removable: bool
        :param cloneable: 是否可复制
        :type cloneable: bool
        :param disabled: 禁用
        :type disabled: bool
        """
        
        

        self._plugins_list = None
        self._display_name = None
        self._business_type = None
        self._unique_id = None
        self._conditions = None
        self._addables = None
        self._editable = None
        self._removable = None
        self._cloneable = None
        self._disabled = None
        self.discriminator = None

        if plugins_list is not None:
            self.plugins_list = plugins_list
        if display_name is not None:
            self.display_name = display_name
        if business_type is not None:
            self.business_type = business_type
        if unique_id is not None:
            self.unique_id = unique_id
        if conditions is not None:
            self.conditions = conditions
        if addables is not None:
            self.addables = addables
        if editable is not None:
            self.editable = editable
        if removable is not None:
            self.removable = removable
        if cloneable is not None:
            self.cloneable = cloneable
        if disabled is not None:
            self.disabled = disabled

    @property
    def plugins_list(self):
        r"""Gets the plugins_list of this FullStagePluginsRelationVOFullStagePluginsItemList.

        插件列表

        :return: The plugins_list of this FullStagePluginsRelationVOFullStagePluginsItemList.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.FullStagePluginsRelationVOPluginsList`]
        """
        return self._plugins_list

    @plugins_list.setter
    def plugins_list(self, plugins_list):
        r"""Sets the plugins_list of this FullStagePluginsRelationVOFullStagePluginsItemList.

        插件列表

        :param plugins_list: The plugins_list of this FullStagePluginsRelationVOFullStagePluginsItemList.
        :type plugins_list: list[:class:`huaweicloudsdkcodeartspipeline.v2.FullStagePluginsRelationVOPluginsList`]
        """
        self._plugins_list = plugins_list

    @property
    def display_name(self):
        r"""Gets the display_name of this FullStagePluginsRelationVOFullStagePluginsItemList.

        展示名

        :return: The display_name of this FullStagePluginsRelationVOFullStagePluginsItemList.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this FullStagePluginsRelationVOFullStagePluginsItemList.

        展示名

        :param display_name: The display_name of this FullStagePluginsRelationVOFullStagePluginsItemList.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def business_type(self):
        r"""Gets the business_type of this FullStagePluginsRelationVOFullStagePluginsItemList.

        业务类型

        :return: The business_type of this FullStagePluginsRelationVOFullStagePluginsItemList.
        :rtype: str
        """
        return self._business_type

    @business_type.setter
    def business_type(self, business_type):
        r"""Sets the business_type of this FullStagePluginsRelationVOFullStagePluginsItemList.

        业务类型

        :param business_type: The business_type of this FullStagePluginsRelationVOFullStagePluginsItemList.
        :type business_type: str
        """
        self._business_type = business_type

    @property
    def unique_id(self):
        r"""Gets the unique_id of this FullStagePluginsRelationVOFullStagePluginsItemList.

        唯一ID

        :return: The unique_id of this FullStagePluginsRelationVOFullStagePluginsItemList.
        :rtype: str
        """
        return self._unique_id

    @unique_id.setter
    def unique_id(self, unique_id):
        r"""Sets the unique_id of this FullStagePluginsRelationVOFullStagePluginsItemList.

        唯一ID

        :param unique_id: The unique_id of this FullStagePluginsRelationVOFullStagePluginsItemList.
        :type unique_id: str
        """
        self._unique_id = unique_id

    @property
    def conditions(self):
        r"""Gets the conditions of this FullStagePluginsRelationVOFullStagePluginsItemList.

        条件

        :return: The conditions of this FullStagePluginsRelationVOFullStagePluginsItemList.
        :rtype: list[str]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        r"""Sets the conditions of this FullStagePluginsRelationVOFullStagePluginsItemList.

        条件

        :param conditions: The conditions of this FullStagePluginsRelationVOFullStagePluginsItemList.
        :type conditions: list[str]
        """
        self._conditions = conditions

    @property
    def addables(self):
        r"""Gets the addables of this FullStagePluginsRelationVOFullStagePluginsItemList.

        额外属性

        :return: The addables of this FullStagePluginsRelationVOFullStagePluginsItemList.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.FullStagePluginsRelationVOAddables`]
        """
        return self._addables

    @addables.setter
    def addables(self, addables):
        r"""Sets the addables of this FullStagePluginsRelationVOFullStagePluginsItemList.

        额外属性

        :param addables: The addables of this FullStagePluginsRelationVOFullStagePluginsItemList.
        :type addables: list[:class:`huaweicloudsdkcodeartspipeline.v2.FullStagePluginsRelationVOAddables`]
        """
        self._addables = addables

    @property
    def editable(self):
        r"""Gets the editable of this FullStagePluginsRelationVOFullStagePluginsItemList.

        是否可编辑

        :return: The editable of this FullStagePluginsRelationVOFullStagePluginsItemList.
        :rtype: bool
        """
        return self._editable

    @editable.setter
    def editable(self, editable):
        r"""Sets the editable of this FullStagePluginsRelationVOFullStagePluginsItemList.

        是否可编辑

        :param editable: The editable of this FullStagePluginsRelationVOFullStagePluginsItemList.
        :type editable: bool
        """
        self._editable = editable

    @property
    def removable(self):
        r"""Gets the removable of this FullStagePluginsRelationVOFullStagePluginsItemList.

        是否可移除

        :return: The removable of this FullStagePluginsRelationVOFullStagePluginsItemList.
        :rtype: bool
        """
        return self._removable

    @removable.setter
    def removable(self, removable):
        r"""Sets the removable of this FullStagePluginsRelationVOFullStagePluginsItemList.

        是否可移除

        :param removable: The removable of this FullStagePluginsRelationVOFullStagePluginsItemList.
        :type removable: bool
        """
        self._removable = removable

    @property
    def cloneable(self):
        r"""Gets the cloneable of this FullStagePluginsRelationVOFullStagePluginsItemList.

        是否可复制

        :return: The cloneable of this FullStagePluginsRelationVOFullStagePluginsItemList.
        :rtype: bool
        """
        return self._cloneable

    @cloneable.setter
    def cloneable(self, cloneable):
        r"""Sets the cloneable of this FullStagePluginsRelationVOFullStagePluginsItemList.

        是否可复制

        :param cloneable: The cloneable of this FullStagePluginsRelationVOFullStagePluginsItemList.
        :type cloneable: bool
        """
        self._cloneable = cloneable

    @property
    def disabled(self):
        r"""Gets the disabled of this FullStagePluginsRelationVOFullStagePluginsItemList.

        禁用

        :return: The disabled of this FullStagePluginsRelationVOFullStagePluginsItemList.
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        r"""Sets the disabled of this FullStagePluginsRelationVOFullStagePluginsItemList.

        禁用

        :param disabled: The disabled of this FullStagePluginsRelationVOFullStagePluginsItemList.
        :type disabled: bool
        """
        self._disabled = disabled

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
        if not isinstance(other, FullStagePluginsRelationVOFullStagePluginsItemList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
