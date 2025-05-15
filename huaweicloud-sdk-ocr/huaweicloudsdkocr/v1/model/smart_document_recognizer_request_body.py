# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SmartDocumentRecognizerRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data': 'str',
        'url': 'str',
        'single_orientation_mode': 'bool',
        'language': 'str',
        'kv': 'bool',
        'table': 'bool',
        'layout': 'bool',
        'return_excel': 'bool',
        'form': 'bool',
        'formula': 'bool',
        'kv_map': 'str',
        'erase_seal': 'bool',
        'pdf_page_number': 'int'
    }

    attribute_map = {
        'data': 'data',
        'url': 'url',
        'single_orientation_mode': 'single_orientation_mode',
        'language': 'language',
        'kv': 'kv',
        'table': 'table',
        'layout': 'layout',
        'return_excel': 'return_excel',
        'form': 'form',
        'formula': 'formula',
        'kv_map': 'kv_map',
        'erase_seal': 'erase_seal',
        'pdf_page_number': 'pdf_page_number'
    }

    def __init__(self, data=None, url=None, single_orientation_mode=None, language=None, kv=None, table=None, layout=None, return_excel=None, form=None, formula=None, kv_map=None, erase_seal=None, pdf_page_number=None):
        r"""SmartDocumentRecognizerRequestBody

        The model defined in huaweicloud sdk

        :param data: 与url二选一。 图片的Base64编码，要求单个图片、PDF文件其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议文件大小不超过7MB。  图像尺寸不小于15×15像素，最长边不超过30000像素，支持JPG/PNG/BMP/TIFF格式。 PDF以144dpi的分辨率转为图像进行文档解析，需符合上述图像尺寸规定。若PDF有多页，当前仅对第1页进行识别。 
        :type data: str
        :param url: 与data二选一。  单个图片、PDF文件其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议文件大小不超过7MB。 图像尺寸不小于15×15像素，最长边不超过30000像素，支持JPG/PNG/BMP/TIFF格式。 PDF以144dpi的分辨率转为图像进行文档解析，需符合上述图像尺寸规定。若PDF有多页，当前仅对第1页进行识别。 图片或PDF的URL路径，目前支持： - 公网http/https url - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，详情参见[配置OBS访问权限](https://support.huaweicloud.com/api-ocr/ocr_03_0132.html)。 &gt; 说明： - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 - url中不能存在中文字符，若存在，中文需要进行utf8编码。 
        :type url: str
        :param single_orientation_mode: 单朝向模式开关。可选值包括： - true：打开单朝向模式。 - false：关闭单朝向模式。  图片文字方向一致时，打开该开关可提升识别精度；图片文字方向不一致时，关闭该开关可支持多朝向文字识别。未传入该参数时默认为\&quot;true\&quot;，既默认图片中的文字方向为单朝向。 
        :type single_orientation_mode: bool
        :param language: 语种选择，未传入该参数时默认为中英文识别模式。参考[华为云通用文字支持语种](https://support.huaweicloud.com/api-ocr/ocr_03_0042.html)。 
        :type language: str
        :param kv: 是否进行键值对（key-value）提取。若是，结果会以“kv_result”这一关键字返回。 
        :type kv: bool
        :param table: 是否进行表格识别。此处表格特指逻辑表格，通常具有M行N列的形式，且第一行或第一列为表头。若是，结果会以“table_result”这一关键字返回。 
        :type table: bool
        :param layout: 是否进行版面分析。若是，结果会以“layout_result”这一关键字返回。 
        :type layout: bool
        :param return_excel: 仅当table为True时有效。是否返回表格转换Microsoft Excel的Base64编码字段。 
        :type return_excel: bool
        :param form: 是否进行有线表单识别。有线表单指关键信息以有线单元格形式进行呈现，例如户口本、机动车发票等。若是，结果会以\&quot;form_result\&quot;这一关键字返回。 
        :type form: bool
        :param formula: 是否进行公式识别，识别结果为latex序列。若是，结果会以“formula_result”这一关键字返回。  - 开启公式识别后会降低响应速度。 - 当前仅支持3行以内公式识别，不支持3行以上的多行公式。 
        :type formula: bool
        :param kv_map: 需要传入字典的json序列化后字符串，用于对kv_result中的特定key值进行归一化映射。例如，kv_result中包含{\&quot;名称\&quot;：\&quot;小明\&quot;}的键值对，若传入{\&quot;名称\&quot;：\&quot;姓名\&quot;}的kv_map，则返回结果为{“姓名”：“小明”}。  &gt; 参数传入示例： - \&quot;kv_map\&quot;:\&quot;{\\\&quot;名称\\\&quot;:\\\&quot;姓名\\\&quot;}\&quot; 
        :type kv_map: str
        :param erase_seal: 是否打开印章擦除功能。可选值包括： - true：打开印章擦除功能。 - false：关闭印章擦除功能。  开启后，可提升印章遮挡区域的文字识别精度。 
        :type erase_seal: bool
        :param pdf_page_number: 指定PDF页码识别。传入该参数时，则识别指定页码的内容。如果不传该参数，则默认识别第1页。 
        :type pdf_page_number: int
        """
        
        

        self._data = None
        self._url = None
        self._single_orientation_mode = None
        self._language = None
        self._kv = None
        self._table = None
        self._layout = None
        self._return_excel = None
        self._form = None
        self._formula = None
        self._kv_map = None
        self._erase_seal = None
        self._pdf_page_number = None
        self.discriminator = None

        if data is not None:
            self.data = data
        if url is not None:
            self.url = url
        if single_orientation_mode is not None:
            self.single_orientation_mode = single_orientation_mode
        if language is not None:
            self.language = language
        if kv is not None:
            self.kv = kv
        if table is not None:
            self.table = table
        if layout is not None:
            self.layout = layout
        if return_excel is not None:
            self.return_excel = return_excel
        if form is not None:
            self.form = form
        if formula is not None:
            self.formula = formula
        if kv_map is not None:
            self.kv_map = kv_map
        if erase_seal is not None:
            self.erase_seal = erase_seal
        if pdf_page_number is not None:
            self.pdf_page_number = pdf_page_number

    @property
    def data(self):
        r"""Gets the data of this SmartDocumentRecognizerRequestBody.

        与url二选一。 图片的Base64编码，要求单个图片、PDF文件其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议文件大小不超过7MB。  图像尺寸不小于15×15像素，最长边不超过30000像素，支持JPG/PNG/BMP/TIFF格式。 PDF以144dpi的分辨率转为图像进行文档解析，需符合上述图像尺寸规定。若PDF有多页，当前仅对第1页进行识别。 

        :return: The data of this SmartDocumentRecognizerRequestBody.
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this SmartDocumentRecognizerRequestBody.

        与url二选一。 图片的Base64编码，要求单个图片、PDF文件其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议文件大小不超过7MB。  图像尺寸不小于15×15像素，最长边不超过30000像素，支持JPG/PNG/BMP/TIFF格式。 PDF以144dpi的分辨率转为图像进行文档解析，需符合上述图像尺寸规定。若PDF有多页，当前仅对第1页进行识别。 

        :param data: The data of this SmartDocumentRecognizerRequestBody.
        :type data: str
        """
        self._data = data

    @property
    def url(self):
        r"""Gets the url of this SmartDocumentRecognizerRequestBody.

        与data二选一。  单个图片、PDF文件其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议文件大小不超过7MB。 图像尺寸不小于15×15像素，最长边不超过30000像素，支持JPG/PNG/BMP/TIFF格式。 PDF以144dpi的分辨率转为图像进行文档解析，需符合上述图像尺寸规定。若PDF有多页，当前仅对第1页进行识别。 图片或PDF的URL路径，目前支持： - 公网http/https url - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，详情参见[配置OBS访问权限](https://support.huaweicloud.com/api-ocr/ocr_03_0132.html)。 > 说明： - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 - url中不能存在中文字符，若存在，中文需要进行utf8编码。 

        :return: The url of this SmartDocumentRecognizerRequestBody.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this SmartDocumentRecognizerRequestBody.

        与data二选一。  单个图片、PDF文件其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议文件大小不超过7MB。 图像尺寸不小于15×15像素，最长边不超过30000像素，支持JPG/PNG/BMP/TIFF格式。 PDF以144dpi的分辨率转为图像进行文档解析，需符合上述图像尺寸规定。若PDF有多页，当前仅对第1页进行识别。 图片或PDF的URL路径，目前支持： - 公网http/https url - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，详情参见[配置OBS访问权限](https://support.huaweicloud.com/api-ocr/ocr_03_0132.html)。 > 说明： - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 - url中不能存在中文字符，若存在，中文需要进行utf8编码。 

        :param url: The url of this SmartDocumentRecognizerRequestBody.
        :type url: str
        """
        self._url = url

    @property
    def single_orientation_mode(self):
        r"""Gets the single_orientation_mode of this SmartDocumentRecognizerRequestBody.

        单朝向模式开关。可选值包括： - true：打开单朝向模式。 - false：关闭单朝向模式。  图片文字方向一致时，打开该开关可提升识别精度；图片文字方向不一致时，关闭该开关可支持多朝向文字识别。未传入该参数时默认为\"true\"，既默认图片中的文字方向为单朝向。 

        :return: The single_orientation_mode of this SmartDocumentRecognizerRequestBody.
        :rtype: bool
        """
        return self._single_orientation_mode

    @single_orientation_mode.setter
    def single_orientation_mode(self, single_orientation_mode):
        r"""Sets the single_orientation_mode of this SmartDocumentRecognizerRequestBody.

        单朝向模式开关。可选值包括： - true：打开单朝向模式。 - false：关闭单朝向模式。  图片文字方向一致时，打开该开关可提升识别精度；图片文字方向不一致时，关闭该开关可支持多朝向文字识别。未传入该参数时默认为\"true\"，既默认图片中的文字方向为单朝向。 

        :param single_orientation_mode: The single_orientation_mode of this SmartDocumentRecognizerRequestBody.
        :type single_orientation_mode: bool
        """
        self._single_orientation_mode = single_orientation_mode

    @property
    def language(self):
        r"""Gets the language of this SmartDocumentRecognizerRequestBody.

        语种选择，未传入该参数时默认为中英文识别模式。参考[华为云通用文字支持语种](https://support.huaweicloud.com/api-ocr/ocr_03_0042.html)。 

        :return: The language of this SmartDocumentRecognizerRequestBody.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this SmartDocumentRecognizerRequestBody.

        语种选择，未传入该参数时默认为中英文识别模式。参考[华为云通用文字支持语种](https://support.huaweicloud.com/api-ocr/ocr_03_0042.html)。 

        :param language: The language of this SmartDocumentRecognizerRequestBody.
        :type language: str
        """
        self._language = language

    @property
    def kv(self):
        r"""Gets the kv of this SmartDocumentRecognizerRequestBody.

        是否进行键值对（key-value）提取。若是，结果会以“kv_result”这一关键字返回。 

        :return: The kv of this SmartDocumentRecognizerRequestBody.
        :rtype: bool
        """
        return self._kv

    @kv.setter
    def kv(self, kv):
        r"""Sets the kv of this SmartDocumentRecognizerRequestBody.

        是否进行键值对（key-value）提取。若是，结果会以“kv_result”这一关键字返回。 

        :param kv: The kv of this SmartDocumentRecognizerRequestBody.
        :type kv: bool
        """
        self._kv = kv

    @property
    def table(self):
        r"""Gets the table of this SmartDocumentRecognizerRequestBody.

        是否进行表格识别。此处表格特指逻辑表格，通常具有M行N列的形式，且第一行或第一列为表头。若是，结果会以“table_result”这一关键字返回。 

        :return: The table of this SmartDocumentRecognizerRequestBody.
        :rtype: bool
        """
        return self._table

    @table.setter
    def table(self, table):
        r"""Sets the table of this SmartDocumentRecognizerRequestBody.

        是否进行表格识别。此处表格特指逻辑表格，通常具有M行N列的形式，且第一行或第一列为表头。若是，结果会以“table_result”这一关键字返回。 

        :param table: The table of this SmartDocumentRecognizerRequestBody.
        :type table: bool
        """
        self._table = table

    @property
    def layout(self):
        r"""Gets the layout of this SmartDocumentRecognizerRequestBody.

        是否进行版面分析。若是，结果会以“layout_result”这一关键字返回。 

        :return: The layout of this SmartDocumentRecognizerRequestBody.
        :rtype: bool
        """
        return self._layout

    @layout.setter
    def layout(self, layout):
        r"""Sets the layout of this SmartDocumentRecognizerRequestBody.

        是否进行版面分析。若是，结果会以“layout_result”这一关键字返回。 

        :param layout: The layout of this SmartDocumentRecognizerRequestBody.
        :type layout: bool
        """
        self._layout = layout

    @property
    def return_excel(self):
        r"""Gets the return_excel of this SmartDocumentRecognizerRequestBody.

        仅当table为True时有效。是否返回表格转换Microsoft Excel的Base64编码字段。 

        :return: The return_excel of this SmartDocumentRecognizerRequestBody.
        :rtype: bool
        """
        return self._return_excel

    @return_excel.setter
    def return_excel(self, return_excel):
        r"""Sets the return_excel of this SmartDocumentRecognizerRequestBody.

        仅当table为True时有效。是否返回表格转换Microsoft Excel的Base64编码字段。 

        :param return_excel: The return_excel of this SmartDocumentRecognizerRequestBody.
        :type return_excel: bool
        """
        self._return_excel = return_excel

    @property
    def form(self):
        r"""Gets the form of this SmartDocumentRecognizerRequestBody.

        是否进行有线表单识别。有线表单指关键信息以有线单元格形式进行呈现，例如户口本、机动车发票等。若是，结果会以\"form_result\"这一关键字返回。 

        :return: The form of this SmartDocumentRecognizerRequestBody.
        :rtype: bool
        """
        return self._form

    @form.setter
    def form(self, form):
        r"""Sets the form of this SmartDocumentRecognizerRequestBody.

        是否进行有线表单识别。有线表单指关键信息以有线单元格形式进行呈现，例如户口本、机动车发票等。若是，结果会以\"form_result\"这一关键字返回。 

        :param form: The form of this SmartDocumentRecognizerRequestBody.
        :type form: bool
        """
        self._form = form

    @property
    def formula(self):
        r"""Gets the formula of this SmartDocumentRecognizerRequestBody.

        是否进行公式识别，识别结果为latex序列。若是，结果会以“formula_result”这一关键字返回。  - 开启公式识别后会降低响应速度。 - 当前仅支持3行以内公式识别，不支持3行以上的多行公式。 

        :return: The formula of this SmartDocumentRecognizerRequestBody.
        :rtype: bool
        """
        return self._formula

    @formula.setter
    def formula(self, formula):
        r"""Sets the formula of this SmartDocumentRecognizerRequestBody.

        是否进行公式识别，识别结果为latex序列。若是，结果会以“formula_result”这一关键字返回。  - 开启公式识别后会降低响应速度。 - 当前仅支持3行以内公式识别，不支持3行以上的多行公式。 

        :param formula: The formula of this SmartDocumentRecognizerRequestBody.
        :type formula: bool
        """
        self._formula = formula

    @property
    def kv_map(self):
        r"""Gets the kv_map of this SmartDocumentRecognizerRequestBody.

        需要传入字典的json序列化后字符串，用于对kv_result中的特定key值进行归一化映射。例如，kv_result中包含{\"名称\"：\"小明\"}的键值对，若传入{\"名称\"：\"姓名\"}的kv_map，则返回结果为{“姓名”：“小明”}。  > 参数传入示例： - \"kv_map\":\"{\\\"名称\\\":\\\"姓名\\\"}\" 

        :return: The kv_map of this SmartDocumentRecognizerRequestBody.
        :rtype: str
        """
        return self._kv_map

    @kv_map.setter
    def kv_map(self, kv_map):
        r"""Sets the kv_map of this SmartDocumentRecognizerRequestBody.

        需要传入字典的json序列化后字符串，用于对kv_result中的特定key值进行归一化映射。例如，kv_result中包含{\"名称\"：\"小明\"}的键值对，若传入{\"名称\"：\"姓名\"}的kv_map，则返回结果为{“姓名”：“小明”}。  > 参数传入示例： - \"kv_map\":\"{\\\"名称\\\":\\\"姓名\\\"}\" 

        :param kv_map: The kv_map of this SmartDocumentRecognizerRequestBody.
        :type kv_map: str
        """
        self._kv_map = kv_map

    @property
    def erase_seal(self):
        r"""Gets the erase_seal of this SmartDocumentRecognizerRequestBody.

        是否打开印章擦除功能。可选值包括： - true：打开印章擦除功能。 - false：关闭印章擦除功能。  开启后，可提升印章遮挡区域的文字识别精度。 

        :return: The erase_seal of this SmartDocumentRecognizerRequestBody.
        :rtype: bool
        """
        return self._erase_seal

    @erase_seal.setter
    def erase_seal(self, erase_seal):
        r"""Sets the erase_seal of this SmartDocumentRecognizerRequestBody.

        是否打开印章擦除功能。可选值包括： - true：打开印章擦除功能。 - false：关闭印章擦除功能。  开启后，可提升印章遮挡区域的文字识别精度。 

        :param erase_seal: The erase_seal of this SmartDocumentRecognizerRequestBody.
        :type erase_seal: bool
        """
        self._erase_seal = erase_seal

    @property
    def pdf_page_number(self):
        r"""Gets the pdf_page_number of this SmartDocumentRecognizerRequestBody.

        指定PDF页码识别。传入该参数时，则识别指定页码的内容。如果不传该参数，则默认识别第1页。 

        :return: The pdf_page_number of this SmartDocumentRecognizerRequestBody.
        :rtype: int
        """
        return self._pdf_page_number

    @pdf_page_number.setter
    def pdf_page_number(self, pdf_page_number):
        r"""Sets the pdf_page_number of this SmartDocumentRecognizerRequestBody.

        指定PDF页码识别。传入该参数时，则识别指定页码的内容。如果不传该参数，则默认识别第1页。 

        :param pdf_page_number: The pdf_page_number of this SmartDocumentRecognizerRequestBody.
        :type pdf_page_number: int
        """
        self._pdf_page_number = pdf_page_number

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
        if not isinstance(other, SmartDocumentRecognizerRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
