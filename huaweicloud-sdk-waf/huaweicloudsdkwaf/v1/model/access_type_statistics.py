# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccessTypeStatistics:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'access_type': 'str',
        'text_request_count': 'int',
        'image_request_count': 'int'
    }

    attribute_map = {
        'access_type': 'access_type',
        'text_request_count': 'text_request_count',
        'image_request_count': 'image_request_count'
    }

    def __init__(self, access_type=None, text_request_count=None, image_request_count=None):
        r"""AccessTypeStatistics

        The model defined in huaweicloud sdk

        :param access_type: 接入类型（api/waf）
        :type access_type: str
        :param text_request_count: 用户输入请求数
        :type text_request_count: int
        :param image_request_count: 用户输出请求数
        :type image_request_count: int
        """
        
        

        self._access_type = None
        self._text_request_count = None
        self._image_request_count = None
        self.discriminator = None

        self.access_type = access_type
        self.text_request_count = text_request_count
        self.image_request_count = image_request_count

    @property
    def access_type(self):
        r"""Gets the access_type of this AccessTypeStatistics.

        接入类型（api/waf）

        :return: The access_type of this AccessTypeStatistics.
        :rtype: str
        """
        return self._access_type

    @access_type.setter
    def access_type(self, access_type):
        r"""Sets the access_type of this AccessTypeStatistics.

        接入类型（api/waf）

        :param access_type: The access_type of this AccessTypeStatistics.
        :type access_type: str
        """
        self._access_type = access_type

    @property
    def text_request_count(self):
        r"""Gets the text_request_count of this AccessTypeStatistics.

        用户输入请求数

        :return: The text_request_count of this AccessTypeStatistics.
        :rtype: int
        """
        return self._text_request_count

    @text_request_count.setter
    def text_request_count(self, text_request_count):
        r"""Sets the text_request_count of this AccessTypeStatistics.

        用户输入请求数

        :param text_request_count: The text_request_count of this AccessTypeStatistics.
        :type text_request_count: int
        """
        self._text_request_count = text_request_count

    @property
    def image_request_count(self):
        r"""Gets the image_request_count of this AccessTypeStatistics.

        用户输出请求数

        :return: The image_request_count of this AccessTypeStatistics.
        :rtype: int
        """
        return self._image_request_count

    @image_request_count.setter
    def image_request_count(self, image_request_count):
        r"""Sets the image_request_count of this AccessTypeStatistics.

        用户输出请求数

        :param image_request_count: The image_request_count of this AccessTypeStatistics.
        :type image_request_count: int
        """
        self._image_request_count = image_request_count

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
        if not isinstance(other, AccessTypeStatistics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
