# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ActionInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'category': 'str',
        'detail': 'DetailInfo'
    }

    attribute_map = {
        'category': 'category',
        'detail': 'detail'
    }

    def __init__(self, category=None, detail=None):
        """ActionInfo

        The model defined in huaweicloud sdk

        :param category: 动作类型：block:阻断,captcha:人机验证;log: 仅记录;dynamic_block:动态阻断
        :type category: str
        :param detail: 
        :type detail: :class:`huaweicloudsdkaad.v2.DetailInfo`
        """
        
        

        self._category = None
        self._detail = None
        self.discriminator = None

        if category is not None:
            self.category = category
        if detail is not None:
            self.detail = detail

    @property
    def category(self):
        """Gets the category of this ActionInfo.

        动作类型：block:阻断,captcha:人机验证;log: 仅记录;dynamic_block:动态阻断

        :return: The category of this ActionInfo.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this ActionInfo.

        动作类型：block:阻断,captcha:人机验证;log: 仅记录;dynamic_block:动态阻断

        :param category: The category of this ActionInfo.
        :type category: str
        """
        self._category = category

    @property
    def detail(self):
        """Gets the detail of this ActionInfo.

        :return: The detail of this ActionInfo.
        :rtype: :class:`huaweicloudsdkaad.v2.DetailInfo`
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this ActionInfo.

        :param detail: The detail of this ActionInfo.
        :type detail: :class:`huaweicloudsdkaad.v2.DetailInfo`
        """
        self._detail = detail

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
        if not isinstance(other, ActionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
