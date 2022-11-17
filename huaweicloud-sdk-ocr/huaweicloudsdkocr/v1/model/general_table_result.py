# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GeneralTableResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'words_region_count': 'int',
        'words_region_list': 'list[WordsRegionList]',
        'excel': 'str'
    }

    attribute_map = {
        'words_region_count': 'words_region_count',
        'words_region_list': 'words_region_list',
        'excel': 'excel'
    }

    def __init__(self, words_region_count=None, words_region_list=None, excel=None):
        """GeneralTableResult

        The model defined in huaweicloud sdk

        :param words_region_count: 文字区域数目。          
        :type words_region_count: int
        :param words_region_list: 文字区域识别结果列表，输出顺序从左到右，先上后下。 
        :type words_region_list: list[:class:`huaweicloudsdkocr.v1.WordsRegionList`]
        :param excel: 表格图像转换为excel的base64编码，图像中的文字和表格按位置写入excel。对返回的excel编码可用base64.b64decode解码并保存为.xlsx文件。 
        :type excel: str
        """
        
        

        self._words_region_count = None
        self._words_region_list = None
        self._excel = None
        self.discriminator = None

        self.words_region_count = words_region_count
        self.words_region_list = words_region_list
        if excel is not None:
            self.excel = excel

    @property
    def words_region_count(self):
        """Gets the words_region_count of this GeneralTableResult.

        文字区域数目。          

        :return: The words_region_count of this GeneralTableResult.
        :rtype: int
        """
        return self._words_region_count

    @words_region_count.setter
    def words_region_count(self, words_region_count):
        """Sets the words_region_count of this GeneralTableResult.

        文字区域数目。          

        :param words_region_count: The words_region_count of this GeneralTableResult.
        :type words_region_count: int
        """
        self._words_region_count = words_region_count

    @property
    def words_region_list(self):
        """Gets the words_region_list of this GeneralTableResult.

        文字区域识别结果列表，输出顺序从左到右，先上后下。 

        :return: The words_region_list of this GeneralTableResult.
        :rtype: list[:class:`huaweicloudsdkocr.v1.WordsRegionList`]
        """
        return self._words_region_list

    @words_region_list.setter
    def words_region_list(self, words_region_list):
        """Sets the words_region_list of this GeneralTableResult.

        文字区域识别结果列表，输出顺序从左到右，先上后下。 

        :param words_region_list: The words_region_list of this GeneralTableResult.
        :type words_region_list: list[:class:`huaweicloudsdkocr.v1.WordsRegionList`]
        """
        self._words_region_list = words_region_list

    @property
    def excel(self):
        """Gets the excel of this GeneralTableResult.

        表格图像转换为excel的base64编码，图像中的文字和表格按位置写入excel。对返回的excel编码可用base64.b64decode解码并保存为.xlsx文件。 

        :return: The excel of this GeneralTableResult.
        :rtype: str
        """
        return self._excel

    @excel.setter
    def excel(self, excel):
        """Sets the excel of this GeneralTableResult.

        表格图像转换为excel的base64编码，图像中的文字和表格按位置写入excel。对返回的excel编码可用base64.b64decode解码并保存为.xlsx文件。 

        :param excel: The excel of this GeneralTableResult.
        :type excel: str
        """
        self._excel = excel

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
        if not isinstance(other, GeneralTableResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
