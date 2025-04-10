# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateCbcOrderRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'charging_mode': 'int',
        'is_auto_renew': 'int',
        'is_auto_pay': 'int',
        'period_num': 'int',
        'period_type': 'int',
        'cloud_service_type': 'str',
        'project_id': 'str',
        'promotion_info': 'str',
        'region_id': 'str',
        'product_infos': 'list[ProductInfo]'
    }

    attribute_map = {
        'charging_mode': 'charging_mode',
        'is_auto_renew': 'is_auto_renew',
        'is_auto_pay': 'is_auto_pay',
        'period_num': 'period_num',
        'period_type': 'period_type',
        'cloud_service_type': 'cloud_service_type',
        'project_id': 'project_id',
        'promotion_info': 'promotion_info',
        'region_id': 'region_id',
        'product_infos': 'product_infos'
    }

    def __init__(self, charging_mode=None, is_auto_renew=None, is_auto_pay=None, period_num=None, period_type=None, cloud_service_type=None, project_id=None, promotion_info=None, region_id=None, product_infos=None):
        r"""CreateCbcOrderRequestBody

        The model defined in huaweicloud sdk

        :param charging_mode: 计费模式： 0：一次性计费（默认值，对应包年包月） 10：RI
        :type charging_mode: int
        :param is_auto_renew: 0：不自动续订 1：自动续订
        :type is_auto_renew: int
        :param is_auto_pay: 该请求参数为预留参数，当前不支持自动支付，使用接口时该参数请使用0 0：不自动支付 1：自动支付
        :type is_auto_pay: int
        :param period_num: period_num
        :type period_num: int
        :param period_type: 订购周期类型： 2：月； 3：年； 4：包小时（仅限带宽加油包购买场景使用） 5：绝对时间；（追加附属资源场景使用，比如主机上追加云硬盘） 6：一次性（chargingMode&#x3D;1 一次性计费场景使用）
        :type period_type: int
        :param cloud_service_type: 用户购买的云服务的主云服务类型
        :type cloud_service_type: str
        :param project_id: project_id
        :type project_id: str
        :param promotion_info: promotion_info
        :type promotion_info: str
        :param region_id: Region标识，填region编码如\&quot;cn-north-1\&quot;，对于global服务，此处固定填写虚拟的Global regionCode(global-cbc-1)
        :type region_id: str
        :param product_infos: product_infos
        :type product_infos: list[:class:`huaweicloudsdkcodeartsinspector.v2.ProductInfo`]
        """
        
        

        self._charging_mode = None
        self._is_auto_renew = None
        self._is_auto_pay = None
        self._period_num = None
        self._period_type = None
        self._cloud_service_type = None
        self._project_id = None
        self._promotion_info = None
        self._region_id = None
        self._product_infos = None
        self.discriminator = None

        self.charging_mode = charging_mode
        self.is_auto_renew = is_auto_renew
        self.is_auto_pay = is_auto_pay
        if period_num is not None:
            self.period_num = period_num
        self.period_type = period_type
        self.cloud_service_type = cloud_service_type
        self.project_id = project_id
        if promotion_info is not None:
            self.promotion_info = promotion_info
        self.region_id = region_id
        self.product_infos = product_infos

    @property
    def charging_mode(self):
        r"""Gets the charging_mode of this CreateCbcOrderRequestBody.

        计费模式： 0：一次性计费（默认值，对应包年包月） 10：RI

        :return: The charging_mode of this CreateCbcOrderRequestBody.
        :rtype: int
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        r"""Sets the charging_mode of this CreateCbcOrderRequestBody.

        计费模式： 0：一次性计费（默认值，对应包年包月） 10：RI

        :param charging_mode: The charging_mode of this CreateCbcOrderRequestBody.
        :type charging_mode: int
        """
        self._charging_mode = charging_mode

    @property
    def is_auto_renew(self):
        r"""Gets the is_auto_renew of this CreateCbcOrderRequestBody.

        0：不自动续订 1：自动续订

        :return: The is_auto_renew of this CreateCbcOrderRequestBody.
        :rtype: int
        """
        return self._is_auto_renew

    @is_auto_renew.setter
    def is_auto_renew(self, is_auto_renew):
        r"""Sets the is_auto_renew of this CreateCbcOrderRequestBody.

        0：不自动续订 1：自动续订

        :param is_auto_renew: The is_auto_renew of this CreateCbcOrderRequestBody.
        :type is_auto_renew: int
        """
        self._is_auto_renew = is_auto_renew

    @property
    def is_auto_pay(self):
        r"""Gets the is_auto_pay of this CreateCbcOrderRequestBody.

        该请求参数为预留参数，当前不支持自动支付，使用接口时该参数请使用0 0：不自动支付 1：自动支付

        :return: The is_auto_pay of this CreateCbcOrderRequestBody.
        :rtype: int
        """
        return self._is_auto_pay

    @is_auto_pay.setter
    def is_auto_pay(self, is_auto_pay):
        r"""Sets the is_auto_pay of this CreateCbcOrderRequestBody.

        该请求参数为预留参数，当前不支持自动支付，使用接口时该参数请使用0 0：不自动支付 1：自动支付

        :param is_auto_pay: The is_auto_pay of this CreateCbcOrderRequestBody.
        :type is_auto_pay: int
        """
        self._is_auto_pay = is_auto_pay

    @property
    def period_num(self):
        r"""Gets the period_num of this CreateCbcOrderRequestBody.

        period_num

        :return: The period_num of this CreateCbcOrderRequestBody.
        :rtype: int
        """
        return self._period_num

    @period_num.setter
    def period_num(self, period_num):
        r"""Sets the period_num of this CreateCbcOrderRequestBody.

        period_num

        :param period_num: The period_num of this CreateCbcOrderRequestBody.
        :type period_num: int
        """
        self._period_num = period_num

    @property
    def period_type(self):
        r"""Gets the period_type of this CreateCbcOrderRequestBody.

        订购周期类型： 2：月； 3：年； 4：包小时（仅限带宽加油包购买场景使用） 5：绝对时间；（追加附属资源场景使用，比如主机上追加云硬盘） 6：一次性（chargingMode=1 一次性计费场景使用）

        :return: The period_type of this CreateCbcOrderRequestBody.
        :rtype: int
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        r"""Sets the period_type of this CreateCbcOrderRequestBody.

        订购周期类型： 2：月； 3：年； 4：包小时（仅限带宽加油包购买场景使用） 5：绝对时间；（追加附属资源场景使用，比如主机上追加云硬盘） 6：一次性（chargingMode=1 一次性计费场景使用）

        :param period_type: The period_type of this CreateCbcOrderRequestBody.
        :type period_type: int
        """
        self._period_type = period_type

    @property
    def cloud_service_type(self):
        r"""Gets the cloud_service_type of this CreateCbcOrderRequestBody.

        用户购买的云服务的主云服务类型

        :return: The cloud_service_type of this CreateCbcOrderRequestBody.
        :rtype: str
        """
        return self._cloud_service_type

    @cloud_service_type.setter
    def cloud_service_type(self, cloud_service_type):
        r"""Sets the cloud_service_type of this CreateCbcOrderRequestBody.

        用户购买的云服务的主云服务类型

        :param cloud_service_type: The cloud_service_type of this CreateCbcOrderRequestBody.
        :type cloud_service_type: str
        """
        self._cloud_service_type = cloud_service_type

    @property
    def project_id(self):
        r"""Gets the project_id of this CreateCbcOrderRequestBody.

        project_id

        :return: The project_id of this CreateCbcOrderRequestBody.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this CreateCbcOrderRequestBody.

        project_id

        :param project_id: The project_id of this CreateCbcOrderRequestBody.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def promotion_info(self):
        r"""Gets the promotion_info of this CreateCbcOrderRequestBody.

        promotion_info

        :return: The promotion_info of this CreateCbcOrderRequestBody.
        :rtype: str
        """
        return self._promotion_info

    @promotion_info.setter
    def promotion_info(self, promotion_info):
        r"""Sets the promotion_info of this CreateCbcOrderRequestBody.

        promotion_info

        :param promotion_info: The promotion_info of this CreateCbcOrderRequestBody.
        :type promotion_info: str
        """
        self._promotion_info = promotion_info

    @property
    def region_id(self):
        r"""Gets the region_id of this CreateCbcOrderRequestBody.

        Region标识，填region编码如\"cn-north-1\"，对于global服务，此处固定填写虚拟的Global regionCode(global-cbc-1)

        :return: The region_id of this CreateCbcOrderRequestBody.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this CreateCbcOrderRequestBody.

        Region标识，填region编码如\"cn-north-1\"，对于global服务，此处固定填写虚拟的Global regionCode(global-cbc-1)

        :param region_id: The region_id of this CreateCbcOrderRequestBody.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def product_infos(self):
        r"""Gets the product_infos of this CreateCbcOrderRequestBody.

        product_infos

        :return: The product_infos of this CreateCbcOrderRequestBody.
        :rtype: list[:class:`huaweicloudsdkcodeartsinspector.v2.ProductInfo`]
        """
        return self._product_infos

    @product_infos.setter
    def product_infos(self, product_infos):
        r"""Sets the product_infos of this CreateCbcOrderRequestBody.

        product_infos

        :param product_infos: The product_infos of this CreateCbcOrderRequestBody.
        :type product_infos: list[:class:`huaweicloudsdkcodeartsinspector.v2.ProductInfo`]
        """
        self._product_infos = product_infos

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
        if not isinstance(other, CreateCbcOrderRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
