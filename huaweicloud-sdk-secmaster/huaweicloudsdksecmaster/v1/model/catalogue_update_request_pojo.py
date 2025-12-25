# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CatalogueUpdateRequestPojo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'parent_alias_en': 'str',
        'parent_alias_zh': 'str',
        'second_catalogue': 'str',
        'second_alias_en': 'str',
        'second_alias_zh': 'str',
        'layout_id': 'str',
        'layout_name': 'str',
        'catalogue_address': 'str',
        'publisher_name': 'str'
    }

    attribute_map = {
        'parent_alias_en': 'parent_alias_en',
        'parent_alias_zh': 'parent_alias_zh',
        'second_catalogue': 'second_catalogue',
        'second_alias_en': 'second_alias_en',
        'second_alias_zh': 'second_alias_zh',
        'layout_id': 'layout_id',
        'layout_name': 'layout_name',
        'catalogue_address': 'catalogue_address',
        'publisher_name': 'publisher_name'
    }

    def __init__(self, parent_alias_en=None, parent_alias_zh=None, second_catalogue=None, second_alias_en=None, second_alias_zh=None, layout_id=None, layout_name=None, catalogue_address=None, publisher_name=None):
        r"""CatalogueUpdateRequestPojo

        The model defined in huaweicloud sdk

        :param parent_alias_en: 一级目录英文别名
        :type parent_alias_en: str
        :param parent_alias_zh: 一级目录中文别名
        :type parent_alias_zh: str
        :param second_catalogue: 二级目录名称
        :type second_catalogue: str
        :param second_alias_en: 二级目录英文别名
        :type second_alias_en: str
        :param second_alias_zh: 二级目录中文别名
        :type second_alias_zh: str
        :param layout_id: 布局ID
        :type layout_id: str
        :param layout_name: 布局名称
        :type layout_name: str
        :param catalogue_address: 目录地址
        :type catalogue_address: str
        :param publisher_name: 发布者
        :type publisher_name: str
        """
        
        

        self._parent_alias_en = None
        self._parent_alias_zh = None
        self._second_catalogue = None
        self._second_alias_en = None
        self._second_alias_zh = None
        self._layout_id = None
        self._layout_name = None
        self._catalogue_address = None
        self._publisher_name = None
        self.discriminator = None

        self.parent_alias_en = parent_alias_en
        self.parent_alias_zh = parent_alias_zh
        self.second_catalogue = second_catalogue
        self.second_alias_en = second_alias_en
        self.second_alias_zh = second_alias_zh
        self.layout_id = layout_id
        if layout_name is not None:
            self.layout_name = layout_name
        self.catalogue_address = catalogue_address
        if publisher_name is not None:
            self.publisher_name = publisher_name

    @property
    def parent_alias_en(self):
        r"""Gets the parent_alias_en of this CatalogueUpdateRequestPojo.

        一级目录英文别名

        :return: The parent_alias_en of this CatalogueUpdateRequestPojo.
        :rtype: str
        """
        return self._parent_alias_en

    @parent_alias_en.setter
    def parent_alias_en(self, parent_alias_en):
        r"""Sets the parent_alias_en of this CatalogueUpdateRequestPojo.

        一级目录英文别名

        :param parent_alias_en: The parent_alias_en of this CatalogueUpdateRequestPojo.
        :type parent_alias_en: str
        """
        self._parent_alias_en = parent_alias_en

    @property
    def parent_alias_zh(self):
        r"""Gets the parent_alias_zh of this CatalogueUpdateRequestPojo.

        一级目录中文别名

        :return: The parent_alias_zh of this CatalogueUpdateRequestPojo.
        :rtype: str
        """
        return self._parent_alias_zh

    @parent_alias_zh.setter
    def parent_alias_zh(self, parent_alias_zh):
        r"""Sets the parent_alias_zh of this CatalogueUpdateRequestPojo.

        一级目录中文别名

        :param parent_alias_zh: The parent_alias_zh of this CatalogueUpdateRequestPojo.
        :type parent_alias_zh: str
        """
        self._parent_alias_zh = parent_alias_zh

    @property
    def second_catalogue(self):
        r"""Gets the second_catalogue of this CatalogueUpdateRequestPojo.

        二级目录名称

        :return: The second_catalogue of this CatalogueUpdateRequestPojo.
        :rtype: str
        """
        return self._second_catalogue

    @second_catalogue.setter
    def second_catalogue(self, second_catalogue):
        r"""Sets the second_catalogue of this CatalogueUpdateRequestPojo.

        二级目录名称

        :param second_catalogue: The second_catalogue of this CatalogueUpdateRequestPojo.
        :type second_catalogue: str
        """
        self._second_catalogue = second_catalogue

    @property
    def second_alias_en(self):
        r"""Gets the second_alias_en of this CatalogueUpdateRequestPojo.

        二级目录英文别名

        :return: The second_alias_en of this CatalogueUpdateRequestPojo.
        :rtype: str
        """
        return self._second_alias_en

    @second_alias_en.setter
    def second_alias_en(self, second_alias_en):
        r"""Sets the second_alias_en of this CatalogueUpdateRequestPojo.

        二级目录英文别名

        :param second_alias_en: The second_alias_en of this CatalogueUpdateRequestPojo.
        :type second_alias_en: str
        """
        self._second_alias_en = second_alias_en

    @property
    def second_alias_zh(self):
        r"""Gets the second_alias_zh of this CatalogueUpdateRequestPojo.

        二级目录中文别名

        :return: The second_alias_zh of this CatalogueUpdateRequestPojo.
        :rtype: str
        """
        return self._second_alias_zh

    @second_alias_zh.setter
    def second_alias_zh(self, second_alias_zh):
        r"""Sets the second_alias_zh of this CatalogueUpdateRequestPojo.

        二级目录中文别名

        :param second_alias_zh: The second_alias_zh of this CatalogueUpdateRequestPojo.
        :type second_alias_zh: str
        """
        self._second_alias_zh = second_alias_zh

    @property
    def layout_id(self):
        r"""Gets the layout_id of this CatalogueUpdateRequestPojo.

        布局ID

        :return: The layout_id of this CatalogueUpdateRequestPojo.
        :rtype: str
        """
        return self._layout_id

    @layout_id.setter
    def layout_id(self, layout_id):
        r"""Sets the layout_id of this CatalogueUpdateRequestPojo.

        布局ID

        :param layout_id: The layout_id of this CatalogueUpdateRequestPojo.
        :type layout_id: str
        """
        self._layout_id = layout_id

    @property
    def layout_name(self):
        r"""Gets the layout_name of this CatalogueUpdateRequestPojo.

        布局名称

        :return: The layout_name of this CatalogueUpdateRequestPojo.
        :rtype: str
        """
        return self._layout_name

    @layout_name.setter
    def layout_name(self, layout_name):
        r"""Sets the layout_name of this CatalogueUpdateRequestPojo.

        布局名称

        :param layout_name: The layout_name of this CatalogueUpdateRequestPojo.
        :type layout_name: str
        """
        self._layout_name = layout_name

    @property
    def catalogue_address(self):
        r"""Gets the catalogue_address of this CatalogueUpdateRequestPojo.

        目录地址

        :return: The catalogue_address of this CatalogueUpdateRequestPojo.
        :rtype: str
        """
        return self._catalogue_address

    @catalogue_address.setter
    def catalogue_address(self, catalogue_address):
        r"""Sets the catalogue_address of this CatalogueUpdateRequestPojo.

        目录地址

        :param catalogue_address: The catalogue_address of this CatalogueUpdateRequestPojo.
        :type catalogue_address: str
        """
        self._catalogue_address = catalogue_address

    @property
    def publisher_name(self):
        r"""Gets the publisher_name of this CatalogueUpdateRequestPojo.

        发布者

        :return: The publisher_name of this CatalogueUpdateRequestPojo.
        :rtype: str
        """
        return self._publisher_name

    @publisher_name.setter
    def publisher_name(self, publisher_name):
        r"""Sets the publisher_name of this CatalogueUpdateRequestPojo.

        发布者

        :param publisher_name: The publisher_name of this CatalogueUpdateRequestPojo.
        :type publisher_name: str
        """
        self._publisher_name = publisher_name

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
        if not isinstance(other, CatalogueUpdateRequestPojo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
