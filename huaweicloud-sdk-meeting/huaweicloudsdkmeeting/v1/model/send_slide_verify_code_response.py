# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SendSlideVerifyCodeResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'shadow_image': 'str',
        'cut_image': 'str',
        'point_y': 'int',
        'token': 'str',
        'expire': 'int'
    }

    attribute_map = {
        'shadow_image': 'shadowImage',
        'cut_image': 'cutImage',
        'point_y': 'pointY',
        'token': 'token',
        'expire': 'expire'
    }

    def __init__(self, shadow_image=None, cut_image=None, point_y=None, token=None, expire=None):
        """SendSlideVerifyCodeResponse

        The model defined in huaweicloud sdk

        :param shadow_image: 抠出图形后的原背景图。通过“data:url”方式来定义图片。
        :type shadow_image: str
        :param cut_image: 抠出的图形。
        :type cut_image: str
        :param point_y: 抠出图形的Y轴座标。
        :type point_y: int
        :param token: 验证码Token字符串。
        :type token: str
        :param expire: 验证码有效时间，单位：秒。
        :type expire: int
        """
        
        super(SendSlideVerifyCodeResponse, self).__init__()

        self._shadow_image = None
        self._cut_image = None
        self._point_y = None
        self._token = None
        self._expire = None
        self.discriminator = None

        if shadow_image is not None:
            self.shadow_image = shadow_image
        if cut_image is not None:
            self.cut_image = cut_image
        if point_y is not None:
            self.point_y = point_y
        if token is not None:
            self.token = token
        if expire is not None:
            self.expire = expire

    @property
    def shadow_image(self):
        """Gets the shadow_image of this SendSlideVerifyCodeResponse.

        抠出图形后的原背景图。通过“data:url”方式来定义图片。

        :return: The shadow_image of this SendSlideVerifyCodeResponse.
        :rtype: str
        """
        return self._shadow_image

    @shadow_image.setter
    def shadow_image(self, shadow_image):
        """Sets the shadow_image of this SendSlideVerifyCodeResponse.

        抠出图形后的原背景图。通过“data:url”方式来定义图片。

        :param shadow_image: The shadow_image of this SendSlideVerifyCodeResponse.
        :type shadow_image: str
        """
        self._shadow_image = shadow_image

    @property
    def cut_image(self):
        """Gets the cut_image of this SendSlideVerifyCodeResponse.

        抠出的图形。

        :return: The cut_image of this SendSlideVerifyCodeResponse.
        :rtype: str
        """
        return self._cut_image

    @cut_image.setter
    def cut_image(self, cut_image):
        """Sets the cut_image of this SendSlideVerifyCodeResponse.

        抠出的图形。

        :param cut_image: The cut_image of this SendSlideVerifyCodeResponse.
        :type cut_image: str
        """
        self._cut_image = cut_image

    @property
    def point_y(self):
        """Gets the point_y of this SendSlideVerifyCodeResponse.

        抠出图形的Y轴座标。

        :return: The point_y of this SendSlideVerifyCodeResponse.
        :rtype: int
        """
        return self._point_y

    @point_y.setter
    def point_y(self, point_y):
        """Sets the point_y of this SendSlideVerifyCodeResponse.

        抠出图形的Y轴座标。

        :param point_y: The point_y of this SendSlideVerifyCodeResponse.
        :type point_y: int
        """
        self._point_y = point_y

    @property
    def token(self):
        """Gets the token of this SendSlideVerifyCodeResponse.

        验证码Token字符串。

        :return: The token of this SendSlideVerifyCodeResponse.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this SendSlideVerifyCodeResponse.

        验证码Token字符串。

        :param token: The token of this SendSlideVerifyCodeResponse.
        :type token: str
        """
        self._token = token

    @property
    def expire(self):
        """Gets the expire of this SendSlideVerifyCodeResponse.

        验证码有效时间，单位：秒。

        :return: The expire of this SendSlideVerifyCodeResponse.
        :rtype: int
        """
        return self._expire

    @expire.setter
    def expire(self, expire):
        """Sets the expire of this SendSlideVerifyCodeResponse.

        验证码有效时间，单位：秒。

        :param expire: The expire of this SendSlideVerifyCodeResponse.
        :type expire: int
        """
        self._expire = expire

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
        if not isinstance(other, SendSlideVerifyCodeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
