# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PostPaidServerExtendParam:

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
        'region_id': 'str',
        'support_auto_recovery': 'bool',
        'enterprise_project_id': 'str',
        'market_type': 'str',
        'spot_price': 'str',
        'disk_prior': 'str',
        'spot_duration_hours': 'int',
        'interruption_policy': 'str',
        'spot_duration_count': 'int',
        'cb_csbs_backup': 'str'
    }

    attribute_map = {
        'charging_mode': 'chargingMode',
        'region_id': 'regionID',
        'support_auto_recovery': 'support_auto_recovery',
        'enterprise_project_id': 'enterprise_project_id',
        'market_type': 'marketType',
        'spot_price': 'spotPrice',
        'disk_prior': 'diskPrior',
        'spot_duration_hours': 'spot_duration_hours',
        'interruption_policy': 'interruption_policy',
        'spot_duration_count': 'spot_duration_count',
        'cb_csbs_backup': 'CB_CSBS_BACKUP'
    }

    def __init__(self, charging_mode=None, region_id=None, support_auto_recovery=None, enterprise_project_id=None, market_type=None, spot_price=None, disk_prior=None, spot_duration_hours=None, interruption_policy=None, spot_duration_count=None, cb_csbs_backup=None):
        """PostPaidServerExtendParam

        The model defined in huaweicloud sdk

        :param charging_mode: 计费模式：  - 0：按需计费。
        :type charging_mode: int
        :param region_id: 云服务器所在区域ID。  请参考[地区和终端节点](https://developer.huaweicloud.com/endpoint)获取。
        :type region_id: str
        :param support_auto_recovery: 是否配置弹性云服务器自动恢复的功能。  - “true”：配置该功能 - “false”：不配置该功能  &gt; 说明： &gt;  &gt; 此参数为boolean类型，若传入非boolean类型字符，程序将按照【“false”：不配置该功能】方式处理。 &gt;  &gt; 当marketType为spot时，不支持该功能。
        :type support_auto_recovery: bool
        :param enterprise_project_id: 企业项目ID。  &gt; 说明： &gt;  &gt; 关于企业项目ID的获取及企业项目特性的详细信息，请参见《[企业管理服务用户指南](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0126101490.html)》。 &gt;  &gt; 该字段不传（或传为字符串“0”），则将资源绑定给默认企业项目。
        :type enterprise_project_id: str
        :param market_type: 创建竞价实例时，需指定该参数的值为“spot”。  &gt; 说明： &gt;  &gt; 当chargingMode&#x3D;0时且marketType&#x3D;spot时此参数生效。
        :type market_type: str
        :param spot_price: 用户愿意为竞价实例每小时支付的最高价格。  &gt; 说明： &gt;  &gt; 仅chargingMode&#x3D;0且marketType&#x3D;spot时，该参数设置后生效。 &gt;  &gt; 当chargingMode&#x3D;0且marketType&#x3D;spot时，如果不传递spotPrice，默认使用按需购买的价格作为竞价。
        :type spot_price: str
        :param disk_prior: 是否支持先创建卷，再创建虚拟机。  “true”：配置该功能 “false”：不配置该功能
        :type disk_prior: str
        :param spot_duration_hours: 购买的竞价实例时长。  - 仅interruption_policy&#x3D;immediate 时该字段有效 。 - pot_duration_hours大于0。最大值由预测系统给出可以从flavor的extra_specs的cond:spot_block:operation:longest_duration_hours字段中查询。
        :type spot_duration_hours: int
        :param interruption_policy: 竞价实例中断策略，当前支持immediate。  - 当interruption_policy&#x3D;immediate时表示释放策略为立即释放。 
        :type interruption_policy: str
        :param spot_duration_count: 表示购买的“竞价实例时长”的个数。  - 仅spot_duration_hours&gt;0 时该字段有效。 - spot_duration_hours小于6时，spot_duration_count值必须为1。 - spot_duration_hours等于6时，spot_duration_count大于等于1。  spot_duration_count的最大值由预测系统给出可以从flavor的extra_specs的cond:spot_block:operation:longest_duration_count字段中查询。
        :type spot_duration_count: int
        :param cb_csbs_backup: 云备份策略和云备份存储库详情，取值包含备份策略ID和云备份存储库ID。
        :type cb_csbs_backup: str
        """
        
        

        self._charging_mode = None
        self._region_id = None
        self._support_auto_recovery = None
        self._enterprise_project_id = None
        self._market_type = None
        self._spot_price = None
        self._disk_prior = None
        self._spot_duration_hours = None
        self._interruption_policy = None
        self._spot_duration_count = None
        self._cb_csbs_backup = None
        self.discriminator = None

        if charging_mode is not None:
            self.charging_mode = charging_mode
        if region_id is not None:
            self.region_id = region_id
        if support_auto_recovery is not None:
            self.support_auto_recovery = support_auto_recovery
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if market_type is not None:
            self.market_type = market_type
        if spot_price is not None:
            self.spot_price = spot_price
        if disk_prior is not None:
            self.disk_prior = disk_prior
        if spot_duration_hours is not None:
            self.spot_duration_hours = spot_duration_hours
        if interruption_policy is not None:
            self.interruption_policy = interruption_policy
        if spot_duration_count is not None:
            self.spot_duration_count = spot_duration_count
        if cb_csbs_backup is not None:
            self.cb_csbs_backup = cb_csbs_backup

    @property
    def charging_mode(self):
        """Gets the charging_mode of this PostPaidServerExtendParam.

        计费模式：  - 0：按需计费。

        :return: The charging_mode of this PostPaidServerExtendParam.
        :rtype: int
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        """Sets the charging_mode of this PostPaidServerExtendParam.

        计费模式：  - 0：按需计费。

        :param charging_mode: The charging_mode of this PostPaidServerExtendParam.
        :type charging_mode: int
        """
        self._charging_mode = charging_mode

    @property
    def region_id(self):
        """Gets the region_id of this PostPaidServerExtendParam.

        云服务器所在区域ID。  请参考[地区和终端节点](https://developer.huaweicloud.com/endpoint)获取。

        :return: The region_id of this PostPaidServerExtendParam.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this PostPaidServerExtendParam.

        云服务器所在区域ID。  请参考[地区和终端节点](https://developer.huaweicloud.com/endpoint)获取。

        :param region_id: The region_id of this PostPaidServerExtendParam.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def support_auto_recovery(self):
        """Gets the support_auto_recovery of this PostPaidServerExtendParam.

        是否配置弹性云服务器自动恢复的功能。  - “true”：配置该功能 - “false”：不配置该功能  > 说明： >  > 此参数为boolean类型，若传入非boolean类型字符，程序将按照【“false”：不配置该功能】方式处理。 >  > 当marketType为spot时，不支持该功能。

        :return: The support_auto_recovery of this PostPaidServerExtendParam.
        :rtype: bool
        """
        return self._support_auto_recovery

    @support_auto_recovery.setter
    def support_auto_recovery(self, support_auto_recovery):
        """Sets the support_auto_recovery of this PostPaidServerExtendParam.

        是否配置弹性云服务器自动恢复的功能。  - “true”：配置该功能 - “false”：不配置该功能  > 说明： >  > 此参数为boolean类型，若传入非boolean类型字符，程序将按照【“false”：不配置该功能】方式处理。 >  > 当marketType为spot时，不支持该功能。

        :param support_auto_recovery: The support_auto_recovery of this PostPaidServerExtendParam.
        :type support_auto_recovery: bool
        """
        self._support_auto_recovery = support_auto_recovery

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this PostPaidServerExtendParam.

        企业项目ID。  > 说明： >  > 关于企业项目ID的获取及企业项目特性的详细信息，请参见《[企业管理服务用户指南](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0126101490.html)》。 >  > 该字段不传（或传为字符串“0”），则将资源绑定给默认企业项目。

        :return: The enterprise_project_id of this PostPaidServerExtendParam.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this PostPaidServerExtendParam.

        企业项目ID。  > 说明： >  > 关于企业项目ID的获取及企业项目特性的详细信息，请参见《[企业管理服务用户指南](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0126101490.html)》。 >  > 该字段不传（或传为字符串“0”），则将资源绑定给默认企业项目。

        :param enterprise_project_id: The enterprise_project_id of this PostPaidServerExtendParam.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def market_type(self):
        """Gets the market_type of this PostPaidServerExtendParam.

        创建竞价实例时，需指定该参数的值为“spot”。  > 说明： >  > 当chargingMode=0时且marketType=spot时此参数生效。

        :return: The market_type of this PostPaidServerExtendParam.
        :rtype: str
        """
        return self._market_type

    @market_type.setter
    def market_type(self, market_type):
        """Sets the market_type of this PostPaidServerExtendParam.

        创建竞价实例时，需指定该参数的值为“spot”。  > 说明： >  > 当chargingMode=0时且marketType=spot时此参数生效。

        :param market_type: The market_type of this PostPaidServerExtendParam.
        :type market_type: str
        """
        self._market_type = market_type

    @property
    def spot_price(self):
        """Gets the spot_price of this PostPaidServerExtendParam.

        用户愿意为竞价实例每小时支付的最高价格。  > 说明： >  > 仅chargingMode=0且marketType=spot时，该参数设置后生效。 >  > 当chargingMode=0且marketType=spot时，如果不传递spotPrice，默认使用按需购买的价格作为竞价。

        :return: The spot_price of this PostPaidServerExtendParam.
        :rtype: str
        """
        return self._spot_price

    @spot_price.setter
    def spot_price(self, spot_price):
        """Sets the spot_price of this PostPaidServerExtendParam.

        用户愿意为竞价实例每小时支付的最高价格。  > 说明： >  > 仅chargingMode=0且marketType=spot时，该参数设置后生效。 >  > 当chargingMode=0且marketType=spot时，如果不传递spotPrice，默认使用按需购买的价格作为竞价。

        :param spot_price: The spot_price of this PostPaidServerExtendParam.
        :type spot_price: str
        """
        self._spot_price = spot_price

    @property
    def disk_prior(self):
        """Gets the disk_prior of this PostPaidServerExtendParam.

        是否支持先创建卷，再创建虚拟机。  “true”：配置该功能 “false”：不配置该功能

        :return: The disk_prior of this PostPaidServerExtendParam.
        :rtype: str
        """
        return self._disk_prior

    @disk_prior.setter
    def disk_prior(self, disk_prior):
        """Sets the disk_prior of this PostPaidServerExtendParam.

        是否支持先创建卷，再创建虚拟机。  “true”：配置该功能 “false”：不配置该功能

        :param disk_prior: The disk_prior of this PostPaidServerExtendParam.
        :type disk_prior: str
        """
        self._disk_prior = disk_prior

    @property
    def spot_duration_hours(self):
        """Gets the spot_duration_hours of this PostPaidServerExtendParam.

        购买的竞价实例时长。  - 仅interruption_policy=immediate 时该字段有效 。 - pot_duration_hours大于0。最大值由预测系统给出可以从flavor的extra_specs的cond:spot_block:operation:longest_duration_hours字段中查询。

        :return: The spot_duration_hours of this PostPaidServerExtendParam.
        :rtype: int
        """
        return self._spot_duration_hours

    @spot_duration_hours.setter
    def spot_duration_hours(self, spot_duration_hours):
        """Sets the spot_duration_hours of this PostPaidServerExtendParam.

        购买的竞价实例时长。  - 仅interruption_policy=immediate 时该字段有效 。 - pot_duration_hours大于0。最大值由预测系统给出可以从flavor的extra_specs的cond:spot_block:operation:longest_duration_hours字段中查询。

        :param spot_duration_hours: The spot_duration_hours of this PostPaidServerExtendParam.
        :type spot_duration_hours: int
        """
        self._spot_duration_hours = spot_duration_hours

    @property
    def interruption_policy(self):
        """Gets the interruption_policy of this PostPaidServerExtendParam.

        竞价实例中断策略，当前支持immediate。  - 当interruption_policy=immediate时表示释放策略为立即释放。 

        :return: The interruption_policy of this PostPaidServerExtendParam.
        :rtype: str
        """
        return self._interruption_policy

    @interruption_policy.setter
    def interruption_policy(self, interruption_policy):
        """Sets the interruption_policy of this PostPaidServerExtendParam.

        竞价实例中断策略，当前支持immediate。  - 当interruption_policy=immediate时表示释放策略为立即释放。 

        :param interruption_policy: The interruption_policy of this PostPaidServerExtendParam.
        :type interruption_policy: str
        """
        self._interruption_policy = interruption_policy

    @property
    def spot_duration_count(self):
        """Gets the spot_duration_count of this PostPaidServerExtendParam.

        表示购买的“竞价实例时长”的个数。  - 仅spot_duration_hours>0 时该字段有效。 - spot_duration_hours小于6时，spot_duration_count值必须为1。 - spot_duration_hours等于6时，spot_duration_count大于等于1。  spot_duration_count的最大值由预测系统给出可以从flavor的extra_specs的cond:spot_block:operation:longest_duration_count字段中查询。

        :return: The spot_duration_count of this PostPaidServerExtendParam.
        :rtype: int
        """
        return self._spot_duration_count

    @spot_duration_count.setter
    def spot_duration_count(self, spot_duration_count):
        """Sets the spot_duration_count of this PostPaidServerExtendParam.

        表示购买的“竞价实例时长”的个数。  - 仅spot_duration_hours>0 时该字段有效。 - spot_duration_hours小于6时，spot_duration_count值必须为1。 - spot_duration_hours等于6时，spot_duration_count大于等于1。  spot_duration_count的最大值由预测系统给出可以从flavor的extra_specs的cond:spot_block:operation:longest_duration_count字段中查询。

        :param spot_duration_count: The spot_duration_count of this PostPaidServerExtendParam.
        :type spot_duration_count: int
        """
        self._spot_duration_count = spot_duration_count

    @property
    def cb_csbs_backup(self):
        """Gets the cb_csbs_backup of this PostPaidServerExtendParam.

        云备份策略和云备份存储库详情，取值包含备份策略ID和云备份存储库ID。

        :return: The cb_csbs_backup of this PostPaidServerExtendParam.
        :rtype: str
        """
        return self._cb_csbs_backup

    @cb_csbs_backup.setter
    def cb_csbs_backup(self, cb_csbs_backup):
        """Sets the cb_csbs_backup of this PostPaidServerExtendParam.

        云备份策略和云备份存储库详情，取值包含备份策略ID和云备份存储库ID。

        :param cb_csbs_backup: The cb_csbs_backup of this PostPaidServerExtendParam.
        :type cb_csbs_backup: str
        """
        self._cb_csbs_backup = cb_csbs_backup

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
        if not isinstance(other, PostPaidServerExtendParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
