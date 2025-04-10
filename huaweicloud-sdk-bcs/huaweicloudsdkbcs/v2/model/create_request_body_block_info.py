# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateRequestBodyBlockInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'batch_timeout': 'int',
        'max_message_count': 'int',
        'preferred_maxbytes': 'int'
    }

    attribute_map = {
        'batch_timeout': 'batch_timeout',
        'max_message_count': 'max_message_count',
        'preferred_maxbytes': 'preferred_maxbytes'
    }

    def __init__(self, batch_timeout=None, max_message_count=None, preferred_maxbytes=None):
        r"""CreateRequestBodyBlockInfo

        The model defined in huaweicloud sdk

        :param batch_timeout: 区块产生时间（单位：秒），默认2秒
        :type batch_timeout: int
        :param max_message_count: 区块包含交易数量，默认500
        :type max_message_count: int
        :param preferred_maxbytes: 区块容量（单位：MB），默认2MB
        :type preferred_maxbytes: int
        """
        
        

        self._batch_timeout = None
        self._max_message_count = None
        self._preferred_maxbytes = None
        self.discriminator = None

        if batch_timeout is not None:
            self.batch_timeout = batch_timeout
        if max_message_count is not None:
            self.max_message_count = max_message_count
        if preferred_maxbytes is not None:
            self.preferred_maxbytes = preferred_maxbytes

    @property
    def batch_timeout(self):
        r"""Gets the batch_timeout of this CreateRequestBodyBlockInfo.

        区块产生时间（单位：秒），默认2秒

        :return: The batch_timeout of this CreateRequestBodyBlockInfo.
        :rtype: int
        """
        return self._batch_timeout

    @batch_timeout.setter
    def batch_timeout(self, batch_timeout):
        r"""Sets the batch_timeout of this CreateRequestBodyBlockInfo.

        区块产生时间（单位：秒），默认2秒

        :param batch_timeout: The batch_timeout of this CreateRequestBodyBlockInfo.
        :type batch_timeout: int
        """
        self._batch_timeout = batch_timeout

    @property
    def max_message_count(self):
        r"""Gets the max_message_count of this CreateRequestBodyBlockInfo.

        区块包含交易数量，默认500

        :return: The max_message_count of this CreateRequestBodyBlockInfo.
        :rtype: int
        """
        return self._max_message_count

    @max_message_count.setter
    def max_message_count(self, max_message_count):
        r"""Sets the max_message_count of this CreateRequestBodyBlockInfo.

        区块包含交易数量，默认500

        :param max_message_count: The max_message_count of this CreateRequestBodyBlockInfo.
        :type max_message_count: int
        """
        self._max_message_count = max_message_count

    @property
    def preferred_maxbytes(self):
        r"""Gets the preferred_maxbytes of this CreateRequestBodyBlockInfo.

        区块容量（单位：MB），默认2MB

        :return: The preferred_maxbytes of this CreateRequestBodyBlockInfo.
        :rtype: int
        """
        return self._preferred_maxbytes

    @preferred_maxbytes.setter
    def preferred_maxbytes(self, preferred_maxbytes):
        r"""Sets the preferred_maxbytes of this CreateRequestBodyBlockInfo.

        区块容量（单位：MB），默认2MB

        :param preferred_maxbytes: The preferred_maxbytes of this CreateRequestBodyBlockInfo.
        :type preferred_maxbytes: int
        """
        self._preferred_maxbytes = preferred_maxbytes

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
        if not isinstance(other, CreateRequestBodyBlockInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
