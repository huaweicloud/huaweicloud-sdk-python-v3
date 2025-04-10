# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProductMediaDetailInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'asset_id': 'str',
        'asset_type': 'str',
        'order': 'int',
        'asset_name': 'str',
        'asset_state': 'str',
        'cover_url': 'str',
        'thumbnail_url': 'str',
        'main_url': 'str'
    }

    attribute_map = {
        'asset_id': 'asset_id',
        'asset_type': 'asset_type',
        'order': 'order',
        'asset_name': 'asset_name',
        'asset_state': 'asset_state',
        'cover_url': 'cover_url',
        'thumbnail_url': 'thumbnail_url',
        'main_url': 'main_url'
    }

    def __init__(self, asset_id=None, asset_type=None, order=None, asset_name=None, asset_state=None, cover_url=None, thumbnail_url=None, main_url=None):
        r"""ProductMediaDetailInfo

        The model defined in huaweicloud sdk

        :param asset_id: 资产ID
        :type asset_id: str
        :param asset_type: 资产类型 * IMAGE：图片 * VIDEO：视频 * AUDIO：音频
        :type asset_type: str
        :param order: **参数解释**： 资产次序。不设置或者0表示按照加入时间先后排序。业务上将次序最靠前的图片设置为商品封面。
        :type order: int
        :param asset_name: 资产名称。
        :type asset_name: str
        :param asset_state: 资产状态。
        :type asset_state: str
        :param cover_url: 封面图片路径。
        :type cover_url: str
        :param thumbnail_url: 缩略图路径。
        :type thumbnail_url: str
        :param main_url: 缩略图路径。
        :type main_url: str
        """
        
        

        self._asset_id = None
        self._asset_type = None
        self._order = None
        self._asset_name = None
        self._asset_state = None
        self._cover_url = None
        self._thumbnail_url = None
        self._main_url = None
        self.discriminator = None

        if asset_id is not None:
            self.asset_id = asset_id
        if asset_type is not None:
            self.asset_type = asset_type
        if order is not None:
            self.order = order
        if asset_name is not None:
            self.asset_name = asset_name
        if asset_state is not None:
            self.asset_state = asset_state
        if cover_url is not None:
            self.cover_url = cover_url
        if thumbnail_url is not None:
            self.thumbnail_url = thumbnail_url
        if main_url is not None:
            self.main_url = main_url

    @property
    def asset_id(self):
        r"""Gets the asset_id of this ProductMediaDetailInfo.

        资产ID

        :return: The asset_id of this ProductMediaDetailInfo.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        r"""Sets the asset_id of this ProductMediaDetailInfo.

        资产ID

        :param asset_id: The asset_id of this ProductMediaDetailInfo.
        :type asset_id: str
        """
        self._asset_id = asset_id

    @property
    def asset_type(self):
        r"""Gets the asset_type of this ProductMediaDetailInfo.

        资产类型 * IMAGE：图片 * VIDEO：视频 * AUDIO：音频

        :return: The asset_type of this ProductMediaDetailInfo.
        :rtype: str
        """
        return self._asset_type

    @asset_type.setter
    def asset_type(self, asset_type):
        r"""Sets the asset_type of this ProductMediaDetailInfo.

        资产类型 * IMAGE：图片 * VIDEO：视频 * AUDIO：音频

        :param asset_type: The asset_type of this ProductMediaDetailInfo.
        :type asset_type: str
        """
        self._asset_type = asset_type

    @property
    def order(self):
        r"""Gets the order of this ProductMediaDetailInfo.

        **参数解释**： 资产次序。不设置或者0表示按照加入时间先后排序。业务上将次序最靠前的图片设置为商品封面。

        :return: The order of this ProductMediaDetailInfo.
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this ProductMediaDetailInfo.

        **参数解释**： 资产次序。不设置或者0表示按照加入时间先后排序。业务上将次序最靠前的图片设置为商品封面。

        :param order: The order of this ProductMediaDetailInfo.
        :type order: int
        """
        self._order = order

    @property
    def asset_name(self):
        r"""Gets the asset_name of this ProductMediaDetailInfo.

        资产名称。

        :return: The asset_name of this ProductMediaDetailInfo.
        :rtype: str
        """
        return self._asset_name

    @asset_name.setter
    def asset_name(self, asset_name):
        r"""Sets the asset_name of this ProductMediaDetailInfo.

        资产名称。

        :param asset_name: The asset_name of this ProductMediaDetailInfo.
        :type asset_name: str
        """
        self._asset_name = asset_name

    @property
    def asset_state(self):
        r"""Gets the asset_state of this ProductMediaDetailInfo.

        资产状态。

        :return: The asset_state of this ProductMediaDetailInfo.
        :rtype: str
        """
        return self._asset_state

    @asset_state.setter
    def asset_state(self, asset_state):
        r"""Sets the asset_state of this ProductMediaDetailInfo.

        资产状态。

        :param asset_state: The asset_state of this ProductMediaDetailInfo.
        :type asset_state: str
        """
        self._asset_state = asset_state

    @property
    def cover_url(self):
        r"""Gets the cover_url of this ProductMediaDetailInfo.

        封面图片路径。

        :return: The cover_url of this ProductMediaDetailInfo.
        :rtype: str
        """
        return self._cover_url

    @cover_url.setter
    def cover_url(self, cover_url):
        r"""Sets the cover_url of this ProductMediaDetailInfo.

        封面图片路径。

        :param cover_url: The cover_url of this ProductMediaDetailInfo.
        :type cover_url: str
        """
        self._cover_url = cover_url

    @property
    def thumbnail_url(self):
        r"""Gets the thumbnail_url of this ProductMediaDetailInfo.

        缩略图路径。

        :return: The thumbnail_url of this ProductMediaDetailInfo.
        :rtype: str
        """
        return self._thumbnail_url

    @thumbnail_url.setter
    def thumbnail_url(self, thumbnail_url):
        r"""Sets the thumbnail_url of this ProductMediaDetailInfo.

        缩略图路径。

        :param thumbnail_url: The thumbnail_url of this ProductMediaDetailInfo.
        :type thumbnail_url: str
        """
        self._thumbnail_url = thumbnail_url

    @property
    def main_url(self):
        r"""Gets the main_url of this ProductMediaDetailInfo.

        缩略图路径。

        :return: The main_url of this ProductMediaDetailInfo.
        :rtype: str
        """
        return self._main_url

    @main_url.setter
    def main_url(self, main_url):
        r"""Sets the main_url of this ProductMediaDetailInfo.

        缩略图路径。

        :param main_url: The main_url of this ProductMediaDetailInfo.
        :type main_url: str
        """
        self._main_url = main_url

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
        if not isinstance(other, ProductMediaDetailInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
