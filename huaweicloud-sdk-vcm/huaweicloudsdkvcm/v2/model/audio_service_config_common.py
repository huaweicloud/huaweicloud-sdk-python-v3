# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AudioServiceConfigCommon:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'categories': 'str'
    }

    attribute_map = {
        'categories': 'categories'
    }

    def __init__(self, categories=None):
        """AudioServiceConfigCommon

        The model defined in huaweicloud sdk

        :param categories: 检测场景。 - politics：政治人物的检测。 - porn：涉黄内容元素的检测。 可通过配置上述场景，来完成对应场景元素的检测。 
        :type categories: str
        """
        
        

        self._categories = None
        self.discriminator = None

        self.categories = categories

    @property
    def categories(self):
        """Gets the categories of this AudioServiceConfigCommon.

        检测场景。 - politics：政治人物的检测。 - porn：涉黄内容元素的检测。 可通过配置上述场景，来完成对应场景元素的检测。 

        :return: The categories of this AudioServiceConfigCommon.
        :rtype: str
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this AudioServiceConfigCommon.

        检测场景。 - politics：政治人物的检测。 - porn：涉黄内容元素的检测。 可通过配置上述场景，来完成对应场景元素的检测。 

        :param categories: The categories of this AudioServiceConfigCommon.
        :type categories: str
        """
        self._categories = categories

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
        if not isinstance(other, AudioServiceConfigCommon):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
