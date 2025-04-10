# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SmartDocumentRecognizerFormResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'form_count': 'int',
        'form_list': 'list[SmartDocumentRecognizerTableBlock]'
    }

    attribute_map = {
        'form_count': 'form_count',
        'form_list': 'form_list'
    }

    def __init__(self, form_count=None, form_list=None):
        r"""SmartDocumentRecognizerFormResult

        The model defined in huaweicloud sdk

        :param form_count: 模型识别到的有线表单数量。 
        :type form_count: int
        :param form_list: 有线表单识别结果列表。 
        :type form_list: list[:class:`huaweicloudsdkocr.v1.SmartDocumentRecognizerTableBlock`]
        """
        
        

        self._form_count = None
        self._form_list = None
        self.discriminator = None

        if form_count is not None:
            self.form_count = form_count
        if form_list is not None:
            self.form_list = form_list

    @property
    def form_count(self):
        r"""Gets the form_count of this SmartDocumentRecognizerFormResult.

        模型识别到的有线表单数量。 

        :return: The form_count of this SmartDocumentRecognizerFormResult.
        :rtype: int
        """
        return self._form_count

    @form_count.setter
    def form_count(self, form_count):
        r"""Sets the form_count of this SmartDocumentRecognizerFormResult.

        模型识别到的有线表单数量。 

        :param form_count: The form_count of this SmartDocumentRecognizerFormResult.
        :type form_count: int
        """
        self._form_count = form_count

    @property
    def form_list(self):
        r"""Gets the form_list of this SmartDocumentRecognizerFormResult.

        有线表单识别结果列表。 

        :return: The form_list of this SmartDocumentRecognizerFormResult.
        :rtype: list[:class:`huaweicloudsdkocr.v1.SmartDocumentRecognizerTableBlock`]
        """
        return self._form_list

    @form_list.setter
    def form_list(self, form_list):
        r"""Sets the form_list of this SmartDocumentRecognizerFormResult.

        有线表单识别结果列表。 

        :param form_list: The form_list of this SmartDocumentRecognizerFormResult.
        :type form_list: list[:class:`huaweicloudsdkocr.v1.SmartDocumentRecognizerTableBlock`]
        """
        self._form_list = form_list

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
        if not isinstance(other, SmartDocumentRecognizerFormResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
