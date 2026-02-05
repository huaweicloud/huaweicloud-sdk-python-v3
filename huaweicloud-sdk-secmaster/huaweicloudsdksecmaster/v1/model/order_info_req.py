# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OrderInfoReq:

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
        'promotion_info': 'str',
        'operate_type': 'str',
        'tag_list': 'list[SubscriptionTag]',
        'product_list': 'list[Product]',
        'config': 'OrderConfig',
        'period_type': 'int',
        'period_num': 'int',
        'is_auto_renew': 'int'
    }

    attribute_map = {
        'scene': 'scene',
        'promotion_info': 'promotion_info',
        'operate_type': 'operate_type',
        'tag_list': 'tag_list',
        'product_list': 'product_list',
        'config': 'config',
        'period_type': 'period_type',
        'period_num': 'period_num',
        'is_auto_renew': 'is_auto_renew'
    }

    def __init__(self, scene=None, promotion_info=None, operate_type=None, tag_list=None, product_list=None, config=None, period_type=None, period_num=None, is_auto_renew=None):
        r"""OrderInfoReq

        The model defined in huaweicloud sdk

        :param scene: 场景描述，执行包年包月(PREPAID)、按需(POSTPAID)开通，或者配置资源（CONFIG）用量，缺省值：PREPAID，大小写不敏感
        :type scene: str
        :param promotion_info: 促销折扣信息 String，JSON格式
        :type promotion_info: str
        :param operate_type: 操作类型，比如创建场景为：CREATE、订单用量预警配置为：ALERT_CONFIG，大小写不敏感
        :type operate_type: str
        :param tag_list: 计费标签
        :type tag_list: list[:class:`huaweicloudsdksecmaster.v1.SubscriptionTag`]
        :param product_list: 当scene&#x3D;PREPAID 或者 POSTPAID时，当前字段必填 商品列表
        :type product_list: list[:class:`huaweicloudsdksecmaster.v1.Product`]
        :param config: 
        :type config: :class:`huaweicloudsdksecmaster.v1.OrderConfig`
        :param period_type: 当scene&#x3D;PREPAID时需要填写，订阅周期类型： 2：月； 3：年；
        :type period_type: int
        :param period_num: 订阅周期数，当scene&#x3D;PREPAID时需要填写该值 取值大于0；小于等于0会报错。 当period_type&#x3D;2时，其可选范围为[1, 9]，当period_type&#x3D;3，其可选范围为[1, 3]
        :type period_num: int
        :param is_auto_renew: 当scene&#x3D;PREPAID时，当前字段必填，是否自动续订，为空时表示不自动续订； 1：自动续订 0：不自动续订（默认）
        :type is_auto_renew: int
        """
        
        

        self._scene = None
        self._promotion_info = None
        self._operate_type = None
        self._tag_list = None
        self._product_list = None
        self._config = None
        self._period_type = None
        self._period_num = None
        self._is_auto_renew = None
        self.discriminator = None

        self.scene = scene
        if promotion_info is not None:
            self.promotion_info = promotion_info
        self.operate_type = operate_type
        if tag_list is not None:
            self.tag_list = tag_list
        if product_list is not None:
            self.product_list = product_list
        if config is not None:
            self.config = config
        if period_type is not None:
            self.period_type = period_type
        if period_num is not None:
            self.period_num = period_num
        if is_auto_renew is not None:
            self.is_auto_renew = is_auto_renew

    @property
    def scene(self):
        r"""Gets the scene of this OrderInfoReq.

        场景描述，执行包年包月(PREPAID)、按需(POSTPAID)开通，或者配置资源（CONFIG）用量，缺省值：PREPAID，大小写不敏感

        :return: The scene of this OrderInfoReq.
        :rtype: str
        """
        return self._scene

    @scene.setter
    def scene(self, scene):
        r"""Sets the scene of this OrderInfoReq.

        场景描述，执行包年包月(PREPAID)、按需(POSTPAID)开通，或者配置资源（CONFIG）用量，缺省值：PREPAID，大小写不敏感

        :param scene: The scene of this OrderInfoReq.
        :type scene: str
        """
        self._scene = scene

    @property
    def promotion_info(self):
        r"""Gets the promotion_info of this OrderInfoReq.

        促销折扣信息 String，JSON格式

        :return: The promotion_info of this OrderInfoReq.
        :rtype: str
        """
        return self._promotion_info

    @promotion_info.setter
    def promotion_info(self, promotion_info):
        r"""Sets the promotion_info of this OrderInfoReq.

        促销折扣信息 String，JSON格式

        :param promotion_info: The promotion_info of this OrderInfoReq.
        :type promotion_info: str
        """
        self._promotion_info = promotion_info

    @property
    def operate_type(self):
        r"""Gets the operate_type of this OrderInfoReq.

        操作类型，比如创建场景为：CREATE、订单用量预警配置为：ALERT_CONFIG，大小写不敏感

        :return: The operate_type of this OrderInfoReq.
        :rtype: str
        """
        return self._operate_type

    @operate_type.setter
    def operate_type(self, operate_type):
        r"""Sets the operate_type of this OrderInfoReq.

        操作类型，比如创建场景为：CREATE、订单用量预警配置为：ALERT_CONFIG，大小写不敏感

        :param operate_type: The operate_type of this OrderInfoReq.
        :type operate_type: str
        """
        self._operate_type = operate_type

    @property
    def tag_list(self):
        r"""Gets the tag_list of this OrderInfoReq.

        计费标签

        :return: The tag_list of this OrderInfoReq.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.SubscriptionTag`]
        """
        return self._tag_list

    @tag_list.setter
    def tag_list(self, tag_list):
        r"""Sets the tag_list of this OrderInfoReq.

        计费标签

        :param tag_list: The tag_list of this OrderInfoReq.
        :type tag_list: list[:class:`huaweicloudsdksecmaster.v1.SubscriptionTag`]
        """
        self._tag_list = tag_list

    @property
    def product_list(self):
        r"""Gets the product_list of this OrderInfoReq.

        当scene=PREPAID 或者 POSTPAID时，当前字段必填 商品列表

        :return: The product_list of this OrderInfoReq.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.Product`]
        """
        return self._product_list

    @product_list.setter
    def product_list(self, product_list):
        r"""Sets the product_list of this OrderInfoReq.

        当scene=PREPAID 或者 POSTPAID时，当前字段必填 商品列表

        :param product_list: The product_list of this OrderInfoReq.
        :type product_list: list[:class:`huaweicloudsdksecmaster.v1.Product`]
        """
        self._product_list = product_list

    @property
    def config(self):
        r"""Gets the config of this OrderInfoReq.

        :return: The config of this OrderInfoReq.
        :rtype: :class:`huaweicloudsdksecmaster.v1.OrderConfig`
        """
        return self._config

    @config.setter
    def config(self, config):
        r"""Sets the config of this OrderInfoReq.

        :param config: The config of this OrderInfoReq.
        :type config: :class:`huaweicloudsdksecmaster.v1.OrderConfig`
        """
        self._config = config

    @property
    def period_type(self):
        r"""Gets the period_type of this OrderInfoReq.

        当scene=PREPAID时需要填写，订阅周期类型： 2：月； 3：年；

        :return: The period_type of this OrderInfoReq.
        :rtype: int
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        r"""Sets the period_type of this OrderInfoReq.

        当scene=PREPAID时需要填写，订阅周期类型： 2：月； 3：年；

        :param period_type: The period_type of this OrderInfoReq.
        :type period_type: int
        """
        self._period_type = period_type

    @property
    def period_num(self):
        r"""Gets the period_num of this OrderInfoReq.

        订阅周期数，当scene=PREPAID时需要填写该值 取值大于0；小于等于0会报错。 当period_type=2时，其可选范围为[1, 9]，当period_type=3，其可选范围为[1, 3]

        :return: The period_num of this OrderInfoReq.
        :rtype: int
        """
        return self._period_num

    @period_num.setter
    def period_num(self, period_num):
        r"""Sets the period_num of this OrderInfoReq.

        订阅周期数，当scene=PREPAID时需要填写该值 取值大于0；小于等于0会报错。 当period_type=2时，其可选范围为[1, 9]，当period_type=3，其可选范围为[1, 3]

        :param period_num: The period_num of this OrderInfoReq.
        :type period_num: int
        """
        self._period_num = period_num

    @property
    def is_auto_renew(self):
        r"""Gets the is_auto_renew of this OrderInfoReq.

        当scene=PREPAID时，当前字段必填，是否自动续订，为空时表示不自动续订； 1：自动续订 0：不自动续订（默认）

        :return: The is_auto_renew of this OrderInfoReq.
        :rtype: int
        """
        return self._is_auto_renew

    @is_auto_renew.setter
    def is_auto_renew(self, is_auto_renew):
        r"""Sets the is_auto_renew of this OrderInfoReq.

        当scene=PREPAID时，当前字段必填，是否自动续订，为空时表示不自动续订； 1：自动续订 0：不自动续订（默认）

        :param is_auto_renew: The is_auto_renew of this OrderInfoReq.
        :type is_auto_renew: int
        """
        self._is_auto_renew = is_auto_renew

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
        if not isinstance(other, OrderInfoReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
