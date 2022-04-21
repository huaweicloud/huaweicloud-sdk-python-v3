# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DiagnosisItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'cause_ids': 'list[ConclusionItem]',
        'impact_ids': 'list[ConclusionItem]',
        'advice_ids': 'list[ConclusionItem]',
        'result': 'str'
    }

    attribute_map = {
        'name': 'name',
        'cause_ids': 'cause_ids',
        'impact_ids': 'impact_ids',
        'advice_ids': 'advice_ids',
        'result': 'result'
    }

    def __init__(self, name=None, cause_ids=None, impact_ids=None, advice_ids=None, result=None):
        """DiagnosisItem

        The model defined in huaweicloud sdk

        :param name: 诊断项名称
        :type name: str
        :param cause_ids: 原因ID列表
        :type cause_ids: list[:class:`huaweicloudsdkdcs.v2.ConclusionItem`]
        :param impact_ids: 影响ID列表
        :type impact_ids: list[:class:`huaweicloudsdkdcs.v2.ConclusionItem`]
        :param advice_ids: 建议ID列表
        :type advice_ids: list[:class:`huaweicloudsdkdcs.v2.ConclusionItem`]
        :param result: 诊断结果
        :type result: str
        """
        
        

        self._name = None
        self._cause_ids = None
        self._impact_ids = None
        self._advice_ids = None
        self._result = None
        self.discriminator = None

        self.name = name
        if cause_ids is not None:
            self.cause_ids = cause_ids
        if impact_ids is not None:
            self.impact_ids = impact_ids
        if advice_ids is not None:
            self.advice_ids = advice_ids
        self.result = result

    @property
    def name(self):
        """Gets the name of this DiagnosisItem.

        诊断项名称

        :return: The name of this DiagnosisItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DiagnosisItem.

        诊断项名称

        :param name: The name of this DiagnosisItem.
        :type name: str
        """
        self._name = name

    @property
    def cause_ids(self):
        """Gets the cause_ids of this DiagnosisItem.

        原因ID列表

        :return: The cause_ids of this DiagnosisItem.
        :rtype: list[:class:`huaweicloudsdkdcs.v2.ConclusionItem`]
        """
        return self._cause_ids

    @cause_ids.setter
    def cause_ids(self, cause_ids):
        """Sets the cause_ids of this DiagnosisItem.

        原因ID列表

        :param cause_ids: The cause_ids of this DiagnosisItem.
        :type cause_ids: list[:class:`huaweicloudsdkdcs.v2.ConclusionItem`]
        """
        self._cause_ids = cause_ids

    @property
    def impact_ids(self):
        """Gets the impact_ids of this DiagnosisItem.

        影响ID列表

        :return: The impact_ids of this DiagnosisItem.
        :rtype: list[:class:`huaweicloudsdkdcs.v2.ConclusionItem`]
        """
        return self._impact_ids

    @impact_ids.setter
    def impact_ids(self, impact_ids):
        """Sets the impact_ids of this DiagnosisItem.

        影响ID列表

        :param impact_ids: The impact_ids of this DiagnosisItem.
        :type impact_ids: list[:class:`huaweicloudsdkdcs.v2.ConclusionItem`]
        """
        self._impact_ids = impact_ids

    @property
    def advice_ids(self):
        """Gets the advice_ids of this DiagnosisItem.

        建议ID列表

        :return: The advice_ids of this DiagnosisItem.
        :rtype: list[:class:`huaweicloudsdkdcs.v2.ConclusionItem`]
        """
        return self._advice_ids

    @advice_ids.setter
    def advice_ids(self, advice_ids):
        """Sets the advice_ids of this DiagnosisItem.

        建议ID列表

        :param advice_ids: The advice_ids of this DiagnosisItem.
        :type advice_ids: list[:class:`huaweicloudsdkdcs.v2.ConclusionItem`]
        """
        self._advice_ids = advice_ids

    @property
    def result(self):
        """Gets the result of this DiagnosisItem.

        诊断结果

        :return: The result of this DiagnosisItem.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this DiagnosisItem.

        诊断结果

        :param result: The result of this DiagnosisItem.
        :type result: str
        """
        self._result = result

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
        if not isinstance(other, DiagnosisItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
