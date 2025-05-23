# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateRecordRuleRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'content_type': 'str',
        'authorization': 'str',
        'x_sdk_date': 'str',
        'x_project_id': 'str',
        'app_id': 'str',
        'body': 'RecordRuleReq'
    }

    attribute_map = {
        'content_type': 'Content-Type',
        'authorization': 'Authorization',
        'x_sdk_date': 'X-Sdk-Date',
        'x_project_id': 'X-Project-Id',
        'app_id': 'app_id',
        'body': 'body'
    }

    def __init__(self, content_type=None, authorization=None, x_sdk_date=None, x_project_id=None, app_id=None, body=None):
        r"""CreateRecordRuleRequest

        The model defined in huaweicloud sdk

        :param content_type: 内容类型。
        :type content_type: str
        :param authorization: 使用AK/SK方式认证时必选，携带的鉴权信息。
        :type authorization: str
        :param x_sdk_date: 使用AK/SK方式认证时必选，请求的发生时间。
        :type x_sdk_date: str
        :param x_project_id: 使用AK/SK方式认证时必选，携带项目ID信息。
        :type x_project_id: str
        :param app_id: 应用id
        :type app_id: str
        :param body: Body of the CreateRecordRuleRequest
        :type body: :class:`huaweicloudsdkcloudrtc.v2.RecordRuleReq`
        """
        
        

        self._content_type = None
        self._authorization = None
        self._x_sdk_date = None
        self._x_project_id = None
        self._app_id = None
        self._body = None
        self.discriminator = None

        self.content_type = content_type
        if authorization is not None:
            self.authorization = authorization
        if x_sdk_date is not None:
            self.x_sdk_date = x_sdk_date
        if x_project_id is not None:
            self.x_project_id = x_project_id
        self.app_id = app_id
        if body is not None:
            self.body = body

    @property
    def content_type(self):
        r"""Gets the content_type of this CreateRecordRuleRequest.

        内容类型。

        :return: The content_type of this CreateRecordRuleRequest.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        r"""Sets the content_type of this CreateRecordRuleRequest.

        内容类型。

        :param content_type: The content_type of this CreateRecordRuleRequest.
        :type content_type: str
        """
        self._content_type = content_type

    @property
    def authorization(self):
        r"""Gets the authorization of this CreateRecordRuleRequest.

        使用AK/SK方式认证时必选，携带的鉴权信息。

        :return: The authorization of this CreateRecordRuleRequest.
        :rtype: str
        """
        return self._authorization

    @authorization.setter
    def authorization(self, authorization):
        r"""Sets the authorization of this CreateRecordRuleRequest.

        使用AK/SK方式认证时必选，携带的鉴权信息。

        :param authorization: The authorization of this CreateRecordRuleRequest.
        :type authorization: str
        """
        self._authorization = authorization

    @property
    def x_sdk_date(self):
        r"""Gets the x_sdk_date of this CreateRecordRuleRequest.

        使用AK/SK方式认证时必选，请求的发生时间。

        :return: The x_sdk_date of this CreateRecordRuleRequest.
        :rtype: str
        """
        return self._x_sdk_date

    @x_sdk_date.setter
    def x_sdk_date(self, x_sdk_date):
        r"""Sets the x_sdk_date of this CreateRecordRuleRequest.

        使用AK/SK方式认证时必选，请求的发生时间。

        :param x_sdk_date: The x_sdk_date of this CreateRecordRuleRequest.
        :type x_sdk_date: str
        """
        self._x_sdk_date = x_sdk_date

    @property
    def x_project_id(self):
        r"""Gets the x_project_id of this CreateRecordRuleRequest.

        使用AK/SK方式认证时必选，携带项目ID信息。

        :return: The x_project_id of this CreateRecordRuleRequest.
        :rtype: str
        """
        return self._x_project_id

    @x_project_id.setter
    def x_project_id(self, x_project_id):
        r"""Sets the x_project_id of this CreateRecordRuleRequest.

        使用AK/SK方式认证时必选，携带项目ID信息。

        :param x_project_id: The x_project_id of this CreateRecordRuleRequest.
        :type x_project_id: str
        """
        self._x_project_id = x_project_id

    @property
    def app_id(self):
        r"""Gets the app_id of this CreateRecordRuleRequest.

        应用id

        :return: The app_id of this CreateRecordRuleRequest.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this CreateRecordRuleRequest.

        应用id

        :param app_id: The app_id of this CreateRecordRuleRequest.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def body(self):
        r"""Gets the body of this CreateRecordRuleRequest.

        :return: The body of this CreateRecordRuleRequest.
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.RecordRuleReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this CreateRecordRuleRequest.

        :param body: The body of this CreateRecordRuleRequest.
        :type body: :class:`huaweicloudsdkcloudrtc.v2.RecordRuleReq`
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
        if not isinstance(other, CreateRecordRuleRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
