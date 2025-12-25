# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecurityCertification:

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
        'kerberos_info': 'list[KerberosStatus]'
    }

    attribute_map = {
        'result': 'result',
        'kerberos_info': 'kerberos_info'
    }

    def __init__(self, result=None, kerberos_info=None):
        r"""SecurityCertification

        The model defined in huaweicloud sdk

        :param result: 检测结果 * NO_RISK 无风险 * MEDIUM_RISK 中风险 * HIGH_RISK 高风险 * NOT_SCANNED 未扫描
        :type result: str
        :param kerberos_info: kerberos信息
        :type kerberos_info: list[:class:`huaweicloudsdkdataartsstudio.v1.KerberosStatus`]
        """
        
        

        self._result = None
        self._kerberos_info = None
        self.discriminator = None

        if result is not None:
            self.result = result
        if kerberos_info is not None:
            self.kerberos_info = kerberos_info

    @property
    def result(self):
        r"""Gets the result of this SecurityCertification.

        检测结果 * NO_RISK 无风险 * MEDIUM_RISK 中风险 * HIGH_RISK 高风险 * NOT_SCANNED 未扫描

        :return: The result of this SecurityCertification.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this SecurityCertification.

        检测结果 * NO_RISK 无风险 * MEDIUM_RISK 中风险 * HIGH_RISK 高风险 * NOT_SCANNED 未扫描

        :param result: The result of this SecurityCertification.
        :type result: str
        """
        self._result = result

    @property
    def kerberos_info(self):
        r"""Gets the kerberos_info of this SecurityCertification.

        kerberos信息

        :return: The kerberos_info of this SecurityCertification.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.KerberosStatus`]
        """
        return self._kerberos_info

    @kerberos_info.setter
    def kerberos_info(self, kerberos_info):
        r"""Sets the kerberos_info of this SecurityCertification.

        kerberos信息

        :param kerberos_info: The kerberos_info of this SecurityCertification.
        :type kerberos_info: list[:class:`huaweicloudsdkdataartsstudio.v1.KerberosStatus`]
        """
        self._kerberos_info = kerberos_info

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
        if not isinstance(other, SecurityCertification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
