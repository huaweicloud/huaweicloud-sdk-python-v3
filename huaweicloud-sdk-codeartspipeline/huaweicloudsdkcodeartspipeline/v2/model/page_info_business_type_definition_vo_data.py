# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PageInfoBusinessTypeDefinitionVOData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'business_type': 'str',
        'display_name': 'str',
        'unique_id': 'str',
        'editable': 'bool',
        'removable': 'bool',
        'cloneable': 'bool',
        'disabled': 'bool',
        'conditions': 'list[str]',
        'plugins_list': 'list[PageInfoBusinessTypeDefinitionVOPluginsList]'
    }

    attribute_map = {
        'business_type': 'business_type',
        'display_name': 'display_name',
        'unique_id': 'unique_id',
        'editable': 'editable',
        'removable': 'removable',
        'cloneable': 'cloneable',
        'disabled': 'disabled',
        'conditions': 'conditions',
        'plugins_list': 'plugins_list'
    }

    def __init__(self, business_type=None, display_name=None, unique_id=None, editable=None, removable=None, cloneable=None, disabled=None, conditions=None, plugins_list=None):
        r"""PageInfoBusinessTypeDefinitionVOData

        The model defined in huaweicloud sdk

        :param business_type: 业务类型
        :type business_type: str
        :param display_name: 展示名
        :type display_name: str
        :param unique_id: 唯一ID
        :type unique_id: str
        :param editable: 可编辑
        :type editable: bool
        :param removable: 可移除
        :type removable: bool
        :param cloneable: 可复制
        :type cloneable: bool
        :param disabled: 禁用
        :type disabled: bool
        :param conditions: 条件
        :type conditions: list[str]
        :param plugins_list: 插件列表
        :type plugins_list: list[:class:`huaweicloudsdkcodeartspipeline.v2.PageInfoBusinessTypeDefinitionVOPluginsList`]
        """
        
        

        self._business_type = None
        self._display_name = None
        self._unique_id = None
        self._editable = None
        self._removable = None
        self._cloneable = None
        self._disabled = None
        self._conditions = None
        self._plugins_list = None
        self.discriminator = None

        if business_type is not None:
            self.business_type = business_type
        if display_name is not None:
            self.display_name = display_name
        if unique_id is not None:
            self.unique_id = unique_id
        if editable is not None:
            self.editable = editable
        if removable is not None:
            self.removable = removable
        if cloneable is not None:
            self.cloneable = cloneable
        if disabled is not None:
            self.disabled = disabled
        if conditions is not None:
            self.conditions = conditions
        if plugins_list is not None:
            self.plugins_list = plugins_list

    @property
    def business_type(self):
        r"""Gets the business_type of this PageInfoBusinessTypeDefinitionVOData.

        业务类型

        :return: The business_type of this PageInfoBusinessTypeDefinitionVOData.
        :rtype: str
        """
        return self._business_type

    @business_type.setter
    def business_type(self, business_type):
        r"""Sets the business_type of this PageInfoBusinessTypeDefinitionVOData.

        业务类型

        :param business_type: The business_type of this PageInfoBusinessTypeDefinitionVOData.
        :type business_type: str
        """
        self._business_type = business_type

    @property
    def display_name(self):
        r"""Gets the display_name of this PageInfoBusinessTypeDefinitionVOData.

        展示名

        :return: The display_name of this PageInfoBusinessTypeDefinitionVOData.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this PageInfoBusinessTypeDefinitionVOData.

        展示名

        :param display_name: The display_name of this PageInfoBusinessTypeDefinitionVOData.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def unique_id(self):
        r"""Gets the unique_id of this PageInfoBusinessTypeDefinitionVOData.

        唯一ID

        :return: The unique_id of this PageInfoBusinessTypeDefinitionVOData.
        :rtype: str
        """
        return self._unique_id

    @unique_id.setter
    def unique_id(self, unique_id):
        r"""Sets the unique_id of this PageInfoBusinessTypeDefinitionVOData.

        唯一ID

        :param unique_id: The unique_id of this PageInfoBusinessTypeDefinitionVOData.
        :type unique_id: str
        """
        self._unique_id = unique_id

    @property
    def editable(self):
        r"""Gets the editable of this PageInfoBusinessTypeDefinitionVOData.

        可编辑

        :return: The editable of this PageInfoBusinessTypeDefinitionVOData.
        :rtype: bool
        """
        return self._editable

    @editable.setter
    def editable(self, editable):
        r"""Sets the editable of this PageInfoBusinessTypeDefinitionVOData.

        可编辑

        :param editable: The editable of this PageInfoBusinessTypeDefinitionVOData.
        :type editable: bool
        """
        self._editable = editable

    @property
    def removable(self):
        r"""Gets the removable of this PageInfoBusinessTypeDefinitionVOData.

        可移除

        :return: The removable of this PageInfoBusinessTypeDefinitionVOData.
        :rtype: bool
        """
        return self._removable

    @removable.setter
    def removable(self, removable):
        r"""Sets the removable of this PageInfoBusinessTypeDefinitionVOData.

        可移除

        :param removable: The removable of this PageInfoBusinessTypeDefinitionVOData.
        :type removable: bool
        """
        self._removable = removable

    @property
    def cloneable(self):
        r"""Gets the cloneable of this PageInfoBusinessTypeDefinitionVOData.

        可复制

        :return: The cloneable of this PageInfoBusinessTypeDefinitionVOData.
        :rtype: bool
        """
        return self._cloneable

    @cloneable.setter
    def cloneable(self, cloneable):
        r"""Sets the cloneable of this PageInfoBusinessTypeDefinitionVOData.

        可复制

        :param cloneable: The cloneable of this PageInfoBusinessTypeDefinitionVOData.
        :type cloneable: bool
        """
        self._cloneable = cloneable

    @property
    def disabled(self):
        r"""Gets the disabled of this PageInfoBusinessTypeDefinitionVOData.

        禁用

        :return: The disabled of this PageInfoBusinessTypeDefinitionVOData.
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        r"""Sets the disabled of this PageInfoBusinessTypeDefinitionVOData.

        禁用

        :param disabled: The disabled of this PageInfoBusinessTypeDefinitionVOData.
        :type disabled: bool
        """
        self._disabled = disabled

    @property
    def conditions(self):
        r"""Gets the conditions of this PageInfoBusinessTypeDefinitionVOData.

        条件

        :return: The conditions of this PageInfoBusinessTypeDefinitionVOData.
        :rtype: list[str]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        r"""Sets the conditions of this PageInfoBusinessTypeDefinitionVOData.

        条件

        :param conditions: The conditions of this PageInfoBusinessTypeDefinitionVOData.
        :type conditions: list[str]
        """
        self._conditions = conditions

    @property
    def plugins_list(self):
        r"""Gets the plugins_list of this PageInfoBusinessTypeDefinitionVOData.

        插件列表

        :return: The plugins_list of this PageInfoBusinessTypeDefinitionVOData.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.PageInfoBusinessTypeDefinitionVOPluginsList`]
        """
        return self._plugins_list

    @plugins_list.setter
    def plugins_list(self, plugins_list):
        r"""Sets the plugins_list of this PageInfoBusinessTypeDefinitionVOData.

        插件列表

        :param plugins_list: The plugins_list of this PageInfoBusinessTypeDefinitionVOData.
        :type plugins_list: list[:class:`huaweicloudsdkcodeartspipeline.v2.PageInfoBusinessTypeDefinitionVOPluginsList`]
        """
        self._plugins_list = plugins_list

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
        if not isinstance(other, PageInfoBusinessTypeDefinitionVOData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
