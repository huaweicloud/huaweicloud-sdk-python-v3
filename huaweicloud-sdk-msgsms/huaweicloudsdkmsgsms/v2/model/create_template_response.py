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
        'id': 'str',
        'template_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'template_name': 'template_name'
    }

    def __init__(self, id=None, template_name=None):
        r"""CreateTemplateResponse

        The model defined in huaweicloud sdk

        :param id: 模板主键ID
        :type id: str
        :param template_name: 模板名称
        :type template_name: str
        """
        
        super(CreateTemplateResponse, self).__init__()

        self._id = None
        self._template_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if template_name is not None:
            self.template_name = template_name

    @property
    def id(self):
        r"""Gets the id of this CreateTemplateResponse.

        模板主键ID

        :return: The id of this CreateTemplateResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CreateTemplateResponse.

        模板主键ID

        :param id: The id of this CreateTemplateResponse.
        :type id: str
        """
        self._id = id

    @property
    def template_name(self):
        r"""Gets the template_name of this CreateTemplateResponse.

        模板名称

        :return: The template_name of this CreateTemplateResponse.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        r"""Sets the template_name of this CreateTemplateResponse.

        模板名称

        :param template_name: The template_name of this CreateTemplateResponse.
        :type template_name: str
        """
        self._template_name = template_name

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
