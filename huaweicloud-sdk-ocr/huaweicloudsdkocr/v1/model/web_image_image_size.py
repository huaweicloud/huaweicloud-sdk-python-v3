# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WebImageImageSize:

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
        """WebImageImageSize

        The model defined in huaweicloud sdk

        :param height: 传入image_size时的返回，为图像高度。 
        :type height: int
        :param width: 传入image_size时的返回，为图像宽度。 
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
        """Gets the height of this WebImageImageSize.

        传入image_size时的返回，为图像高度。 

        :return: The height of this WebImageImageSize.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this WebImageImageSize.

        传入image_size时的返回，为图像高度。 

        :param height: The height of this WebImageImageSize.
        :type height: int
        """
        self._height = height

    @property
    def width(self):
        """Gets the width of this WebImageImageSize.

        传入image_size时的返回，为图像宽度。 

        :return: The width of this WebImageImageSize.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this WebImageImageSize.

        传入image_size时的返回，为图像宽度。 

        :param width: The width of this WebImageImageSize.
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
        if not isinstance(other, WebImageImageSize):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
