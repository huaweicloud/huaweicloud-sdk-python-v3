# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTemplateVersionRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'version_description': 'str',
        'template_body': 'str',
        'template_uri': 'str'
    }

    attribute_map = {
        'version_description': 'version_description',
        'template_body': 'template_body',
        'template_uri': 'template_uri'
    }

    def __init__(self, version_description=None, template_body=None, template_uri=None):
        r"""CreateTemplateVersionRequestBody

        The model defined in huaweicloud sdk

        :param version_description: 模板版本的描述。可用于客户识别自己的模板版本
        :type version_description: str
        :param template_body: HCL模板，描述了模板中使用的资源 template_body 和 template_uri 有且仅有一个存在
        :type template_body: str
        :param template_uri: HCL模板的obs链接，该模板描述了资源的目标状态  对应的文件应该是纯tf文件或zip压缩包  纯tf文件需要以&#x60;.tf&#x60;或者&#x60;.tf.json&#x60;结尾，并遵守hcl语法  压缩包目前只支持zip格式，文件需要以\&quot;.zip\&quot;结尾。解压后的文件不得包含\&quot;.tfvars\&quot;文件  template_body 和 template_uri 有且仅有一个存在
        :type template_uri: str
        """
        
        

        self._version_description = None
        self._template_body = None
        self._template_uri = None
        self.discriminator = None

        if version_description is not None:
            self.version_description = version_description
        if template_body is not None:
            self.template_body = template_body
        if template_uri is not None:
            self.template_uri = template_uri

    @property
    def version_description(self):
        r"""Gets the version_description of this CreateTemplateVersionRequestBody.

        模板版本的描述。可用于客户识别自己的模板版本

        :return: The version_description of this CreateTemplateVersionRequestBody.
        :rtype: str
        """
        return self._version_description

    @version_description.setter
    def version_description(self, version_description):
        r"""Sets the version_description of this CreateTemplateVersionRequestBody.

        模板版本的描述。可用于客户识别自己的模板版本

        :param version_description: The version_description of this CreateTemplateVersionRequestBody.
        :type version_description: str
        """
        self._version_description = version_description

    @property
    def template_body(self):
        r"""Gets the template_body of this CreateTemplateVersionRequestBody.

        HCL模板，描述了模板中使用的资源 template_body 和 template_uri 有且仅有一个存在

        :return: The template_body of this CreateTemplateVersionRequestBody.
        :rtype: str
        """
        return self._template_body

    @template_body.setter
    def template_body(self, template_body):
        r"""Sets the template_body of this CreateTemplateVersionRequestBody.

        HCL模板，描述了模板中使用的资源 template_body 和 template_uri 有且仅有一个存在

        :param template_body: The template_body of this CreateTemplateVersionRequestBody.
        :type template_body: str
        """
        self._template_body = template_body

    @property
    def template_uri(self):
        r"""Gets the template_uri of this CreateTemplateVersionRequestBody.

        HCL模板的obs链接，该模板描述了资源的目标状态  对应的文件应该是纯tf文件或zip压缩包  纯tf文件需要以`.tf`或者`.tf.json`结尾，并遵守hcl语法  压缩包目前只支持zip格式，文件需要以\".zip\"结尾。解压后的文件不得包含\".tfvars\"文件  template_body 和 template_uri 有且仅有一个存在

        :return: The template_uri of this CreateTemplateVersionRequestBody.
        :rtype: str
        """
        return self._template_uri

    @template_uri.setter
    def template_uri(self, template_uri):
        r"""Sets the template_uri of this CreateTemplateVersionRequestBody.

        HCL模板的obs链接，该模板描述了资源的目标状态  对应的文件应该是纯tf文件或zip压缩包  纯tf文件需要以`.tf`或者`.tf.json`结尾，并遵守hcl语法  压缩包目前只支持zip格式，文件需要以\".zip\"结尾。解压后的文件不得包含\".tfvars\"文件  template_body 和 template_uri 有且仅有一个存在

        :param template_uri: The template_uri of this CreateTemplateVersionRequestBody.
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
        if not isinstance(other, CreateTemplateVersionRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
