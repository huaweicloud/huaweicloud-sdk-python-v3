# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTemplateResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'template': 'TemplateResponseBody'
    }

    attribute_map = {
        'template': 'template'
    }

    def __init__(self, template=None):
        r"""ShowTemplateResponse

        The model defined in huaweicloud sdk

        :param template: 
        :type template: :class:`huaweicloudsdksms.v3.TemplateResponseBody`
        """
        
        super(ShowTemplateResponse, self).__init__()

        self._template = None
        self.discriminator = None

        if template is not None:
            self.template = template

    @property
    def template(self):
        r"""Gets the template of this ShowTemplateResponse.

        :return: The template of this ShowTemplateResponse.
        :rtype: :class:`huaweicloudsdksms.v3.TemplateResponseBody`
        """
        return self._template

    @template.setter
    def template(self, template):
        r"""Sets the template of this ShowTemplateResponse.

        :param template: The template of this ShowTemplateResponse.
        :type template: :class:`huaweicloudsdksms.v3.TemplateResponseBody`
        """
        self._template = template

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
        if not isinstance(other, ShowTemplateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
