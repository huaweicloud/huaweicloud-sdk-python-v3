# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListNotificationTemplateResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'template': 'str'
    }

    attribute_map = {
        'template': 'template'
    }

    def __init__(self, template=None):
        r"""ListNotificationTemplateResponse

        The model defined in huaweicloud sdk

        :param template: 为一个html文本，需要进行相应的解析后展示
        :type template: str
        """
        
        super().__init__()

        self._template = None
        self.discriminator = None

        if template is not None:
            self.template = template

    @property
    def template(self):
        r"""Gets the template of this ListNotificationTemplateResponse.

        为一个html文本，需要进行相应的解析后展示

        :return: The template of this ListNotificationTemplateResponse.
        :rtype: str
        """
        return self._template

    @template.setter
    def template(self, template):
        r"""Sets the template of this ListNotificationTemplateResponse.

        为一个html文本，需要进行相应的解析后展示

        :param template: The template of this ListNotificationTemplateResponse.
        :type template: str
        """
        self._template = template

    def to_dict(self):
        import warnings
        warnings.warn("ListNotificationTemplateResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListNotificationTemplateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
