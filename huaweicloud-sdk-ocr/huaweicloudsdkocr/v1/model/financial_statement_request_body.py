# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FinancialStatementRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image': 'str',
        'url': 'str',
        'return_text_location': 'bool',
        'return_confidence': 'bool',
        'return_excel': 'bool',
        'return_table_location': 'bool',
        'return_image_size': 'bool',
        'return_rectification_matrix': 'bool'
    }

    attribute_map = {
        'image': 'image',
        'url': 'url',
        'return_text_location': 'return_text_location',
        'return_confidence': 'return_confidence',
        'return_excel': 'return_excel',
        'return_table_location': 'return_table_location',
        'return_image_size': 'return_image_size',
        'return_rectification_matrix': 'return_rectification_matrix'
    }

    def __init__(self, image=None, url=None, return_text_location=None, return_confidence=None, return_excel=None, return_table_location=None, return_image_size=None, return_rectification_matrix=None):
        """FinancialStatementRequestBody

        The model defined in huaweicloud sdk

        :param image: 与url二选一  图像数据，base64编码，要求base64编码后大小不超过10MB。图片最小边不小于15px，最长边不超过8192px，支持JPEG、JPG、PNG、BMP、TIFF格式。  图片文件Base64编码字符串，点击[这里](https://support.huaweicloud.com/ocr_faq/ocr_01_0032.html)查看详细获取方式。   
        :type image: str
        :param url: 与image二选一 图片的URL路径，目前支持： - 公网http/https url - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，详情参见[配置OBS访问权限](https://support.huaweicloud.com/api-ocr/ocr_03_0132.html)。 &gt; 说明： - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 - url中不能存在中文字符，若存在，中文需要进行utf8编码。 
        :type url: str
        :param return_text_location: 返回文本块坐标及单元格坐标信息，可选值包括： - true：返回文本块和单元格坐标; - false：不返回。  &gt; 说明： - 未传入该参数时默认为false，即不返回。 
        :type return_text_location: bool
        :param return_confidence: 返回字段识别置信度，小数点后四位。可选值包括： - true：返回字段置信度; - false：不返回。  &gt; 说明： - 未传入该参数时默认为false，即不返回字段置信度。 
        :type return_confidence: bool
        :param return_excel: 是否返回表格转换Microsoft Excel的base64编码字段。可选值包括： - true：返回’excel’字段，表示xlsx格式的表格识别结果的base64编码; - false：不返回。  &gt; 说明： - 对返回的Excel编码，可用Python函数 base64.b64decode解码后保存为xlsx文件。 
        :type return_excel: bool
        :param return_table_location: 返回表格坐标，可选值包括： - true：返回表格坐标; - false：不返回。  &gt; 说明： - 未传入该参数时默认为false，即不返回。 
        :type return_table_location: bool
        :param return_image_size: 返回矫正后的图像大小，可选值包括： - true：返回矫正图像大小; - false：不返回。  &gt; 说明： - 未传入该参数时默认为false，即不返回。 
        :type return_image_size: bool
        :param return_rectification_matrix: 透视变换矩阵，可选值包括： - true：返回透视变换矩阵; - false：不返回。  &gt; 说明： - 未传入该参数时默认为false，即不返回透视变换矩阵。 
        :type return_rectification_matrix: bool
        """
        
        

        self._image = None
        self._url = None
        self._return_text_location = None
        self._return_confidence = None
        self._return_excel = None
        self._return_table_location = None
        self._return_image_size = None
        self._return_rectification_matrix = None
        self.discriminator = None

        if image is not None:
            self.image = image
        if url is not None:
            self.url = url
        if return_text_location is not None:
            self.return_text_location = return_text_location
        if return_confidence is not None:
            self.return_confidence = return_confidence
        if return_excel is not None:
            self.return_excel = return_excel
        if return_table_location is not None:
            self.return_table_location = return_table_location
        if return_image_size is not None:
            self.return_image_size = return_image_size
        if return_rectification_matrix is not None:
            self.return_rectification_matrix = return_rectification_matrix

    @property
    def image(self):
        """Gets the image of this FinancialStatementRequestBody.

        与url二选一  图像数据，base64编码，要求base64编码后大小不超过10MB。图片最小边不小于15px，最长边不超过8192px，支持JPEG、JPG、PNG、BMP、TIFF格式。  图片文件Base64编码字符串，点击[这里](https://support.huaweicloud.com/ocr_faq/ocr_01_0032.html)查看详细获取方式。   

        :return: The image of this FinancialStatementRequestBody.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this FinancialStatementRequestBody.

        与url二选一  图像数据，base64编码，要求base64编码后大小不超过10MB。图片最小边不小于15px，最长边不超过8192px，支持JPEG、JPG、PNG、BMP、TIFF格式。  图片文件Base64编码字符串，点击[这里](https://support.huaweicloud.com/ocr_faq/ocr_01_0032.html)查看详细获取方式。   

        :param image: The image of this FinancialStatementRequestBody.
        :type image: str
        """
        self._image = image

    @property
    def url(self):
        """Gets the url of this FinancialStatementRequestBody.

        与image二选一 图片的URL路径，目前支持： - 公网http/https url - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，详情参见[配置OBS访问权限](https://support.huaweicloud.com/api-ocr/ocr_03_0132.html)。 > 说明： - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 - url中不能存在中文字符，若存在，中文需要进行utf8编码。 

        :return: The url of this FinancialStatementRequestBody.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this FinancialStatementRequestBody.

        与image二选一 图片的URL路径，目前支持： - 公网http/https url - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，详情参见[配置OBS访问权限](https://support.huaweicloud.com/api-ocr/ocr_03_0132.html)。 > 说明： - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 - url中不能存在中文字符，若存在，中文需要进行utf8编码。 

        :param url: The url of this FinancialStatementRequestBody.
        :type url: str
        """
        self._url = url

    @property
    def return_text_location(self):
        """Gets the return_text_location of this FinancialStatementRequestBody.

        返回文本块坐标及单元格坐标信息，可选值包括： - true：返回文本块和单元格坐标; - false：不返回。  > 说明： - 未传入该参数时默认为false，即不返回。 

        :return: The return_text_location of this FinancialStatementRequestBody.
        :rtype: bool
        """
        return self._return_text_location

    @return_text_location.setter
    def return_text_location(self, return_text_location):
        """Sets the return_text_location of this FinancialStatementRequestBody.

        返回文本块坐标及单元格坐标信息，可选值包括： - true：返回文本块和单元格坐标; - false：不返回。  > 说明： - 未传入该参数时默认为false，即不返回。 

        :param return_text_location: The return_text_location of this FinancialStatementRequestBody.
        :type return_text_location: bool
        """
        self._return_text_location = return_text_location

    @property
    def return_confidence(self):
        """Gets the return_confidence of this FinancialStatementRequestBody.

        返回字段识别置信度，小数点后四位。可选值包括： - true：返回字段置信度; - false：不返回。  > 说明： - 未传入该参数时默认为false，即不返回字段置信度。 

        :return: The return_confidence of this FinancialStatementRequestBody.
        :rtype: bool
        """
        return self._return_confidence

    @return_confidence.setter
    def return_confidence(self, return_confidence):
        """Sets the return_confidence of this FinancialStatementRequestBody.

        返回字段识别置信度，小数点后四位。可选值包括： - true：返回字段置信度; - false：不返回。  > 说明： - 未传入该参数时默认为false，即不返回字段置信度。 

        :param return_confidence: The return_confidence of this FinancialStatementRequestBody.
        :type return_confidence: bool
        """
        self._return_confidence = return_confidence

    @property
    def return_excel(self):
        """Gets the return_excel of this FinancialStatementRequestBody.

        是否返回表格转换Microsoft Excel的base64编码字段。可选值包括： - true：返回’excel’字段，表示xlsx格式的表格识别结果的base64编码; - false：不返回。  > 说明： - 对返回的Excel编码，可用Python函数 base64.b64decode解码后保存为xlsx文件。 

        :return: The return_excel of this FinancialStatementRequestBody.
        :rtype: bool
        """
        return self._return_excel

    @return_excel.setter
    def return_excel(self, return_excel):
        """Sets the return_excel of this FinancialStatementRequestBody.

        是否返回表格转换Microsoft Excel的base64编码字段。可选值包括： - true：返回’excel’字段，表示xlsx格式的表格识别结果的base64编码; - false：不返回。  > 说明： - 对返回的Excel编码，可用Python函数 base64.b64decode解码后保存为xlsx文件。 

        :param return_excel: The return_excel of this FinancialStatementRequestBody.
        :type return_excel: bool
        """
        self._return_excel = return_excel

    @property
    def return_table_location(self):
        """Gets the return_table_location of this FinancialStatementRequestBody.

        返回表格坐标，可选值包括： - true：返回表格坐标; - false：不返回。  > 说明： - 未传入该参数时默认为false，即不返回。 

        :return: The return_table_location of this FinancialStatementRequestBody.
        :rtype: bool
        """
        return self._return_table_location

    @return_table_location.setter
    def return_table_location(self, return_table_location):
        """Sets the return_table_location of this FinancialStatementRequestBody.

        返回表格坐标，可选值包括： - true：返回表格坐标; - false：不返回。  > 说明： - 未传入该参数时默认为false，即不返回。 

        :param return_table_location: The return_table_location of this FinancialStatementRequestBody.
        :type return_table_location: bool
        """
        self._return_table_location = return_table_location

    @property
    def return_image_size(self):
        """Gets the return_image_size of this FinancialStatementRequestBody.

        返回矫正后的图像大小，可选值包括： - true：返回矫正图像大小; - false：不返回。  > 说明： - 未传入该参数时默认为false，即不返回。 

        :return: The return_image_size of this FinancialStatementRequestBody.
        :rtype: bool
        """
        return self._return_image_size

    @return_image_size.setter
    def return_image_size(self, return_image_size):
        """Sets the return_image_size of this FinancialStatementRequestBody.

        返回矫正后的图像大小，可选值包括： - true：返回矫正图像大小; - false：不返回。  > 说明： - 未传入该参数时默认为false，即不返回。 

        :param return_image_size: The return_image_size of this FinancialStatementRequestBody.
        :type return_image_size: bool
        """
        self._return_image_size = return_image_size

    @property
    def return_rectification_matrix(self):
        """Gets the return_rectification_matrix of this FinancialStatementRequestBody.

        透视变换矩阵，可选值包括： - true：返回透视变换矩阵; - false：不返回。  > 说明： - 未传入该参数时默认为false，即不返回透视变换矩阵。 

        :return: The return_rectification_matrix of this FinancialStatementRequestBody.
        :rtype: bool
        """
        return self._return_rectification_matrix

    @return_rectification_matrix.setter
    def return_rectification_matrix(self, return_rectification_matrix):
        """Sets the return_rectification_matrix of this FinancialStatementRequestBody.

        透视变换矩阵，可选值包括： - true：返回透视变换矩阵; - false：不返回。  > 说明： - 未传入该参数时默认为false，即不返回透视变换矩阵。 

        :param return_rectification_matrix: The return_rectification_matrix of this FinancialStatementRequestBody.
        :type return_rectification_matrix: bool
        """
        self._return_rectification_matrix = return_rectification_matrix

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
        if not isinstance(other, FinancialStatementRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
