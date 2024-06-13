# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateProductRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'tags': 'list[str]',
        'cover': 'ProductCoverInfo',
        'text_list': 'list[ProductTextInfo]',
        'asset_list': 'list[ProductMediaInfo]',
        'auto_active': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'tags': 'tags',
        'cover': 'cover',
        'text_list': 'text_list',
        'asset_list': 'asset_list',
        'auto_active': 'auto_active'
    }

    def __init__(self, name=None, description=None, tags=None, cover=None, text_list=None, asset_list=None, auto_active=None):
        """CreateProductRequestBody

        The model defined in huaweicloud sdk

        :param name: 商品名称
        :type name: str
        :param description: 商品描述
        :type description: str
        :param tags: 标签。单个标签16字节，多个用逗号分隔，最多50个。
        :type tags: list[str]
        :param cover: 
        :type cover: :class:`huaweicloudsdkmetastudio.v1.ProductCoverInfo`
        :param text_list: 文本列表
        :type text_list: list[:class:`huaweicloudsdkmetastudio.v1.ProductTextInfo`]
        :param asset_list: 素材资产列表
        :type asset_list: list[:class:`huaweicloudsdkmetastudio.v1.ProductMediaInfo`]
        :param auto_active: 自动激活商品
        :type auto_active: bool
        """
        
        

        self._name = None
        self._description = None
        self._tags = None
        self._cover = None
        self._text_list = None
        self._asset_list = None
        self._auto_active = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags
        if cover is not None:
            self.cover = cover
        if text_list is not None:
            self.text_list = text_list
        if asset_list is not None:
            self.asset_list = asset_list
        if auto_active is not None:
            self.auto_active = auto_active

    @property
    def name(self):
        """Gets the name of this CreateProductRequestBody.

        商品名称

        :return: The name of this CreateProductRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateProductRequestBody.

        商品名称

        :param name: The name of this CreateProductRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateProductRequestBody.

        商品描述

        :return: The description of this CreateProductRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateProductRequestBody.

        商品描述

        :param description: The description of this CreateProductRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def tags(self):
        """Gets the tags of this CreateProductRequestBody.

        标签。单个标签16字节，多个用逗号分隔，最多50个。

        :return: The tags of this CreateProductRequestBody.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateProductRequestBody.

        标签。单个标签16字节，多个用逗号分隔，最多50个。

        :param tags: The tags of this CreateProductRequestBody.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def cover(self):
        """Gets the cover of this CreateProductRequestBody.

        :return: The cover of this CreateProductRequestBody.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ProductCoverInfo`
        """
        return self._cover

    @cover.setter
    def cover(self, cover):
        """Sets the cover of this CreateProductRequestBody.

        :param cover: The cover of this CreateProductRequestBody.
        :type cover: :class:`huaweicloudsdkmetastudio.v1.ProductCoverInfo`
        """
        self._cover = cover

    @property
    def text_list(self):
        """Gets the text_list of this CreateProductRequestBody.

        文本列表

        :return: The text_list of this CreateProductRequestBody.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.ProductTextInfo`]
        """
        return self._text_list

    @text_list.setter
    def text_list(self, text_list):
        """Sets the text_list of this CreateProductRequestBody.

        文本列表

        :param text_list: The text_list of this CreateProductRequestBody.
        :type text_list: list[:class:`huaweicloudsdkmetastudio.v1.ProductTextInfo`]
        """
        self._text_list = text_list

    @property
    def asset_list(self):
        """Gets the asset_list of this CreateProductRequestBody.

        素材资产列表

        :return: The asset_list of this CreateProductRequestBody.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.ProductMediaInfo`]
        """
        return self._asset_list

    @asset_list.setter
    def asset_list(self, asset_list):
        """Sets the asset_list of this CreateProductRequestBody.

        素材资产列表

        :param asset_list: The asset_list of this CreateProductRequestBody.
        :type asset_list: list[:class:`huaweicloudsdkmetastudio.v1.ProductMediaInfo`]
        """
        self._asset_list = asset_list

    @property
    def auto_active(self):
        """Gets the auto_active of this CreateProductRequestBody.

        自动激活商品

        :return: The auto_active of this CreateProductRequestBody.
        :rtype: bool
        """
        return self._auto_active

    @auto_active.setter
    def auto_active(self, auto_active):
        """Sets the auto_active of this CreateProductRequestBody.

        自动激活商品

        :param auto_active: The auto_active of this CreateProductRequestBody.
        :type auto_active: bool
        """
        self._auto_active = auto_active

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
        if not isinstance(other, CreateProductRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
