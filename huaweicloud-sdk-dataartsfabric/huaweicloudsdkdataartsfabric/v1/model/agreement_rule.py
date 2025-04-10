# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AgreementRule:

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
        'agreement_display_name': 'str',
        'agreement_version': 'str',
        'agreement_url': 'str'
    }

    attribute_map = {
        'agreement_name': 'agreement_name',
        'agreement_display_name': 'agreement_display_name',
        'agreement_version': 'agreement_version',
        'agreement_url': 'agreement_url'
    }

    def __init__(self, agreement_name=None, agreement_display_name=None, agreement_version=None, agreement_url=None):
        r"""AgreementRule

        The model defined in huaweicloud sdk

        :param agreement_name: 协议名称
        :type agreement_name: str
        :param agreement_display_name: 协议展示名称
        :type agreement_display_name: str
        :param agreement_version: 协议版本
        :type agreement_version: str
        :param agreement_url: 协议链接
        :type agreement_url: str
        """
        
        

        self._agreement_name = None
        self._agreement_display_name = None
        self._agreement_version = None
        self._agreement_url = None
        self.discriminator = None

        if agreement_name is not None:
            self.agreement_name = agreement_name
        if agreement_display_name is not None:
            self.agreement_display_name = agreement_display_name
        if agreement_version is not None:
            self.agreement_version = agreement_version
        if agreement_url is not None:
            self.agreement_url = agreement_url

    @property
    def agreement_name(self):
        r"""Gets the agreement_name of this AgreementRule.

        协议名称

        :return: The agreement_name of this AgreementRule.
        :rtype: str
        """
        return self._agreement_name

    @agreement_name.setter
    def agreement_name(self, agreement_name):
        r"""Sets the agreement_name of this AgreementRule.

        协议名称

        :param agreement_name: The agreement_name of this AgreementRule.
        :type agreement_name: str
        """
        self._agreement_name = agreement_name

    @property
    def agreement_display_name(self):
        r"""Gets the agreement_display_name of this AgreementRule.

        协议展示名称

        :return: The agreement_display_name of this AgreementRule.
        :rtype: str
        """
        return self._agreement_display_name

    @agreement_display_name.setter
    def agreement_display_name(self, agreement_display_name):
        r"""Sets the agreement_display_name of this AgreementRule.

        协议展示名称

        :param agreement_display_name: The agreement_display_name of this AgreementRule.
        :type agreement_display_name: str
        """
        self._agreement_display_name = agreement_display_name

    @property
    def agreement_version(self):
        r"""Gets the agreement_version of this AgreementRule.

        协议版本

        :return: The agreement_version of this AgreementRule.
        :rtype: str
        """
        return self._agreement_version

    @agreement_version.setter
    def agreement_version(self, agreement_version):
        r"""Sets the agreement_version of this AgreementRule.

        协议版本

        :param agreement_version: The agreement_version of this AgreementRule.
        :type agreement_version: str
        """
        self._agreement_version = agreement_version

    @property
    def agreement_url(self):
        r"""Gets the agreement_url of this AgreementRule.

        协议链接

        :return: The agreement_url of this AgreementRule.
        :rtype: str
        """
        return self._agreement_url

    @agreement_url.setter
    def agreement_url(self, agreement_url):
        r"""Sets the agreement_url of this AgreementRule.

        协议链接

        :param agreement_url: The agreement_url of this AgreementRule.
        :type agreement_url: str
        """
        self._agreement_url = agreement_url

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
        if not isinstance(other, AgreementRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
