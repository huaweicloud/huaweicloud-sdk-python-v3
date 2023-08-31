# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SmartDocumentRecognizerResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ocr_result': 'SmartDocumentRecognizerOcrResult',
        'kv_result': 'SmartDocumentRecognizerKvResult',
        'table_result': 'SmartDocumentRecognizerTableResult',
        'layout_result': 'SmartDocumentRecognizerLayoutResult'
    }

    attribute_map = {
        'ocr_result': 'ocr_result',
        'kv_result': 'kv_result',
        'table_result': 'table_result',
        'layout_result': 'layout_result'
    }

    def __init__(self, ocr_result=None, kv_result=None, table_result=None, layout_result=None):
        """SmartDocumentRecognizerResult

        The model defined in huaweicloud sdk

        :param ocr_result: 
        :type ocr_result: :class:`huaweicloudsdkocr.v1.SmartDocumentRecognizerOcrResult`
        :param kv_result: 
        :type kv_result: :class:`huaweicloudsdkocr.v1.SmartDocumentRecognizerKvResult`
        :param table_result: 
        :type table_result: :class:`huaweicloudsdkocr.v1.SmartDocumentRecognizerTableResult`
        :param layout_result: 
        :type layout_result: :class:`huaweicloudsdkocr.v1.SmartDocumentRecognizerLayoutResult`
        """
        
        

        self._ocr_result = None
        self._kv_result = None
        self._table_result = None
        self._layout_result = None
        self.discriminator = None

        self.ocr_result = ocr_result
        if kv_result is not None:
            self.kv_result = kv_result
        if table_result is not None:
            self.table_result = table_result
        if layout_result is not None:
            self.layout_result = layout_result

    @property
    def ocr_result(self):
        """Gets the ocr_result of this SmartDocumentRecognizerResult.

        :return: The ocr_result of this SmartDocumentRecognizerResult.
        :rtype: :class:`huaweicloudsdkocr.v1.SmartDocumentRecognizerOcrResult`
        """
        return self._ocr_result

    @ocr_result.setter
    def ocr_result(self, ocr_result):
        """Sets the ocr_result of this SmartDocumentRecognizerResult.

        :param ocr_result: The ocr_result of this SmartDocumentRecognizerResult.
        :type ocr_result: :class:`huaweicloudsdkocr.v1.SmartDocumentRecognizerOcrResult`
        """
        self._ocr_result = ocr_result

    @property
    def kv_result(self):
        """Gets the kv_result of this SmartDocumentRecognizerResult.

        :return: The kv_result of this SmartDocumentRecognizerResult.
        :rtype: :class:`huaweicloudsdkocr.v1.SmartDocumentRecognizerKvResult`
        """
        return self._kv_result

    @kv_result.setter
    def kv_result(self, kv_result):
        """Sets the kv_result of this SmartDocumentRecognizerResult.

        :param kv_result: The kv_result of this SmartDocumentRecognizerResult.
        :type kv_result: :class:`huaweicloudsdkocr.v1.SmartDocumentRecognizerKvResult`
        """
        self._kv_result = kv_result

    @property
    def table_result(self):
        """Gets the table_result of this SmartDocumentRecognizerResult.

        :return: The table_result of this SmartDocumentRecognizerResult.
        :rtype: :class:`huaweicloudsdkocr.v1.SmartDocumentRecognizerTableResult`
        """
        return self._table_result

    @table_result.setter
    def table_result(self, table_result):
        """Sets the table_result of this SmartDocumentRecognizerResult.

        :param table_result: The table_result of this SmartDocumentRecognizerResult.
        :type table_result: :class:`huaweicloudsdkocr.v1.SmartDocumentRecognizerTableResult`
        """
        self._table_result = table_result

    @property
    def layout_result(self):
        """Gets the layout_result of this SmartDocumentRecognizerResult.

        :return: The layout_result of this SmartDocumentRecognizerResult.
        :rtype: :class:`huaweicloudsdkocr.v1.SmartDocumentRecognizerLayoutResult`
        """
        return self._layout_result

    @layout_result.setter
    def layout_result(self, layout_result):
        """Sets the layout_result of this SmartDocumentRecognizerResult.

        :param layout_result: The layout_result of this SmartDocumentRecognizerResult.
        :type layout_result: :class:`huaweicloudsdkocr.v1.SmartDocumentRecognizerLayoutResult`
        """
        self._layout_result = layout_result

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
        if not isinstance(other, SmartDocumentRecognizerResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
