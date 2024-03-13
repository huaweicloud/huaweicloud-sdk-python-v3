# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetUserProfileImageRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_request_id': 'str',
        'user_id': 'str',
        'body': 'SetUserProfileImageRequestBody'
    }

    attribute_map = {
        'x_request_id': 'X-Request-Id',
        'user_id': 'user_id',
        'body': 'body'
    }

    def __init__(self, x_request_id=None, user_id=None, body=None):
        """SetUserProfileImageRequest

        The model defined in huaweicloud sdk

        :param x_request_id: 请求requestId，用来标识一路请求，用于问题跟踪定位，建议使用UUID，若不携带，则后台自动生成。
        :type x_request_id: str
        :param user_id: 设置头像的企业用户id
        :type user_id: str
        :param body: Body of the SetUserProfileImageRequest
        :type body: :class:`huaweicloudsdkmeeting.v1.SetUserProfileImageRequestBody`
        """
        
        

        self._x_request_id = None
        self._user_id = None
        self._body = None
        self.discriminator = None

        if x_request_id is not None:
            self.x_request_id = x_request_id
        self.user_id = user_id
        if body is not None:
            self.body = body

    @property
    def x_request_id(self):
        """Gets the x_request_id of this SetUserProfileImageRequest.

        请求requestId，用来标识一路请求，用于问题跟踪定位，建议使用UUID，若不携带，则后台自动生成。

        :return: The x_request_id of this SetUserProfileImageRequest.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this SetUserProfileImageRequest.

        请求requestId，用来标识一路请求，用于问题跟踪定位，建议使用UUID，若不携带，则后台自动生成。

        :param x_request_id: The x_request_id of this SetUserProfileImageRequest.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    @property
    def user_id(self):
        """Gets the user_id of this SetUserProfileImageRequest.

        设置头像的企业用户id

        :return: The user_id of this SetUserProfileImageRequest.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this SetUserProfileImageRequest.

        设置头像的企业用户id

        :param user_id: The user_id of this SetUserProfileImageRequest.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def body(self):
        """Gets the body of this SetUserProfileImageRequest.

        :return: The body of this SetUserProfileImageRequest.
        :rtype: :class:`huaweicloudsdkmeeting.v1.SetUserProfileImageRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this SetUserProfileImageRequest.

        :param body: The body of this SetUserProfileImageRequest.
        :type body: :class:`huaweicloudsdkmeeting.v1.SetUserProfileImageRequestBody`
        """
        self._body = body

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
        if not isinstance(other, SetUserProfileImageRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
