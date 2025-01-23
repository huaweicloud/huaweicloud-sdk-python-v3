# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDocumentResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'result': 'str',
        'data': 'list[StructuredDocView]',
        'errors': 'list[str]'
    }

    attribute_map = {
        'result': 'result',
        'data': 'data',
        'errors': 'errors'
    }

    def __init__(self, result=None, data=None, errors=None):
        """CreateDocumentResponse

        The model defined in huaweicloud sdk

        :param result: **参数解释：**  请求结果。  **取值范围：**  - SUCCESS：请求成功。 - FAIL：请求失败。  **默认取值：**  不涉及。 
        :type result: str
        :param data: 
        :type data: list[:class:`huaweicloudsdkidmeclassicapi.v1.StructuredDocView`]
        :param errors: **参数解释：**  异常信息。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type errors: list[str]
        """
        
        super(CreateDocumentResponse, self).__init__()

        self._result = None
        self._data = None
        self._errors = None
        self.discriminator = None

        if result is not None:
            self.result = result
        if data is not None:
            self.data = data
        if errors is not None:
            self.errors = errors

    @property
    def result(self):
        """Gets the result of this CreateDocumentResponse.

        **参数解释：**  请求结果。  **取值范围：**  - SUCCESS：请求成功。 - FAIL：请求失败。  **默认取值：**  不涉及。 

        :return: The result of this CreateDocumentResponse.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this CreateDocumentResponse.

        **参数解释：**  请求结果。  **取值范围：**  - SUCCESS：请求成功。 - FAIL：请求失败。  **默认取值：**  不涉及。 

        :param result: The result of this CreateDocumentResponse.
        :type result: str
        """
        self._result = result

    @property
    def data(self):
        """Gets the data of this CreateDocumentResponse.

        :return: The data of this CreateDocumentResponse.
        :rtype: list[:class:`huaweicloudsdkidmeclassicapi.v1.StructuredDocView`]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this CreateDocumentResponse.

        :param data: The data of this CreateDocumentResponse.
        :type data: list[:class:`huaweicloudsdkidmeclassicapi.v1.StructuredDocView`]
        """
        self._data = data

    @property
    def errors(self):
        """Gets the errors of this CreateDocumentResponse.

        **参数解释：**  异常信息。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The errors of this CreateDocumentResponse.
        :rtype: list[str]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this CreateDocumentResponse.

        **参数解释：**  异常信息。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param errors: The errors of this CreateDocumentResponse.
        :type errors: list[str]
        """
        self._errors = errors

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
        if not isinstance(other, CreateDocumentResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
