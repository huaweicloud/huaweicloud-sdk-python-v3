# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateBlockchainCertByUserNameRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'security_mode': 'bool'
    }

    attribute_map = {
        'security_mode': 'security_mode'
    }

    def __init__(self, security_mode=None):
        r"""CreateBlockchainCertByUserNameRequestBody

        The model defined in huaweicloud sdk

        :param security_mode: 生成证书的安全模式： true：安全模式（证书由系统托管，每个用户名只能生成一个证书，每个组织生成上限100个） false：非安全模式（证书由用户自己保障，不限制生成数量）
        :type security_mode: bool
        """
        
        

        self._security_mode = None
        self.discriminator = None

        if security_mode is not None:
            self.security_mode = security_mode

    @property
    def security_mode(self):
        r"""Gets the security_mode of this CreateBlockchainCertByUserNameRequestBody.

        生成证书的安全模式： true：安全模式（证书由系统托管，每个用户名只能生成一个证书，每个组织生成上限100个） false：非安全模式（证书由用户自己保障，不限制生成数量）

        :return: The security_mode of this CreateBlockchainCertByUserNameRequestBody.
        :rtype: bool
        """
        return self._security_mode

    @security_mode.setter
    def security_mode(self, security_mode):
        r"""Sets the security_mode of this CreateBlockchainCertByUserNameRequestBody.

        生成证书的安全模式： true：安全模式（证书由系统托管，每个用户名只能生成一个证书，每个组织生成上限100个） false：非安全模式（证书由用户自己保障，不限制生成数量）

        :param security_mode: The security_mode of this CreateBlockchainCertByUserNameRequestBody.
        :type security_mode: bool
        """
        self._security_mode = security_mode

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
        if not isinstance(other, CreateBlockchainCertByUserNameRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
