# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MenuItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'action_type': 'str',
        'content': 'str',
        'ext_msg': 'ExtMsg',
        'sub_menu_items': 'list[MenuItem]'
    }

    attribute_map = {
        'name': 'name',
        'action_type': 'action_type',
        'content': 'content',
        'ext_msg': 'ext_msg',
        'sub_menu_items': 'sub_menu_items'
    }

    def __init__(self, name=None, action_type=None, content=None, ext_msg=None, sub_menu_items=None):
        r"""MenuItem

        The model defined in huaweicloud sdk

        :param name: 子菜单名称。  1. 一级菜单名长度和菜单数量有关，具体约束为：     - 当菜单数量为1个时，菜单名长度范围在1-24个字符。    - 当菜单数量为2个时，菜单名长度范围在1-12个字符。    - 当菜单数量为3个时，菜单名长度范围在1-8个字符。  2. 二级菜单名长度范围恒为1-16个字符。  &gt; 以上字符区分中英文，一个中文占2个字符，字母和数字占1个字符，且同时生效的一组菜单内名称不能重复。
        :type name: str
        :param action_type: 菜单动作类型。 - OPEN_SUBMENU：打开子菜单 - OPEN_URL：打开URL - CALLING：拨打电话 - OPEN_APP：打开APP - OPEN_QUICK：打开快应用 
        :type action_type: str
        :param content: 对应值类型。对应不同action_type值，content含义如下： - action_type&#x3D;OPEN_SUBMENU：不填 - action_type&#x3D;OPEN_URL：参数数值为跳转URL - action_type&#x3D;CALLING：参数数值为电话号码 - action_type&#x3D;OPEN_APP：参数数值为APP的跳转deeplink - action_type&#x3D;OPEN_QUICK：参数数值为快应用跳转的deeplink 
        :type content: str
        :param ext_msg: 
        :type ext_msg: :class:`huaweicloudsdkkoomessage.v1.ExtMsg`
        :param sub_menu_items: 子菜单配置项。  &gt; 仅当action_type&#x3D;OPEN_SUBMENU时生效，且该项内不允许再配置子菜单。 
        :type sub_menu_items: list[:class:`huaweicloudsdkkoomessage.v1.MenuItem`]
        """
        
        

        self._name = None
        self._action_type = None
        self._content = None
        self._ext_msg = None
        self._sub_menu_items = None
        self.discriminator = None

        self.name = name
        self.action_type = action_type
        if content is not None:
            self.content = content
        if ext_msg is not None:
            self.ext_msg = ext_msg
        if sub_menu_items is not None:
            self.sub_menu_items = sub_menu_items

    @property
    def name(self):
        r"""Gets the name of this MenuItem.

        子菜单名称。  1. 一级菜单名长度和菜单数量有关，具体约束为：     - 当菜单数量为1个时，菜单名长度范围在1-24个字符。    - 当菜单数量为2个时，菜单名长度范围在1-12个字符。    - 当菜单数量为3个时，菜单名长度范围在1-8个字符。  2. 二级菜单名长度范围恒为1-16个字符。  > 以上字符区分中英文，一个中文占2个字符，字母和数字占1个字符，且同时生效的一组菜单内名称不能重复。

        :return: The name of this MenuItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this MenuItem.

        子菜单名称。  1. 一级菜单名长度和菜单数量有关，具体约束为：     - 当菜单数量为1个时，菜单名长度范围在1-24个字符。    - 当菜单数量为2个时，菜单名长度范围在1-12个字符。    - 当菜单数量为3个时，菜单名长度范围在1-8个字符。  2. 二级菜单名长度范围恒为1-16个字符。  > 以上字符区分中英文，一个中文占2个字符，字母和数字占1个字符，且同时生效的一组菜单内名称不能重复。

        :param name: The name of this MenuItem.
        :type name: str
        """
        self._name = name

    @property
    def action_type(self):
        r"""Gets the action_type of this MenuItem.

        菜单动作类型。 - OPEN_SUBMENU：打开子菜单 - OPEN_URL：打开URL - CALLING：拨打电话 - OPEN_APP：打开APP - OPEN_QUICK：打开快应用 

        :return: The action_type of this MenuItem.
        :rtype: str
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        r"""Sets the action_type of this MenuItem.

        菜单动作类型。 - OPEN_SUBMENU：打开子菜单 - OPEN_URL：打开URL - CALLING：拨打电话 - OPEN_APP：打开APP - OPEN_QUICK：打开快应用 

        :param action_type: The action_type of this MenuItem.
        :type action_type: str
        """
        self._action_type = action_type

    @property
    def content(self):
        r"""Gets the content of this MenuItem.

        对应值类型。对应不同action_type值，content含义如下： - action_type=OPEN_SUBMENU：不填 - action_type=OPEN_URL：参数数值为跳转URL - action_type=CALLING：参数数值为电话号码 - action_type=OPEN_APP：参数数值为APP的跳转deeplink - action_type=OPEN_QUICK：参数数值为快应用跳转的deeplink 

        :return: The content of this MenuItem.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this MenuItem.

        对应值类型。对应不同action_type值，content含义如下： - action_type=OPEN_SUBMENU：不填 - action_type=OPEN_URL：参数数值为跳转URL - action_type=CALLING：参数数值为电话号码 - action_type=OPEN_APP：参数数值为APP的跳转deeplink - action_type=OPEN_QUICK：参数数值为快应用跳转的deeplink 

        :param content: The content of this MenuItem.
        :type content: str
        """
        self._content = content

    @property
    def ext_msg(self):
        r"""Gets the ext_msg of this MenuItem.

        :return: The ext_msg of this MenuItem.
        :rtype: :class:`huaweicloudsdkkoomessage.v1.ExtMsg`
        """
        return self._ext_msg

    @ext_msg.setter
    def ext_msg(self, ext_msg):
        r"""Sets the ext_msg of this MenuItem.

        :param ext_msg: The ext_msg of this MenuItem.
        :type ext_msg: :class:`huaweicloudsdkkoomessage.v1.ExtMsg`
        """
        self._ext_msg = ext_msg

    @property
    def sub_menu_items(self):
        r"""Gets the sub_menu_items of this MenuItem.

        子菜单配置项。  > 仅当action_type=OPEN_SUBMENU时生效，且该项内不允许再配置子菜单。 

        :return: The sub_menu_items of this MenuItem.
        :rtype: list[:class:`huaweicloudsdkkoomessage.v1.MenuItem`]
        """
        return self._sub_menu_items

    @sub_menu_items.setter
    def sub_menu_items(self, sub_menu_items):
        r"""Sets the sub_menu_items of this MenuItem.

        子菜单配置项。  > 仅当action_type=OPEN_SUBMENU时生效，且该项内不允许再配置子菜单。 

        :param sub_menu_items: The sub_menu_items of this MenuItem.
        :type sub_menu_items: list[:class:`huaweicloudsdkkoomessage.v1.MenuItem`]
        """
        self._sub_menu_items = sub_menu_items

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
        if not isinstance(other, MenuItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
