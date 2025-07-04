# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTemplateResponse(SdkResponse):

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
        'version_id': 'str'
    }

    attribute_map = {
        'template_id': 'template_id',
        'version_id': 'version_id'
    }

    def __init__(self, template_id=None, version_id=None):
        r"""CreateTemplateResponse

        The model defined in huaweicloud sdk

        :param template_id: 模板的唯一ID，由模板服务随机生成
        :type template_id: str
        :param version_id: 模板模板版本ID
        :type version_id: str
        """
        
        super(CreateTemplateResponse, self).__init__()

        self._template_id = None
        self._version_id = None
        self.discriminator = None

        if template_id is not None:
            self.template_id = template_id
        if version_id is not None:
            self.version_id = version_id

    @property
    def template_id(self):
        r"""Gets the template_id of this CreateTemplateResponse.

        模板的唯一ID，由模板服务随机生成

        :return: The template_id of this CreateTemplateResponse.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this CreateTemplateResponse.

        模板的唯一ID，由模板服务随机生成

        :param template_id: The template_id of this CreateTemplateResponse.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def version_id(self):
        r"""Gets the version_id of this CreateTemplateResponse.

        模板模板版本ID

        :return: The version_id of this CreateTemplateResponse.
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        r"""Sets the version_id of this CreateTemplateResponse.

        模板模板版本ID

        :param version_id: The version_id of this CreateTemplateResponse.
        :type version_id: str
        """
        self._version_id = version_id

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
        if not isinstance(other, CreateTemplateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
