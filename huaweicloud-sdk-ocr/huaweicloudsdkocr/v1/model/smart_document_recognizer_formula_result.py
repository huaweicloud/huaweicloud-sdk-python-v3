# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SmartDocumentRecognizerFormulaResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'formula_count': 'int',
        'formula_list': 'list[SmartDocumentRecognizerFormulaBlock]'
    }

    attribute_map = {
        'formula_count': 'formula_count',
        'formula_list': 'formula_list'
    }

    def __init__(self, formula_count=None, formula_list=None):
        r"""SmartDocumentRecognizerFormulaResult

        The model defined in huaweicloud sdk

        :param formula_count: 数学公式数量。 
        :type formula_count: int
        :param formula_list: 数学公式识别结果列表。 
        :type formula_list: list[:class:`huaweicloudsdkocr.v1.SmartDocumentRecognizerFormulaBlock`]
        """
        
        

        self._formula_count = None
        self._formula_list = None
        self.discriminator = None

        if formula_count is not None:
            self.formula_count = formula_count
        if formula_list is not None:
            self.formula_list = formula_list

    @property
    def formula_count(self):
        r"""Gets the formula_count of this SmartDocumentRecognizerFormulaResult.

        数学公式数量。 

        :return: The formula_count of this SmartDocumentRecognizerFormulaResult.
        :rtype: int
        """
        return self._formula_count

    @formula_count.setter
    def formula_count(self, formula_count):
        r"""Sets the formula_count of this SmartDocumentRecognizerFormulaResult.

        数学公式数量。 

        :param formula_count: The formula_count of this SmartDocumentRecognizerFormulaResult.
        :type formula_count: int
        """
        self._formula_count = formula_count

    @property
    def formula_list(self):
        r"""Gets the formula_list of this SmartDocumentRecognizerFormulaResult.

        数学公式识别结果列表。 

        :return: The formula_list of this SmartDocumentRecognizerFormulaResult.
        :rtype: list[:class:`huaweicloudsdkocr.v1.SmartDocumentRecognizerFormulaBlock`]
        """
        return self._formula_list

    @formula_list.setter
    def formula_list(self, formula_list):
        r"""Sets the formula_list of this SmartDocumentRecognizerFormulaResult.

        数学公式识别结果列表。 

        :param formula_list: The formula_list of this SmartDocumentRecognizerFormulaResult.
        :type formula_list: list[:class:`huaweicloudsdkocr.v1.SmartDocumentRecognizerFormulaBlock`]
        """
        self._formula_list = formula_list

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
        if not isinstance(other, SmartDocumentRecognizerFormulaResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
