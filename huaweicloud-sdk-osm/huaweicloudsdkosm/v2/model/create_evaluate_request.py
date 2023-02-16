# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateEvaluateRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_service_key': 'str',
        'x_site': 'str',
        'x_language': 'str',
        'session_id': 'str',
        'request_id': 'str',
        'body': 'EvaluateRequestReq'
    }

    attribute_map = {
        'x_service_key': 'x-service-key',
        'x_site': 'x-site',
        'x_language': 'x-language',
        'session_id': 'session_id',
        'request_id': 'request_id',
        'body': 'body'
    }

    def __init__(self, x_service_key=None, x_site=None, x_language=None, session_id=None, request_id=None, body=None):
        """CreateEvaluateRequest

        The model defined in huaweicloud sdk

        :param x_service_key: 调用智能客服服务标志。
        :type x_service_key: str
        :param x_site: 站点标记，0-中国站  1-国际站
        :type x_site: str
        :param x_language: 区域语言简写，en-us  zh-cn
        :type x_language: str
        :param session_id: 会话Id
        :type session_id: str
        :param request_id: 请求Id
        :type request_id: str
        :param body: Body of the CreateEvaluateRequest
        :type body: :class:`huaweicloudsdkosm.v2.EvaluateRequestReq`
        """
        
        

        self._x_service_key = None
        self._x_site = None
        self._x_language = None
        self._session_id = None
        self._request_id = None
        self._body = None
        self.discriminator = None

        self.x_service_key = x_service_key
        if x_site is not None:
            self.x_site = x_site
        if x_language is not None:
            self.x_language = x_language
        self.session_id = session_id
        self.request_id = request_id
        if body is not None:
            self.body = body

    @property
    def x_service_key(self):
        """Gets the x_service_key of this CreateEvaluateRequest.

        调用智能客服服务标志。

        :return: The x_service_key of this CreateEvaluateRequest.
        :rtype: str
        """
        return self._x_service_key

    @x_service_key.setter
    def x_service_key(self, x_service_key):
        """Sets the x_service_key of this CreateEvaluateRequest.

        调用智能客服服务标志。

        :param x_service_key: The x_service_key of this CreateEvaluateRequest.
        :type x_service_key: str
        """
        self._x_service_key = x_service_key

    @property
    def x_site(self):
        """Gets the x_site of this CreateEvaluateRequest.

        站点标记，0-中国站  1-国际站

        :return: The x_site of this CreateEvaluateRequest.
        :rtype: str
        """
        return self._x_site

    @x_site.setter
    def x_site(self, x_site):
        """Sets the x_site of this CreateEvaluateRequest.

        站点标记，0-中国站  1-国际站

        :param x_site: The x_site of this CreateEvaluateRequest.
        :type x_site: str
        """
        self._x_site = x_site

    @property
    def x_language(self):
        """Gets the x_language of this CreateEvaluateRequest.

        区域语言简写，en-us  zh-cn

        :return: The x_language of this CreateEvaluateRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this CreateEvaluateRequest.

        区域语言简写，en-us  zh-cn

        :param x_language: The x_language of this CreateEvaluateRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def session_id(self):
        """Gets the session_id of this CreateEvaluateRequest.

        会话Id

        :return: The session_id of this CreateEvaluateRequest.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """Sets the session_id of this CreateEvaluateRequest.

        会话Id

        :param session_id: The session_id of this CreateEvaluateRequest.
        :type session_id: str
        """
        self._session_id = session_id

    @property
    def request_id(self):
        """Gets the request_id of this CreateEvaluateRequest.

        请求Id

        :return: The request_id of this CreateEvaluateRequest.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this CreateEvaluateRequest.

        请求Id

        :param request_id: The request_id of this CreateEvaluateRequest.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def body(self):
        """Gets the body of this CreateEvaluateRequest.

        :return: The body of this CreateEvaluateRequest.
        :rtype: :class:`huaweicloudsdkosm.v2.EvaluateRequestReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CreateEvaluateRequest.

        :param body: The body of this CreateEvaluateRequest.
        :type body: :class:`huaweicloudsdkosm.v2.EvaluateRequestReq`
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
        if not isinstance(other, CreateEvaluateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
