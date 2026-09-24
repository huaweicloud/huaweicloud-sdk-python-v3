# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PrePaidBillingCreate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cloud_type': 'str',
        'consistent_level': 'str',
        'object_type': 'str',
        'protect_type': 'str',
        'size': 'int',
        'charging_mode': 'str',
        'period_type': 'str',
        'period_num': 'int',
        'is_auto_renew': 'bool',
        'is_auto_pay': 'bool',
        'console_url': 'str',
        'is_multi_az': 'bool',
        'is_double_az': 'bool',
        'promotion_info': 'str',
        'purchase_mode': 'str',
        'order_id': 'str'
    }

    attribute_map = {
        'cloud_type': 'cloud_type',
        'consistent_level': 'consistent_level',
        'object_type': 'object_type',
        'protect_type': 'protect_type',
        'size': 'size',
        'charging_mode': 'charging_mode',
        'period_type': 'period_type',
        'period_num': 'period_num',
        'is_auto_renew': 'is_auto_renew',
        'is_auto_pay': 'is_auto_pay',
        'console_url': 'console_url',
        'is_multi_az': 'is_multi_az',
        'is_double_az': 'is_double_az',
        'promotion_info': 'promotion_info',
        'purchase_mode': 'purchase_mode',
        'order_id': 'order_id'
    }

    def __init__(self, cloud_type=None, consistent_level=None, object_type=None, protect_type=None, size=None, charging_mode=None, period_type=None, period_num=None, is_auto_renew=None, is_auto_pay=None, console_url=None, is_multi_az=None, is_double_az=None, promotion_info=None, purchase_mode=None, order_id=None):
        r"""PrePaidBillingCreate

        The model defined in huaweicloud sdk

        :param cloud_type: 云类型，默认为public，支持类型如下。 [public：公有云; hybrid: 混合云](tag:hws,hws_hk,ctc) [public：公有云](tag:dt,ocb,tlf,sbc,g42,tm,hk_g42)
        :type cloud_type: str
        :param consistent_level: [功能描述：存储库规格。取值范围：app_consistent: 应用一致性，crash_consistent: 崩溃一致性。默认取值不涉及。](tag:hws,hws_hk,fcs_vm,ctc,tm,g42,hk_g42) [功能描述：存储库规格。取值范围：crash_consistent: 崩溃一致性。默认取值不涉及。](tag:dt,ocb,tlf,sbc,hcso_dt)
        :type consistent_level: str
        :param object_type: [对象类型，支持\&quot;server\&quot;, \&quot;disk\&quot;, \&quot;turbo\&quot;, \&quot;workspace\&quot;, \&quot;vmware\&quot;, \&quot;rds\&quot;和\&quot;file\&quot;共七种。server：云服务器，disk：云硬盘，turbo：文件系统，workspace：云桌面，vmware：VMware，rds：关系型数据库，file：文件。默认取值不涉及。](tag:hws,hws_hk) [对象类型，支持\&quot;server\&quot;, \&quot;disk\&quot;和\&quot;turbo\&quot;共三种。server：云服务器，disk：云硬盘，turbo：文件系统。默认取值不涉及。](tag:ctc,fcs_vm,ocb,hk_g42,sbc,hws_ocb) [对象类型，支持\&quot;server\&quot;和\&quot;disk\&quot;共两种。server：云服务器，disk：云硬盘。默认取值不涉及。](tag:dt,tlf,tm,cmcc,hcso_dt) [对象类型，支持\&quot;server\&quot;, \&quot;disk\&quot;, \&quot;turbo\&quot;和\&quot;workspace\&quot;共四种。server：云服务器，disk：云硬盘，turbo：文件系统，workspace：云桌面。默认取值不涉及。](tag:g42)
        :type object_type: str
        :param protect_type: 保护类型，默认取值不涉及。取值范围如下： [backup：备份，replication：复制](tag:hws,hws_hk,ocb,hws_ocb) [backup：备份](tag:tlf,tm,cmcc,fcs_vm,g42,dt,hk_g42,sbc,hcso_dt)
        :type protect_type: str
        :param size: 资源容量大小，单位GB，取值范围：10-10485760，默认取值不涉及。
        :type size: int
        :param charging_mode: 计费模式，仅支持填写pre_paid：代表包年/包月模式
        :type charging_mode: str
        :param period_type: 功能说明：订购周期单位。charging_mode参数为pre_paid时period_type参数会生效，并且period_type参数为必选。默认取值不涉及。 取值范围： - month：月 - year：年
        :type period_type: str
        :param period_num: 功能说明：订购周期数，charging_mode为pre_paid时period_num参数会生效，并且period_num参数为为必选。默认取值不涉及。 取值范围：[1-9]
        :type period_num: int
        :param is_auto_renew: 功能说明：到期后是否自动续期，默认为false 取值范围： - true：到期后自动续期 - false：到期后不自动续期
        :type is_auto_renew: bool
        :param is_auto_pay: 功能说明：是否自动付费，默认为false 取值范围： - true：下单后自动付费 - false：下单后不自动付费
        :type is_auto_pay: bool
        :param console_url: 云服务console_url。 订购订单支付完成后，客户可以通过此URL跳转到云服务Console页面查看信息。（仅手动支付时涉及）。默认取值不涉及。
        :type console_url: str
        :param is_multi_az: 功能说明：存储库是否具有多AZ属性，即底层备份是否为多AZ备份，默认为false 取值范围： - true：存储库具有多AZ属性 - false：存储库不具有多AZ属性
        :type is_multi_az: bool
        :param is_double_az: 功能说明：存储库是否具有融合桶属性，即底层备份是否为融合桶备份，默认为false 取值范围： - true：存储库具有融合桶属性 - false：存储库不具有融合桶属性
        :type is_double_az: bool
        :param promotion_info: 促销信息，包周期时可选参数，取值范围不涉及，默认取值不涉及。
        :type promotion_info: str
        :param purchase_mode: 购买模式，包周期时可选参数，取值范围不涉及，默认取值不涉及。
        :type purchase_mode: str
        :param order_id: 订单 ID，包周期时可选参数，取值范围不涉及，默认取值不涉及。
        :type order_id: str
        """
        
        

        self._cloud_type = None
        self._consistent_level = None
        self._object_type = None
        self._protect_type = None
        self._size = None
        self._charging_mode = None
        self._period_type = None
        self._period_num = None
        self._is_auto_renew = None
        self._is_auto_pay = None
        self._console_url = None
        self._is_multi_az = None
        self._is_double_az = None
        self._promotion_info = None
        self._purchase_mode = None
        self._order_id = None
        self.discriminator = None

        if cloud_type is not None:
            self.cloud_type = cloud_type
        self.consistent_level = consistent_level
        self.object_type = object_type
        self.protect_type = protect_type
        self.size = size
        self.charging_mode = charging_mode
        self.period_type = period_type
        self.period_num = period_num
        if is_auto_renew is not None:
            self.is_auto_renew = is_auto_renew
        if is_auto_pay is not None:
            self.is_auto_pay = is_auto_pay
        if console_url is not None:
            self.console_url = console_url
        if is_multi_az is not None:
            self.is_multi_az = is_multi_az
        if is_double_az is not None:
            self.is_double_az = is_double_az
        if promotion_info is not None:
            self.promotion_info = promotion_info
        if purchase_mode is not None:
            self.purchase_mode = purchase_mode
        if order_id is not None:
            self.order_id = order_id

    @property
    def cloud_type(self):
        r"""Gets the cloud_type of this PrePaidBillingCreate.

        云类型，默认为public，支持类型如下。 [public：公有云; hybrid: 混合云](tag:hws,hws_hk,ctc) [public：公有云](tag:dt,ocb,tlf,sbc,g42,tm,hk_g42)

        :return: The cloud_type of this PrePaidBillingCreate.
        :rtype: str
        """
        return self._cloud_type

    @cloud_type.setter
    def cloud_type(self, cloud_type):
        r"""Sets the cloud_type of this PrePaidBillingCreate.

        云类型，默认为public，支持类型如下。 [public：公有云; hybrid: 混合云](tag:hws,hws_hk,ctc) [public：公有云](tag:dt,ocb,tlf,sbc,g42,tm,hk_g42)

        :param cloud_type: The cloud_type of this PrePaidBillingCreate.
        :type cloud_type: str
        """
        self._cloud_type = cloud_type

    @property
    def consistent_level(self):
        r"""Gets the consistent_level of this PrePaidBillingCreate.

        [功能描述：存储库规格。取值范围：app_consistent: 应用一致性，crash_consistent: 崩溃一致性。默认取值不涉及。](tag:hws,hws_hk,fcs_vm,ctc,tm,g42,hk_g42) [功能描述：存储库规格。取值范围：crash_consistent: 崩溃一致性。默认取值不涉及。](tag:dt,ocb,tlf,sbc,hcso_dt)

        :return: The consistent_level of this PrePaidBillingCreate.
        :rtype: str
        """
        return self._consistent_level

    @consistent_level.setter
    def consistent_level(self, consistent_level):
        r"""Sets the consistent_level of this PrePaidBillingCreate.

        [功能描述：存储库规格。取值范围：app_consistent: 应用一致性，crash_consistent: 崩溃一致性。默认取值不涉及。](tag:hws,hws_hk,fcs_vm,ctc,tm,g42,hk_g42) [功能描述：存储库规格。取值范围：crash_consistent: 崩溃一致性。默认取值不涉及。](tag:dt,ocb,tlf,sbc,hcso_dt)

        :param consistent_level: The consistent_level of this PrePaidBillingCreate.
        :type consistent_level: str
        """
        self._consistent_level = consistent_level

    @property
    def object_type(self):
        r"""Gets the object_type of this PrePaidBillingCreate.

        [对象类型，支持\"server\", \"disk\", \"turbo\", \"workspace\", \"vmware\", \"rds\"和\"file\"共七种。server：云服务器，disk：云硬盘，turbo：文件系统，workspace：云桌面，vmware：VMware，rds：关系型数据库，file：文件。默认取值不涉及。](tag:hws,hws_hk) [对象类型，支持\"server\", \"disk\"和\"turbo\"共三种。server：云服务器，disk：云硬盘，turbo：文件系统。默认取值不涉及。](tag:ctc,fcs_vm,ocb,hk_g42,sbc,hws_ocb) [对象类型，支持\"server\"和\"disk\"共两种。server：云服务器，disk：云硬盘。默认取值不涉及。](tag:dt,tlf,tm,cmcc,hcso_dt) [对象类型，支持\"server\", \"disk\", \"turbo\"和\"workspace\"共四种。server：云服务器，disk：云硬盘，turbo：文件系统，workspace：云桌面。默认取值不涉及。](tag:g42)

        :return: The object_type of this PrePaidBillingCreate.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        r"""Sets the object_type of this PrePaidBillingCreate.

        [对象类型，支持\"server\", \"disk\", \"turbo\", \"workspace\", \"vmware\", \"rds\"和\"file\"共七种。server：云服务器，disk：云硬盘，turbo：文件系统，workspace：云桌面，vmware：VMware，rds：关系型数据库，file：文件。默认取值不涉及。](tag:hws,hws_hk) [对象类型，支持\"server\", \"disk\"和\"turbo\"共三种。server：云服务器，disk：云硬盘，turbo：文件系统。默认取值不涉及。](tag:ctc,fcs_vm,ocb,hk_g42,sbc,hws_ocb) [对象类型，支持\"server\"和\"disk\"共两种。server：云服务器，disk：云硬盘。默认取值不涉及。](tag:dt,tlf,tm,cmcc,hcso_dt) [对象类型，支持\"server\", \"disk\", \"turbo\"和\"workspace\"共四种。server：云服务器，disk：云硬盘，turbo：文件系统，workspace：云桌面。默认取值不涉及。](tag:g42)

        :param object_type: The object_type of this PrePaidBillingCreate.
        :type object_type: str
        """
        self._object_type = object_type

    @property
    def protect_type(self):
        r"""Gets the protect_type of this PrePaidBillingCreate.

        保护类型，默认取值不涉及。取值范围如下： [backup：备份，replication：复制](tag:hws,hws_hk,ocb,hws_ocb) [backup：备份](tag:tlf,tm,cmcc,fcs_vm,g42,dt,hk_g42,sbc,hcso_dt)

        :return: The protect_type of this PrePaidBillingCreate.
        :rtype: str
        """
        return self._protect_type

    @protect_type.setter
    def protect_type(self, protect_type):
        r"""Sets the protect_type of this PrePaidBillingCreate.

        保护类型，默认取值不涉及。取值范围如下： [backup：备份，replication：复制](tag:hws,hws_hk,ocb,hws_ocb) [backup：备份](tag:tlf,tm,cmcc,fcs_vm,g42,dt,hk_g42,sbc,hcso_dt)

        :param protect_type: The protect_type of this PrePaidBillingCreate.
        :type protect_type: str
        """
        self._protect_type = protect_type

    @property
    def size(self):
        r"""Gets the size of this PrePaidBillingCreate.

        资源容量大小，单位GB，取值范围：10-10485760，默认取值不涉及。

        :return: The size of this PrePaidBillingCreate.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this PrePaidBillingCreate.

        资源容量大小，单位GB，取值范围：10-10485760，默认取值不涉及。

        :param size: The size of this PrePaidBillingCreate.
        :type size: int
        """
        self._size = size

    @property
    def charging_mode(self):
        r"""Gets the charging_mode of this PrePaidBillingCreate.

        计费模式，仅支持填写pre_paid：代表包年/包月模式

        :return: The charging_mode of this PrePaidBillingCreate.
        :rtype: str
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        r"""Sets the charging_mode of this PrePaidBillingCreate.

        计费模式，仅支持填写pre_paid：代表包年/包月模式

        :param charging_mode: The charging_mode of this PrePaidBillingCreate.
        :type charging_mode: str
        """
        self._charging_mode = charging_mode

    @property
    def period_type(self):
        r"""Gets the period_type of this PrePaidBillingCreate.

        功能说明：订购周期单位。charging_mode参数为pre_paid时period_type参数会生效，并且period_type参数为必选。默认取值不涉及。 取值范围： - month：月 - year：年

        :return: The period_type of this PrePaidBillingCreate.
        :rtype: str
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        r"""Sets the period_type of this PrePaidBillingCreate.

        功能说明：订购周期单位。charging_mode参数为pre_paid时period_type参数会生效，并且period_type参数为必选。默认取值不涉及。 取值范围： - month：月 - year：年

        :param period_type: The period_type of this PrePaidBillingCreate.
        :type period_type: str
        """
        self._period_type = period_type

    @property
    def period_num(self):
        r"""Gets the period_num of this PrePaidBillingCreate.

        功能说明：订购周期数，charging_mode为pre_paid时period_num参数会生效，并且period_num参数为为必选。默认取值不涉及。 取值范围：[1-9]

        :return: The period_num of this PrePaidBillingCreate.
        :rtype: int
        """
        return self._period_num

    @period_num.setter
    def period_num(self, period_num):
        r"""Sets the period_num of this PrePaidBillingCreate.

        功能说明：订购周期数，charging_mode为pre_paid时period_num参数会生效，并且period_num参数为为必选。默认取值不涉及。 取值范围：[1-9]

        :param period_num: The period_num of this PrePaidBillingCreate.
        :type period_num: int
        """
        self._period_num = period_num

    @property
    def is_auto_renew(self):
        r"""Gets the is_auto_renew of this PrePaidBillingCreate.

        功能说明：到期后是否自动续期，默认为false 取值范围： - true：到期后自动续期 - false：到期后不自动续期

        :return: The is_auto_renew of this PrePaidBillingCreate.
        :rtype: bool
        """
        return self._is_auto_renew

    @is_auto_renew.setter
    def is_auto_renew(self, is_auto_renew):
        r"""Sets the is_auto_renew of this PrePaidBillingCreate.

        功能说明：到期后是否自动续期，默认为false 取值范围： - true：到期后自动续期 - false：到期后不自动续期

        :param is_auto_renew: The is_auto_renew of this PrePaidBillingCreate.
        :type is_auto_renew: bool
        """
        self._is_auto_renew = is_auto_renew

    @property
    def is_auto_pay(self):
        r"""Gets the is_auto_pay of this PrePaidBillingCreate.

        功能说明：是否自动付费，默认为false 取值范围： - true：下单后自动付费 - false：下单后不自动付费

        :return: The is_auto_pay of this PrePaidBillingCreate.
        :rtype: bool
        """
        return self._is_auto_pay

    @is_auto_pay.setter
    def is_auto_pay(self, is_auto_pay):
        r"""Sets the is_auto_pay of this PrePaidBillingCreate.

        功能说明：是否自动付费，默认为false 取值范围： - true：下单后自动付费 - false：下单后不自动付费

        :param is_auto_pay: The is_auto_pay of this PrePaidBillingCreate.
        :type is_auto_pay: bool
        """
        self._is_auto_pay = is_auto_pay

    @property
    def console_url(self):
        r"""Gets the console_url of this PrePaidBillingCreate.

        云服务console_url。 订购订单支付完成后，客户可以通过此URL跳转到云服务Console页面查看信息。（仅手动支付时涉及）。默认取值不涉及。

        :return: The console_url of this PrePaidBillingCreate.
        :rtype: str
        """
        return self._console_url

    @console_url.setter
    def console_url(self, console_url):
        r"""Sets the console_url of this PrePaidBillingCreate.

        云服务console_url。 订购订单支付完成后，客户可以通过此URL跳转到云服务Console页面查看信息。（仅手动支付时涉及）。默认取值不涉及。

        :param console_url: The console_url of this PrePaidBillingCreate.
        :type console_url: str
        """
        self._console_url = console_url

    @property
    def is_multi_az(self):
        r"""Gets the is_multi_az of this PrePaidBillingCreate.

        功能说明：存储库是否具有多AZ属性，即底层备份是否为多AZ备份，默认为false 取值范围： - true：存储库具有多AZ属性 - false：存储库不具有多AZ属性

        :return: The is_multi_az of this PrePaidBillingCreate.
        :rtype: bool
        """
        return self._is_multi_az

    @is_multi_az.setter
    def is_multi_az(self, is_multi_az):
        r"""Sets the is_multi_az of this PrePaidBillingCreate.

        功能说明：存储库是否具有多AZ属性，即底层备份是否为多AZ备份，默认为false 取值范围： - true：存储库具有多AZ属性 - false：存储库不具有多AZ属性

        :param is_multi_az: The is_multi_az of this PrePaidBillingCreate.
        :type is_multi_az: bool
        """
        self._is_multi_az = is_multi_az

    @property
    def is_double_az(self):
        r"""Gets the is_double_az of this PrePaidBillingCreate.

        功能说明：存储库是否具有融合桶属性，即底层备份是否为融合桶备份，默认为false 取值范围： - true：存储库具有融合桶属性 - false：存储库不具有融合桶属性

        :return: The is_double_az of this PrePaidBillingCreate.
        :rtype: bool
        """
        return self._is_double_az

    @is_double_az.setter
    def is_double_az(self, is_double_az):
        r"""Sets the is_double_az of this PrePaidBillingCreate.

        功能说明：存储库是否具有融合桶属性，即底层备份是否为融合桶备份，默认为false 取值范围： - true：存储库具有融合桶属性 - false：存储库不具有融合桶属性

        :param is_double_az: The is_double_az of this PrePaidBillingCreate.
        :type is_double_az: bool
        """
        self._is_double_az = is_double_az

    @property
    def promotion_info(self):
        r"""Gets the promotion_info of this PrePaidBillingCreate.

        促销信息，包周期时可选参数，取值范围不涉及，默认取值不涉及。

        :return: The promotion_info of this PrePaidBillingCreate.
        :rtype: str
        """
        return self._promotion_info

    @promotion_info.setter
    def promotion_info(self, promotion_info):
        r"""Sets the promotion_info of this PrePaidBillingCreate.

        促销信息，包周期时可选参数，取值范围不涉及，默认取值不涉及。

        :param promotion_info: The promotion_info of this PrePaidBillingCreate.
        :type promotion_info: str
        """
        self._promotion_info = promotion_info

    @property
    def purchase_mode(self):
        r"""Gets the purchase_mode of this PrePaidBillingCreate.

        购买模式，包周期时可选参数，取值范围不涉及，默认取值不涉及。

        :return: The purchase_mode of this PrePaidBillingCreate.
        :rtype: str
        """
        return self._purchase_mode

    @purchase_mode.setter
    def purchase_mode(self, purchase_mode):
        r"""Sets the purchase_mode of this PrePaidBillingCreate.

        购买模式，包周期时可选参数，取值范围不涉及，默认取值不涉及。

        :param purchase_mode: The purchase_mode of this PrePaidBillingCreate.
        :type purchase_mode: str
        """
        self._purchase_mode = purchase_mode

    @property
    def order_id(self):
        r"""Gets the order_id of this PrePaidBillingCreate.

        订单 ID，包周期时可选参数，取值范围不涉及，默认取值不涉及。

        :return: The order_id of this PrePaidBillingCreate.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        r"""Sets the order_id of this PrePaidBillingCreate.

        订单 ID，包周期时可选参数，取值范围不涉及，默认取值不涉及。

        :param order_id: The order_id of this PrePaidBillingCreate.
        :type order_id: str
        """
        self._order_id = order_id

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
        if not isinstance(other, PrePaidBillingCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
