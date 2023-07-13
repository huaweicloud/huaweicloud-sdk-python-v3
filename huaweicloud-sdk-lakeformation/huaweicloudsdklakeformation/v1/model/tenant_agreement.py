# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TenantAgreement:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agreement_name': 'str',
        'agreement_version': 'str'
    }

    attribute_map = {
        'agreement_name': 'agreement_name',
        'agreement_version': 'agreement_version'
    }

    def __init__(self, agreement_name=None, agreement_version=None):
        """TenantAgreement

        The model defined in huaweicloud sdk

        :param agreement_name: 协议名称
        :type agreement_name: str
        :param agreement_version: 协议版本号
        :type agreement_version: str
        """
        
        

        self._agreement_name = None
        self._agreement_version = None
        self.discriminator = None

        if agreement_name is not None:
            self.agreement_name = agreement_name
        if agreement_version is not None:
            self.agreement_version = agreement_version

    @property
    def agreement_name(self):
        """Gets the agreement_name of this TenantAgreement.

        协议名称

        :return: The agreement_name of this TenantAgreement.
        :rtype: str
        """
        return self._agreement_name

    @agreement_name.setter
    def agreement_name(self, agreement_name):
        """Sets the agreement_name of this TenantAgreement.

        协议名称

        :param agreement_name: The agreement_name of this TenantAgreement.
        :type agreement_name: str
        """
        self._agreement_name = agreement_name

    @property
    def agreement_version(self):
        """Gets the agreement_version of this TenantAgreement.

        协议版本号

        :return: The agreement_version of this TenantAgreement.
        :rtype: str
        """
        return self._agreement_version

    @agreement_version.setter
    def agreement_version(self, agreement_version):
        """Sets the agreement_version of this TenantAgreement.

        协议版本号

        :param agreement_version: The agreement_version of this TenantAgreement.
        :type agreement_version: str
        """
        self._agreement_version = agreement_version

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
        if not isinstance(other, TenantAgreement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
