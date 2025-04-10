# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProductBasicInfo:

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
        'asset_list': 'list[ProductMediaInfo]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'tags': 'tags',
        'cover': 'cover',
        'text_list': 'text_list',
        'asset_list': 'asset_list'
    }

    def __init__(self, name=None, description=None, tags=None, cover=None, text_list=None, asset_list=None):
        r"""ProductBasicInfo

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
        :param asset_list: 资产列表,仅支持图片、视频、音频资产
        :type asset_list: list[:class:`huaweicloudsdkmetastudio.v1.ProductMediaInfo`]
        """
        
        

        self._name = None
        self._description = None
        self._tags = None
        self._cover = None
        self._text_list = None
        self._asset_list = None
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

    @property
    def name(self):
        r"""Gets the name of this ProductBasicInfo.

        商品名称

        :return: The name of this ProductBasicInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ProductBasicInfo.

        商品名称

        :param name: The name of this ProductBasicInfo.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ProductBasicInfo.

        商品描述

        :return: The description of this ProductBasicInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ProductBasicInfo.

        商品描述

        :param description: The description of this ProductBasicInfo.
        :type description: str
        """
        self._description = description

    @property
    def tags(self):
        r"""Gets the tags of this ProductBasicInfo.

        标签。单个标签16字节，多个用逗号分隔，最多50个。

        :return: The tags of this ProductBasicInfo.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ProductBasicInfo.

        标签。单个标签16字节，多个用逗号分隔，最多50个。

        :param tags: The tags of this ProductBasicInfo.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def cover(self):
        r"""Gets the cover of this ProductBasicInfo.

        :return: The cover of this ProductBasicInfo.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ProductCoverInfo`
        """
        return self._cover

    @cover.setter
    def cover(self, cover):
        r"""Sets the cover of this ProductBasicInfo.

        :param cover: The cover of this ProductBasicInfo.
        :type cover: :class:`huaweicloudsdkmetastudio.v1.ProductCoverInfo`
        """
        self._cover = cover

    @property
    def text_list(self):
        r"""Gets the text_list of this ProductBasicInfo.

        文本列表

        :return: The text_list of this ProductBasicInfo.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.ProductTextInfo`]
        """
        return self._text_list

    @text_list.setter
    def text_list(self, text_list):
        r"""Sets the text_list of this ProductBasicInfo.

        文本列表

        :param text_list: The text_list of this ProductBasicInfo.
        :type text_list: list[:class:`huaweicloudsdkmetastudio.v1.ProductTextInfo`]
        """
        self._text_list = text_list

    @property
    def asset_list(self):
        r"""Gets the asset_list of this ProductBasicInfo.

        资产列表,仅支持图片、视频、音频资产

        :return: The asset_list of this ProductBasicInfo.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.ProductMediaInfo`]
        """
        return self._asset_list

    @asset_list.setter
    def asset_list(self, asset_list):
        r"""Sets the asset_list of this ProductBasicInfo.

        资产列表,仅支持图片、视频、音频资产

        :param asset_list: The asset_list of this ProductBasicInfo.
        :type asset_list: list[:class:`huaweicloudsdkmetastudio.v1.ProductMediaInfo`]
        """
        self._asset_list = asset_list

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
        if not isinstance(other, ProductBasicInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
