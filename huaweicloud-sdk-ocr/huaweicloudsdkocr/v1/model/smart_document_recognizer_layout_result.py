# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SmartDocumentRecognizerLayoutResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'layout_block_count': 'int',
        'layout_block_list': 'list[SmartDocumentRecognizerLayoutBlock]'
    }

    attribute_map = {
        'layout_block_count': 'layout_block_count',
        'layout_block_list': 'layout_block_list'
    }

    def __init__(self, layout_block_count=None, layout_block_list=None):
        """SmartDocumentRecognizerLayoutResult

        The model defined in huaweicloud sdk

        :param layout_block_count: 模型识别到的文档版面区域数量。        
        :type layout_block_count: int
        :param layout_block_list: 文档版面区域识别结果列表。 
        :type layout_block_list: list[:class:`huaweicloudsdkocr.v1.SmartDocumentRecognizerLayoutBlock`]
        """
        
        

        self._layout_block_count = None
        self._layout_block_list = None
        self.discriminator = None

        if layout_block_count is not None:
            self.layout_block_count = layout_block_count
        if layout_block_list is not None:
            self.layout_block_list = layout_block_list

    @property
    def layout_block_count(self):
        """Gets the layout_block_count of this SmartDocumentRecognizerLayoutResult.

        模型识别到的文档版面区域数量。        

        :return: The layout_block_count of this SmartDocumentRecognizerLayoutResult.
        :rtype: int
        """
        return self._layout_block_count

    @layout_block_count.setter
    def layout_block_count(self, layout_block_count):
        """Sets the layout_block_count of this SmartDocumentRecognizerLayoutResult.

        模型识别到的文档版面区域数量。        

        :param layout_block_count: The layout_block_count of this SmartDocumentRecognizerLayoutResult.
        :type layout_block_count: int
        """
        self._layout_block_count = layout_block_count

    @property
    def layout_block_list(self):
        """Gets the layout_block_list of this SmartDocumentRecognizerLayoutResult.

        文档版面区域识别结果列表。 

        :return: The layout_block_list of this SmartDocumentRecognizerLayoutResult.
        :rtype: list[:class:`huaweicloudsdkocr.v1.SmartDocumentRecognizerLayoutBlock`]
        """
        return self._layout_block_list

    @layout_block_list.setter
    def layout_block_list(self, layout_block_list):
        """Sets the layout_block_list of this SmartDocumentRecognizerLayoutResult.

        文档版面区域识别结果列表。 

        :param layout_block_list: The layout_block_list of this SmartDocumentRecognizerLayoutResult.
        :type layout_block_list: list[:class:`huaweicloudsdkocr.v1.SmartDocumentRecognizerLayoutBlock`]
        """
        self._layout_block_list = layout_block_list

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
        if not isinstance(other, SmartDocumentRecognizerLayoutResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
