# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SseSpecification:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable': 'bool',
        'sse_type': 'str',
        'sse_algorithm': 'str',
        'cmk_id': 'str'
    }

    attribute_map = {
        'enable': 'enable',
        'sse_type': 'sse_type',
        'sse_algorithm': 'sse_algorithm',
        'cmk_id': 'cmk_id'
    }

    def __init__(self, enable=None, sse_type=None, sse_algorithm=None, cmk_id=None):
        r"""SseSpecification

        The model defined in huaweicloud sdk

        :param enable: 启用静态加密。
        :type enable: bool
        :param sse_type: 加密类型，支持SSE-KMS-S和SSE-KMS-C。
        :type sse_type: str
        :param sse_algorithm: 加密算法，支持AES256_GCM。
        :type sse_algorithm: str
        :param cmk_id: KMS中的用户主密钥ID。非必填项，仅当加密类型是SSE-KMS-C时需要填写该字段。
        :type cmk_id: str
        """
        
        

        self._enable = None
        self._sse_type = None
        self._sse_algorithm = None
        self._cmk_id = None
        self.discriminator = None

        self.enable = enable
        if sse_type is not None:
            self.sse_type = sse_type
        if sse_algorithm is not None:
            self.sse_algorithm = sse_algorithm
        if cmk_id is not None:
            self.cmk_id = cmk_id

    @property
    def enable(self):
        r"""Gets the enable of this SseSpecification.

        启用静态加密。

        :return: The enable of this SseSpecification.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this SseSpecification.

        启用静态加密。

        :param enable: The enable of this SseSpecification.
        :type enable: bool
        """
        self._enable = enable

    @property
    def sse_type(self):
        r"""Gets the sse_type of this SseSpecification.

        加密类型，支持SSE-KMS-S和SSE-KMS-C。

        :return: The sse_type of this SseSpecification.
        :rtype: str
        """
        return self._sse_type

    @sse_type.setter
    def sse_type(self, sse_type):
        r"""Sets the sse_type of this SseSpecification.

        加密类型，支持SSE-KMS-S和SSE-KMS-C。

        :param sse_type: The sse_type of this SseSpecification.
        :type sse_type: str
        """
        self._sse_type = sse_type

    @property
    def sse_algorithm(self):
        r"""Gets the sse_algorithm of this SseSpecification.

        加密算法，支持AES256_GCM。

        :return: The sse_algorithm of this SseSpecification.
        :rtype: str
        """
        return self._sse_algorithm

    @sse_algorithm.setter
    def sse_algorithm(self, sse_algorithm):
        r"""Sets the sse_algorithm of this SseSpecification.

        加密算法，支持AES256_GCM。

        :param sse_algorithm: The sse_algorithm of this SseSpecification.
        :type sse_algorithm: str
        """
        self._sse_algorithm = sse_algorithm

    @property
    def cmk_id(self):
        r"""Gets the cmk_id of this SseSpecification.

        KMS中的用户主密钥ID。非必填项，仅当加密类型是SSE-KMS-C时需要填写该字段。

        :return: The cmk_id of this SseSpecification.
        :rtype: str
        """
        return self._cmk_id

    @cmk_id.setter
    def cmk_id(self, cmk_id):
        r"""Sets the cmk_id of this SseSpecification.

        KMS中的用户主密钥ID。非必填项，仅当加密类型是SSE-KMS-C时需要填写该字段。

        :param cmk_id: The cmk_id of this SseSpecification.
        :type cmk_id: str
        """
        self._cmk_id = cmk_id

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
        if not isinstance(other, SseSpecification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
