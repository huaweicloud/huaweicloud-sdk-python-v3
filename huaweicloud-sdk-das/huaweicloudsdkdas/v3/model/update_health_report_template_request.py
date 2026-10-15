# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateHealthReportTemplateRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'template_id': 'str',
        'x_language': 'str',
        'body': 'UpdateHealthReportTemplateReq'
    }

    attribute_map = {
        'template_id': 'template_id',
        'x_language': 'X-Language',
        'body': 'body'
    }

    def __init__(self, template_id=None, x_language=None, body=None):
        r"""UpdateHealthReportTemplateRequest

        The model defined in huaweicloud sdk

        :param template_id: 健康报告模板ID。
        :type template_id: str
        :param x_language: 请求语言类型。en-us：英文。 zh-cn：中文。
        :type x_language: str
        :param body: Body of the UpdateHealthReportTemplateRequest
        :type body: :class:`huaweicloudsdkdas.v3.UpdateHealthReportTemplateReq`
        """
        
        

        self._template_id = None
        self._x_language = None
        self._body = None
        self.discriminator = None

        self.template_id = template_id
        if x_language is not None:
            self.x_language = x_language
        if body is not None:
            self.body = body

    @property
    def template_id(self):
        r"""Gets the template_id of this UpdateHealthReportTemplateRequest.

        健康报告模板ID。

        :return: The template_id of this UpdateHealthReportTemplateRequest.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this UpdateHealthReportTemplateRequest.

        健康报告模板ID。

        :param template_id: The template_id of this UpdateHealthReportTemplateRequest.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def x_language(self):
        r"""Gets the x_language of this UpdateHealthReportTemplateRequest.

        请求语言类型。en-us：英文。 zh-cn：中文。

        :return: The x_language of this UpdateHealthReportTemplateRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this UpdateHealthReportTemplateRequest.

        请求语言类型。en-us：英文。 zh-cn：中文。

        :param x_language: The x_language of this UpdateHealthReportTemplateRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def body(self):
        r"""Gets the body of this UpdateHealthReportTemplateRequest.

        :return: The body of this UpdateHealthReportTemplateRequest.
        :rtype: :class:`huaweicloudsdkdas.v3.UpdateHealthReportTemplateReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateHealthReportTemplateRequest.

        :param body: The body of this UpdateHealthReportTemplateRequest.
        :type body: :class:`huaweicloudsdkdas.v3.UpdateHealthReportTemplateReq`
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
        if not isinstance(other, UpdateHealthReportTemplateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
