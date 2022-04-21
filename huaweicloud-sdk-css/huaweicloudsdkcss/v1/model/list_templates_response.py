# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTemplatesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'system_templates': 'list[SystemTemplates]',
        'custom_templates': 'list[CustomTemplates]'
    }

    attribute_map = {
        'system_templates': 'systemTemplates',
        'custom_templates': 'customTemplates'
    }

    def __init__(self, system_templates=None, custom_templates=None):
        """ListTemplatesResponse

        The model defined in huaweicloud sdk

        :param system_templates: 系统模板列表。
        :type system_templates: list[:class:`huaweicloudsdkcss.v1.SystemTemplates`]
        :param custom_templates: 自定义模板列表。
        :type custom_templates: list[:class:`huaweicloudsdkcss.v1.CustomTemplates`]
        """
        
        super(ListTemplatesResponse, self).__init__()

        self._system_templates = None
        self._custom_templates = None
        self.discriminator = None

        if system_templates is not None:
            self.system_templates = system_templates
        if custom_templates is not None:
            self.custom_templates = custom_templates

    @property
    def system_templates(self):
        """Gets the system_templates of this ListTemplatesResponse.

        系统模板列表。

        :return: The system_templates of this ListTemplatesResponse.
        :rtype: list[:class:`huaweicloudsdkcss.v1.SystemTemplates`]
        """
        return self._system_templates

    @system_templates.setter
    def system_templates(self, system_templates):
        """Sets the system_templates of this ListTemplatesResponse.

        系统模板列表。

        :param system_templates: The system_templates of this ListTemplatesResponse.
        :type system_templates: list[:class:`huaweicloudsdkcss.v1.SystemTemplates`]
        """
        self._system_templates = system_templates

    @property
    def custom_templates(self):
        """Gets the custom_templates of this ListTemplatesResponse.

        自定义模板列表。

        :return: The custom_templates of this ListTemplatesResponse.
        :rtype: list[:class:`huaweicloudsdkcss.v1.CustomTemplates`]
        """
        return self._custom_templates

    @custom_templates.setter
    def custom_templates(self, custom_templates):
        """Sets the custom_templates of this ListTemplatesResponse.

        自定义模板列表。

        :param custom_templates: The custom_templates of this ListTemplatesResponse.
        :type custom_templates: list[:class:`huaweicloudsdkcss.v1.CustomTemplates`]
        """
        self._custom_templates = custom_templates

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
        if not isinstance(other, ListTemplatesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
