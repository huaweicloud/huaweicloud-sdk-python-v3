# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTemplateResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'template_array': 'list[TemplateInfo]',
        'total': 'int'
    }

    attribute_map = {
        'template_array': 'template_array',
        'total': 'total'
    }

    def __init__(self, template_array=None, total=None):
        """ListTemplateResponse

        The model defined in huaweicloud sdk

        :param template_array: 转码模板
        :type template_array: list[:class:`huaweicloudsdkmpc.v1.TemplateInfo`]
        :param total: 转码模板总数 
        :type total: int
        """
        
        super(ListTemplateResponse, self).__init__()

        self._template_array = None
        self._total = None
        self.discriminator = None

        if template_array is not None:
            self.template_array = template_array
        if total is not None:
            self.total = total

    @property
    def template_array(self):
        """Gets the template_array of this ListTemplateResponse.

        转码模板

        :return: The template_array of this ListTemplateResponse.
        :rtype: list[:class:`huaweicloudsdkmpc.v1.TemplateInfo`]
        """
        return self._template_array

    @template_array.setter
    def template_array(self, template_array):
        """Sets the template_array of this ListTemplateResponse.

        转码模板

        :param template_array: The template_array of this ListTemplateResponse.
        :type template_array: list[:class:`huaweicloudsdkmpc.v1.TemplateInfo`]
        """
        self._template_array = template_array

    @property
    def total(self):
        """Gets the total of this ListTemplateResponse.

        转码模板总数 

        :return: The total of this ListTemplateResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListTemplateResponse.

        转码模板总数 

        :param total: The total of this ListTemplateResponse.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, ListTemplateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
