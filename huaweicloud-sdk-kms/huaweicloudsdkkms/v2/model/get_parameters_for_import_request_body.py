# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetParametersForImportRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'key_id': 'str',
        'wrapping_algorithm': 'str',
        'sequence': 'str'
    }

    attribute_map = {
        'key_id': 'key_id',
        'wrapping_algorithm': 'wrapping_algorithm',
        'sequence': 'sequence'
    }

    def __init__(self, key_id=None, wrapping_algorithm=None, sequence=None):
        """GetParametersForImportRequestBody

        The model defined in huaweicloud sdk

        :param key_id: 密钥ID，36字节，满足正则匹配“^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$”。 例如：0d0466b0-e727-4d9c-b35d-f84bb474a37f。
        :type key_id: str
        :param wrapping_algorithm: 密钥材料加密算法，枚举如下：  - RSAES_OAEP_SHA_256  - SM2_ENCRYPT，部分局点不支持该导入类型
        :type wrapping_algorithm: str
        :param sequence: 请求消息序列号，36字节序列号。 例如：919c82d4-8046-4722-9094-35c3c6524cff
        :type sequence: str
        """
        
        

        self._key_id = None
        self._wrapping_algorithm = None
        self._sequence = None
        self.discriminator = None

        self.key_id = key_id
        self.wrapping_algorithm = wrapping_algorithm
        if sequence is not None:
            self.sequence = sequence

    @property
    def key_id(self):
        """Gets the key_id of this GetParametersForImportRequestBody.

        密钥ID，36字节，满足正则匹配“^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$”。 例如：0d0466b0-e727-4d9c-b35d-f84bb474a37f。

        :return: The key_id of this GetParametersForImportRequestBody.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        """Sets the key_id of this GetParametersForImportRequestBody.

        密钥ID，36字节，满足正则匹配“^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$”。 例如：0d0466b0-e727-4d9c-b35d-f84bb474a37f。

        :param key_id: The key_id of this GetParametersForImportRequestBody.
        :type key_id: str
        """
        self._key_id = key_id

    @property
    def wrapping_algorithm(self):
        """Gets the wrapping_algorithm of this GetParametersForImportRequestBody.

        密钥材料加密算法，枚举如下：  - RSAES_OAEP_SHA_256  - SM2_ENCRYPT，部分局点不支持该导入类型

        :return: The wrapping_algorithm of this GetParametersForImportRequestBody.
        :rtype: str
        """
        return self._wrapping_algorithm

    @wrapping_algorithm.setter
    def wrapping_algorithm(self, wrapping_algorithm):
        """Sets the wrapping_algorithm of this GetParametersForImportRequestBody.

        密钥材料加密算法，枚举如下：  - RSAES_OAEP_SHA_256  - SM2_ENCRYPT，部分局点不支持该导入类型

        :param wrapping_algorithm: The wrapping_algorithm of this GetParametersForImportRequestBody.
        :type wrapping_algorithm: str
        """
        self._wrapping_algorithm = wrapping_algorithm

    @property
    def sequence(self):
        """Gets the sequence of this GetParametersForImportRequestBody.

        请求消息序列号，36字节序列号。 例如：919c82d4-8046-4722-9094-35c3c6524cff

        :return: The sequence of this GetParametersForImportRequestBody.
        :rtype: str
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        """Sets the sequence of this GetParametersForImportRequestBody.

        请求消息序列号，36字节序列号。 例如：919c82d4-8046-4722-9094-35c3c6524cff

        :param sequence: The sequence of this GetParametersForImportRequestBody.
        :type sequence: str
        """
        self._sequence = sequence

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
        if not isinstance(other, GetParametersForImportRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
