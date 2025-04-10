# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteMultiViewRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'mv_model_name': 'str',
        'identifier': 'str',
        'body': 'RDMParamVOMultiViewModelMasterIdModifierDTO'
    }

    attribute_map = {
        'mv_model_name': 'mvModelName',
        'identifier': 'identifier',
        'body': 'body'
    }

    def __init__(self, mv_model_name=None, identifier=None, body=None):
        r"""DeleteMultiViewRequest

        The model defined in huaweicloud sdk

        :param mv_model_name: **参数解释：**  数据模型的英文名称。  **约束限制：**  不涉及。  **取值范围：**  大写字母开头，只能包含字母、数字、“_”，且长度为[1-60]个字符。  **默认取值：**  不涉及。 
        :type mv_model_name: str
        :param identifier: 应用ID。
        :type identifier: str
        :param body: Body of the DeleteMultiViewRequest
        :type body: :class:`huaweicloudsdkidmeclassicapi.v1.RDMParamVOMultiViewModelMasterIdModifierDTO`
        """
        
        

        self._mv_model_name = None
        self._identifier = None
        self._body = None
        self.discriminator = None

        self.mv_model_name = mv_model_name
        self.identifier = identifier
        if body is not None:
            self.body = body

    @property
    def mv_model_name(self):
        r"""Gets the mv_model_name of this DeleteMultiViewRequest.

        **参数解释：**  数据模型的英文名称。  **约束限制：**  不涉及。  **取值范围：**  大写字母开头，只能包含字母、数字、“_”，且长度为[1-60]个字符。  **默认取值：**  不涉及。 

        :return: The mv_model_name of this DeleteMultiViewRequest.
        :rtype: str
        """
        return self._mv_model_name

    @mv_model_name.setter
    def mv_model_name(self, mv_model_name):
        r"""Sets the mv_model_name of this DeleteMultiViewRequest.

        **参数解释：**  数据模型的英文名称。  **约束限制：**  不涉及。  **取值范围：**  大写字母开头，只能包含字母、数字、“_”，且长度为[1-60]个字符。  **默认取值：**  不涉及。 

        :param mv_model_name: The mv_model_name of this DeleteMultiViewRequest.
        :type mv_model_name: str
        """
        self._mv_model_name = mv_model_name

    @property
    def identifier(self):
        r"""Gets the identifier of this DeleteMultiViewRequest.

        应用ID。

        :return: The identifier of this DeleteMultiViewRequest.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        r"""Sets the identifier of this DeleteMultiViewRequest.

        应用ID。

        :param identifier: The identifier of this DeleteMultiViewRequest.
        :type identifier: str
        """
        self._identifier = identifier

    @property
    def body(self):
        r"""Gets the body of this DeleteMultiViewRequest.

        :return: The body of this DeleteMultiViewRequest.
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.RDMParamVOMultiViewModelMasterIdModifierDTO`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this DeleteMultiViewRequest.

        :param body: The body of this DeleteMultiViewRequest.
        :type body: :class:`huaweicloudsdkidmeclassicapi.v1.RDMParamVOMultiViewModelMasterIdModifierDTO`
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
        if not isinstance(other, DeleteMultiViewRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
