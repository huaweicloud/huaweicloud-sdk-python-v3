# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QuotaHostStatistics:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'version': 'str',
        'total_num': 'int',
        'about_to_expire_num': 'int',
        'idle_num': 'int',
        'host_num': 'int'
    }

    attribute_map = {
        'version': 'version',
        'total_num': 'total_num',
        'about_to_expire_num': 'about_to_expire_num',
        'idle_num': 'idle_num',
        'host_num': 'host_num'
    }

    def __init__(self, version=None, total_num=None, about_to_expire_num=None, idle_num=None, host_num=None):
        r"""QuotaHostStatistics

        The model defined in huaweicloud sdk

        :param version: **参数解释**: 配额版本 **取值范围**: - hss.version.basic：基础版 - hss.version.advanced：高级版 - hss.version.enterprise：企业版 - hss.version.premium：旗舰版 - hss.version.container：容器版 - hss.version.wtp：网页防篡改版 - hss.version.container_wtp：容器网页防篡改版 
        :type version: str
        :param total_num: **参数解释**: 该版本配额总数 **取值范围**: 最小值0，最大值2147483647 
        :type total_num: int
        :param about_to_expire_num: **参数解释**: 即将过期的配额数量 **取值范围**: 最小值0，最大值2147483647 
        :type about_to_expire_num: int
        :param idle_num: **参数解释**: 空闲配额数量 **取值范围**: 最小值0，最大值2147483647 
        :type idle_num: int
        :param host_num: **参数解释**: 已使用该版本配额的主机数量 **取值范围**: 最小值0，最大值2147483647 
        :type host_num: int
        """
        
        

        self._version = None
        self._total_num = None
        self._about_to_expire_num = None
        self._idle_num = None
        self._host_num = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if total_num is not None:
            self.total_num = total_num
        if about_to_expire_num is not None:
            self.about_to_expire_num = about_to_expire_num
        if idle_num is not None:
            self.idle_num = idle_num
        if host_num is not None:
            self.host_num = host_num

    @property
    def version(self):
        r"""Gets the version of this QuotaHostStatistics.

        **参数解释**: 配额版本 **取值范围**: - hss.version.basic：基础版 - hss.version.advanced：高级版 - hss.version.enterprise：企业版 - hss.version.premium：旗舰版 - hss.version.container：容器版 - hss.version.wtp：网页防篡改版 - hss.version.container_wtp：容器网页防篡改版 

        :return: The version of this QuotaHostStatistics.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this QuotaHostStatistics.

        **参数解释**: 配额版本 **取值范围**: - hss.version.basic：基础版 - hss.version.advanced：高级版 - hss.version.enterprise：企业版 - hss.version.premium：旗舰版 - hss.version.container：容器版 - hss.version.wtp：网页防篡改版 - hss.version.container_wtp：容器网页防篡改版 

        :param version: The version of this QuotaHostStatistics.
        :type version: str
        """
        self._version = version

    @property
    def total_num(self):
        r"""Gets the total_num of this QuotaHostStatistics.

        **参数解释**: 该版本配额总数 **取值范围**: 最小值0，最大值2147483647 

        :return: The total_num of this QuotaHostStatistics.
        :rtype: int
        """
        return self._total_num

    @total_num.setter
    def total_num(self, total_num):
        r"""Sets the total_num of this QuotaHostStatistics.

        **参数解释**: 该版本配额总数 **取值范围**: 最小值0，最大值2147483647 

        :param total_num: The total_num of this QuotaHostStatistics.
        :type total_num: int
        """
        self._total_num = total_num

    @property
    def about_to_expire_num(self):
        r"""Gets the about_to_expire_num of this QuotaHostStatistics.

        **参数解释**: 即将过期的配额数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The about_to_expire_num of this QuotaHostStatistics.
        :rtype: int
        """
        return self._about_to_expire_num

    @about_to_expire_num.setter
    def about_to_expire_num(self, about_to_expire_num):
        r"""Sets the about_to_expire_num of this QuotaHostStatistics.

        **参数解释**: 即将过期的配额数量 **取值范围**: 最小值0，最大值2147483647 

        :param about_to_expire_num: The about_to_expire_num of this QuotaHostStatistics.
        :type about_to_expire_num: int
        """
        self._about_to_expire_num = about_to_expire_num

    @property
    def idle_num(self):
        r"""Gets the idle_num of this QuotaHostStatistics.

        **参数解释**: 空闲配额数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The idle_num of this QuotaHostStatistics.
        :rtype: int
        """
        return self._idle_num

    @idle_num.setter
    def idle_num(self, idle_num):
        r"""Sets the idle_num of this QuotaHostStatistics.

        **参数解释**: 空闲配额数量 **取值范围**: 最小值0，最大值2147483647 

        :param idle_num: The idle_num of this QuotaHostStatistics.
        :type idle_num: int
        """
        self._idle_num = idle_num

    @property
    def host_num(self):
        r"""Gets the host_num of this QuotaHostStatistics.

        **参数解释**: 已使用该版本配额的主机数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The host_num of this QuotaHostStatistics.
        :rtype: int
        """
        return self._host_num

    @host_num.setter
    def host_num(self, host_num):
        r"""Sets the host_num of this QuotaHostStatistics.

        **参数解释**: 已使用该版本配额的主机数量 **取值范围**: 最小值0，最大值2147483647 

        :param host_num: The host_num of this QuotaHostStatistics.
        :type host_num: int
        """
        self._host_num = host_num

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
        if not isinstance(other, QuotaHostStatistics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
