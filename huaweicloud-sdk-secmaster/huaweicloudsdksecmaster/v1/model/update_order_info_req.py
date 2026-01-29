# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateOrderInfoReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'scene': 'str',
        'operate_type': 'str',
        'promotion_info': 'str',
        'tag_list': 'list[SubscriptionTag]',
        'product_list': 'list[UpdateProduct]'
    }

    attribute_map = {
        'scene': 'scene',
        'operate_type': 'operate_type',
        'promotion_info': 'promotion_info',
        'tag_list': 'tag_list',
        'product_list': 'product_list'
    }

    def __init__(self, scene=None, operate_type=None, promotion_info=None, tag_list=None, product_list=None):
        r"""UpdateOrderInfoReq

        The model defined in huaweicloud sdk

        :param scene: 操作场景，包周期场景：PREPAID 或者 按需场景：POSTPAID
        :type scene: str
        :param operate_type: 按需或者包周期场景下，要进行的操作类型 比如增减配额，规格升降配，按需转包周期 规格升级：UPGRADE，配额增加：ADDITION，配额减少：DECREASE，按需转包周期：POSTPAID_2_PREPAID 注：目前不支持规格降级，比如不支持从专业版降级为标准版或基础版
        :type operate_type: str
        :param promotion_info: 促销折扣信息
        :type promotion_info: str
        :param tag_list: 计费标签
        :type tag_list: list[:class:`huaweicloudsdksecmaster.v1.SubscriptionTag`]
        :param product_list: 要进行变更的商品列表
        :type product_list: list[:class:`huaweicloudsdksecmaster.v1.UpdateProduct`]
        """
        
        

        self._scene = None
        self._operate_type = None
        self._promotion_info = None
        self._tag_list = None
        self._product_list = None
        self.discriminator = None

        self.scene = scene
        self.operate_type = operate_type
        if promotion_info is not None:
            self.promotion_info = promotion_info
        if tag_list is not None:
            self.tag_list = tag_list
        if product_list is not None:
            self.product_list = product_list

    @property
    def scene(self):
        r"""Gets the scene of this UpdateOrderInfoReq.

        操作场景，包周期场景：PREPAID 或者 按需场景：POSTPAID

        :return: The scene of this UpdateOrderInfoReq.
        :rtype: str
        """
        return self._scene

    @scene.setter
    def scene(self, scene):
        r"""Sets the scene of this UpdateOrderInfoReq.

        操作场景，包周期场景：PREPAID 或者 按需场景：POSTPAID

        :param scene: The scene of this UpdateOrderInfoReq.
        :type scene: str
        """
        self._scene = scene

    @property
    def operate_type(self):
        r"""Gets the operate_type of this UpdateOrderInfoReq.

        按需或者包周期场景下，要进行的操作类型 比如增减配额，规格升降配，按需转包周期 规格升级：UPGRADE，配额增加：ADDITION，配额减少：DECREASE，按需转包周期：POSTPAID_2_PREPAID 注：目前不支持规格降级，比如不支持从专业版降级为标准版或基础版

        :return: The operate_type of this UpdateOrderInfoReq.
        :rtype: str
        """
        return self._operate_type

    @operate_type.setter
    def operate_type(self, operate_type):
        r"""Sets the operate_type of this UpdateOrderInfoReq.

        按需或者包周期场景下，要进行的操作类型 比如增减配额，规格升降配，按需转包周期 规格升级：UPGRADE，配额增加：ADDITION，配额减少：DECREASE，按需转包周期：POSTPAID_2_PREPAID 注：目前不支持规格降级，比如不支持从专业版降级为标准版或基础版

        :param operate_type: The operate_type of this UpdateOrderInfoReq.
        :type operate_type: str
        """
        self._operate_type = operate_type

    @property
    def promotion_info(self):
        r"""Gets the promotion_info of this UpdateOrderInfoReq.

        促销折扣信息

        :return: The promotion_info of this UpdateOrderInfoReq.
        :rtype: str
        """
        return self._promotion_info

    @promotion_info.setter
    def promotion_info(self, promotion_info):
        r"""Sets the promotion_info of this UpdateOrderInfoReq.

        促销折扣信息

        :param promotion_info: The promotion_info of this UpdateOrderInfoReq.
        :type promotion_info: str
        """
        self._promotion_info = promotion_info

    @property
    def tag_list(self):
        r"""Gets the tag_list of this UpdateOrderInfoReq.

        计费标签

        :return: The tag_list of this UpdateOrderInfoReq.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.SubscriptionTag`]
        """
        return self._tag_list

    @tag_list.setter
    def tag_list(self, tag_list):
        r"""Sets the tag_list of this UpdateOrderInfoReq.

        计费标签

        :param tag_list: The tag_list of this UpdateOrderInfoReq.
        :type tag_list: list[:class:`huaweicloudsdksecmaster.v1.SubscriptionTag`]
        """
        self._tag_list = tag_list

    @property
    def product_list(self):
        r"""Gets the product_list of this UpdateOrderInfoReq.

        要进行变更的商品列表

        :return: The product_list of this UpdateOrderInfoReq.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.UpdateProduct`]
        """
        return self._product_list

    @product_list.setter
    def product_list(self, product_list):
        r"""Sets the product_list of this UpdateOrderInfoReq.

        要进行变更的商品列表

        :param product_list: The product_list of this UpdateOrderInfoReq.
        :type product_list: list[:class:`huaweicloudsdksecmaster.v1.UpdateProduct`]
        """
        self._product_list = product_list

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
        if not isinstance(other, UpdateOrderInfoReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
