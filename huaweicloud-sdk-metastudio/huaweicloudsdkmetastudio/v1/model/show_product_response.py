# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowProductResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'product_id': 'str',
        'name': 'str',
        'description': 'str',
        'tags': 'list[str]',
        'cover': 'ProductCoverDetailInfo',
        'text_list': 'list[ProductTextInfo]',
        'asset_list': 'list[ProductMediaDetailInfo]',
        'create_time': 'str',
        'update_time': 'str',
        'state': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'product_id': 'product_id',
        'name': 'name',
        'description': 'description',
        'tags': 'tags',
        'cover': 'cover',
        'text_list': 'text_list',
        'asset_list': 'asset_list',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'state': 'state',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, product_id=None, name=None, description=None, tags=None, cover=None, text_list=None, asset_list=None, create_time=None, update_time=None, state=None, x_request_id=None):
        r"""ShowProductResponse

        The model defined in huaweicloud sdk

        :param product_id: 商品ID
        :type product_id: str
        :param name: 商品名称
        :type name: str
        :param description: 商品描述
        :type description: str
        :param tags: 标签。单个标签16字节，多个用逗号分隔，最多50个。
        :type tags: list[str]
        :param cover: 
        :type cover: :class:`huaweicloudsdkmetastudio.v1.ProductCoverDetailInfo`
        :param text_list: 文本列表
        :type text_list: list[:class:`huaweicloudsdkmetastudio.v1.ProductTextInfo`]
        :param asset_list: 资产列表,仅支持图片、视频、音频资产
        :type asset_list: list[:class:`huaweicloudsdkmetastudio.v1.ProductMediaDetailInfo`]
        :param create_time: 商品创建时间，格式遵循：RFC 3339。 例 “2020-07-30T10:43:17Z”。
        :type create_time: str
        :param update_time: 商品更新时间，格式遵循：RFC 3339。 例 “2020-07-30T10:43:17Z”。
        :type update_time: str
        :param state: 商品状态枚举 * ACTIVED：已激活 * UNACTIVED：未激活 * BLOCK: 被冻结，商品不可用 * DELETED：已删除
        :type state: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ShowProductResponse, self).__init__()

        self._product_id = None
        self._name = None
        self._description = None
        self._tags = None
        self._cover = None
        self._text_list = None
        self._asset_list = None
        self._create_time = None
        self._update_time = None
        self._state = None
        self._x_request_id = None
        self.discriminator = None

        if product_id is not None:
            self.product_id = product_id
        if name is not None:
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
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if state is not None:
            self.state = state
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def product_id(self):
        r"""Gets the product_id of this ShowProductResponse.

        商品ID

        :return: The product_id of this ShowProductResponse.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this ShowProductResponse.

        商品ID

        :param product_id: The product_id of this ShowProductResponse.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def name(self):
        r"""Gets the name of this ShowProductResponse.

        商品名称

        :return: The name of this ShowProductResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowProductResponse.

        商品名称

        :param name: The name of this ShowProductResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ShowProductResponse.

        商品描述

        :return: The description of this ShowProductResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowProductResponse.

        商品描述

        :param description: The description of this ShowProductResponse.
        :type description: str
        """
        self._description = description

    @property
    def tags(self):
        r"""Gets the tags of this ShowProductResponse.

        标签。单个标签16字节，多个用逗号分隔，最多50个。

        :return: The tags of this ShowProductResponse.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ShowProductResponse.

        标签。单个标签16字节，多个用逗号分隔，最多50个。

        :param tags: The tags of this ShowProductResponse.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def cover(self):
        r"""Gets the cover of this ShowProductResponse.

        :return: The cover of this ShowProductResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ProductCoverDetailInfo`
        """
        return self._cover

    @cover.setter
    def cover(self, cover):
        r"""Sets the cover of this ShowProductResponse.

        :param cover: The cover of this ShowProductResponse.
        :type cover: :class:`huaweicloudsdkmetastudio.v1.ProductCoverDetailInfo`
        """
        self._cover = cover

    @property
    def text_list(self):
        r"""Gets the text_list of this ShowProductResponse.

        文本列表

        :return: The text_list of this ShowProductResponse.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.ProductTextInfo`]
        """
        return self._text_list

    @text_list.setter
    def text_list(self, text_list):
        r"""Sets the text_list of this ShowProductResponse.

        文本列表

        :param text_list: The text_list of this ShowProductResponse.
        :type text_list: list[:class:`huaweicloudsdkmetastudio.v1.ProductTextInfo`]
        """
        self._text_list = text_list

    @property
    def asset_list(self):
        r"""Gets the asset_list of this ShowProductResponse.

        资产列表,仅支持图片、视频、音频资产

        :return: The asset_list of this ShowProductResponse.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.ProductMediaDetailInfo`]
        """
        return self._asset_list

    @asset_list.setter
    def asset_list(self, asset_list):
        r"""Sets the asset_list of this ShowProductResponse.

        资产列表,仅支持图片、视频、音频资产

        :param asset_list: The asset_list of this ShowProductResponse.
        :type asset_list: list[:class:`huaweicloudsdkmetastudio.v1.ProductMediaDetailInfo`]
        """
        self._asset_list = asset_list

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowProductResponse.

        商品创建时间，格式遵循：RFC 3339。 例 “2020-07-30T10:43:17Z”。

        :return: The create_time of this ShowProductResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowProductResponse.

        商品创建时间，格式遵循：RFC 3339。 例 “2020-07-30T10:43:17Z”。

        :param create_time: The create_time of this ShowProductResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ShowProductResponse.

        商品更新时间，格式遵循：RFC 3339。 例 “2020-07-30T10:43:17Z”。

        :return: The update_time of this ShowProductResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ShowProductResponse.

        商品更新时间，格式遵循：RFC 3339。 例 “2020-07-30T10:43:17Z”。

        :param update_time: The update_time of this ShowProductResponse.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def state(self):
        r"""Gets the state of this ShowProductResponse.

        商品状态枚举 * ACTIVED：已激活 * UNACTIVED：未激活 * BLOCK: 被冻结，商品不可用 * DELETED：已删除

        :return: The state of this ShowProductResponse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ShowProductResponse.

        商品状态枚举 * ACTIVED：已激活 * UNACTIVED：未激活 * BLOCK: 被冻结，商品不可用 * DELETED：已删除

        :param state: The state of this ShowProductResponse.
        :type state: str
        """
        self._state = state

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ShowProductResponse.

        :return: The x_request_id of this ShowProductResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ShowProductResponse.

        :param x_request_id: The x_request_id of this ShowProductResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ShowProductResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
