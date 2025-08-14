# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListApplicationTemplatesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'application_templates': 'list[ApplicationTemplateDto]'
    }

    attribute_map = {
        'application_templates': 'application_templates'
    }

    def __init__(self, application_templates=None):
        r"""ListApplicationTemplatesResponse

        The model defined in huaweicloud sdk

        :param application_templates: 应用程序模板列表
        :type application_templates: list[:class:`huaweicloudsdkidentitycenter.v1.ApplicationTemplateDto`]
        """
        
        super(ListApplicationTemplatesResponse, self).__init__()

        self._application_templates = None
        self.discriminator = None

        if application_templates is not None:
            self.application_templates = application_templates

    @property
    def application_templates(self):
        r"""Gets the application_templates of this ListApplicationTemplatesResponse.

        应用程序模板列表

        :return: The application_templates of this ListApplicationTemplatesResponse.
        :rtype: list[:class:`huaweicloudsdkidentitycenter.v1.ApplicationTemplateDto`]
        """
        return self._application_templates

    @application_templates.setter
    def application_templates(self, application_templates):
        r"""Sets the application_templates of this ListApplicationTemplatesResponse.

        应用程序模板列表

        :param application_templates: The application_templates of this ListApplicationTemplatesResponse.
        :type application_templates: list[:class:`huaweicloudsdkidentitycenter.v1.ApplicationTemplateDto`]
        """
        self._application_templates = application_templates

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
        if not isinstance(other, ListApplicationTemplatesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
