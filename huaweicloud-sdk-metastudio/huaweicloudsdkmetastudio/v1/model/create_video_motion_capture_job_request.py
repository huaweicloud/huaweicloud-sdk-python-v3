# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateVideoMotionCaptureJobRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_app_user_id': 'str',
        'x_user_privilege': 'str',
        'body': 'VideoMotionCaptureJobReq'
    }

    attribute_map = {
        'x_app_user_id': 'X-App-UserId',
        'x_user_privilege': 'X-User-Privilege',
        'body': 'body'
    }

    def __init__(self, x_app_user_id=None, x_user_privilege=None, body=None):
        """CreateVideoMotionCaptureJobRequest

        The model defined in huaweicloud sdk

        :param x_app_user_id: 开发者应用作为资产权属的可选字段。
        :type x_app_user_id: str
        :param x_user_privilege: 测试用户判断。
        :type x_user_privilege: str
        :param body: Body of the CreateVideoMotionCaptureJobRequest
        :type body: :class:`huaweicloudsdkmetastudio.v1.VideoMotionCaptureJobReq`
        """
        
        

        self._x_app_user_id = None
        self._x_user_privilege = None
        self._body = None
        self.discriminator = None

        if x_app_user_id is not None:
            self.x_app_user_id = x_app_user_id
        if x_user_privilege is not None:
            self.x_user_privilege = x_user_privilege
        if body is not None:
            self.body = body

    @property
    def x_app_user_id(self):
        """Gets the x_app_user_id of this CreateVideoMotionCaptureJobRequest.

        开发者应用作为资产权属的可选字段。

        :return: The x_app_user_id of this CreateVideoMotionCaptureJobRequest.
        :rtype: str
        """
        return self._x_app_user_id

    @x_app_user_id.setter
    def x_app_user_id(self, x_app_user_id):
        """Sets the x_app_user_id of this CreateVideoMotionCaptureJobRequest.

        开发者应用作为资产权属的可选字段。

        :param x_app_user_id: The x_app_user_id of this CreateVideoMotionCaptureJobRequest.
        :type x_app_user_id: str
        """
        self._x_app_user_id = x_app_user_id

    @property
    def x_user_privilege(self):
        """Gets the x_user_privilege of this CreateVideoMotionCaptureJobRequest.

        测试用户判断。

        :return: The x_user_privilege of this CreateVideoMotionCaptureJobRequest.
        :rtype: str
        """
        return self._x_user_privilege

    @x_user_privilege.setter
    def x_user_privilege(self, x_user_privilege):
        """Sets the x_user_privilege of this CreateVideoMotionCaptureJobRequest.

        测试用户判断。

        :param x_user_privilege: The x_user_privilege of this CreateVideoMotionCaptureJobRequest.
        :type x_user_privilege: str
        """
        self._x_user_privilege = x_user_privilege

    @property
    def body(self):
        """Gets the body of this CreateVideoMotionCaptureJobRequest.

        :return: The body of this CreateVideoMotionCaptureJobRequest.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.VideoMotionCaptureJobReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CreateVideoMotionCaptureJobRequest.

        :param body: The body of this CreateVideoMotionCaptureJobRequest.
        :type body: :class:`huaweicloudsdkmetastudio.v1.VideoMotionCaptureJobReq`
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
        if not isinstance(other, CreateVideoMotionCaptureJobRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
