# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SmartDocumentRecognizerKvResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'kv_block_count': 'int',
        'kv_block_list': 'list[SmartDocumentRecognizerKVBlock]'
    }

    attribute_map = {
        'kv_block_count': 'kv_block_count',
        'kv_block_list': 'kv_block_list'
    }

    def __init__(self, kv_block_count=None, kv_block_list=None):
        """SmartDocumentRecognizerKvResult

        The model defined in huaweicloud sdk

        :param kv_block_count: 模型识别到的键值对数量。 
        :type kv_block_count: int
        :param kv_block_list: 键值对识别结果列表。 
        :type kv_block_list: list[:class:`huaweicloudsdkocr.v1.SmartDocumentRecognizerKVBlock`]
        """
        
        

        self._kv_block_count = None
        self._kv_block_list = None
        self.discriminator = None

        if kv_block_count is not None:
            self.kv_block_count = kv_block_count
        if kv_block_list is not None:
            self.kv_block_list = kv_block_list

    @property
    def kv_block_count(self):
        """Gets the kv_block_count of this SmartDocumentRecognizerKvResult.

        模型识别到的键值对数量。 

        :return: The kv_block_count of this SmartDocumentRecognizerKvResult.
        :rtype: int
        """
        return self._kv_block_count

    @kv_block_count.setter
    def kv_block_count(self, kv_block_count):
        """Sets the kv_block_count of this SmartDocumentRecognizerKvResult.

        模型识别到的键值对数量。 

        :param kv_block_count: The kv_block_count of this SmartDocumentRecognizerKvResult.
        :type kv_block_count: int
        """
        self._kv_block_count = kv_block_count

    @property
    def kv_block_list(self):
        """Gets the kv_block_list of this SmartDocumentRecognizerKvResult.

        键值对识别结果列表。 

        :return: The kv_block_list of this SmartDocumentRecognizerKvResult.
        :rtype: list[:class:`huaweicloudsdkocr.v1.SmartDocumentRecognizerKVBlock`]
        """
        return self._kv_block_list

    @kv_block_list.setter
    def kv_block_list(self, kv_block_list):
        """Sets the kv_block_list of this SmartDocumentRecognizerKvResult.

        键值对识别结果列表。 

        :param kv_block_list: The kv_block_list of this SmartDocumentRecognizerKvResult.
        :type kv_block_list: list[:class:`huaweicloudsdkocr.v1.SmartDocumentRecognizerKVBlock`]
        """
        self._kv_block_list = kv_block_list

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
        if not isinstance(other, SmartDocumentRecognizerKvResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
