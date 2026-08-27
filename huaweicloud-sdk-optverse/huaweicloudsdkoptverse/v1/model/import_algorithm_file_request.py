# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImportAlgorithmFileRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'algorithm_id': 'str',
        'body': 'ImportAlgorithmFileRequestBody'
    }

    attribute_map = {
        'algorithm_id': 'algorithm_id',
        'body': 'body'
    }

    def __init__(self, algorithm_id=None, body=None):
        r"""ImportAlgorithmFileRequest

        The model defined in huaweicloud sdk

        :param algorithm_id: **参数解释**： 算法项目标识符。 **约束限制**： 不涉及 **取值范围**： 仅支持字母、数字、中划线和下划线，长度为[1-128]个字符。 **默认取值**： 不涉及 
        :type algorithm_id: str
        :param body: Body of the ImportAlgorithmFileRequest
        :type body: :class:`huaweicloudsdkoptverse.v1.ImportAlgorithmFileRequestBody`
        """
        
        

        self._algorithm_id = None
        self._body = None
        self.discriminator = None

        self.algorithm_id = algorithm_id
        if body is not None:
            self.body = body

    @property
    def algorithm_id(self):
        r"""Gets the algorithm_id of this ImportAlgorithmFileRequest.

        **参数解释**： 算法项目标识符。 **约束限制**： 不涉及 **取值范围**： 仅支持字母、数字、中划线和下划线，长度为[1-128]个字符。 **默认取值**： 不涉及 

        :return: The algorithm_id of this ImportAlgorithmFileRequest.
        :rtype: str
        """
        return self._algorithm_id

    @algorithm_id.setter
    def algorithm_id(self, algorithm_id):
        r"""Sets the algorithm_id of this ImportAlgorithmFileRequest.

        **参数解释**： 算法项目标识符。 **约束限制**： 不涉及 **取值范围**： 仅支持字母、数字、中划线和下划线，长度为[1-128]个字符。 **默认取值**： 不涉及 

        :param algorithm_id: The algorithm_id of this ImportAlgorithmFileRequest.
        :type algorithm_id: str
        """
        self._algorithm_id = algorithm_id

    @property
    def body(self):
        r"""Gets the body of this ImportAlgorithmFileRequest.

        :return: The body of this ImportAlgorithmFileRequest.
        :rtype: :class:`huaweicloudsdkoptverse.v1.ImportAlgorithmFileRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this ImportAlgorithmFileRequest.

        :param body: The body of this ImportAlgorithmFileRequest.
        :type body: :class:`huaweicloudsdkoptverse.v1.ImportAlgorithmFileRequestBody`
        """
        self._body = body

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ImportAlgorithmFileRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
