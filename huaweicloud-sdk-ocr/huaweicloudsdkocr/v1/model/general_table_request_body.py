# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GeneralTableRequestBody:

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
        'return_char_location': 'bool',
        'return_confidence': 'bool',
        'return_excel': 'bool',
        'return_rectification_matrix': 'bool',
        'with_borders': 'bool'
    }

    attribute_map = {
        'image': 'image',
        'url': 'url',
        'return_text_location': 'return_text_location',
        'return_char_location': 'return_char_location',
        'return_confidence': 'return_confidence',
        'return_excel': 'return_excel',
        'return_rectification_matrix': 'return_rectification_matrix',
        'with_borders': 'with_borders'
    }

    def __init__(self, image=None, url=None, return_text_location=None, return_char_location=None, return_confidence=None, return_excel=None, return_rectification_matrix=None, with_borders=None):
        """GeneralTableRequestBody

        The model defined in huaweicloud sdk

        :param image: 与url二选一  图片最小边不小于15px，最长边不超过8192px，支持JPEG、JPG、PNG、BMP、TIFF格式。  图片文件Base64编码字符串，点击[这里](https://support.huaweicloud.com/ocr_faq/ocr_01_0032.html)查看详细获取方式。   
        :type image: str
        :param url: 与image二选一 图片的URL路径，目前支持： - 公网http/https url - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，详情参见[配置OBS访问权限](https://support.huaweicloud.com/api-ocr/ocr_03_0132.html)。 &gt; 说明： - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 - url中不能存在中文字符，若存在，中文需要进行utf8编码。 
        :type url: str
        :param return_text_location: 返回文本块坐标及单元格坐标信息，可选值如下所示： - true：返回文本块和单元格坐标 - false：不返回  &gt; 说明： - 如果未传入该参数时默认为false，即不返回。 
        :type return_text_location: bool
        :param return_char_location: 返回单字符的坐标信息，可选值包括： - true：返回单字符的坐标 - false：不返回  未传入该参数时默认为false，即不返回。如果此参数为true时，return_text_loaction必须为true 
        :type return_char_location: bool
        :param return_confidence: 是否返回置信度的开关，可选值包括： - true：返回置信度 - false：不返回置信度  &gt; 说明： - 如果未传入该参数，系统默认为“false”，即不返回置信度。 
        :type return_confidence: bool
        :param return_excel: 是否返回表格转换Microsoft Excel的base64编码字段。可选值包括： - true：返回&#39;excel&#39;字段，表示xlsx格式的表格识别结果的base64编码 - false：不返回。默认为false  &gt; 说明： - 对返回的Excel编码，可用Python函数 base64.b64decode解码后保存为.xlsx文件。 
        :type return_excel: bool
        :param return_rectification_matrix: 可选值包括： - true：返回透视变换矩阵 - false：不返回  未传入该参数时默认为false，即不返回透视变换矩阵。 
        :type return_rectification_matrix: bool
        :param with_borders: 可选值包括： - true：输入图像仅包含有线表格，仅进行有线表格识别。 - false: 输入图像可能包含无线表格，同时进行有线表格与无线表格识别。  未传入该参数时默认为false，即同时进行有线表格与无线表格识别。当确认输入仅包含有线表格时，该参数设为true可达到更优识别效果。 
        :type with_borders: bool
        """
        
        

        self._image = None
        self._url = None
        self._return_text_location = None
        self._return_char_location = None
        self._return_confidence = None
        self._return_excel = None
        self._return_rectification_matrix = None
        self._with_borders = None
        self.discriminator = None

        if image is not None:
            self.image = image
        if url is not None:
            self.url = url
        if return_text_location is not None:
            self.return_text_location = return_text_location
        if return_char_location is not None:
            self.return_char_location = return_char_location
        if return_confidence is not None:
            self.return_confidence = return_confidence
        if return_excel is not None:
            self.return_excel = return_excel
        if return_rectification_matrix is not None:
            self.return_rectification_matrix = return_rectification_matrix
        if with_borders is not None:
            self.with_borders = with_borders

    @property
    def image(self):
        """Gets the image of this GeneralTableRequestBody.

        与url二选一  图片最小边不小于15px，最长边不超过8192px，支持JPEG、JPG、PNG、BMP、TIFF格式。  图片文件Base64编码字符串，点击[这里](https://support.huaweicloud.com/ocr_faq/ocr_01_0032.html)查看详细获取方式。   

        :return: The image of this GeneralTableRequestBody.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this GeneralTableRequestBody.

        与url二选一  图片最小边不小于15px，最长边不超过8192px，支持JPEG、JPG、PNG、BMP、TIFF格式。  图片文件Base64编码字符串，点击[这里](https://support.huaweicloud.com/ocr_faq/ocr_01_0032.html)查看详细获取方式。   

        :param image: The image of this GeneralTableRequestBody.
        :type image: str
        """
        self._image = image

    @property
    def url(self):
        """Gets the url of this GeneralTableRequestBody.

        与image二选一 图片的URL路径，目前支持： - 公网http/https url - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，详情参见[配置OBS访问权限](https://support.huaweicloud.com/api-ocr/ocr_03_0132.html)。 > 说明： - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 - url中不能存在中文字符，若存在，中文需要进行utf8编码。 

        :return: The url of this GeneralTableRequestBody.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this GeneralTableRequestBody.

        与image二选一 图片的URL路径，目前支持： - 公网http/https url - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，详情参见[配置OBS访问权限](https://support.huaweicloud.com/api-ocr/ocr_03_0132.html)。 > 说明： - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 - url中不能存在中文字符，若存在，中文需要进行utf8编码。 

        :param url: The url of this GeneralTableRequestBody.
        :type url: str
        """
        self._url = url

    @property
    def return_text_location(self):
        """Gets the return_text_location of this GeneralTableRequestBody.

        返回文本块坐标及单元格坐标信息，可选值如下所示： - true：返回文本块和单元格坐标 - false：不返回  > 说明： - 如果未传入该参数时默认为false，即不返回。 

        :return: The return_text_location of this GeneralTableRequestBody.
        :rtype: bool
        """
        return self._return_text_location

    @return_text_location.setter
    def return_text_location(self, return_text_location):
        """Sets the return_text_location of this GeneralTableRequestBody.

        返回文本块坐标及单元格坐标信息，可选值如下所示： - true：返回文本块和单元格坐标 - false：不返回  > 说明： - 如果未传入该参数时默认为false，即不返回。 

        :param return_text_location: The return_text_location of this GeneralTableRequestBody.
        :type return_text_location: bool
        """
        self._return_text_location = return_text_location

    @property
    def return_char_location(self):
        """Gets the return_char_location of this GeneralTableRequestBody.

        返回单字符的坐标信息，可选值包括： - true：返回单字符的坐标 - false：不返回  未传入该参数时默认为false，即不返回。如果此参数为true时，return_text_loaction必须为true 

        :return: The return_char_location of this GeneralTableRequestBody.
        :rtype: bool
        """
        return self._return_char_location

    @return_char_location.setter
    def return_char_location(self, return_char_location):
        """Sets the return_char_location of this GeneralTableRequestBody.

        返回单字符的坐标信息，可选值包括： - true：返回单字符的坐标 - false：不返回  未传入该参数时默认为false，即不返回。如果此参数为true时，return_text_loaction必须为true 

        :param return_char_location: The return_char_location of this GeneralTableRequestBody.
        :type return_char_location: bool
        """
        self._return_char_location = return_char_location

    @property
    def return_confidence(self):
        """Gets the return_confidence of this GeneralTableRequestBody.

        是否返回置信度的开关，可选值包括： - true：返回置信度 - false：不返回置信度  > 说明： - 如果未传入该参数，系统默认为“false”，即不返回置信度。 

        :return: The return_confidence of this GeneralTableRequestBody.
        :rtype: bool
        """
        return self._return_confidence

    @return_confidence.setter
    def return_confidence(self, return_confidence):
        """Sets the return_confidence of this GeneralTableRequestBody.

        是否返回置信度的开关，可选值包括： - true：返回置信度 - false：不返回置信度  > 说明： - 如果未传入该参数，系统默认为“false”，即不返回置信度。 

        :param return_confidence: The return_confidence of this GeneralTableRequestBody.
        :type return_confidence: bool
        """
        self._return_confidence = return_confidence

    @property
    def return_excel(self):
        """Gets the return_excel of this GeneralTableRequestBody.

        是否返回表格转换Microsoft Excel的base64编码字段。可选值包括： - true：返回'excel'字段，表示xlsx格式的表格识别结果的base64编码 - false：不返回。默认为false  > 说明： - 对返回的Excel编码，可用Python函数 base64.b64decode解码后保存为.xlsx文件。 

        :return: The return_excel of this GeneralTableRequestBody.
        :rtype: bool
        """
        return self._return_excel

    @return_excel.setter
    def return_excel(self, return_excel):
        """Sets the return_excel of this GeneralTableRequestBody.

        是否返回表格转换Microsoft Excel的base64编码字段。可选值包括： - true：返回'excel'字段，表示xlsx格式的表格识别结果的base64编码 - false：不返回。默认为false  > 说明： - 对返回的Excel编码，可用Python函数 base64.b64decode解码后保存为.xlsx文件。 

        :param return_excel: The return_excel of this GeneralTableRequestBody.
        :type return_excel: bool
        """
        self._return_excel = return_excel

    @property
    def return_rectification_matrix(self):
        """Gets the return_rectification_matrix of this GeneralTableRequestBody.

        可选值包括： - true：返回透视变换矩阵 - false：不返回  未传入该参数时默认为false，即不返回透视变换矩阵。 

        :return: The return_rectification_matrix of this GeneralTableRequestBody.
        :rtype: bool
        """
        return self._return_rectification_matrix

    @return_rectification_matrix.setter
    def return_rectification_matrix(self, return_rectification_matrix):
        """Sets the return_rectification_matrix of this GeneralTableRequestBody.

        可选值包括： - true：返回透视变换矩阵 - false：不返回  未传入该参数时默认为false，即不返回透视变换矩阵。 

        :param return_rectification_matrix: The return_rectification_matrix of this GeneralTableRequestBody.
        :type return_rectification_matrix: bool
        """
        self._return_rectification_matrix = return_rectification_matrix

    @property
    def with_borders(self):
        """Gets the with_borders of this GeneralTableRequestBody.

        可选值包括： - true：输入图像仅包含有线表格，仅进行有线表格识别。 - false: 输入图像可能包含无线表格，同时进行有线表格与无线表格识别。  未传入该参数时默认为false，即同时进行有线表格与无线表格识别。当确认输入仅包含有线表格时，该参数设为true可达到更优识别效果。 

        :return: The with_borders of this GeneralTableRequestBody.
        :rtype: bool
        """
        return self._with_borders

    @with_borders.setter
    def with_borders(self, with_borders):
        """Sets the with_borders of this GeneralTableRequestBody.

        可选值包括： - true：输入图像仅包含有线表格，仅进行有线表格识别。 - false: 输入图像可能包含无线表格，同时进行有线表格与无线表格识别。  未传入该参数时默认为false，即同时进行有线表格与无线表格识别。当确认输入仅包含有线表格时，该参数设为true可达到更优识别效果。 

        :param with_borders: The with_borders of this GeneralTableRequestBody.
        :type with_borders: bool
        """
        self._with_borders = with_borders

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
        if not isinstance(other, GeneralTableRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
