# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SmartDocumentRecognizerLayoutBlock:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'location': 'list[list[int]]',
        'type': 'str',
        'text': 'str',
        'words_ids': 'list[int]',
        'table_id': 'int',
        'form_id': 'int'
    }

    attribute_map = {
        'location': 'location',
        'type': 'type',
        'text': 'text',
        'words_ids': 'words_ids',
        'table_id': 'table_id',
        'form_id': 'form_id'
    }

    def __init__(self, location=None, type=None, text=None, words_ids=None, table_id=None, form_id=None):
        r"""SmartDocumentRecognizerLayoutBlock

        The model defined in huaweicloud sdk

        :param location: 文字块的区域位置信息，列表形式，包含文字区域四个顶点的二维坐标（x,y）;坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 
        :type location: list[list[int]]
        :param type: 文档区域类别，包含text、title、sub_title、image、image_caption、form、table、table_caption、header、footer、page_number、reference、formula、stamp、directory共15个类别。     
        :type type: str
        :param text: 文档区域文字内容。对于表格与图像，不返回其中的文字内容。 
        :type text: str
        :param words_ids: 文字识别结果索引列表，表示ocr_result的words_block_list中哪些文本框位于该文档区域内。 
        :type words_ids: list[int]
        :param table_id: 仅当type为\&quot;table\&quot;且入参table为True时返回该字段，表示当前逻辑表格区域对应table_result中哪一项识别结果。 
        :type table_id: int
        :param form_id: 仅当type为\&quot;form\&quot;且入参form为True时返回该字段，表示当前有线表单区域对应form_result中哪一项识别结果。 
        :type form_id: int
        """
        
        

        self._location = None
        self._type = None
        self._text = None
        self._words_ids = None
        self._table_id = None
        self._form_id = None
        self.discriminator = None

        if location is not None:
            self.location = location
        if type is not None:
            self.type = type
        if text is not None:
            self.text = text
        if words_ids is not None:
            self.words_ids = words_ids
        if table_id is not None:
            self.table_id = table_id
        if form_id is not None:
            self.form_id = form_id

    @property
    def location(self):
        r"""Gets the location of this SmartDocumentRecognizerLayoutBlock.

        文字块的区域位置信息，列表形式，包含文字区域四个顶点的二维坐标（x,y）;坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :return: The location of this SmartDocumentRecognizerLayoutBlock.
        :rtype: list[list[int]]
        """
        return self._location

    @location.setter
    def location(self, location):
        r"""Sets the location of this SmartDocumentRecognizerLayoutBlock.

        文字块的区域位置信息，列表形式，包含文字区域四个顶点的二维坐标（x,y）;坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :param location: The location of this SmartDocumentRecognizerLayoutBlock.
        :type location: list[list[int]]
        """
        self._location = location

    @property
    def type(self):
        r"""Gets the type of this SmartDocumentRecognizerLayoutBlock.

        文档区域类别，包含text、title、sub_title、image、image_caption、form、table、table_caption、header、footer、page_number、reference、formula、stamp、directory共15个类别。     

        :return: The type of this SmartDocumentRecognizerLayoutBlock.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this SmartDocumentRecognizerLayoutBlock.

        文档区域类别，包含text、title、sub_title、image、image_caption、form、table、table_caption、header、footer、page_number、reference、formula、stamp、directory共15个类别。     

        :param type: The type of this SmartDocumentRecognizerLayoutBlock.
        :type type: str
        """
        self._type = type

    @property
    def text(self):
        r"""Gets the text of this SmartDocumentRecognizerLayoutBlock.

        文档区域文字内容。对于表格与图像，不返回其中的文字内容。 

        :return: The text of this SmartDocumentRecognizerLayoutBlock.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        r"""Sets the text of this SmartDocumentRecognizerLayoutBlock.

        文档区域文字内容。对于表格与图像，不返回其中的文字内容。 

        :param text: The text of this SmartDocumentRecognizerLayoutBlock.
        :type text: str
        """
        self._text = text

    @property
    def words_ids(self):
        r"""Gets the words_ids of this SmartDocumentRecognizerLayoutBlock.

        文字识别结果索引列表，表示ocr_result的words_block_list中哪些文本框位于该文档区域内。 

        :return: The words_ids of this SmartDocumentRecognizerLayoutBlock.
        :rtype: list[int]
        """
        return self._words_ids

    @words_ids.setter
    def words_ids(self, words_ids):
        r"""Sets the words_ids of this SmartDocumentRecognizerLayoutBlock.

        文字识别结果索引列表，表示ocr_result的words_block_list中哪些文本框位于该文档区域内。 

        :param words_ids: The words_ids of this SmartDocumentRecognizerLayoutBlock.
        :type words_ids: list[int]
        """
        self._words_ids = words_ids

    @property
    def table_id(self):
        r"""Gets the table_id of this SmartDocumentRecognizerLayoutBlock.

        仅当type为\"table\"且入参table为True时返回该字段，表示当前逻辑表格区域对应table_result中哪一项识别结果。 

        :return: The table_id of this SmartDocumentRecognizerLayoutBlock.
        :rtype: int
        """
        return self._table_id

    @table_id.setter
    def table_id(self, table_id):
        r"""Sets the table_id of this SmartDocumentRecognizerLayoutBlock.

        仅当type为\"table\"且入参table为True时返回该字段，表示当前逻辑表格区域对应table_result中哪一项识别结果。 

        :param table_id: The table_id of this SmartDocumentRecognizerLayoutBlock.
        :type table_id: int
        """
        self._table_id = table_id

    @property
    def form_id(self):
        r"""Gets the form_id of this SmartDocumentRecognizerLayoutBlock.

        仅当type为\"form\"且入参form为True时返回该字段，表示当前有线表单区域对应form_result中哪一项识别结果。 

        :return: The form_id of this SmartDocumentRecognizerLayoutBlock.
        :rtype: int
        """
        return self._form_id

    @form_id.setter
    def form_id(self, form_id):
        r"""Sets the form_id of this SmartDocumentRecognizerLayoutBlock.

        仅当type为\"form\"且入参form为True时返回该字段，表示当前有线表单区域对应form_result中哪一项识别结果。 

        :param form_id: The form_id of this SmartDocumentRecognizerLayoutBlock.
        :type form_id: int
        """
        self._form_id = form_id

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
        if not isinstance(other, SmartDocumentRecognizerLayoutBlock):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
