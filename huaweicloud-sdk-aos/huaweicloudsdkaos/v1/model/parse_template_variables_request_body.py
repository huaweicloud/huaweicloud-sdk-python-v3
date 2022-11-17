# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ParseTemplateVariablesRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'template_body': 'str',
        'template_uri': 'str'
    }

    attribute_map = {
        'template_body': 'template_body',
        'template_uri': 'template_uri'
    }

    def __init__(self, template_body=None, template_uri=None):
        """ParseTemplateVariablesRequestBody

        The model defined in huaweicloud sdk

        :param template_body: HCL模板，描述了资源的目标状态 template_body 和 template_uri 有且仅有一个存在
        :type template_body: str
        :param template_uri: HCL模板文件的uri，代码需从该uri下载HCL模板获取模板内容。其描述了资源的目标状态 template_body 和 template_uri 有且仅有一个存在
        :type template_uri: str
        """
        
        

        self._template_body = None
        self._template_uri = None
        self.discriminator = None

        if template_body is not None:
            self.template_body = template_body
        if template_uri is not None:
            self.template_uri = template_uri

    @property
    def template_body(self):
        """Gets the template_body of this ParseTemplateVariablesRequestBody.

        HCL模板，描述了资源的目标状态 template_body 和 template_uri 有且仅有一个存在

        :return: The template_body of this ParseTemplateVariablesRequestBody.
        :rtype: str
        """
        return self._template_body

    @template_body.setter
    def template_body(self, template_body):
        """Sets the template_body of this ParseTemplateVariablesRequestBody.

        HCL模板，描述了资源的目标状态 template_body 和 template_uri 有且仅有一个存在

        :param template_body: The template_body of this ParseTemplateVariablesRequestBody.
        :type template_body: str
        """
        self._template_body = template_body

    @property
    def template_uri(self):
        """Gets the template_uri of this ParseTemplateVariablesRequestBody.

        HCL模板文件的uri，代码需从该uri下载HCL模板获取模板内容。其描述了资源的目标状态 template_body 和 template_uri 有且仅有一个存在

        :return: The template_uri of this ParseTemplateVariablesRequestBody.
        :rtype: str
        """
        return self._template_uri

    @template_uri.setter
    def template_uri(self, template_uri):
        """Sets the template_uri of this ParseTemplateVariablesRequestBody.

        HCL模板文件的uri，代码需从该uri下载HCL模板获取模板内容。其描述了资源的目标状态 template_body 和 template_uri 有且仅有一个存在

        :param template_uri: The template_uri of this ParseTemplateVariablesRequestBody.
        :type template_uri: str
        """
        self._template_uri = template_uri

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
        if not isinstance(other, ParseTemplateVariablesRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
