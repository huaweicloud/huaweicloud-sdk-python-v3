# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SlideVerifyCodeCheckDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user': 'str',
        'client_type': 'int',
        'check_type': 'int',
        'token': 'str',
        'point_x': 'int',
        'slide_time': 'int'
    }

    attribute_map = {
        'user': 'user',
        'client_type': 'clientType',
        'check_type': 'checkType',
        'token': 'token',
        'point_x': 'pointX',
        'slide_time': 'slideTime'
    }

    def __init__(self, user=None, client_type=None, check_type=None, token=None, point_x=None, slide_time=None):
        r"""SlideVerifyCodeCheckDTO

        The model defined in huaweicloud sdk

        :param user: 必须和发送验证码时带的用户身份信息相同。 
        :type user: str
        :param client_type: 登录客户端类型。 * 0：Web客户端类型 * 5：PC客户端 * 6：移动客户端 
        :type client_type: int
        :param check_type: 校验类型。默认值：0。 * 0：登录； * 1：忘记密码; 
        :type check_type: int
        :param token: 验证码Token字符串。通过[[发送滑块验证码](https://support.huaweicloud.com/api-meeting/meeting_21_0100.html)](tag:hws)[[发送滑块验证码](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0100.html)](tag:hk) 接口获取。 
        :type token: str
        :param point_x: 抠出图形的X轴坐标。
        :type point_x: int
        :param slide_time: 滑动时间，单位ms。
        :type slide_time: int
        """
        
        

        self._user = None
        self._client_type = None
        self._check_type = None
        self._token = None
        self._point_x = None
        self._slide_time = None
        self.discriminator = None

        self.user = user
        self.client_type = client_type
        if check_type is not None:
            self.check_type = check_type
        self.token = token
        self.point_x = point_x
        self.slide_time = slide_time

    @property
    def user(self):
        r"""Gets the user of this SlideVerifyCodeCheckDTO.

        必须和发送验证码时带的用户身份信息相同。 

        :return: The user of this SlideVerifyCodeCheckDTO.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        r"""Sets the user of this SlideVerifyCodeCheckDTO.

        必须和发送验证码时带的用户身份信息相同。 

        :param user: The user of this SlideVerifyCodeCheckDTO.
        :type user: str
        """
        self._user = user

    @property
    def client_type(self):
        r"""Gets the client_type of this SlideVerifyCodeCheckDTO.

        登录客户端类型。 * 0：Web客户端类型 * 5：PC客户端 * 6：移动客户端 

        :return: The client_type of this SlideVerifyCodeCheckDTO.
        :rtype: int
        """
        return self._client_type

    @client_type.setter
    def client_type(self, client_type):
        r"""Sets the client_type of this SlideVerifyCodeCheckDTO.

        登录客户端类型。 * 0：Web客户端类型 * 5：PC客户端 * 6：移动客户端 

        :param client_type: The client_type of this SlideVerifyCodeCheckDTO.
        :type client_type: int
        """
        self._client_type = client_type

    @property
    def check_type(self):
        r"""Gets the check_type of this SlideVerifyCodeCheckDTO.

        校验类型。默认值：0。 * 0：登录； * 1：忘记密码; 

        :return: The check_type of this SlideVerifyCodeCheckDTO.
        :rtype: int
        """
        return self._check_type

    @check_type.setter
    def check_type(self, check_type):
        r"""Sets the check_type of this SlideVerifyCodeCheckDTO.

        校验类型。默认值：0。 * 0：登录； * 1：忘记密码; 

        :param check_type: The check_type of this SlideVerifyCodeCheckDTO.
        :type check_type: int
        """
        self._check_type = check_type

    @property
    def token(self):
        r"""Gets the token of this SlideVerifyCodeCheckDTO.

        验证码Token字符串。通过[[发送滑块验证码](https://support.huaweicloud.com/api-meeting/meeting_21_0100.html)](tag:hws)[[发送滑块验证码](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0100.html)](tag:hk) 接口获取。 

        :return: The token of this SlideVerifyCodeCheckDTO.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        r"""Sets the token of this SlideVerifyCodeCheckDTO.

        验证码Token字符串。通过[[发送滑块验证码](https://support.huaweicloud.com/api-meeting/meeting_21_0100.html)](tag:hws)[[发送滑块验证码](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0100.html)](tag:hk) 接口获取。 

        :param token: The token of this SlideVerifyCodeCheckDTO.
        :type token: str
        """
        self._token = token

    @property
    def point_x(self):
        r"""Gets the point_x of this SlideVerifyCodeCheckDTO.

        抠出图形的X轴坐标。

        :return: The point_x of this SlideVerifyCodeCheckDTO.
        :rtype: int
        """
        return self._point_x

    @point_x.setter
    def point_x(self, point_x):
        r"""Sets the point_x of this SlideVerifyCodeCheckDTO.

        抠出图形的X轴坐标。

        :param point_x: The point_x of this SlideVerifyCodeCheckDTO.
        :type point_x: int
        """
        self._point_x = point_x

    @property
    def slide_time(self):
        r"""Gets the slide_time of this SlideVerifyCodeCheckDTO.

        滑动时间，单位ms。

        :return: The slide_time of this SlideVerifyCodeCheckDTO.
        :rtype: int
        """
        return self._slide_time

    @slide_time.setter
    def slide_time(self, slide_time):
        r"""Sets the slide_time of this SlideVerifyCodeCheckDTO.

        滑动时间，单位ms。

        :param slide_time: The slide_time of this SlideVerifyCodeCheckDTO.
        :type slide_time: int
        """
        self._slide_time = slide_time

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
        if not isinstance(other, SlideVerifyCodeCheckDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
