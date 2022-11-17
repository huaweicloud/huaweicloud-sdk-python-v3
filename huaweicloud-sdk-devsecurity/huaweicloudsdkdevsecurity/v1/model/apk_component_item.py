# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApkComponentItem:

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
        'action_list': 'list[str]',
        'category_list': 'list[str]',
        'is_main_activity': 'bool',
        'exported': 'str'
    }

    attribute_map = {
        'name': 'name',
        'action_list': 'action_list',
        'category_list': 'category_list',
        'is_main_activity': 'is_main_activity',
        'exported': 'exported'
    }

    def __init__(self, name=None, action_list=None, category_list=None, is_main_activity=None, exported=None):
        """ApkComponentItem

        The model defined in huaweicloud sdk

        :param name: 组件名称
        :type name: str
        :param action_list: 动作列表
        :type action_list: list[str]
        :param category_list: 类别列表
        :type category_list: list[str]
        :param is_main_activity: 主要活动
        :type is_main_activity: bool
        :param exported: 导出
        :type exported: str
        """
        
        

        self._name = None
        self._action_list = None
        self._category_list = None
        self._is_main_activity = None
        self._exported = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if action_list is not None:
            self.action_list = action_list
        if category_list is not None:
            self.category_list = category_list
        if is_main_activity is not None:
            self.is_main_activity = is_main_activity
        if exported is not None:
            self.exported = exported

    @property
    def name(self):
        """Gets the name of this ApkComponentItem.

        组件名称

        :return: The name of this ApkComponentItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApkComponentItem.

        组件名称

        :param name: The name of this ApkComponentItem.
        :type name: str
        """
        self._name = name

    @property
    def action_list(self):
        """Gets the action_list of this ApkComponentItem.

        动作列表

        :return: The action_list of this ApkComponentItem.
        :rtype: list[str]
        """
        return self._action_list

    @action_list.setter
    def action_list(self, action_list):
        """Sets the action_list of this ApkComponentItem.

        动作列表

        :param action_list: The action_list of this ApkComponentItem.
        :type action_list: list[str]
        """
        self._action_list = action_list

    @property
    def category_list(self):
        """Gets the category_list of this ApkComponentItem.

        类别列表

        :return: The category_list of this ApkComponentItem.
        :rtype: list[str]
        """
        return self._category_list

    @category_list.setter
    def category_list(self, category_list):
        """Sets the category_list of this ApkComponentItem.

        类别列表

        :param category_list: The category_list of this ApkComponentItem.
        :type category_list: list[str]
        """
        self._category_list = category_list

    @property
    def is_main_activity(self):
        """Gets the is_main_activity of this ApkComponentItem.

        主要活动

        :return: The is_main_activity of this ApkComponentItem.
        :rtype: bool
        """
        return self._is_main_activity

    @is_main_activity.setter
    def is_main_activity(self, is_main_activity):
        """Sets the is_main_activity of this ApkComponentItem.

        主要活动

        :param is_main_activity: The is_main_activity of this ApkComponentItem.
        :type is_main_activity: bool
        """
        self._is_main_activity = is_main_activity

    @property
    def exported(self):
        """Gets the exported of this ApkComponentItem.

        导出

        :return: The exported of this ApkComponentItem.
        :rtype: str
        """
        return self._exported

    @exported.setter
    def exported(self, exported):
        """Sets the exported of this ApkComponentItem.

        导出

        :param exported: The exported of this ApkComponentItem.
        :type exported: str
        """
        self._exported = exported

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
        if not isinstance(other, ApkComponentItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
