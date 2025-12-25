# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CatalogueDetailInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'parent_catalogue': 'str',
        'second_catalogue': 'str',
        'catalogue_status': 'bool',
        'catalogue_address': 'str',
        'layout_id': 'str',
        'layout_name': 'str',
        'publisher_name': 'str',
        'is_card_area': 'bool',
        'is_display': 'bool',
        'is_landing_page': 'bool',
        'is_navigation': 'bool',
        'parent_alias_en': 'str',
        'parent_alias_zh': 'str',
        'second_alias_en': 'str',
        'second_alias_zh': 'str'
    }

    attribute_map = {
        'id': 'id',
        'parent_catalogue': 'parent_catalogue',
        'second_catalogue': 'second_catalogue',
        'catalogue_status': 'catalogue_status',
        'catalogue_address': 'catalogue_address',
        'layout_id': 'layout_id',
        'layout_name': 'layout_name',
        'publisher_name': 'publisher_name',
        'is_card_area': 'is_card_area',
        'is_display': 'is_display',
        'is_landing_page': 'is_landing_page',
        'is_navigation': 'is_navigation',
        'parent_alias_en': 'parent_alias_en',
        'parent_alias_zh': 'parent_alias_zh',
        'second_alias_en': 'second_alias_en',
        'second_alias_zh': 'second_alias_zh'
    }

    def __init__(self, id=None, parent_catalogue=None, second_catalogue=None, catalogue_status=None, catalogue_address=None, layout_id=None, layout_name=None, publisher_name=None, is_card_area=None, is_display=None, is_landing_page=None, is_navigation=None, parent_alias_en=None, parent_alias_zh=None, second_alias_en=None, second_alias_zh=None):
        r"""CatalogueDetailInfo

        The model defined in huaweicloud sdk

        :param id: 目录id
        :type id: str
        :param parent_catalogue: 一级目录名称
        :type parent_catalogue: str
        :param second_catalogue: 二级目录名称
        :type second_catalogue: str
        :param catalogue_status: 是否内置
        :type catalogue_status: bool
        :param catalogue_address: 目录地址
        :type catalogue_address: str
        :param layout_id: 布局ID
        :type layout_id: str
        :param layout_name: 布局名称
        :type layout_name: str
        :param publisher_name: 发布者
        :type publisher_name: str
        :param is_card_area: 是否展示名片区
        :type is_card_area: bool
        :param is_display: 是否展示目录
        :type is_display: bool
        :param is_landing_page: 是否为落地页
        :type is_landing_page: bool
        :param is_navigation: 是否展示面包屑导航
        :type is_navigation: bool
        :param parent_alias_en: 一级目录英文别名
        :type parent_alias_en: str
        :param parent_alias_zh: 一级目录中文别名
        :type parent_alias_zh: str
        :param second_alias_en: 二级目录英文别名
        :type second_alias_en: str
        :param second_alias_zh: 二级目录中文别名
        :type second_alias_zh: str
        """
        
        

        self._id = None
        self._parent_catalogue = None
        self._second_catalogue = None
        self._catalogue_status = None
        self._catalogue_address = None
        self._layout_id = None
        self._layout_name = None
        self._publisher_name = None
        self._is_card_area = None
        self._is_display = None
        self._is_landing_page = None
        self._is_navigation = None
        self._parent_alias_en = None
        self._parent_alias_zh = None
        self._second_alias_en = None
        self._second_alias_zh = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if parent_catalogue is not None:
            self.parent_catalogue = parent_catalogue
        if second_catalogue is not None:
            self.second_catalogue = second_catalogue
        if catalogue_status is not None:
            self.catalogue_status = catalogue_status
        if catalogue_address is not None:
            self.catalogue_address = catalogue_address
        if layout_id is not None:
            self.layout_id = layout_id
        if layout_name is not None:
            self.layout_name = layout_name
        if publisher_name is not None:
            self.publisher_name = publisher_name
        if is_card_area is not None:
            self.is_card_area = is_card_area
        if is_display is not None:
            self.is_display = is_display
        if is_landing_page is not None:
            self.is_landing_page = is_landing_page
        if is_navigation is not None:
            self.is_navigation = is_navigation
        if parent_alias_en is not None:
            self.parent_alias_en = parent_alias_en
        if parent_alias_zh is not None:
            self.parent_alias_zh = parent_alias_zh
        if second_alias_en is not None:
            self.second_alias_en = second_alias_en
        if second_alias_zh is not None:
            self.second_alias_zh = second_alias_zh

    @property
    def id(self):
        r"""Gets the id of this CatalogueDetailInfo.

        目录id

        :return: The id of this CatalogueDetailInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CatalogueDetailInfo.

        目录id

        :param id: The id of this CatalogueDetailInfo.
        :type id: str
        """
        self._id = id

    @property
    def parent_catalogue(self):
        r"""Gets the parent_catalogue of this CatalogueDetailInfo.

        一级目录名称

        :return: The parent_catalogue of this CatalogueDetailInfo.
        :rtype: str
        """
        return self._parent_catalogue

    @parent_catalogue.setter
    def parent_catalogue(self, parent_catalogue):
        r"""Sets the parent_catalogue of this CatalogueDetailInfo.

        一级目录名称

        :param parent_catalogue: The parent_catalogue of this CatalogueDetailInfo.
        :type parent_catalogue: str
        """
        self._parent_catalogue = parent_catalogue

    @property
    def second_catalogue(self):
        r"""Gets the second_catalogue of this CatalogueDetailInfo.

        二级目录名称

        :return: The second_catalogue of this CatalogueDetailInfo.
        :rtype: str
        """
        return self._second_catalogue

    @second_catalogue.setter
    def second_catalogue(self, second_catalogue):
        r"""Sets the second_catalogue of this CatalogueDetailInfo.

        二级目录名称

        :param second_catalogue: The second_catalogue of this CatalogueDetailInfo.
        :type second_catalogue: str
        """
        self._second_catalogue = second_catalogue

    @property
    def catalogue_status(self):
        r"""Gets the catalogue_status of this CatalogueDetailInfo.

        是否内置

        :return: The catalogue_status of this CatalogueDetailInfo.
        :rtype: bool
        """
        return self._catalogue_status

    @catalogue_status.setter
    def catalogue_status(self, catalogue_status):
        r"""Sets the catalogue_status of this CatalogueDetailInfo.

        是否内置

        :param catalogue_status: The catalogue_status of this CatalogueDetailInfo.
        :type catalogue_status: bool
        """
        self._catalogue_status = catalogue_status

    @property
    def catalogue_address(self):
        r"""Gets the catalogue_address of this CatalogueDetailInfo.

        目录地址

        :return: The catalogue_address of this CatalogueDetailInfo.
        :rtype: str
        """
        return self._catalogue_address

    @catalogue_address.setter
    def catalogue_address(self, catalogue_address):
        r"""Sets the catalogue_address of this CatalogueDetailInfo.

        目录地址

        :param catalogue_address: The catalogue_address of this CatalogueDetailInfo.
        :type catalogue_address: str
        """
        self._catalogue_address = catalogue_address

    @property
    def layout_id(self):
        r"""Gets the layout_id of this CatalogueDetailInfo.

        布局ID

        :return: The layout_id of this CatalogueDetailInfo.
        :rtype: str
        """
        return self._layout_id

    @layout_id.setter
    def layout_id(self, layout_id):
        r"""Sets the layout_id of this CatalogueDetailInfo.

        布局ID

        :param layout_id: The layout_id of this CatalogueDetailInfo.
        :type layout_id: str
        """
        self._layout_id = layout_id

    @property
    def layout_name(self):
        r"""Gets the layout_name of this CatalogueDetailInfo.

        布局名称

        :return: The layout_name of this CatalogueDetailInfo.
        :rtype: str
        """
        return self._layout_name

    @layout_name.setter
    def layout_name(self, layout_name):
        r"""Sets the layout_name of this CatalogueDetailInfo.

        布局名称

        :param layout_name: The layout_name of this CatalogueDetailInfo.
        :type layout_name: str
        """
        self._layout_name = layout_name

    @property
    def publisher_name(self):
        r"""Gets the publisher_name of this CatalogueDetailInfo.

        发布者

        :return: The publisher_name of this CatalogueDetailInfo.
        :rtype: str
        """
        return self._publisher_name

    @publisher_name.setter
    def publisher_name(self, publisher_name):
        r"""Sets the publisher_name of this CatalogueDetailInfo.

        发布者

        :param publisher_name: The publisher_name of this CatalogueDetailInfo.
        :type publisher_name: str
        """
        self._publisher_name = publisher_name

    @property
    def is_card_area(self):
        r"""Gets the is_card_area of this CatalogueDetailInfo.

        是否展示名片区

        :return: The is_card_area of this CatalogueDetailInfo.
        :rtype: bool
        """
        return self._is_card_area

    @is_card_area.setter
    def is_card_area(self, is_card_area):
        r"""Sets the is_card_area of this CatalogueDetailInfo.

        是否展示名片区

        :param is_card_area: The is_card_area of this CatalogueDetailInfo.
        :type is_card_area: bool
        """
        self._is_card_area = is_card_area

    @property
    def is_display(self):
        r"""Gets the is_display of this CatalogueDetailInfo.

        是否展示目录

        :return: The is_display of this CatalogueDetailInfo.
        :rtype: bool
        """
        return self._is_display

    @is_display.setter
    def is_display(self, is_display):
        r"""Sets the is_display of this CatalogueDetailInfo.

        是否展示目录

        :param is_display: The is_display of this CatalogueDetailInfo.
        :type is_display: bool
        """
        self._is_display = is_display

    @property
    def is_landing_page(self):
        r"""Gets the is_landing_page of this CatalogueDetailInfo.

        是否为落地页

        :return: The is_landing_page of this CatalogueDetailInfo.
        :rtype: bool
        """
        return self._is_landing_page

    @is_landing_page.setter
    def is_landing_page(self, is_landing_page):
        r"""Sets the is_landing_page of this CatalogueDetailInfo.

        是否为落地页

        :param is_landing_page: The is_landing_page of this CatalogueDetailInfo.
        :type is_landing_page: bool
        """
        self._is_landing_page = is_landing_page

    @property
    def is_navigation(self):
        r"""Gets the is_navigation of this CatalogueDetailInfo.

        是否展示面包屑导航

        :return: The is_navigation of this CatalogueDetailInfo.
        :rtype: bool
        """
        return self._is_navigation

    @is_navigation.setter
    def is_navigation(self, is_navigation):
        r"""Sets the is_navigation of this CatalogueDetailInfo.

        是否展示面包屑导航

        :param is_navigation: The is_navigation of this CatalogueDetailInfo.
        :type is_navigation: bool
        """
        self._is_navigation = is_navigation

    @property
    def parent_alias_en(self):
        r"""Gets the parent_alias_en of this CatalogueDetailInfo.

        一级目录英文别名

        :return: The parent_alias_en of this CatalogueDetailInfo.
        :rtype: str
        """
        return self._parent_alias_en

    @parent_alias_en.setter
    def parent_alias_en(self, parent_alias_en):
        r"""Sets the parent_alias_en of this CatalogueDetailInfo.

        一级目录英文别名

        :param parent_alias_en: The parent_alias_en of this CatalogueDetailInfo.
        :type parent_alias_en: str
        """
        self._parent_alias_en = parent_alias_en

    @property
    def parent_alias_zh(self):
        r"""Gets the parent_alias_zh of this CatalogueDetailInfo.

        一级目录中文别名

        :return: The parent_alias_zh of this CatalogueDetailInfo.
        :rtype: str
        """
        return self._parent_alias_zh

    @parent_alias_zh.setter
    def parent_alias_zh(self, parent_alias_zh):
        r"""Sets the parent_alias_zh of this CatalogueDetailInfo.

        一级目录中文别名

        :param parent_alias_zh: The parent_alias_zh of this CatalogueDetailInfo.
        :type parent_alias_zh: str
        """
        self._parent_alias_zh = parent_alias_zh

    @property
    def second_alias_en(self):
        r"""Gets the second_alias_en of this CatalogueDetailInfo.

        二级目录英文别名

        :return: The second_alias_en of this CatalogueDetailInfo.
        :rtype: str
        """
        return self._second_alias_en

    @second_alias_en.setter
    def second_alias_en(self, second_alias_en):
        r"""Sets the second_alias_en of this CatalogueDetailInfo.

        二级目录英文别名

        :param second_alias_en: The second_alias_en of this CatalogueDetailInfo.
        :type second_alias_en: str
        """
        self._second_alias_en = second_alias_en

    @property
    def second_alias_zh(self):
        r"""Gets the second_alias_zh of this CatalogueDetailInfo.

        二级目录中文别名

        :return: The second_alias_zh of this CatalogueDetailInfo.
        :rtype: str
        """
        return self._second_alias_zh

    @second_alias_zh.setter
    def second_alias_zh(self, second_alias_zh):
        r"""Sets the second_alias_zh of this CatalogueDetailInfo.

        二级目录中文别名

        :param second_alias_zh: The second_alias_zh of this CatalogueDetailInfo.
        :type second_alias_zh: str
        """
        self._second_alias_zh = second_alias_zh

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CatalogueDetailInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
