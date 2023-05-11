# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateTemplateMetadataRequestBody:

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
        'template_description': 'str'
    }

    attribute_map = {
        'template_id': 'template_id',
        'template_description': 'template_description'
    }

    def __init__(self, template_id=None, template_description=None):
        """UpdateTemplateMetadataRequestBody

        The model defined in huaweicloud sdk

        :param template_id: 模板的唯一ID，由模板服务随机生成
        :type template_id: str
        :param template_description: 模板的描述。可用于客户识别自己的模板
        :type template_description: str
        """
        
        

        self._template_id = None
        self._template_description = None
        self.discriminator = None

        if template_id is not None:
            self.template_id = template_id
        if template_description is not None:
            self.template_description = template_description

    @property
    def template_id(self):
        """Gets the template_id of this UpdateTemplateMetadataRequestBody.

        模板的唯一ID，由模板服务随机生成

        :return: The template_id of this UpdateTemplateMetadataRequestBody.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this UpdateTemplateMetadataRequestBody.

        模板的唯一ID，由模板服务随机生成

        :param template_id: The template_id of this UpdateTemplateMetadataRequestBody.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def template_description(self):
        """Gets the template_description of this UpdateTemplateMetadataRequestBody.

        模板的描述。可用于客户识别自己的模板

        :return: The template_description of this UpdateTemplateMetadataRequestBody.
        :rtype: str
        """
        return self._template_description

    @template_description.setter
    def template_description(self, template_description):
        """Sets the template_description of this UpdateTemplateMetadataRequestBody.

        模板的描述。可用于客户识别自己的模板

        :param template_description: The template_description of this UpdateTemplateMetadataRequestBody.
        :type template_description: str
        """
        self._template_description = template_description

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
        if not isinstance(other, UpdateTemplateMetadataRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
