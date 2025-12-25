# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCatalogueRequestPojo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_navigation': 'bool',
        'is_card_area': 'bool',
        'landing_page': 'str',
        'parent_alias_zh': 'str',
        'parent_alias_en': 'str',
        'parent_catalogue': 'str',
        'catalogue_infos': 'list[CatalogueBatchPojo]'
    }

    attribute_map = {
        'is_navigation': 'is_navigation',
        'is_card_area': 'is_card_area',
        'landing_page': 'landing_page',
        'parent_alias_zh': 'parent_alias_zh',
        'parent_alias_en': 'parent_alias_en',
        'parent_catalogue': 'parent_catalogue',
        'catalogue_infos': 'catalogue_infos'
    }

    def __init__(self, is_navigation=None, is_card_area=None, landing_page=None, parent_alias_zh=None, parent_alias_en=None, parent_catalogue=None, catalogue_infos=None):
        r"""BatchCatalogueRequestPojo

        The model defined in huaweicloud sdk

        :param is_navigation: 是否显示面包屑导航
        :type is_navigation: bool
        :param is_card_area: 是否显示名片区
        :type is_card_area: bool
        :param landing_page: 落地页
        :type landing_page: str
        :param parent_alias_zh: 一级目录中文别名
        :type parent_alias_zh: str
        :param parent_alias_en: 一级目录中文别名
        :type parent_alias_en: str
        :param parent_catalogue: 一级目录名称
        :type parent_catalogue: str
        :param catalogue_infos: 目录详情列表
        :type catalogue_infos: list[:class:`huaweicloudsdksecmaster.v1.CatalogueBatchPojo`]
        """
        
        

        self._is_navigation = None
        self._is_card_area = None
        self._landing_page = None
        self._parent_alias_zh = None
        self._parent_alias_en = None
        self._parent_catalogue = None
        self._catalogue_infos = None
        self.discriminator = None

        if is_navigation is not None:
            self.is_navigation = is_navigation
        if is_card_area is not None:
            self.is_card_area = is_card_area
        if landing_page is not None:
            self.landing_page = landing_page
        if parent_alias_zh is not None:
            self.parent_alias_zh = parent_alias_zh
        if parent_alias_en is not None:
            self.parent_alias_en = parent_alias_en
        if parent_catalogue is not None:
            self.parent_catalogue = parent_catalogue
        if catalogue_infos is not None:
            self.catalogue_infos = catalogue_infos

    @property
    def is_navigation(self):
        r"""Gets the is_navigation of this BatchCatalogueRequestPojo.

        是否显示面包屑导航

        :return: The is_navigation of this BatchCatalogueRequestPojo.
        :rtype: bool
        """
        return self._is_navigation

    @is_navigation.setter
    def is_navigation(self, is_navigation):
        r"""Sets the is_navigation of this BatchCatalogueRequestPojo.

        是否显示面包屑导航

        :param is_navigation: The is_navigation of this BatchCatalogueRequestPojo.
        :type is_navigation: bool
        """
        self._is_navigation = is_navigation

    @property
    def is_card_area(self):
        r"""Gets the is_card_area of this BatchCatalogueRequestPojo.

        是否显示名片区

        :return: The is_card_area of this BatchCatalogueRequestPojo.
        :rtype: bool
        """
        return self._is_card_area

    @is_card_area.setter
    def is_card_area(self, is_card_area):
        r"""Sets the is_card_area of this BatchCatalogueRequestPojo.

        是否显示名片区

        :param is_card_area: The is_card_area of this BatchCatalogueRequestPojo.
        :type is_card_area: bool
        """
        self._is_card_area = is_card_area

    @property
    def landing_page(self):
        r"""Gets the landing_page of this BatchCatalogueRequestPojo.

        落地页

        :return: The landing_page of this BatchCatalogueRequestPojo.
        :rtype: str
        """
        return self._landing_page

    @landing_page.setter
    def landing_page(self, landing_page):
        r"""Sets the landing_page of this BatchCatalogueRequestPojo.

        落地页

        :param landing_page: The landing_page of this BatchCatalogueRequestPojo.
        :type landing_page: str
        """
        self._landing_page = landing_page

    @property
    def parent_alias_zh(self):
        r"""Gets the parent_alias_zh of this BatchCatalogueRequestPojo.

        一级目录中文别名

        :return: The parent_alias_zh of this BatchCatalogueRequestPojo.
        :rtype: str
        """
        return self._parent_alias_zh

    @parent_alias_zh.setter
    def parent_alias_zh(self, parent_alias_zh):
        r"""Sets the parent_alias_zh of this BatchCatalogueRequestPojo.

        一级目录中文别名

        :param parent_alias_zh: The parent_alias_zh of this BatchCatalogueRequestPojo.
        :type parent_alias_zh: str
        """
        self._parent_alias_zh = parent_alias_zh

    @property
    def parent_alias_en(self):
        r"""Gets the parent_alias_en of this BatchCatalogueRequestPojo.

        一级目录中文别名

        :return: The parent_alias_en of this BatchCatalogueRequestPojo.
        :rtype: str
        """
        return self._parent_alias_en

    @parent_alias_en.setter
    def parent_alias_en(self, parent_alias_en):
        r"""Sets the parent_alias_en of this BatchCatalogueRequestPojo.

        一级目录中文别名

        :param parent_alias_en: The parent_alias_en of this BatchCatalogueRequestPojo.
        :type parent_alias_en: str
        """
        self._parent_alias_en = parent_alias_en

    @property
    def parent_catalogue(self):
        r"""Gets the parent_catalogue of this BatchCatalogueRequestPojo.

        一级目录名称

        :return: The parent_catalogue of this BatchCatalogueRequestPojo.
        :rtype: str
        """
        return self._parent_catalogue

    @parent_catalogue.setter
    def parent_catalogue(self, parent_catalogue):
        r"""Sets the parent_catalogue of this BatchCatalogueRequestPojo.

        一级目录名称

        :param parent_catalogue: The parent_catalogue of this BatchCatalogueRequestPojo.
        :type parent_catalogue: str
        """
        self._parent_catalogue = parent_catalogue

    @property
    def catalogue_infos(self):
        r"""Gets the catalogue_infos of this BatchCatalogueRequestPojo.

        目录详情列表

        :return: The catalogue_infos of this BatchCatalogueRequestPojo.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.CatalogueBatchPojo`]
        """
        return self._catalogue_infos

    @catalogue_infos.setter
    def catalogue_infos(self, catalogue_infos):
        r"""Sets the catalogue_infos of this BatchCatalogueRequestPojo.

        目录详情列表

        :param catalogue_infos: The catalogue_infos of this BatchCatalogueRequestPojo.
        :type catalogue_infos: list[:class:`huaweicloudsdksecmaster.v1.CatalogueBatchPojo`]
        """
        self._catalogue_infos = catalogue_infos

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
        if not isinstance(other, BatchCatalogueRequestPojo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
