# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateGeoipRuleResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'policyid': 'str',
        'geoip': 'str',
        'white': 'int',
        'status': 'int',
        'ip_type': 'str',
        'description': 'str',
        'timestamp': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'policyid': 'policyid',
        'geoip': 'geoip',
        'white': 'white',
        'status': 'status',
        'ip_type': 'ip_type',
        'description': 'description',
        'timestamp': 'timestamp'
    }

    def __init__(self, id=None, name=None, policyid=None, geoip=None, white=None, status=None, ip_type=None, description=None, timestamp=None):
        r"""CreateGeoipRuleResponse

        The model defined in huaweicloud sdk

        :param id: 规则id
        :type id: str
        :param name: 地理位置控制规则名称
        :type name: str
        :param policyid: 策略id
        :type policyid: str
        :param geoip: 地理位置封禁区域： (CN： 中国,,CA： 加拿大,US： 美国,AU： 澳大利亚,IN： 印度,JP： 日本,UK： 英国,FR： 法国,DE： 德国,BR： 巴西,Ukraine： 乌克兰,North Korea： 朝鲜,The Republic of Korea： 韩国,Iran： 伊朗,Cuba： 古巴,Sultan： 苏丹,Syria： 叙利亚,Pakistan： 巴基斯坦,Palestine： 巴勒斯坦,Israel： 以色列,Iraq： 伊拉克,Afghanistan： 阿富汗,Libya： 利比亚,Turkey： 土耳其,Thailand： 泰国,Singapore： 新加坡,South Africa： 南非,Mexico： 墨西哥,Peru： 秘鲁,Indonesia： 印度尼西亚,GD： 广东,FJ： 福建,JL： 吉林,LN： 辽宁,TW： 台湾,GZ： 贵州,AH： 安徽,HL： 黑龙江,HA： 河南,SC： 四川,HE： 河北,YN： 云南,HB： 湖北,HI： 海南,QH： 青海,HN： 湖南,JX： 江西,SX： 山西,SN： 陕西,ZJ： 浙江,GS： 甘肃,JS： 江苏,SD： 山东,BJ： 北京,SH： 上海,TJ： 天津,CQ： 重庆,MO： 澳门,HK： 香港,NX： 宁夏,GX： 广西,XJ： 新疆,XZ： 西藏,NM： 内蒙古)
        :type geoip: str
        :param white: 防护动作：  - 0 拦截  - 1 放行  - 2 仅记录
        :type white: int
        :param status: **参数解释：** 规则状态标识，用于指定规则的启用或关闭状态 **约束限制：** 不涉及 **取值范围：**  - 0：关闭  - 1：开启 **默认取值：** 不涉及
        :type status: int
        :param ip_type: ip范围。若您的网站使用独享模式，请确认独享引擎是否全部升级到最新版本，避免造成异常。202412之后的版本支持配置IP范围
        :type ip_type: str
        :param description: 规则描述
        :type description: str
        :param timestamp: 创建规则时间戳
        :type timestamp: int
        """
        
        super().__init__()

        self._id = None
        self._name = None
        self._policyid = None
        self._geoip = None
        self._white = None
        self._status = None
        self._ip_type = None
        self._description = None
        self._timestamp = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if policyid is not None:
            self.policyid = policyid
        if geoip is not None:
            self.geoip = geoip
        if white is not None:
            self.white = white
        if status is not None:
            self.status = status
        if ip_type is not None:
            self.ip_type = ip_type
        if description is not None:
            self.description = description
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def id(self):
        r"""Gets the id of this CreateGeoipRuleResponse.

        规则id

        :return: The id of this CreateGeoipRuleResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CreateGeoipRuleResponse.

        规则id

        :param id: The id of this CreateGeoipRuleResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this CreateGeoipRuleResponse.

        地理位置控制规则名称

        :return: The name of this CreateGeoipRuleResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateGeoipRuleResponse.

        地理位置控制规则名称

        :param name: The name of this CreateGeoipRuleResponse.
        :type name: str
        """
        self._name = name

    @property
    def policyid(self):
        r"""Gets the policyid of this CreateGeoipRuleResponse.

        策略id

        :return: The policyid of this CreateGeoipRuleResponse.
        :rtype: str
        """
        return self._policyid

    @policyid.setter
    def policyid(self, policyid):
        r"""Sets the policyid of this CreateGeoipRuleResponse.

        策略id

        :param policyid: The policyid of this CreateGeoipRuleResponse.
        :type policyid: str
        """
        self._policyid = policyid

    @property
    def geoip(self):
        r"""Gets the geoip of this CreateGeoipRuleResponse.

        地理位置封禁区域： (CN： 中国,,CA： 加拿大,US： 美国,AU： 澳大利亚,IN： 印度,JP： 日本,UK： 英国,FR： 法国,DE： 德国,BR： 巴西,Ukraine： 乌克兰,North Korea： 朝鲜,The Republic of Korea： 韩国,Iran： 伊朗,Cuba： 古巴,Sultan： 苏丹,Syria： 叙利亚,Pakistan： 巴基斯坦,Palestine： 巴勒斯坦,Israel： 以色列,Iraq： 伊拉克,Afghanistan： 阿富汗,Libya： 利比亚,Turkey： 土耳其,Thailand： 泰国,Singapore： 新加坡,South Africa： 南非,Mexico： 墨西哥,Peru： 秘鲁,Indonesia： 印度尼西亚,GD： 广东,FJ： 福建,JL： 吉林,LN： 辽宁,TW： 台湾,GZ： 贵州,AH： 安徽,HL： 黑龙江,HA： 河南,SC： 四川,HE： 河北,YN： 云南,HB： 湖北,HI： 海南,QH： 青海,HN： 湖南,JX： 江西,SX： 山西,SN： 陕西,ZJ： 浙江,GS： 甘肃,JS： 江苏,SD： 山东,BJ： 北京,SH： 上海,TJ： 天津,CQ： 重庆,MO： 澳门,HK： 香港,NX： 宁夏,GX： 广西,XJ： 新疆,XZ： 西藏,NM： 内蒙古)

        :return: The geoip of this CreateGeoipRuleResponse.
        :rtype: str
        """
        return self._geoip

    @geoip.setter
    def geoip(self, geoip):
        r"""Sets the geoip of this CreateGeoipRuleResponse.

        地理位置封禁区域： (CN： 中国,,CA： 加拿大,US： 美国,AU： 澳大利亚,IN： 印度,JP： 日本,UK： 英国,FR： 法国,DE： 德国,BR： 巴西,Ukraine： 乌克兰,North Korea： 朝鲜,The Republic of Korea： 韩国,Iran： 伊朗,Cuba： 古巴,Sultan： 苏丹,Syria： 叙利亚,Pakistan： 巴基斯坦,Palestine： 巴勒斯坦,Israel： 以色列,Iraq： 伊拉克,Afghanistan： 阿富汗,Libya： 利比亚,Turkey： 土耳其,Thailand： 泰国,Singapore： 新加坡,South Africa： 南非,Mexico： 墨西哥,Peru： 秘鲁,Indonesia： 印度尼西亚,GD： 广东,FJ： 福建,JL： 吉林,LN： 辽宁,TW： 台湾,GZ： 贵州,AH： 安徽,HL： 黑龙江,HA： 河南,SC： 四川,HE： 河北,YN： 云南,HB： 湖北,HI： 海南,QH： 青海,HN： 湖南,JX： 江西,SX： 山西,SN： 陕西,ZJ： 浙江,GS： 甘肃,JS： 江苏,SD： 山东,BJ： 北京,SH： 上海,TJ： 天津,CQ： 重庆,MO： 澳门,HK： 香港,NX： 宁夏,GX： 广西,XJ： 新疆,XZ： 西藏,NM： 内蒙古)

        :param geoip: The geoip of this CreateGeoipRuleResponse.
        :type geoip: str
        """
        self._geoip = geoip

    @property
    def white(self):
        r"""Gets the white of this CreateGeoipRuleResponse.

        防护动作：  - 0 拦截  - 1 放行  - 2 仅记录

        :return: The white of this CreateGeoipRuleResponse.
        :rtype: int
        """
        return self._white

    @white.setter
    def white(self, white):
        r"""Sets the white of this CreateGeoipRuleResponse.

        防护动作：  - 0 拦截  - 1 放行  - 2 仅记录

        :param white: The white of this CreateGeoipRuleResponse.
        :type white: int
        """
        self._white = white

    @property
    def status(self):
        r"""Gets the status of this CreateGeoipRuleResponse.

        **参数解释：** 规则状态标识，用于指定规则的启用或关闭状态 **约束限制：** 不涉及 **取值范围：**  - 0：关闭  - 1：开启 **默认取值：** 不涉及

        :return: The status of this CreateGeoipRuleResponse.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CreateGeoipRuleResponse.

        **参数解释：** 规则状态标识，用于指定规则的启用或关闭状态 **约束限制：** 不涉及 **取值范围：**  - 0：关闭  - 1：开启 **默认取值：** 不涉及

        :param status: The status of this CreateGeoipRuleResponse.
        :type status: int
        """
        self._status = status

    @property
    def ip_type(self):
        r"""Gets the ip_type of this CreateGeoipRuleResponse.

        ip范围。若您的网站使用独享模式，请确认独享引擎是否全部升级到最新版本，避免造成异常。202412之后的版本支持配置IP范围

        :return: The ip_type of this CreateGeoipRuleResponse.
        :rtype: str
        """
        return self._ip_type

    @ip_type.setter
    def ip_type(self, ip_type):
        r"""Sets the ip_type of this CreateGeoipRuleResponse.

        ip范围。若您的网站使用独享模式，请确认独享引擎是否全部升级到最新版本，避免造成异常。202412之后的版本支持配置IP范围

        :param ip_type: The ip_type of this CreateGeoipRuleResponse.
        :type ip_type: str
        """
        self._ip_type = ip_type

    @property
    def description(self):
        r"""Gets the description of this CreateGeoipRuleResponse.

        规则描述

        :return: The description of this CreateGeoipRuleResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateGeoipRuleResponse.

        规则描述

        :param description: The description of this CreateGeoipRuleResponse.
        :type description: str
        """
        self._description = description

    @property
    def timestamp(self):
        r"""Gets the timestamp of this CreateGeoipRuleResponse.

        创建规则时间戳

        :return: The timestamp of this CreateGeoipRuleResponse.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        r"""Sets the timestamp of this CreateGeoipRuleResponse.

        创建规则时间戳

        :param timestamp: The timestamp of this CreateGeoipRuleResponse.
        :type timestamp: int
        """
        self._timestamp = timestamp

    def to_dict(self):
        import warnings
        warnings.warn("CreateGeoipRuleResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, CreateGeoipRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
