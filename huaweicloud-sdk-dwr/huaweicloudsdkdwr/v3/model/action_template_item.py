# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ActionTemplateItem:

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
        'category': 'str'
    }

    attribute_map = {
        'name': 'name',
        'category': 'category'
    }

    def __init__(self, name=None, category=None):
        """ActionTemplateItem

        The model defined in huaweicloud sdk

        :param name: 名称。
        :type name: str
        :param category: 第三方算子模板的分类。默认分类为FileProcess,MediaProcess,ImageProcess,ContentReview,NotificationProcess,VoiceInteraction
        :type category: str
        """
        
        

        self._name = None
        self._category = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if category is not None:
            self.category = category

    @property
    def name(self):
        """Gets the name of this ActionTemplateItem.

        名称。

        :return: The name of this ActionTemplateItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ActionTemplateItem.

        名称。

        :param name: The name of this ActionTemplateItem.
        :type name: str
        """
        self._name = name

    @property
    def category(self):
        """Gets the category of this ActionTemplateItem.

        第三方算子模板的分类。默认分类为FileProcess,MediaProcess,ImageProcess,ContentReview,NotificationProcess,VoiceInteraction

        :return: The category of this ActionTemplateItem.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this ActionTemplateItem.

        第三方算子模板的分类。默认分类为FileProcess,MediaProcess,ImageProcess,ContentReview,NotificationProcess,VoiceInteraction

        :param category: The category of this ActionTemplateItem.
        :type category: str
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
        if not isinstance(other, ActionTemplateItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
