# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DetectLabels:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'compliance_labels': 'list[str]',
        'inject_labels': 'list[str]',
        'immunity_lexicon_labels': 'list[str]',
        'lexicon_labels': 'list[str]',
        'lexicon_internal_labels': 'list[str]',
        'supported_language_labels': 'list[str]',
        'pii_labels': 'list[str]'
    }

    attribute_map = {
        'compliance_labels': 'compliance_labels',
        'inject_labels': 'inject_labels',
        'immunity_lexicon_labels': 'immunity_lexicon_labels',
        'lexicon_labels': 'lexicon_labels',
        'lexicon_internal_labels': 'lexicon_internal_labels',
        'supported_language_labels': 'supported_language_labels',
        'pii_labels': 'pii_labels'
    }

    def __init__(self, compliance_labels=None, inject_labels=None, immunity_lexicon_labels=None, lexicon_labels=None, lexicon_internal_labels=None, supported_language_labels=None, pii_labels=None):
        r"""DetectLabels

        The model defined in huaweicloud sdk

        :param compliance_labels: 合规检测标签列表
        :type compliance_labels: list[str]
        :param inject_labels: 注入检测标签列表
        :type inject_labels: list[str]
        :param immunity_lexicon_labels: 豁免词库标签列表
        :type immunity_lexicon_labels: list[str]
        :param lexicon_labels: 自定义词库检测标签列表
        :type lexicon_labels: list[str]
        :param lexicon_internal_labels: 内置词库检测标签列表
        :type lexicon_internal_labels: list[str]
        :param supported_language_labels: 支持检测语言标签列表
        :type supported_language_labels: list[str]
        :param pii_labels: 敏感词标签列表
        :type pii_labels: list[str]
        """
        
        

        self._compliance_labels = None
        self._inject_labels = None
        self._immunity_lexicon_labels = None
        self._lexicon_labels = None
        self._lexicon_internal_labels = None
        self._supported_language_labels = None
        self._pii_labels = None
        self.discriminator = None

        if compliance_labels is not None:
            self.compliance_labels = compliance_labels
        if inject_labels is not None:
            self.inject_labels = inject_labels
        if immunity_lexicon_labels is not None:
            self.immunity_lexicon_labels = immunity_lexicon_labels
        if lexicon_labels is not None:
            self.lexicon_labels = lexicon_labels
        if lexicon_internal_labels is not None:
            self.lexicon_internal_labels = lexicon_internal_labels
        if supported_language_labels is not None:
            self.supported_language_labels = supported_language_labels
        if pii_labels is not None:
            self.pii_labels = pii_labels

    @property
    def compliance_labels(self):
        r"""Gets the compliance_labels of this DetectLabels.

        合规检测标签列表

        :return: The compliance_labels of this DetectLabels.
        :rtype: list[str]
        """
        return self._compliance_labels

    @compliance_labels.setter
    def compliance_labels(self, compliance_labels):
        r"""Sets the compliance_labels of this DetectLabels.

        合规检测标签列表

        :param compliance_labels: The compliance_labels of this DetectLabels.
        :type compliance_labels: list[str]
        """
        self._compliance_labels = compliance_labels

    @property
    def inject_labels(self):
        r"""Gets the inject_labels of this DetectLabels.

        注入检测标签列表

        :return: The inject_labels of this DetectLabels.
        :rtype: list[str]
        """
        return self._inject_labels

    @inject_labels.setter
    def inject_labels(self, inject_labels):
        r"""Sets the inject_labels of this DetectLabels.

        注入检测标签列表

        :param inject_labels: The inject_labels of this DetectLabels.
        :type inject_labels: list[str]
        """
        self._inject_labels = inject_labels

    @property
    def immunity_lexicon_labels(self):
        r"""Gets the immunity_lexicon_labels of this DetectLabels.

        豁免词库标签列表

        :return: The immunity_lexicon_labels of this DetectLabels.
        :rtype: list[str]
        """
        return self._immunity_lexicon_labels

    @immunity_lexicon_labels.setter
    def immunity_lexicon_labels(self, immunity_lexicon_labels):
        r"""Sets the immunity_lexicon_labels of this DetectLabels.

        豁免词库标签列表

        :param immunity_lexicon_labels: The immunity_lexicon_labels of this DetectLabels.
        :type immunity_lexicon_labels: list[str]
        """
        self._immunity_lexicon_labels = immunity_lexicon_labels

    @property
    def lexicon_labels(self):
        r"""Gets the lexicon_labels of this DetectLabels.

        自定义词库检测标签列表

        :return: The lexicon_labels of this DetectLabels.
        :rtype: list[str]
        """
        return self._lexicon_labels

    @lexicon_labels.setter
    def lexicon_labels(self, lexicon_labels):
        r"""Sets the lexicon_labels of this DetectLabels.

        自定义词库检测标签列表

        :param lexicon_labels: The lexicon_labels of this DetectLabels.
        :type lexicon_labels: list[str]
        """
        self._lexicon_labels = lexicon_labels

    @property
    def lexicon_internal_labels(self):
        r"""Gets the lexicon_internal_labels of this DetectLabels.

        内置词库检测标签列表

        :return: The lexicon_internal_labels of this DetectLabels.
        :rtype: list[str]
        """
        return self._lexicon_internal_labels

    @lexicon_internal_labels.setter
    def lexicon_internal_labels(self, lexicon_internal_labels):
        r"""Sets the lexicon_internal_labels of this DetectLabels.

        内置词库检测标签列表

        :param lexicon_internal_labels: The lexicon_internal_labels of this DetectLabels.
        :type lexicon_internal_labels: list[str]
        """
        self._lexicon_internal_labels = lexicon_internal_labels

    @property
    def supported_language_labels(self):
        r"""Gets the supported_language_labels of this DetectLabels.

        支持检测语言标签列表

        :return: The supported_language_labels of this DetectLabels.
        :rtype: list[str]
        """
        return self._supported_language_labels

    @supported_language_labels.setter
    def supported_language_labels(self, supported_language_labels):
        r"""Sets the supported_language_labels of this DetectLabels.

        支持检测语言标签列表

        :param supported_language_labels: The supported_language_labels of this DetectLabels.
        :type supported_language_labels: list[str]
        """
        self._supported_language_labels = supported_language_labels

    @property
    def pii_labels(self):
        r"""Gets the pii_labels of this DetectLabels.

        敏感词标签列表

        :return: The pii_labels of this DetectLabels.
        :rtype: list[str]
        """
        return self._pii_labels

    @pii_labels.setter
    def pii_labels(self, pii_labels):
        r"""Sets the pii_labels of this DetectLabels.

        敏感词标签列表

        :param pii_labels: The pii_labels of this DetectLabels.
        :type pii_labels: list[str]
        """
        self._pii_labels = pii_labels

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
        if not isinstance(other, DetectLabels):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
