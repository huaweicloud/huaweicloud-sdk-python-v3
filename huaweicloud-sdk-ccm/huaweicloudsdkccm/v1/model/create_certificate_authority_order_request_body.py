# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateCertificateAuthorityOrderRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cloud_service_type': 'str',
        'charging_mode': 'int',
        'period_type': 'int',
        'period_num': 'int',
        'is_auto_renew': 'int',
        'promotion_info': 'str',
        'subscription_num': 'int',
        'is_auto_pay': 'int',
        'enterprise_project_id': 'str',
        'product_infos': 'list[ProductInfo]'
    }

    attribute_map = {
        'cloud_service_type': 'cloud_service_type',
        'charging_mode': 'charging_mode',
        'period_type': 'period_type',
        'period_num': 'period_num',
        'is_auto_renew': 'is_auto_renew',
        'promotion_info': 'promotion_info',
        'subscription_num': 'subscription_num',
        'is_auto_pay': 'is_auto_pay',
        'enterprise_project_id': 'enterprise_project_id',
        'product_infos': 'product_infos'
    }

    def __init__(self, cloud_service_type=None, charging_mode=None, period_type=None, period_num=None, is_auto_renew=None, promotion_info=None, subscription_num=None, is_auto_pay=None, enterprise_project_id=None, product_infos=None):
        """CreateCertificateAuthorityOrderRequestBody

        The model defined in huaweicloud sdk

        :param cloud_service_type: 云服务类型，固定为&#39;hws.service.type.ccm&#39;
        :type cloud_service_type: str
        :param charging_mode: 计费模式 0包周期
        :type charging_mode: int
        :param period_type: 订购周期 2月 3年
        :type period_type: int
        :param period_num: 订购周期数
        :type period_num: int
        :param is_auto_renew: 是否自动续费 1是 0否
        :type is_auto_renew: int
        :param promotion_info: 折扣信息
        :type promotion_info: str
        :param subscription_num: 订购数量
        :type subscription_num: int
        :param is_auto_pay: 是否自动支付 1是 0否 不填默认为0
        :type is_auto_pay: int
        :param enterprise_project_id: 企业项目ID
        :type enterprise_project_id: str
        :param product_infos: 产品列表，详情请参见**ProductInfo**字段数据结构说明。
        :type product_infos: list[:class:`huaweicloudsdkccm.v1.ProductInfo`]
        """
        
        

        self._cloud_service_type = None
        self._charging_mode = None
        self._period_type = None
        self._period_num = None
        self._is_auto_renew = None
        self._promotion_info = None
        self._subscription_num = None
        self._is_auto_pay = None
        self._enterprise_project_id = None
        self._product_infos = None
        self.discriminator = None

        self.cloud_service_type = cloud_service_type
        self.charging_mode = charging_mode
        self.period_type = period_type
        self.period_num = period_num
        self.is_auto_renew = is_auto_renew
        if promotion_info is not None:
            self.promotion_info = promotion_info
        self.subscription_num = subscription_num
        if is_auto_pay is not None:
            self.is_auto_pay = is_auto_pay
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.product_infos = product_infos

    @property
    def cloud_service_type(self):
        """Gets the cloud_service_type of this CreateCertificateAuthorityOrderRequestBody.

        云服务类型，固定为'hws.service.type.ccm'

        :return: The cloud_service_type of this CreateCertificateAuthorityOrderRequestBody.
        :rtype: str
        """
        return self._cloud_service_type

    @cloud_service_type.setter
    def cloud_service_type(self, cloud_service_type):
        """Sets the cloud_service_type of this CreateCertificateAuthorityOrderRequestBody.

        云服务类型，固定为'hws.service.type.ccm'

        :param cloud_service_type: The cloud_service_type of this CreateCertificateAuthorityOrderRequestBody.
        :type cloud_service_type: str
        """
        self._cloud_service_type = cloud_service_type

    @property
    def charging_mode(self):
        """Gets the charging_mode of this CreateCertificateAuthorityOrderRequestBody.

        计费模式 0包周期

        :return: The charging_mode of this CreateCertificateAuthorityOrderRequestBody.
        :rtype: int
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        """Sets the charging_mode of this CreateCertificateAuthorityOrderRequestBody.

        计费模式 0包周期

        :param charging_mode: The charging_mode of this CreateCertificateAuthorityOrderRequestBody.
        :type charging_mode: int
        """
        self._charging_mode = charging_mode

    @property
    def period_type(self):
        """Gets the period_type of this CreateCertificateAuthorityOrderRequestBody.

        订购周期 2月 3年

        :return: The period_type of this CreateCertificateAuthorityOrderRequestBody.
        :rtype: int
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        """Sets the period_type of this CreateCertificateAuthorityOrderRequestBody.

        订购周期 2月 3年

        :param period_type: The period_type of this CreateCertificateAuthorityOrderRequestBody.
        :type period_type: int
        """
        self._period_type = period_type

    @property
    def period_num(self):
        """Gets the period_num of this CreateCertificateAuthorityOrderRequestBody.

        订购周期数

        :return: The period_num of this CreateCertificateAuthorityOrderRequestBody.
        :rtype: int
        """
        return self._period_num

    @period_num.setter
    def period_num(self, period_num):
        """Sets the period_num of this CreateCertificateAuthorityOrderRequestBody.

        订购周期数

        :param period_num: The period_num of this CreateCertificateAuthorityOrderRequestBody.
        :type period_num: int
        """
        self._period_num = period_num

    @property
    def is_auto_renew(self):
        """Gets the is_auto_renew of this CreateCertificateAuthorityOrderRequestBody.

        是否自动续费 1是 0否

        :return: The is_auto_renew of this CreateCertificateAuthorityOrderRequestBody.
        :rtype: int
        """
        return self._is_auto_renew

    @is_auto_renew.setter
    def is_auto_renew(self, is_auto_renew):
        """Sets the is_auto_renew of this CreateCertificateAuthorityOrderRequestBody.

        是否自动续费 1是 0否

        :param is_auto_renew: The is_auto_renew of this CreateCertificateAuthorityOrderRequestBody.
        :type is_auto_renew: int
        """
        self._is_auto_renew = is_auto_renew

    @property
    def promotion_info(self):
        """Gets the promotion_info of this CreateCertificateAuthorityOrderRequestBody.

        折扣信息

        :return: The promotion_info of this CreateCertificateAuthorityOrderRequestBody.
        :rtype: str
        """
        return self._promotion_info

    @promotion_info.setter
    def promotion_info(self, promotion_info):
        """Sets the promotion_info of this CreateCertificateAuthorityOrderRequestBody.

        折扣信息

        :param promotion_info: The promotion_info of this CreateCertificateAuthorityOrderRequestBody.
        :type promotion_info: str
        """
        self._promotion_info = promotion_info

    @property
    def subscription_num(self):
        """Gets the subscription_num of this CreateCertificateAuthorityOrderRequestBody.

        订购数量

        :return: The subscription_num of this CreateCertificateAuthorityOrderRequestBody.
        :rtype: int
        """
        return self._subscription_num

    @subscription_num.setter
    def subscription_num(self, subscription_num):
        """Sets the subscription_num of this CreateCertificateAuthorityOrderRequestBody.

        订购数量

        :param subscription_num: The subscription_num of this CreateCertificateAuthorityOrderRequestBody.
        :type subscription_num: int
        """
        self._subscription_num = subscription_num

    @property
    def is_auto_pay(self):
        """Gets the is_auto_pay of this CreateCertificateAuthorityOrderRequestBody.

        是否自动支付 1是 0否 不填默认为0

        :return: The is_auto_pay of this CreateCertificateAuthorityOrderRequestBody.
        :rtype: int
        """
        return self._is_auto_pay

    @is_auto_pay.setter
    def is_auto_pay(self, is_auto_pay):
        """Sets the is_auto_pay of this CreateCertificateAuthorityOrderRequestBody.

        是否自动支付 1是 0否 不填默认为0

        :param is_auto_pay: The is_auto_pay of this CreateCertificateAuthorityOrderRequestBody.
        :type is_auto_pay: int
        """
        self._is_auto_pay = is_auto_pay

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CreateCertificateAuthorityOrderRequestBody.

        企业项目ID

        :return: The enterprise_project_id of this CreateCertificateAuthorityOrderRequestBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CreateCertificateAuthorityOrderRequestBody.

        企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this CreateCertificateAuthorityOrderRequestBody.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def product_infos(self):
        """Gets the product_infos of this CreateCertificateAuthorityOrderRequestBody.

        产品列表，详情请参见**ProductInfo**字段数据结构说明。

        :return: The product_infos of this CreateCertificateAuthorityOrderRequestBody.
        :rtype: list[:class:`huaweicloudsdkccm.v1.ProductInfo`]
        """
        return self._product_infos

    @product_infos.setter
    def product_infos(self, product_infos):
        """Sets the product_infos of this CreateCertificateAuthorityOrderRequestBody.

        产品列表，详情请参见**ProductInfo**字段数据结构说明。

        :param product_infos: The product_infos of this CreateCertificateAuthorityOrderRequestBody.
        :type product_infos: list[:class:`huaweicloudsdkccm.v1.ProductInfo`]
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
        if not isinstance(other, CreateCertificateAuthorityOrderRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
