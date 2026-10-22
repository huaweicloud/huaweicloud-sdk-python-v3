# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class V2AgreementRule:

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
        'display_name': 'str',
        'version': 'str',
        'url': 'str'
    }

    attribute_map = {
        'agreement_name': 'agreement_name',
        'display_name': 'display_name',
        'version': 'version',
        'url': 'url'
    }

    def __init__(self, agreement_name=None, display_name=None, version=None, url=None):
        r"""V2AgreementRule

        The model defined in huaweicloud sdk

        :param agreement_name: **参数解释**：协议名称。 **取值范围**：长度为1~128的英文字母、数字、下划线和中划线的组合。
        :type agreement_name: str
        :param display_name: **参数解释**：协议展示名称。 **取值范围**：由中文字符、英文字母、数字及特殊字符组成，长度不超过512个字符。
        :type display_name: str
        :param version: **参数解释**：协议版本，例如v1.0.0。 **取值范围**：长度为1~128的英文字母、数字、下划线、中划线和小数点的组合。
        :type version: str
        :param url: **参数解释**：协议链接。 **取值范围**：符合URL格式规范，由英文字母、数字及URL合法特殊字符组成，长度不超过2000个字符。
        :type url: str
        """
        
        

        self._agreement_name = None
        self._display_name = None
        self._version = None
        self._url = None
        self.discriminator = None

        if agreement_name is not None:
            self.agreement_name = agreement_name
        if display_name is not None:
            self.display_name = display_name
        if version is not None:
            self.version = version
        if url is not None:
            self.url = url

    @property
    def agreement_name(self):
        r"""Gets the agreement_name of this V2AgreementRule.

        **参数解释**：协议名称。 **取值范围**：长度为1~128的英文字母、数字、下划线和中划线的组合。

        :return: The agreement_name of this V2AgreementRule.
        :rtype: str
        """
        return self._agreement_name

    @agreement_name.setter
    def agreement_name(self, agreement_name):
        r"""Sets the agreement_name of this V2AgreementRule.

        **参数解释**：协议名称。 **取值范围**：长度为1~128的英文字母、数字、下划线和中划线的组合。

        :param agreement_name: The agreement_name of this V2AgreementRule.
        :type agreement_name: str
        """
        self._agreement_name = agreement_name

    @property
    def display_name(self):
        r"""Gets the display_name of this V2AgreementRule.

        **参数解释**：协议展示名称。 **取值范围**：由中文字符、英文字母、数字及特殊字符组成，长度不超过512个字符。

        :return: The display_name of this V2AgreementRule.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this V2AgreementRule.

        **参数解释**：协议展示名称。 **取值范围**：由中文字符、英文字母、数字及特殊字符组成，长度不超过512个字符。

        :param display_name: The display_name of this V2AgreementRule.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def version(self):
        r"""Gets the version of this V2AgreementRule.

        **参数解释**：协议版本，例如v1.0.0。 **取值范围**：长度为1~128的英文字母、数字、下划线、中划线和小数点的组合。

        :return: The version of this V2AgreementRule.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this V2AgreementRule.

        **参数解释**：协议版本，例如v1.0.0。 **取值范围**：长度为1~128的英文字母、数字、下划线、中划线和小数点的组合。

        :param version: The version of this V2AgreementRule.
        :type version: str
        """
        self._version = version

    @property
    def url(self):
        r"""Gets the url of this V2AgreementRule.

        **参数解释**：协议链接。 **取值范围**：符合URL格式规范，由英文字母、数字及URL合法特殊字符组成，长度不超过2000个字符。

        :return: The url of this V2AgreementRule.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this V2AgreementRule.

        **参数解释**：协议链接。 **取值范围**：符合URL格式规范，由英文字母、数字及URL合法特殊字符组成，长度不超过2000个字符。

        :param url: The url of this V2AgreementRule.
        :type url: str
        """
        self._url = url

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
        if not isinstance(other, V2AgreementRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
