# coding: utf-8

import pprint
import re

import six





class WebImageWordsBlockList:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'words': 'str',
        'confidence': 'float',
        'location': 'list[int]',
        'extracted_data': 'object',
        'contact_info': 'object',
        'image_size': 'object',
        'height': 'int',
        'width': 'int',
        'name': 'str',
        'phone': 'str',
        'province': 'str',
        'city': 'str',
        'district': 'str',
        'detail_address': 'str'
    }

    attribute_map = {
        'words': 'words',
        'confidence': 'confidence',
        'location': 'location',
        'extracted_data': 'extracted_data',
        'contact_info': 'contact_info',
        'image_size': 'image_size',
        'height': 'height',
        'width': 'width',
        'name': 'name',
        'phone': 'phone',
        'province': 'province',
        'city': 'city',
        'district': 'district',
        'detail_address': 'detail_address'
    }

    def __init__(self, words=None, confidence=None, location=None, extracted_data=None, contact_info=None, image_size=None, height=None, width=None, name=None, phone=None, province=None, city=None, district=None, detail_address=None):
        """WebImageWordsBlockList - a model defined in huaweicloud sdk"""
        
        

        self._words = None
        self._confidence = None
        self._location = None
        self._extracted_data = None
        self._contact_info = None
        self._image_size = None
        self._height = None
        self._width = None
        self._name = None
        self._phone = None
        self._province = None
        self._city = None
        self._district = None
        self._detail_address = None
        self.discriminator = None

        if words is not None:
            self.words = words
        if confidence is not None:
            self.confidence = confidence
        if location is not None:
            self.location = location
        if extracted_data is not None:
            self.extracted_data = extracted_data
        if contact_info is not None:
            self.contact_info = contact_info
        if image_size is not None:
            self.image_size = image_size
        if height is not None:
            self.height = height
        if width is not None:
            self.width = width
        if name is not None:
            self.name = name
        if phone is not None:
            self.phone = phone
        if province is not None:
            self.province = province
        if city is not None:
            self.city = city
        if district is not None:
            self.district = district
        if detail_address is not None:
            self.detail_address = detail_address

    @property
    def words(self):
        """Gets the words of this WebImageWordsBlockList.

        文字块识别结果。 

        :return: The words of this WebImageWordsBlockList.
        :rtype: str
        """
        return self._words

    @words.setter
    def words(self, words):
        """Sets the words of this WebImageWordsBlockList.

        文字块识别结果。 

        :param words: The words of this WebImageWordsBlockList.
        :type: str
        """
        self._words = words

    @property
    def confidence(self):
        """Gets the confidence of this WebImageWordsBlockList.

        相关字段的置信度信息，置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。 置信度由算法给出，不直接等价于对应字段的准确率。 

        :return: The confidence of this WebImageWordsBlockList.
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this WebImageWordsBlockList.

        相关字段的置信度信息，置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。 置信度由算法给出，不直接等价于对应字段的准确率。 

        :param confidence: The confidence of this WebImageWordsBlockList.
        :type: float
        """
        self._confidence = confidence

    @property
    def location(self):
        """Gets the location of this WebImageWordsBlockList.

        文字块的区域位置信息，列表形式，包含文字区域四个顶点的二维坐标（x,y）;坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :return: The location of this WebImageWordsBlockList.
        :rtype: list[int]
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this WebImageWordsBlockList.

        文字块的区域位置信息，列表形式，包含文字区域四个顶点的二维坐标（x,y）;坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :param location: The location of this WebImageWordsBlockList.
        :type: list[int]
        """
        self._location = location

    @property
    def extracted_data(self):
        """Gets the extracted_data of this WebImageWordsBlockList.

        提取出的结构化JSON结果，该字典内的key值与入参列表extract_type的值一致，目前仅支持联系人信息提取，亦即key值为\"contact_info\"的字段。 若入参extract_type为空列表或该字段缺失时，不进行提取，此字段为空。 

        :return: The extracted_data of this WebImageWordsBlockList.
        :rtype: object
        """
        return self._extracted_data

    @extracted_data.setter
    def extracted_data(self, extracted_data):
        """Sets the extracted_data of this WebImageWordsBlockList.

        提取出的结构化JSON结果，该字典内的key值与入参列表extract_type的值一致，目前仅支持联系人信息提取，亦即key值为\"contact_info\"的字段。 若入参extract_type为空列表或该字段缺失时，不进行提取，此字段为空。 

        :param extracted_data: The extracted_data of this WebImageWordsBlockList.
        :type: object
        """
        self._extracted_data = extracted_data

    @property
    def contact_info(self):
        """Gets the contact_info of this WebImageWordsBlockList.

        该字段表示提取的联系人信息，包括：姓名、联系电话、省市区以及详细地址。 若入参extract_type列表中无该字段，则此字段不存在。 

        :return: The contact_info of this WebImageWordsBlockList.
        :rtype: object
        """
        return self._contact_info

    @contact_info.setter
    def contact_info(self, contact_info):
        """Sets the contact_info of this WebImageWordsBlockList.

        该字段表示提取的联系人信息，包括：姓名、联系电话、省市区以及详细地址。 若入参extract_type列表中无该字段，则此字段不存在。 

        :param contact_info: The contact_info of this WebImageWordsBlockList.
        :type: object
        """
        self._contact_info = contact_info

    @property
    def image_size(self):
        """Gets the image_size of this WebImageWordsBlockList.

        该字段表示返回图片宽高信息。 如入参extract_type列表中无该字段，则此字段不存在。 

        :return: The image_size of this WebImageWordsBlockList.
        :rtype: object
        """
        return self._image_size

    @image_size.setter
    def image_size(self, image_size):
        """Sets the image_size of this WebImageWordsBlockList.

        该字段表示返回图片宽高信息。 如入参extract_type列表中无该字段，则此字段不存在。 

        :param image_size: The image_size of this WebImageWordsBlockList.
        :type: object
        """
        self._image_size = image_size

    @property
    def height(self):
        """Gets the height of this WebImageWordsBlockList.

        传入image_size时的返回，为图像高度。 

        :return: The height of this WebImageWordsBlockList.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this WebImageWordsBlockList.

        传入image_size时的返回，为图像高度。 

        :param height: The height of this WebImageWordsBlockList.
        :type: int
        """
        self._height = height

    @property
    def width(self):
        """Gets the width of this WebImageWordsBlockList.

        传入image_size时的返回，为图像宽度。 

        :return: The width of this WebImageWordsBlockList.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this WebImageWordsBlockList.

        传入image_size时的返回，为图像宽度。 

        :param width: The width of this WebImageWordsBlockList.
        :type: int
        """
        self._width = width

    @property
    def name(self):
        """Gets the name of this WebImageWordsBlockList.

        传入contact_info时的返回，为姓名。 

        :return: The name of this WebImageWordsBlockList.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WebImageWordsBlockList.

        传入contact_info时的返回，为姓名。 

        :param name: The name of this WebImageWordsBlockList.
        :type: str
        """
        self._name = name

    @property
    def phone(self):
        """Gets the phone of this WebImageWordsBlockList.

        传入contact_info时的返回，联系电话。 

        :return: The phone of this WebImageWordsBlockList.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this WebImageWordsBlockList.

        传入contact_info时的返回，联系电话。 

        :param phone: The phone of this WebImageWordsBlockList.
        :type: str
        """
        self._phone = phone

    @property
    def province(self):
        """Gets the province of this WebImageWordsBlockList.

        传入contact_info时的返回，省。 

        :return: The province of this WebImageWordsBlockList.
        :rtype: str
        """
        return self._province

    @province.setter
    def province(self, province):
        """Sets the province of this WebImageWordsBlockList.

        传入contact_info时的返回，省。 

        :param province: The province of this WebImageWordsBlockList.
        :type: str
        """
        self._province = province

    @property
    def city(self):
        """Gets the city of this WebImageWordsBlockList.

        传入contact_info时的返回，市。 

        :return: The city of this WebImageWordsBlockList.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this WebImageWordsBlockList.

        传入contact_info时的返回，市。 

        :param city: The city of this WebImageWordsBlockList.
        :type: str
        """
        self._city = city

    @property
    def district(self):
        """Gets the district of this WebImageWordsBlockList.

        传入contact_info时的返回，县区。 

        :return: The district of this WebImageWordsBlockList.
        :rtype: str
        """
        return self._district

    @district.setter
    def district(self, district):
        """Sets the district of this WebImageWordsBlockList.

        传入contact_info时的返回，县区。 

        :param district: The district of this WebImageWordsBlockList.
        :type: str
        """
        self._district = district

    @property
    def detail_address(self):
        """Gets the detail_address of this WebImageWordsBlockList.

        传入contact_info时的返回，详细地址（不含省市区）。 

        :return: The detail_address of this WebImageWordsBlockList.
        :rtype: str
        """
        return self._detail_address

    @detail_address.setter
    def detail_address(self, detail_address):
        """Sets the detail_address of this WebImageWordsBlockList.

        传入contact_info时的返回，详细地址（不含省市区）。 

        :param detail_address: The detail_address of this WebImageWordsBlockList.
        :type: str
        """
        self._detail_address = detail_address

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, WebImageWordsBlockList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
