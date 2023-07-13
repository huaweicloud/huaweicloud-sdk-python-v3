# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTemplateDetailRequest:

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
        'template_type': 'str',
        'source': 'str'
    }

    attribute_map = {
        'template_id': 'template_id',
        'template_type': 'template_type',
        'source': 'source'
    }

    def __init__(self, template_id=None, template_type=None, source=None):
        """ShowTemplateDetailRequest

        The model defined in huaweicloud sdk

        :param template_id: 模板ID
        :type template_id: str
        :param template_type: 模板类型
        :type template_type: str
        :param source: 接口调用方
        :type source: str
        """
        
        

        self._template_id = None
        self._template_type = None
        self._source = None
        self.discriminator = None

        self.template_id = template_id
        self.template_type = template_type
        if source is not None:
            self.source = source

    @property
    def template_id(self):
        """Gets the template_id of this ShowTemplateDetailRequest.

        模板ID

        :return: The template_id of this ShowTemplateDetailRequest.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this ShowTemplateDetailRequest.

        模板ID

        :param template_id: The template_id of this ShowTemplateDetailRequest.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def template_type(self):
        """Gets the template_type of this ShowTemplateDetailRequest.

        模板类型

        :return: The template_type of this ShowTemplateDetailRequest.
        :rtype: str
        """
        return self._template_type

    @template_type.setter
    def template_type(self, template_type):
        """Sets the template_type of this ShowTemplateDetailRequest.

        模板类型

        :param template_type: The template_type of this ShowTemplateDetailRequest.
        :type template_type: str
        """
        self._template_type = template_type

    @property
    def source(self):
        """Gets the source of this ShowTemplateDetailRequest.

        接口调用方

        :return: The source of this ShowTemplateDetailRequest.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this ShowTemplateDetailRequest.

        接口调用方

        :param source: The source of this ShowTemplateDetailRequest.
        :type source: str
        """
        self._source = source

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
        if not isinstance(other, ShowTemplateDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
