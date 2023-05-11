# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateGeoipRuleRequestBody:

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
        'geoip': 'str',
        'white': 'int'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'geoip': 'geoip',
        'white': 'white'
    }

    def __init__(self, name=None, description=None, geoip=None, white=None):
        """UpdateGeoipRuleRequestBody

        The model defined in huaweicloud sdk

        :param name: 地理位置控制规则名称
        :type name: str
        :param description: 描述
        :type description: str
        :param geoip: 地理位置封禁区域，选择区域对应的字母代号： (CN： 中国,CA： 加拿大,US： 美国,AU： 澳大利亚,IN： 印度,JP： 日本,UK： 英国,FR： 法国,DE： 德国,BR： 巴西,Ukraine： 乌克兰,North Korea： 朝鲜,The Republic of Korea： 韩国,Iran： 伊朗,Cuba： 古巴,Sultan： 苏丹,Syria： 叙利亚,Pakistan： 巴基斯坦,Palestine： 巴勒斯坦,Israel： 以色列,Iraq： 伊拉克,Afghanistan： 阿富汗,Libya： 利比亚,Turkey： 土耳其,Thailand： 泰国,Singapore： 新加坡,South Africa： 南非,Mexico： 墨西哥,Peru： 秘鲁,Indonesia： 印度尼西亚,GD： 广东,FJ： 福建,JL： 吉林,LN： 辽宁,TW： 台湾,GZ： 贵州,AH： 安徽,HL： 黑龙江,HA： 河南,SC： 四川,HE： 河北,YN： 云南,HB： 湖北,HI： 海南,QH： 青海,HN： 湖南,JX： 江西,SX： 山西,SN： 陕西,ZJ： 浙江,GS： 甘肃,JS： 江苏,SD： 山东,BJ： 北京,SH： 上海,TJ： 天津,CQ： 重庆,MO： 澳门,HK： 香港,NX： 宁夏,GX： 广西,XJ： 新疆,XZ： 西藏,NM： 内蒙古)
        :type geoip: str
        :param white: 防护动作：  - 0 拦截  - 1 放行  - 2 仅记录
        :type white: int
        """
        
        

        self._name = None
        self._description = None
        self._geoip = None
        self._white = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        self.geoip = geoip
        self.white = white

    @property
    def name(self):
        """Gets the name of this UpdateGeoipRuleRequestBody.

        地理位置控制规则名称

        :return: The name of this UpdateGeoipRuleRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateGeoipRuleRequestBody.

        地理位置控制规则名称

        :param name: The name of this UpdateGeoipRuleRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this UpdateGeoipRuleRequestBody.

        描述

        :return: The description of this UpdateGeoipRuleRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateGeoipRuleRequestBody.

        描述

        :param description: The description of this UpdateGeoipRuleRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def geoip(self):
        """Gets the geoip of this UpdateGeoipRuleRequestBody.

        地理位置封禁区域，选择区域对应的字母代号： (CN： 中国,CA： 加拿大,US： 美国,AU： 澳大利亚,IN： 印度,JP： 日本,UK： 英国,FR： 法国,DE： 德国,BR： 巴西,Ukraine： 乌克兰,North Korea： 朝鲜,The Republic of Korea： 韩国,Iran： 伊朗,Cuba： 古巴,Sultan： 苏丹,Syria： 叙利亚,Pakistan： 巴基斯坦,Palestine： 巴勒斯坦,Israel： 以色列,Iraq： 伊拉克,Afghanistan： 阿富汗,Libya： 利比亚,Turkey： 土耳其,Thailand： 泰国,Singapore： 新加坡,South Africa： 南非,Mexico： 墨西哥,Peru： 秘鲁,Indonesia： 印度尼西亚,GD： 广东,FJ： 福建,JL： 吉林,LN： 辽宁,TW： 台湾,GZ： 贵州,AH： 安徽,HL： 黑龙江,HA： 河南,SC： 四川,HE： 河北,YN： 云南,HB： 湖北,HI： 海南,QH： 青海,HN： 湖南,JX： 江西,SX： 山西,SN： 陕西,ZJ： 浙江,GS： 甘肃,JS： 江苏,SD： 山东,BJ： 北京,SH： 上海,TJ： 天津,CQ： 重庆,MO： 澳门,HK： 香港,NX： 宁夏,GX： 广西,XJ： 新疆,XZ： 西藏,NM： 内蒙古)

        :return: The geoip of this UpdateGeoipRuleRequestBody.
        :rtype: str
        """
        return self._geoip

    @geoip.setter
    def geoip(self, geoip):
        """Sets the geoip of this UpdateGeoipRuleRequestBody.

        地理位置封禁区域，选择区域对应的字母代号： (CN： 中国,CA： 加拿大,US： 美国,AU： 澳大利亚,IN： 印度,JP： 日本,UK： 英国,FR： 法国,DE： 德国,BR： 巴西,Ukraine： 乌克兰,North Korea： 朝鲜,The Republic of Korea： 韩国,Iran： 伊朗,Cuba： 古巴,Sultan： 苏丹,Syria： 叙利亚,Pakistan： 巴基斯坦,Palestine： 巴勒斯坦,Israel： 以色列,Iraq： 伊拉克,Afghanistan： 阿富汗,Libya： 利比亚,Turkey： 土耳其,Thailand： 泰国,Singapore： 新加坡,South Africa： 南非,Mexico： 墨西哥,Peru： 秘鲁,Indonesia： 印度尼西亚,GD： 广东,FJ： 福建,JL： 吉林,LN： 辽宁,TW： 台湾,GZ： 贵州,AH： 安徽,HL： 黑龙江,HA： 河南,SC： 四川,HE： 河北,YN： 云南,HB： 湖北,HI： 海南,QH： 青海,HN： 湖南,JX： 江西,SX： 山西,SN： 陕西,ZJ： 浙江,GS： 甘肃,JS： 江苏,SD： 山东,BJ： 北京,SH： 上海,TJ： 天津,CQ： 重庆,MO： 澳门,HK： 香港,NX： 宁夏,GX： 广西,XJ： 新疆,XZ： 西藏,NM： 内蒙古)

        :param geoip: The geoip of this UpdateGeoipRuleRequestBody.
        :type geoip: str
        """
        self._geoip = geoip

    @property
    def white(self):
        """Gets the white of this UpdateGeoipRuleRequestBody.

        防护动作：  - 0 拦截  - 1 放行  - 2 仅记录

        :return: The white of this UpdateGeoipRuleRequestBody.
        :rtype: int
        """
        return self._white

    @white.setter
    def white(self, white):
        """Sets the white of this UpdateGeoipRuleRequestBody.

        防护动作：  - 0 拦截  - 1 放行  - 2 仅记录

        :param white: The white of this UpdateGeoipRuleRequestBody.
        :type white: int
        """
        self._white = white

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
        if not isinstance(other, UpdateGeoipRuleRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
