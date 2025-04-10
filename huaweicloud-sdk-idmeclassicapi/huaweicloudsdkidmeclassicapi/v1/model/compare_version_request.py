# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CompareVersionRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'identifier': 'str',
        'model_name': 'str',
        'body': 'RDMParamVOCompareVersionVO'
    }

    attribute_map = {
        'identifier': 'identifier',
        'model_name': 'modelName',
        'body': 'body'
    }

    def __init__(self, identifier=None, model_name=None, body=None):
        r"""CompareVersionRequest

        The model defined in huaweicloud sdk

        :param identifier: **参数解释：**  应用唯一标识。  **约束限制：**  不涉及。  **取值范围：**  由英文字母和数字组成，且长度为32个字符。  **默认取值：**  不涉及。 
        :type identifier: str
        :param model_name: **参数解释：**  数据模型的英文名称。  **约束限制：**  不涉及。  **取值范围：**  大写字母开头，只能包含字母、数字、“_”，且长度为[1-60]个字符。  **默认取值：**  不涉及。 
        :type model_name: str
        :param body: Body of the CompareVersionRequest
        :type body: :class:`huaweicloudsdkidmeclassicapi.v1.RDMParamVOCompareVersionVO`
        """
        
        

        self._identifier = None
        self._model_name = None
        self._body = None
        self.discriminator = None

        self.identifier = identifier
        self.model_name = model_name
        if body is not None:
            self.body = body

    @property
    def identifier(self):
        r"""Gets the identifier of this CompareVersionRequest.

        **参数解释：**  应用唯一标识。  **约束限制：**  不涉及。  **取值范围：**  由英文字母和数字组成，且长度为32个字符。  **默认取值：**  不涉及。 

        :return: The identifier of this CompareVersionRequest.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        r"""Sets the identifier of this CompareVersionRequest.

        **参数解释：**  应用唯一标识。  **约束限制：**  不涉及。  **取值范围：**  由英文字母和数字组成，且长度为32个字符。  **默认取值：**  不涉及。 

        :param identifier: The identifier of this CompareVersionRequest.
        :type identifier: str
        """
        self._identifier = identifier

    @property
    def model_name(self):
        r"""Gets the model_name of this CompareVersionRequest.

        **参数解释：**  数据模型的英文名称。  **约束限制：**  不涉及。  **取值范围：**  大写字母开头，只能包含字母、数字、“_”，且长度为[1-60]个字符。  **默认取值：**  不涉及。 

        :return: The model_name of this CompareVersionRequest.
        :rtype: str
        """
        return self._model_name

    @model_name.setter
    def model_name(self, model_name):
        r"""Sets the model_name of this CompareVersionRequest.

        **参数解释：**  数据模型的英文名称。  **约束限制：**  不涉及。  **取值范围：**  大写字母开头，只能包含字母、数字、“_”，且长度为[1-60]个字符。  **默认取值：**  不涉及。 

        :param model_name: The model_name of this CompareVersionRequest.
        :type model_name: str
        """
        self._model_name = model_name

    @property
    def body(self):
        r"""Gets the body of this CompareVersionRequest.

        :return: The body of this CompareVersionRequest.
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.RDMParamVOCompareVersionVO`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this CompareVersionRequest.

        :param body: The body of this CompareVersionRequest.
        :type body: :class:`huaweicloudsdkidmeclassicapi.v1.RDMParamVOCompareVersionVO`
        """
        self._body = body

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
        if not isinstance(other, CompareVersionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
