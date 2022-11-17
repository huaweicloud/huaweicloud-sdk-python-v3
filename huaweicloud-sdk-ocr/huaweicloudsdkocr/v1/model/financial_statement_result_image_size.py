# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FinancialStatementResultImageSize:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'height': 'int',
        'width': 'int'
    }

    attribute_map = {
        'height': 'height',
        'width': 'width'
    }

    def __init__(self, height=None, width=None):
        """FinancialStatementResultImageSize

        The model defined in huaweicloud sdk

        :param height: 矫正后图像的高。 
        :type height: int
        :param width: 矫正后图像的宽。 
        :type width: int
        """
        
        

        self._height = None
        self._width = None
        self.discriminator = None

        if height is not None:
            self.height = height
        if width is not None:
            self.width = width

    @property
    def height(self):
        """Gets the height of this FinancialStatementResultImageSize.

        矫正后图像的高。 

        :return: The height of this FinancialStatementResultImageSize.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this FinancialStatementResultImageSize.

        矫正后图像的高。 

        :param height: The height of this FinancialStatementResultImageSize.
        :type height: int
        """
        self._height = height

    @property
    def width(self):
        """Gets the width of this FinancialStatementResultImageSize.

        矫正后图像的宽。 

        :return: The width of this FinancialStatementResultImageSize.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this FinancialStatementResultImageSize.

        矫正后图像的宽。 

        :param width: The width of this FinancialStatementResultImageSize.
        :type width: int
        """
        self._width = width

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
        if not isinstance(other, FinancialStatementResultImageSize):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
