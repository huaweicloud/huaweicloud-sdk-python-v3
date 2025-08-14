# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTemplateVersionRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'client_request_id': 'str',
        'template_name': 'str',
        'template_id': 'str',
        'body': 'CreateTemplateVersionRequestBody'
    }

    attribute_map = {
        'client_request_id': 'Client-Request-Id',
        'template_name': 'template_name',
        'template_id': 'template_id',
        'body': 'body'
    }

    def __init__(self, client_request_id=None, template_name=None, template_id=None, body=None):
        r"""CreateTemplateVersionRequest

        The model defined in huaweicloud sdk

        :param client_request_id: 用户指定的，对于此请求的唯一ID，用于定位某个请求，推荐使用UUID
        :type client_request_id: str
        :param template_name: 模板（Template）的名字。此名字在domain_id+region下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。
        :type template_name: str
        :param template_id: 模板的ID。当template_id存在时，模板服务会检查template_id是否和template_name匹配，不匹配会返回400
        :type template_id: str
        :param body: Body of the CreateTemplateVersionRequest
        :type body: :class:`huaweicloudsdkaos.v1.CreateTemplateVersionRequestBody`
        """
        
        

        self._client_request_id = None
        self._template_name = None
        self._template_id = None
        self._body = None
        self.discriminator = None

        self.client_request_id = client_request_id
        self.template_name = template_name
        if template_id is not None:
            self.template_id = template_id
        if body is not None:
            self.body = body

    @property
    def client_request_id(self):
        r"""Gets the client_request_id of this CreateTemplateVersionRequest.

        用户指定的，对于此请求的唯一ID，用于定位某个请求，推荐使用UUID

        :return: The client_request_id of this CreateTemplateVersionRequest.
        :rtype: str
        """
        return self._client_request_id

    @client_request_id.setter
    def client_request_id(self, client_request_id):
        r"""Sets the client_request_id of this CreateTemplateVersionRequest.

        用户指定的，对于此请求的唯一ID，用于定位某个请求，推荐使用UUID

        :param client_request_id: The client_request_id of this CreateTemplateVersionRequest.
        :type client_request_id: str
        """
        self._client_request_id = client_request_id

    @property
    def template_name(self):
        r"""Gets the template_name of this CreateTemplateVersionRequest.

        模板（Template）的名字。此名字在domain_id+region下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。

        :return: The template_name of this CreateTemplateVersionRequest.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        r"""Sets the template_name of this CreateTemplateVersionRequest.

        模板（Template）的名字。此名字在domain_id+region下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。

        :param template_name: The template_name of this CreateTemplateVersionRequest.
        :type template_name: str
        """
        self._template_name = template_name

    @property
    def template_id(self):
        r"""Gets the template_id of this CreateTemplateVersionRequest.

        模板的ID。当template_id存在时，模板服务会检查template_id是否和template_name匹配，不匹配会返回400

        :return: The template_id of this CreateTemplateVersionRequest.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this CreateTemplateVersionRequest.

        模板的ID。当template_id存在时，模板服务会检查template_id是否和template_name匹配，不匹配会返回400

        :param template_id: The template_id of this CreateTemplateVersionRequest.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def body(self):
        r"""Gets the body of this CreateTemplateVersionRequest.

        :return: The body of this CreateTemplateVersionRequest.
        :rtype: :class:`huaweicloudsdkaos.v1.CreateTemplateVersionRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this CreateTemplateVersionRequest.

        :param body: The body of this CreateTemplateVersionRequest.
        :type body: :class:`huaweicloudsdkaos.v1.CreateTemplateVersionRequestBody`
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
        if not isinstance(other, CreateTemplateVersionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
