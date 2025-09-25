# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RiskHandleInfoVulInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vul_scan_task_num': 'int',
        'vul_num': 'int',
        'handled_vul_num': 'int',
        'handled_rate': 'float',
        'beat_rate': 'float',
        'new_urgent_vul_num': 'int'
    }

    attribute_map = {
        'vul_scan_task_num': 'vul_scan_task_num',
        'vul_num': 'vul_num',
        'handled_vul_num': 'handled_vul_num',
        'handled_rate': 'handled_rate',
        'beat_rate': 'beat_rate',
        'new_urgent_vul_num': 'new_urgent_vul_num'
    }

    def __init__(self, vul_scan_task_num=None, vul_num=None, handled_vul_num=None, handled_rate=None, beat_rate=None, new_urgent_vul_num=None):
        r"""RiskHandleInfoVulInfo

        The model defined in huaweicloud sdk

        :param vul_scan_task_num: **参数解释**: 漏洞扫描任务次数 **取值范围**: 最小值0，最大值2147483647 
        :type vul_scan_task_num: int
        :param vul_num: **参数解释**: 发现的漏洞数 **取值范围**: 最小值0，最大值2147483647 
        :type vul_num: int
        :param handled_vul_num: **参数解释**: 已经处置的漏洞数 **取值范围**: 最小值0，最大值2147483647 
        :type handled_vul_num: int
        :param handled_rate: **参数解释**: 处置率 **取值范围**: 最小值0，最大值1 
        :type handled_rate: float
        :param beat_rate: **参数解释**: 处置率击败的用户率 **取值范围**: 最小值0，最大值1 
        :type beat_rate: float
        :param new_urgent_vul_num: **参数解释**: 新增应急漏洞数 **取值范围**: 最小值0，最大值2147483647 
        :type new_urgent_vul_num: int
        """
        
        

        self._vul_scan_task_num = None
        self._vul_num = None
        self._handled_vul_num = None
        self._handled_rate = None
        self._beat_rate = None
        self._new_urgent_vul_num = None
        self.discriminator = None

        if vul_scan_task_num is not None:
            self.vul_scan_task_num = vul_scan_task_num
        if vul_num is not None:
            self.vul_num = vul_num
        if handled_vul_num is not None:
            self.handled_vul_num = handled_vul_num
        if handled_rate is not None:
            self.handled_rate = handled_rate
        if beat_rate is not None:
            self.beat_rate = beat_rate
        if new_urgent_vul_num is not None:
            self.new_urgent_vul_num = new_urgent_vul_num

    @property
    def vul_scan_task_num(self):
        r"""Gets the vul_scan_task_num of this RiskHandleInfoVulInfo.

        **参数解释**: 漏洞扫描任务次数 **取值范围**: 最小值0，最大值2147483647 

        :return: The vul_scan_task_num of this RiskHandleInfoVulInfo.
        :rtype: int
        """
        return self._vul_scan_task_num

    @vul_scan_task_num.setter
    def vul_scan_task_num(self, vul_scan_task_num):
        r"""Sets the vul_scan_task_num of this RiskHandleInfoVulInfo.

        **参数解释**: 漏洞扫描任务次数 **取值范围**: 最小值0，最大值2147483647 

        :param vul_scan_task_num: The vul_scan_task_num of this RiskHandleInfoVulInfo.
        :type vul_scan_task_num: int
        """
        self._vul_scan_task_num = vul_scan_task_num

    @property
    def vul_num(self):
        r"""Gets the vul_num of this RiskHandleInfoVulInfo.

        **参数解释**: 发现的漏洞数 **取值范围**: 最小值0，最大值2147483647 

        :return: The vul_num of this RiskHandleInfoVulInfo.
        :rtype: int
        """
        return self._vul_num

    @vul_num.setter
    def vul_num(self, vul_num):
        r"""Sets the vul_num of this RiskHandleInfoVulInfo.

        **参数解释**: 发现的漏洞数 **取值范围**: 最小值0，最大值2147483647 

        :param vul_num: The vul_num of this RiskHandleInfoVulInfo.
        :type vul_num: int
        """
        self._vul_num = vul_num

    @property
    def handled_vul_num(self):
        r"""Gets the handled_vul_num of this RiskHandleInfoVulInfo.

        **参数解释**: 已经处置的漏洞数 **取值范围**: 最小值0，最大值2147483647 

        :return: The handled_vul_num of this RiskHandleInfoVulInfo.
        :rtype: int
        """
        return self._handled_vul_num

    @handled_vul_num.setter
    def handled_vul_num(self, handled_vul_num):
        r"""Sets the handled_vul_num of this RiskHandleInfoVulInfo.

        **参数解释**: 已经处置的漏洞数 **取值范围**: 最小值0，最大值2147483647 

        :param handled_vul_num: The handled_vul_num of this RiskHandleInfoVulInfo.
        :type handled_vul_num: int
        """
        self._handled_vul_num = handled_vul_num

    @property
    def handled_rate(self):
        r"""Gets the handled_rate of this RiskHandleInfoVulInfo.

        **参数解释**: 处置率 **取值范围**: 最小值0，最大值1 

        :return: The handled_rate of this RiskHandleInfoVulInfo.
        :rtype: float
        """
        return self._handled_rate

    @handled_rate.setter
    def handled_rate(self, handled_rate):
        r"""Sets the handled_rate of this RiskHandleInfoVulInfo.

        **参数解释**: 处置率 **取值范围**: 最小值0，最大值1 

        :param handled_rate: The handled_rate of this RiskHandleInfoVulInfo.
        :type handled_rate: float
        """
        self._handled_rate = handled_rate

    @property
    def beat_rate(self):
        r"""Gets the beat_rate of this RiskHandleInfoVulInfo.

        **参数解释**: 处置率击败的用户率 **取值范围**: 最小值0，最大值1 

        :return: The beat_rate of this RiskHandleInfoVulInfo.
        :rtype: float
        """
        return self._beat_rate

    @beat_rate.setter
    def beat_rate(self, beat_rate):
        r"""Sets the beat_rate of this RiskHandleInfoVulInfo.

        **参数解释**: 处置率击败的用户率 **取值范围**: 最小值0，最大值1 

        :param beat_rate: The beat_rate of this RiskHandleInfoVulInfo.
        :type beat_rate: float
        """
        self._beat_rate = beat_rate

    @property
    def new_urgent_vul_num(self):
        r"""Gets the new_urgent_vul_num of this RiskHandleInfoVulInfo.

        **参数解释**: 新增应急漏洞数 **取值范围**: 最小值0，最大值2147483647 

        :return: The new_urgent_vul_num of this RiskHandleInfoVulInfo.
        :rtype: int
        """
        return self._new_urgent_vul_num

    @new_urgent_vul_num.setter
    def new_urgent_vul_num(self, new_urgent_vul_num):
        r"""Sets the new_urgent_vul_num of this RiskHandleInfoVulInfo.

        **参数解释**: 新增应急漏洞数 **取值范围**: 最小值0，最大值2147483647 

        :param new_urgent_vul_num: The new_urgent_vul_num of this RiskHandleInfoVulInfo.
        :type new_urgent_vul_num: int
        """
        self._new_urgent_vul_num = new_urgent_vul_num

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
        if not isinstance(other, RiskHandleInfoVulInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
