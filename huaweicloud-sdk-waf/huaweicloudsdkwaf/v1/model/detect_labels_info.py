# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DetectLabelsInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'compliance_labels_info': 'list[LabelInfo]',
        'inject_labels_info': 'list[LabelInfo]',
        'immunity_lexicon_labels_info': 'list[LabelInfo]',
        'lexicon_labels_info': 'list[LabelInfo]',
        'lexicon_internal_labels_info': 'list[LabelInfo]',
        'supported_language_labels': 'list[LabelInfo]',
        'pii_labels_info': 'list[LabelInfo]'
    }

    attribute_map = {
        'compliance_labels_info': 'compliance_labels_info',
        'inject_labels_info': 'inject_labels_info',
        'immunity_lexicon_labels_info': 'immunity_lexicon_labels_info',
        'lexicon_labels_info': 'lexicon_labels_info',
        'lexicon_internal_labels_info': 'lexicon_internal_labels_info',
        'supported_language_labels': 'supported_language_labels',
        'pii_labels_info': 'pii_labels_info'
    }

    def __init__(self, compliance_labels_info=None, inject_labels_info=None, immunity_lexicon_labels_info=None, lexicon_labels_info=None, lexicon_internal_labels_info=None, supported_language_labels=None, pii_labels_info=None):
        r"""DetectLabelsInfo

        The model defined in huaweicloud sdk

        :param compliance_labels_info: 合规检测标签详情列表
        :type compliance_labels_info: list[:class:`huaweicloudsdkwaf.v1.LabelInfo`]
        :param inject_labels_info: 注入检测标签详情列表
        :type inject_labels_info: list[:class:`huaweicloudsdkwaf.v1.LabelInfo`]
        :param immunity_lexicon_labels_info: 豁免词库标签详情列表
        :type immunity_lexicon_labels_info: list[:class:`huaweicloudsdkwaf.v1.LabelInfo`]
        :param lexicon_labels_info: 自定义词库检测标签详情列表
        :type lexicon_labels_info: list[:class:`huaweicloudsdkwaf.v1.LabelInfo`]
        :param lexicon_internal_labels_info: 内置词库检测标签详情列表
        :type lexicon_internal_labels_info: list[:class:`huaweicloudsdkwaf.v1.LabelInfo`]
        :param supported_language_labels: 语言检测标签信息列表
        :type supported_language_labels: list[:class:`huaweicloudsdkwaf.v1.LabelInfo`]
        :param pii_labels_info: 敏感词的标签详情列表
        :type pii_labels_info: list[:class:`huaweicloudsdkwaf.v1.LabelInfo`]
        """
        
        

        self._compliance_labels_info = None
        self._inject_labels_info = None
        self._immunity_lexicon_labels_info = None
        self._lexicon_labels_info = None
        self._lexicon_internal_labels_info = None
        self._supported_language_labels = None
        self._pii_labels_info = None
        self.discriminator = None

        if compliance_labels_info is not None:
            self.compliance_labels_info = compliance_labels_info
        if inject_labels_info is not None:
            self.inject_labels_info = inject_labels_info
        if immunity_lexicon_labels_info is not None:
            self.immunity_lexicon_labels_info = immunity_lexicon_labels_info
        if lexicon_labels_info is not None:
            self.lexicon_labels_info = lexicon_labels_info
        if lexicon_internal_labels_info is not None:
            self.lexicon_internal_labels_info = lexicon_internal_labels_info
        if supported_language_labels is not None:
            self.supported_language_labels = supported_language_labels
        if pii_labels_info is not None:
            self.pii_labels_info = pii_labels_info

    @property
    def compliance_labels_info(self):
        r"""Gets the compliance_labels_info of this DetectLabelsInfo.

        合规检测标签详情列表

        :return: The compliance_labels_info of this DetectLabelsInfo.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.LabelInfo`]
        """
        return self._compliance_labels_info

    @compliance_labels_info.setter
    def compliance_labels_info(self, compliance_labels_info):
        r"""Sets the compliance_labels_info of this DetectLabelsInfo.

        合规检测标签详情列表

        :param compliance_labels_info: The compliance_labels_info of this DetectLabelsInfo.
        :type compliance_labels_info: list[:class:`huaweicloudsdkwaf.v1.LabelInfo`]
        """
        self._compliance_labels_info = compliance_labels_info

    @property
    def inject_labels_info(self):
        r"""Gets the inject_labels_info of this DetectLabelsInfo.

        注入检测标签详情列表

        :return: The inject_labels_info of this DetectLabelsInfo.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.LabelInfo`]
        """
        return self._inject_labels_info

    @inject_labels_info.setter
    def inject_labels_info(self, inject_labels_info):
        r"""Sets the inject_labels_info of this DetectLabelsInfo.

        注入检测标签详情列表

        :param inject_labels_info: The inject_labels_info of this DetectLabelsInfo.
        :type inject_labels_info: list[:class:`huaweicloudsdkwaf.v1.LabelInfo`]
        """
        self._inject_labels_info = inject_labels_info

    @property
    def immunity_lexicon_labels_info(self):
        r"""Gets the immunity_lexicon_labels_info of this DetectLabelsInfo.

        豁免词库标签详情列表

        :return: The immunity_lexicon_labels_info of this DetectLabelsInfo.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.LabelInfo`]
        """
        return self._immunity_lexicon_labels_info

    @immunity_lexicon_labels_info.setter
    def immunity_lexicon_labels_info(self, immunity_lexicon_labels_info):
        r"""Sets the immunity_lexicon_labels_info of this DetectLabelsInfo.

        豁免词库标签详情列表

        :param immunity_lexicon_labels_info: The immunity_lexicon_labels_info of this DetectLabelsInfo.
        :type immunity_lexicon_labels_info: list[:class:`huaweicloudsdkwaf.v1.LabelInfo`]
        """
        self._immunity_lexicon_labels_info = immunity_lexicon_labels_info

    @property
    def lexicon_labels_info(self):
        r"""Gets the lexicon_labels_info of this DetectLabelsInfo.

        自定义词库检测标签详情列表

        :return: The lexicon_labels_info of this DetectLabelsInfo.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.LabelInfo`]
        """
        return self._lexicon_labels_info

    @lexicon_labels_info.setter
    def lexicon_labels_info(self, lexicon_labels_info):
        r"""Sets the lexicon_labels_info of this DetectLabelsInfo.

        自定义词库检测标签详情列表

        :param lexicon_labels_info: The lexicon_labels_info of this DetectLabelsInfo.
        :type lexicon_labels_info: list[:class:`huaweicloudsdkwaf.v1.LabelInfo`]
        """
        self._lexicon_labels_info = lexicon_labels_info

    @property
    def lexicon_internal_labels_info(self):
        r"""Gets the lexicon_internal_labels_info of this DetectLabelsInfo.

        内置词库检测标签详情列表

        :return: The lexicon_internal_labels_info of this DetectLabelsInfo.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.LabelInfo`]
        """
        return self._lexicon_internal_labels_info

    @lexicon_internal_labels_info.setter
    def lexicon_internal_labels_info(self, lexicon_internal_labels_info):
        r"""Sets the lexicon_internal_labels_info of this DetectLabelsInfo.

        内置词库检测标签详情列表

        :param lexicon_internal_labels_info: The lexicon_internal_labels_info of this DetectLabelsInfo.
        :type lexicon_internal_labels_info: list[:class:`huaweicloudsdkwaf.v1.LabelInfo`]
        """
        self._lexicon_internal_labels_info = lexicon_internal_labels_info

    @property
    def supported_language_labels(self):
        r"""Gets the supported_language_labels of this DetectLabelsInfo.

        语言检测标签信息列表

        :return: The supported_language_labels of this DetectLabelsInfo.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.LabelInfo`]
        """
        return self._supported_language_labels

    @supported_language_labels.setter
    def supported_language_labels(self, supported_language_labels):
        r"""Sets the supported_language_labels of this DetectLabelsInfo.

        语言检测标签信息列表

        :param supported_language_labels: The supported_language_labels of this DetectLabelsInfo.
        :type supported_language_labels: list[:class:`huaweicloudsdkwaf.v1.LabelInfo`]
        """
        self._supported_language_labels = supported_language_labels

    @property
    def pii_labels_info(self):
        r"""Gets the pii_labels_info of this DetectLabelsInfo.

        敏感词的标签详情列表

        :return: The pii_labels_info of this DetectLabelsInfo.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.LabelInfo`]
        """
        return self._pii_labels_info

    @pii_labels_info.setter
    def pii_labels_info(self, pii_labels_info):
        r"""Sets the pii_labels_info of this DetectLabelsInfo.

        敏感词的标签详情列表

        :param pii_labels_info: The pii_labels_info of this DetectLabelsInfo.
        :type pii_labels_info: list[:class:`huaweicloudsdkwaf.v1.LabelInfo`]
        """
        self._pii_labels_info = pii_labels_info

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
        if not isinstance(other, DetectLabelsInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
