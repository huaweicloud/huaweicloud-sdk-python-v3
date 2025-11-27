# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEmailTemplateResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'email_template_list': 'list[EmailTemplate]'
    }

    attribute_map = {
        'total': 'total',
        'email_template_list': 'email_template_list'
    }

    def __init__(self, total=None, email_template_list=None):
        r"""ListEmailTemplateResponse

        The model defined in huaweicloud sdk

        :param total: 总数
        :type total: int
        :param email_template_list: 邮件模板列表
        :type email_template_list: list[:class:`huaweicloudsdkdas.v3.EmailTemplate`]
        """
        
        super().__init__()

        self._total = None
        self._email_template_list = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if email_template_list is not None:
            self.email_template_list = email_template_list

    @property
    def total(self):
        r"""Gets the total of this ListEmailTemplateResponse.

        总数

        :return: The total of this ListEmailTemplateResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListEmailTemplateResponse.

        总数

        :param total: The total of this ListEmailTemplateResponse.
        :type total: int
        """
        self._total = total

    @property
    def email_template_list(self):
        r"""Gets the email_template_list of this ListEmailTemplateResponse.

        邮件模板列表

        :return: The email_template_list of this ListEmailTemplateResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.EmailTemplate`]
        """
        return self._email_template_list

    @email_template_list.setter
    def email_template_list(self, email_template_list):
        r"""Sets the email_template_list of this ListEmailTemplateResponse.

        邮件模板列表

        :param email_template_list: The email_template_list of this ListEmailTemplateResponse.
        :type email_template_list: list[:class:`huaweicloudsdkdas.v3.EmailTemplate`]
        """
        self._email_template_list = email_template_list

    def to_dict(self):
        import warnings
        warnings.warn("ListEmailTemplateResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ListEmailTemplateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
