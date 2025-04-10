# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClassificationResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'result': 'DiagnoseResult',
        'security_level': 'bool',
        'classification': 'bool'
    }

    attribute_map = {
        'result': 'result',
        'security_level': 'security_level',
        'classification': 'classification'
    }

    def __init__(self, result=None, security_level=None, classification=None):
        r"""ClassificationResult

        The model defined in huaweicloud sdk

        :param result: 
        :type result: :class:`huaweicloudsdkdataartsstudio.v1.DiagnoseResult`
        :param security_level: 是否配置了密级
        :type security_level: bool
        :param classification: 是否配置了分类
        :type classification: bool
        """
        
        

        self._result = None
        self._security_level = None
        self._classification = None
        self.discriminator = None

        if result is not None:
            self.result = result
        if security_level is not None:
            self.security_level = security_level
        if classification is not None:
            self.classification = classification

    @property
    def result(self):
        r"""Gets the result of this ClassificationResult.

        :return: The result of this ClassificationResult.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.DiagnoseResult`
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this ClassificationResult.

        :param result: The result of this ClassificationResult.
        :type result: :class:`huaweicloudsdkdataartsstudio.v1.DiagnoseResult`
        """
        self._result = result

    @property
    def security_level(self):
        r"""Gets the security_level of this ClassificationResult.

        是否配置了密级

        :return: The security_level of this ClassificationResult.
        :rtype: bool
        """
        return self._security_level

    @security_level.setter
    def security_level(self, security_level):
        r"""Sets the security_level of this ClassificationResult.

        是否配置了密级

        :param security_level: The security_level of this ClassificationResult.
        :type security_level: bool
        """
        self._security_level = security_level

    @property
    def classification(self):
        r"""Gets the classification of this ClassificationResult.

        是否配置了分类

        :return: The classification of this ClassificationResult.
        :rtype: bool
        """
        return self._classification

    @classification.setter
    def classification(self, classification):
        r"""Sets the classification of this ClassificationResult.

        是否配置了分类

        :param classification: The classification of this ClassificationResult.
        :type classification: bool
        """
        self._classification = classification

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
        if not isinstance(other, ClassificationResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
