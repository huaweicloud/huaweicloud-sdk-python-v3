# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PageConfigPx:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'width': 'int',
        'height': 'int',
        'margin': 'MarginInfo'
    }

    attribute_map = {
        'width': 'width',
        'height': 'height',
        'margin': 'margin'
    }

    def __init__(self, width=None, height=None, margin=None):
        r"""PageConfigPx

        The model defined in huaweicloud sdk

        :param width: 安全报告的宽度
        :type width: int
        :param height: 安全报告的高度
        :type height: int
        :param margin: 
        :type margin: :class:`huaweicloudsdksecmaster.v1.MarginInfo`
        """
        
        

        self._width = None
        self._height = None
        self._margin = None
        self.discriminator = None

        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if margin is not None:
            self.margin = margin

    @property
    def width(self):
        r"""Gets the width of this PageConfigPx.

        安全报告的宽度

        :return: The width of this PageConfigPx.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        r"""Sets the width of this PageConfigPx.

        安全报告的宽度

        :param width: The width of this PageConfigPx.
        :type width: int
        """
        self._width = width

    @property
    def height(self):
        r"""Gets the height of this PageConfigPx.

        安全报告的高度

        :return: The height of this PageConfigPx.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        r"""Sets the height of this PageConfigPx.

        安全报告的高度

        :param height: The height of this PageConfigPx.
        :type height: int
        """
        self._height = height

    @property
    def margin(self):
        r"""Gets the margin of this PageConfigPx.

        :return: The margin of this PageConfigPx.
        :rtype: :class:`huaweicloudsdksecmaster.v1.MarginInfo`
        """
        return self._margin

    @margin.setter
    def margin(self, margin):
        r"""Sets the margin of this PageConfigPx.

        :param margin: The margin of this PageConfigPx.
        :type margin: :class:`huaweicloudsdksecmaster.v1.MarginInfo`
        """
        self._margin = margin

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PageConfigPx):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
