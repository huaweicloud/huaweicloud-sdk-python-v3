# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateMyActionTemplateRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'template_name': 'str',
        'body': 'ThirdTemplateRequestBody'
    }

    attribute_map = {
        'template_name': 'template_name',
        'body': 'body'
    }

    def __init__(self, template_name=None, body=None):
        r"""CreateMyActionTemplateRequest

        The model defined in huaweicloud sdk

        :param template_name: 算子名称，名称必须以以third开头，只能由字母、数字、下划线和中划线组成，长度小于等于64个字符，且不能重名。
        :type template_name: str
        :param body: Body of the CreateMyActionTemplateRequest
        :type body: :class:`huaweicloudsdkdwr.v3.ThirdTemplateRequestBody`
        """
        
        

        self._template_name = None
        self._body = None
        self.discriminator = None

        self.template_name = template_name
        if body is not None:
            self.body = body

    @property
    def template_name(self):
        r"""Gets the template_name of this CreateMyActionTemplateRequest.

        算子名称，名称必须以以third开头，只能由字母、数字、下划线和中划线组成，长度小于等于64个字符，且不能重名。

        :return: The template_name of this CreateMyActionTemplateRequest.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        r"""Sets the template_name of this CreateMyActionTemplateRequest.

        算子名称，名称必须以以third开头，只能由字母、数字、下划线和中划线组成，长度小于等于64个字符，且不能重名。

        :param template_name: The template_name of this CreateMyActionTemplateRequest.
        :type template_name: str
        """
        self._template_name = template_name

    @property
    def body(self):
        r"""Gets the body of this CreateMyActionTemplateRequest.

        :return: The body of this CreateMyActionTemplateRequest.
        :rtype: :class:`huaweicloudsdkdwr.v3.ThirdTemplateRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this CreateMyActionTemplateRequest.

        :param body: The body of this CreateMyActionTemplateRequest.
        :type body: :class:`huaweicloudsdkdwr.v3.ThirdTemplateRequestBody`
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
        if not isinstance(other, CreateMyActionTemplateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
