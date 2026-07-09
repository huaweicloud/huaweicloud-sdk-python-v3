# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListResourceSpecsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'body': 'ResourceSpecsQueryReq'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'body': 'body'
    }

    def __init__(self, x_language=None, body=None):
        r"""ListResourceSpecsRequest

        The model defined in huaweicloud sdk

        :param x_language: |参数名称：语言| |参数的约束及描述：非必填，忽略大小写，默认zh_cn，枚举：zh_cn：中文 en_us：英文|
        :type x_language: str
        :param body: Body of the ListResourceSpecsRequest
        :type body: :class:`huaweicloudsdkbssintl.v2.ResourceSpecsQueryReq`
        """
        
        

        self._x_language = None
        self._body = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        if body is not None:
            self.body = body

    @property
    def x_language(self):
        r"""Gets the x_language of this ListResourceSpecsRequest.

        |参数名称：语言| |参数的约束及描述：非必填，忽略大小写，默认zh_cn，枚举：zh_cn：中文 en_us：英文|

        :return: The x_language of this ListResourceSpecsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListResourceSpecsRequest.

        |参数名称：语言| |参数的约束及描述：非必填，忽略大小写，默认zh_cn，枚举：zh_cn：中文 en_us：英文|

        :param x_language: The x_language of this ListResourceSpecsRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def body(self):
        r"""Gets the body of this ListResourceSpecsRequest.

        :return: The body of this ListResourceSpecsRequest.
        :rtype: :class:`huaweicloudsdkbssintl.v2.ResourceSpecsQueryReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this ListResourceSpecsRequest.

        :param body: The body of this ListResourceSpecsRequest.
        :type body: :class:`huaweicloudsdkbssintl.v2.ResourceSpecsQueryReq`
        """
        self._body = body

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
        if not isinstance(other, ListResourceSpecsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
