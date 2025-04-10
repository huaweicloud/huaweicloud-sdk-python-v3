# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FailedKeypair:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'keypair_name': 'str',
        'failed_reason': 'str'
    }

    attribute_map = {
        'keypair_name': 'keypair_name',
        'failed_reason': 'failed_reason'
    }

    def __init__(self, keypair_name=None, failed_reason=None):
        r"""FailedKeypair

        The model defined in huaweicloud sdk

        :param keypair_name: SSH密钥对名称
        :type keypair_name: str
        :param failed_reason: 导入失败的原因
        :type failed_reason: str
        """
        
        

        self._keypair_name = None
        self._failed_reason = None
        self.discriminator = None

        self.keypair_name = keypair_name
        self.failed_reason = failed_reason

    @property
    def keypair_name(self):
        r"""Gets the keypair_name of this FailedKeypair.

        SSH密钥对名称

        :return: The keypair_name of this FailedKeypair.
        :rtype: str
        """
        return self._keypair_name

    @keypair_name.setter
    def keypair_name(self, keypair_name):
        r"""Sets the keypair_name of this FailedKeypair.

        SSH密钥对名称

        :param keypair_name: The keypair_name of this FailedKeypair.
        :type keypair_name: str
        """
        self._keypair_name = keypair_name

    @property
    def failed_reason(self):
        r"""Gets the failed_reason of this FailedKeypair.

        导入失败的原因

        :return: The failed_reason of this FailedKeypair.
        :rtype: str
        """
        return self._failed_reason

    @failed_reason.setter
    def failed_reason(self, failed_reason):
        r"""Sets the failed_reason of this FailedKeypair.

        导入失败的原因

        :param failed_reason: The failed_reason of this FailedKeypair.
        :type failed_reason: str
        """
        self._failed_reason = failed_reason

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
        if not isinstance(other, FailedKeypair):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
