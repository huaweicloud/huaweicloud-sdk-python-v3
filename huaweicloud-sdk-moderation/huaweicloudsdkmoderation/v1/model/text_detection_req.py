# coding: utf-8

import pprint
import re

import six





class TextDetectionReq:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'categories': 'list[str]',
        'items': 'list[TextDetectionItemsReq]'
    }

    attribute_map = {
        'categories': 'categories',
        'items': 'items'
    }

    def __init__(self, categories=None, items=None):
        """TextDetectionReq - a model defined in huaweicloud sdk"""
        
        

        self._categories = None
        self._items = None
        self.discriminator = None

        if categories is not None:
            self.categories = categories
        self.items = items

    @property
    def categories(self):
        """Gets the categories of this TextDetectionReq.

        检测场景。  当前支持的场景有默认场景和用户自定义场景：  默认场景为：  * politics：涉政  * porn：涉黄  * ad：广告  * abuse：辱骂  * contraband：违禁品  * flood：灌水  - 用户自定义场景为：自定义黑名单词库。  > 说明： - 自定义词库的创建和使用请参见[配置自定义词库](https://support.huaweicloud.com/api-moderation/moderation_03_0027.html)。 - flood场景不支持使用自定义白名单词库。

        :return: The categories of this TextDetectionReq.
        :rtype: list[str]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this TextDetectionReq.

        检测场景。  当前支持的场景有默认场景和用户自定义场景：  默认场景为：  * politics：涉政  * porn：涉黄  * ad：广告  * abuse：辱骂  * contraband：违禁品  * flood：灌水  - 用户自定义场景为：自定义黑名单词库。  > 说明： - 自定义词库的创建和使用请参见[配置自定义词库](https://support.huaweicloud.com/api-moderation/moderation_03_0027.html)。 - flood场景不支持使用自定义白名单词库。

        :param categories: The categories of this TextDetectionReq.
        :type: list[str]
        """
        self._categories = categories

    @property
    def items(self):
        """Gets the items of this TextDetectionReq.

        待检测的文本列表，目前暂时每次只支持传一个item。

        :return: The items of this TextDetectionReq.
        :rtype: list[TextDetectionItemsReq]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this TextDetectionReq.

        待检测的文本列表，目前暂时每次只支持传一个item。

        :param items: The items of this TextDetectionReq.
        :type: list[TextDetectionItemsReq]
        """
        self._items = items

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TextDetectionReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
