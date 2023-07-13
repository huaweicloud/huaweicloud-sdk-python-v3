# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTemplateByJobIdResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_elements': 'int',
        'elements': 'list[Template]'
    }

    attribute_map = {
        'total_elements': 'total_elements',
        'elements': 'elements'
    }

    def __init__(self, total_elements=None, elements=None):
        """ListTemplateByJobIdResponse

        The model defined in huaweicloud sdk

        :param total_elements: 总数
        :type total_elements: int
        :param elements: 查询作业信息集合
        :type elements: list[:class:`huaweicloudsdkaom.v1.Template`]
        """
        
        super(ListTemplateByJobIdResponse, self).__init__()

        self._total_elements = None
        self._elements = None
        self.discriminator = None

        if total_elements is not None:
            self.total_elements = total_elements
        if elements is not None:
            self.elements = elements

    @property
    def total_elements(self):
        """Gets the total_elements of this ListTemplateByJobIdResponse.

        总数

        :return: The total_elements of this ListTemplateByJobIdResponse.
        :rtype: int
        """
        return self._total_elements

    @total_elements.setter
    def total_elements(self, total_elements):
        """Sets the total_elements of this ListTemplateByJobIdResponse.

        总数

        :param total_elements: The total_elements of this ListTemplateByJobIdResponse.
        :type total_elements: int
        """
        self._total_elements = total_elements

    @property
    def elements(self):
        """Gets the elements of this ListTemplateByJobIdResponse.

        查询作业信息集合

        :return: The elements of this ListTemplateByJobIdResponse.
        :rtype: list[:class:`huaweicloudsdkaom.v1.Template`]
        """
        return self._elements

    @elements.setter
    def elements(self, elements):
        """Sets the elements of this ListTemplateByJobIdResponse.

        查询作业信息集合

        :param elements: The elements of this ListTemplateByJobIdResponse.
        :type elements: list[:class:`huaweicloudsdkaom.v1.Template`]
        """
        self._elements = elements

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
        if not isinstance(other, ListTemplateByJobIdResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
