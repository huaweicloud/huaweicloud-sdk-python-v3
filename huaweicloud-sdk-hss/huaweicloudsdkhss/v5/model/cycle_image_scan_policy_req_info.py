# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CycleImageScanPolicyReqInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enabled': 'bool',
        'scan_cycle': 'int',
        'scan_scope': 'int',
        'rate_limit': 'int',
        'time_scope': 'int',
        'registry_info': 'list[CycleImageScanPolicyReqInfoRegistryInfo]'
    }

    attribute_map = {
        'enabled': 'enabled',
        'scan_cycle': 'scan_cycle',
        'scan_scope': 'scan_scope',
        'rate_limit': 'rate_limit',
        'time_scope': 'time_scope',
        'registry_info': 'registry_info'
    }

    def __init__(self, enabled=None, scan_cycle=None, scan_scope=None, rate_limit=None, time_scope=None, registry_info=None):
        r"""CycleImageScanPolicyReqInfo

        The model defined in huaweicloud sdk

        :param enabled: 定时扫描策略开关
        :type enabled: bool
        :param scan_cycle: 定时扫描周期 | 3 每三天 7 每一周 14 每两周
        :type scan_cycle: int
        :param scan_scope: 扫描风险类型 | 0:无 0x7fffffff:全部 0x000f0000:漏洞 0x0000f000:基线检查 0x00000f00:恶意文件 0x000000f0:敏感信息 0x0000000f:软件合规
        :type scan_scope: int
        :param rate_limit: 扫描限速 单位：个/h | 0 不限制
        :type rate_limit: int
        :param time_scope: 时间范围 单位：天 | 0 全部镜像 1 3 7
        :type time_scope: int
        :param registry_info: 镜像仓库列表
        :type registry_info: list[:class:`huaweicloudsdkhss.v5.CycleImageScanPolicyReqInfoRegistryInfo`]
        """
        
        

        self._enabled = None
        self._scan_cycle = None
        self._scan_scope = None
        self._rate_limit = None
        self._time_scope = None
        self._registry_info = None
        self.discriminator = None

        if enabled is not None:
            self.enabled = enabled
        if scan_cycle is not None:
            self.scan_cycle = scan_cycle
        if scan_scope is not None:
            self.scan_scope = scan_scope
        if rate_limit is not None:
            self.rate_limit = rate_limit
        if time_scope is not None:
            self.time_scope = time_scope
        if registry_info is not None:
            self.registry_info = registry_info

    @property
    def enabled(self):
        r"""Gets the enabled of this CycleImageScanPolicyReqInfo.

        定时扫描策略开关

        :return: The enabled of this CycleImageScanPolicyReqInfo.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this CycleImageScanPolicyReqInfo.

        定时扫描策略开关

        :param enabled: The enabled of this CycleImageScanPolicyReqInfo.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def scan_cycle(self):
        r"""Gets the scan_cycle of this CycleImageScanPolicyReqInfo.

        定时扫描周期 | 3 每三天 7 每一周 14 每两周

        :return: The scan_cycle of this CycleImageScanPolicyReqInfo.
        :rtype: int
        """
        return self._scan_cycle

    @scan_cycle.setter
    def scan_cycle(self, scan_cycle):
        r"""Sets the scan_cycle of this CycleImageScanPolicyReqInfo.

        定时扫描周期 | 3 每三天 7 每一周 14 每两周

        :param scan_cycle: The scan_cycle of this CycleImageScanPolicyReqInfo.
        :type scan_cycle: int
        """
        self._scan_cycle = scan_cycle

    @property
    def scan_scope(self):
        r"""Gets the scan_scope of this CycleImageScanPolicyReqInfo.

        扫描风险类型 | 0:无 0x7fffffff:全部 0x000f0000:漏洞 0x0000f000:基线检查 0x00000f00:恶意文件 0x000000f0:敏感信息 0x0000000f:软件合规

        :return: The scan_scope of this CycleImageScanPolicyReqInfo.
        :rtype: int
        """
        return self._scan_scope

    @scan_scope.setter
    def scan_scope(self, scan_scope):
        r"""Sets the scan_scope of this CycleImageScanPolicyReqInfo.

        扫描风险类型 | 0:无 0x7fffffff:全部 0x000f0000:漏洞 0x0000f000:基线检查 0x00000f00:恶意文件 0x000000f0:敏感信息 0x0000000f:软件合规

        :param scan_scope: The scan_scope of this CycleImageScanPolicyReqInfo.
        :type scan_scope: int
        """
        self._scan_scope = scan_scope

    @property
    def rate_limit(self):
        r"""Gets the rate_limit of this CycleImageScanPolicyReqInfo.

        扫描限速 单位：个/h | 0 不限制

        :return: The rate_limit of this CycleImageScanPolicyReqInfo.
        :rtype: int
        """
        return self._rate_limit

    @rate_limit.setter
    def rate_limit(self, rate_limit):
        r"""Sets the rate_limit of this CycleImageScanPolicyReqInfo.

        扫描限速 单位：个/h | 0 不限制

        :param rate_limit: The rate_limit of this CycleImageScanPolicyReqInfo.
        :type rate_limit: int
        """
        self._rate_limit = rate_limit

    @property
    def time_scope(self):
        r"""Gets the time_scope of this CycleImageScanPolicyReqInfo.

        时间范围 单位：天 | 0 全部镜像 1 3 7

        :return: The time_scope of this CycleImageScanPolicyReqInfo.
        :rtype: int
        """
        return self._time_scope

    @time_scope.setter
    def time_scope(self, time_scope):
        r"""Sets the time_scope of this CycleImageScanPolicyReqInfo.

        时间范围 单位：天 | 0 全部镜像 1 3 7

        :param time_scope: The time_scope of this CycleImageScanPolicyReqInfo.
        :type time_scope: int
        """
        self._time_scope = time_scope

    @property
    def registry_info(self):
        r"""Gets the registry_info of this CycleImageScanPolicyReqInfo.

        镜像仓库列表

        :return: The registry_info of this CycleImageScanPolicyReqInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.CycleImageScanPolicyReqInfoRegistryInfo`]
        """
        return self._registry_info

    @registry_info.setter
    def registry_info(self, registry_info):
        r"""Sets the registry_info of this CycleImageScanPolicyReqInfo.

        镜像仓库列表

        :param registry_info: The registry_info of this CycleImageScanPolicyReqInfo.
        :type registry_info: list[:class:`huaweicloudsdkhss.v5.CycleImageScanPolicyReqInfoRegistryInfo`]
        """
        self._registry_info = registry_info

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
        if not isinstance(other, CycleImageScanPolicyReqInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
