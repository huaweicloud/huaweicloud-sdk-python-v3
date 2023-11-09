# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DocumentQueryResponseResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'suggestion': 'str',
        'details': 'list[DocumentQueryResponseResultDetails]'
    }

    attribute_map = {
        'suggestion': 'suggestion',
        'details': 'details'
    }

    def __init__(self, suggestion=None, details=None):
        """DocumentQueryResponseResult

        The model defined in huaweicloud sdk

        :param suggestion: 文档审核结果是否通过。 block：包含敏感信息，不通过 pass：不包含敏感信息，通过 review：需要人工复检
        :type suggestion: str
        :param details: 审核详情
        :type details: list[:class:`huaweicloudsdkmoderation.v3.DocumentQueryResponseResultDetails`]
        """
        
        

        self._suggestion = None
        self._details = None
        self.discriminator = None

        if suggestion is not None:
            self.suggestion = suggestion
        if details is not None:
            self.details = details

    @property
    def suggestion(self):
        """Gets the suggestion of this DocumentQueryResponseResult.

        文档审核结果是否通过。 block：包含敏感信息，不通过 pass：不包含敏感信息，通过 review：需要人工复检

        :return: The suggestion of this DocumentQueryResponseResult.
        :rtype: str
        """
        return self._suggestion

    @suggestion.setter
    def suggestion(self, suggestion):
        """Sets the suggestion of this DocumentQueryResponseResult.

        文档审核结果是否通过。 block：包含敏感信息，不通过 pass：不包含敏感信息，通过 review：需要人工复检

        :param suggestion: The suggestion of this DocumentQueryResponseResult.
        :type suggestion: str
        """
        self._suggestion = suggestion

    @property
    def details(self):
        """Gets the details of this DocumentQueryResponseResult.

        审核详情

        :return: The details of this DocumentQueryResponseResult.
        :rtype: list[:class:`huaweicloudsdkmoderation.v3.DocumentQueryResponseResultDetails`]
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this DocumentQueryResponseResult.

        审核详情

        :param details: The details of this DocumentQueryResponseResult.
        :type details: list[:class:`huaweicloudsdkmoderation.v3.DocumentQueryResponseResultDetails`]
        """
        self._details = details

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
        if not isinstance(other, DocumentQueryResponseResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
