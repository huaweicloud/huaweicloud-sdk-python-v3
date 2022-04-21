# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FinancialStatementResult:

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
        'words_region_list': 'list[FinancialStatementWordsRegionList]',
        'excel': 'str',
        'image_size': 'FinancialStatementResultImageSize'
    }

    attribute_map = {
        'words_region_count': 'words_region_count',
        'words_region_list': 'words_region_list',
        'excel': 'excel',
        'image_size': 'image_size'
    }

    def __init__(self, words_region_count=None, words_region_list=None, excel=None, image_size=None):
        """FinancialStatementResult

        The model defined in huaweicloud sdk

        :param words_region_count: 识别出来的表格、文本区域个数。 
        :type words_region_count: int
        :param words_region_list: 返回的表格、文本区域列表。输出顺序从左到右，从上到下。 
        :type words_region_list: list[:class:`huaweicloudsdkocr.v1.FinancialStatementWordsRegionList`]
        :param excel: 表格图像转换为excel的base64编码，图像中的文字和表格按位置写入excel，可编辑。对返回的excel编码，可用base64.b64decode解码并保存为xlsx文件。 
        :type excel: str
        :param image_size: 
        :type image_size: :class:`huaweicloudsdkocr.v1.FinancialStatementResultImageSize`
        """
        
        

        self._words_region_count = None
        self._words_region_list = None
        self._excel = None
        self._image_size = None
        self.discriminator = None

        self.words_region_count = words_region_count
        self.words_region_list = words_region_list
        if excel is not None:
            self.excel = excel
        if image_size is not None:
            self.image_size = image_size

    @property
    def words_region_count(self):
        """Gets the words_region_count of this FinancialStatementResult.

        识别出来的表格、文本区域个数。 

        :return: The words_region_count of this FinancialStatementResult.
        :rtype: int
        """
        return self._words_region_count

    @words_region_count.setter
    def words_region_count(self, words_region_count):
        """Sets the words_region_count of this FinancialStatementResult.

        识别出来的表格、文本区域个数。 

        :param words_region_count: The words_region_count of this FinancialStatementResult.
        :type words_region_count: int
        """
        self._words_region_count = words_region_count

    @property
    def words_region_list(self):
        """Gets the words_region_list of this FinancialStatementResult.

        返回的表格、文本区域列表。输出顺序从左到右，从上到下。 

        :return: The words_region_list of this FinancialStatementResult.
        :rtype: list[:class:`huaweicloudsdkocr.v1.FinancialStatementWordsRegionList`]
        """
        return self._words_region_list

    @words_region_list.setter
    def words_region_list(self, words_region_list):
        """Sets the words_region_list of this FinancialStatementResult.

        返回的表格、文本区域列表。输出顺序从左到右，从上到下。 

        :param words_region_list: The words_region_list of this FinancialStatementResult.
        :type words_region_list: list[:class:`huaweicloudsdkocr.v1.FinancialStatementWordsRegionList`]
        """
        self._words_region_list = words_region_list

    @property
    def excel(self):
        """Gets the excel of this FinancialStatementResult.

        表格图像转换为excel的base64编码，图像中的文字和表格按位置写入excel，可编辑。对返回的excel编码，可用base64.b64decode解码并保存为xlsx文件。 

        :return: The excel of this FinancialStatementResult.
        :rtype: str
        """
        return self._excel

    @excel.setter
    def excel(self, excel):
        """Sets the excel of this FinancialStatementResult.

        表格图像转换为excel的base64编码，图像中的文字和表格按位置写入excel，可编辑。对返回的excel编码，可用base64.b64decode解码并保存为xlsx文件。 

        :param excel: The excel of this FinancialStatementResult.
        :type excel: str
        """
        self._excel = excel

    @property
    def image_size(self):
        """Gets the image_size of this FinancialStatementResult.


        :return: The image_size of this FinancialStatementResult.
        :rtype: :class:`huaweicloudsdkocr.v1.FinancialStatementResultImageSize`
        """
        return self._image_size

    @image_size.setter
    def image_size(self, image_size):
        """Sets the image_size of this FinancialStatementResult.


        :param image_size: The image_size of this FinancialStatementResult.
        :type image_size: :class:`huaweicloudsdkocr.v1.FinancialStatementResultImageSize`
        """
        self._image_size = image_size

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
        if not isinstance(other, FinancialStatementResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
