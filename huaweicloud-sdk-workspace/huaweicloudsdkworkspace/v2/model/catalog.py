# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Catalog:

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
        'catalog_zh': 'str',
        'catalog_en': 'str'
    }

    attribute_map = {
        'id': 'id',
        'catalog_zh': 'catalog_zh',
        'catalog_en': 'catalog_en'
    }

    def __init__(self, id=None, catalog_zh=None, catalog_en=None):
        r"""Catalog

        The model defined in huaweicloud sdk

        :param id: 唯一标识ID。
        :type id: str
        :param catalog_zh: 分类描述(中文)。
        :type catalog_zh: str
        :param catalog_en: 分类描述(英文)。
        :type catalog_en: str
        """
        
        

        self._id = None
        self._catalog_zh = None
        self._catalog_en = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if catalog_zh is not None:
            self.catalog_zh = catalog_zh
        if catalog_en is not None:
            self.catalog_en = catalog_en

    @property
    def id(self):
        r"""Gets the id of this Catalog.

        唯一标识ID。

        :return: The id of this Catalog.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Catalog.

        唯一标识ID。

        :param id: The id of this Catalog.
        :type id: str
        """
        self._id = id

    @property
    def catalog_zh(self):
        r"""Gets the catalog_zh of this Catalog.

        分类描述(中文)。

        :return: The catalog_zh of this Catalog.
        :rtype: str
        """
        return self._catalog_zh

    @catalog_zh.setter
    def catalog_zh(self, catalog_zh):
        r"""Sets the catalog_zh of this Catalog.

        分类描述(中文)。

        :param catalog_zh: The catalog_zh of this Catalog.
        :type catalog_zh: str
        """
        self._catalog_zh = catalog_zh

    @property
    def catalog_en(self):
        r"""Gets the catalog_en of this Catalog.

        分类描述(英文)。

        :return: The catalog_en of this Catalog.
        :rtype: str
        """
        return self._catalog_en

    @catalog_en.setter
    def catalog_en(self, catalog_en):
        r"""Sets the catalog_en of this Catalog.

        分类描述(英文)。

        :param catalog_en: The catalog_en of this Catalog.
        :type catalog_en: str
        """
        self._catalog_en = catalog_en

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
        if not isinstance(other, Catalog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
