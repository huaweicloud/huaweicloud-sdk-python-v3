# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowImagePayPerScanStatisticsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'repository_scan_num': 'int',
        'cicd_scan_num': 'int',
        'free_quota_num': 'int',
        'already_given': 'bool',
        'image_free_quota': 'int',
        'high_risk': 'ImageTypeRiskInfo',
        'has_risk': 'ImageTypeRiskInfo',
        'total': 'ImageTypeRiskInfo',
        'unscan': 'ImageTypeRiskInfo'
    }

    attribute_map = {
        'repository_scan_num': 'repository_scan_num',
        'cicd_scan_num': 'cicd_scan_num',
        'free_quota_num': 'free_quota_num',
        'already_given': 'already_given',
        'image_free_quota': 'image_free_quota',
        'high_risk': 'high_risk',
        'has_risk': 'has_risk',
        'total': 'total',
        'unscan': 'unscan'
    }

    def __init__(self, repository_scan_num=None, cicd_scan_num=None, free_quota_num=None, already_given=None, image_free_quota=None, high_risk=None, has_risk=None, total=None, unscan=None):
        r"""ShowImagePayPerScanStatisticsResponse

        The model defined in huaweicloud sdk

        :param repository_scan_num: 仓库镜像扫描成功次数
        :type repository_scan_num: int
        :param cicd_scan_num: CICD镜像扫描成功次数
        :type cicd_scan_num: int
        :param free_quota_num: 免费扫描次数
        :type free_quota_num: int
        :param already_given: 是否赠送过免费次数
        :type already_given: bool
        :param image_free_quota: 登录容器镜像界面赠送的次数
        :type image_free_quota: int
        :param high_risk: 
        :type high_risk: :class:`huaweicloudsdkhss.v5.ImageTypeRiskInfo`
        :param has_risk: 
        :type has_risk: :class:`huaweicloudsdkhss.v5.ImageTypeRiskInfo`
        :param total: 
        :type total: :class:`huaweicloudsdkhss.v5.ImageTypeRiskInfo`
        :param unscan: 
        :type unscan: :class:`huaweicloudsdkhss.v5.ImageTypeRiskInfo`
        """
        
        super().__init__()

        self._repository_scan_num = None
        self._cicd_scan_num = None
        self._free_quota_num = None
        self._already_given = None
        self._image_free_quota = None
        self._high_risk = None
        self._has_risk = None
        self._total = None
        self._unscan = None
        self.discriminator = None

        if repository_scan_num is not None:
            self.repository_scan_num = repository_scan_num
        if cicd_scan_num is not None:
            self.cicd_scan_num = cicd_scan_num
        if free_quota_num is not None:
            self.free_quota_num = free_quota_num
        if already_given is not None:
            self.already_given = already_given
        if image_free_quota is not None:
            self.image_free_quota = image_free_quota
        if high_risk is not None:
            self.high_risk = high_risk
        if has_risk is not None:
            self.has_risk = has_risk
        if total is not None:
            self.total = total
        if unscan is not None:
            self.unscan = unscan

    @property
    def repository_scan_num(self):
        r"""Gets the repository_scan_num of this ShowImagePayPerScanStatisticsResponse.

        仓库镜像扫描成功次数

        :return: The repository_scan_num of this ShowImagePayPerScanStatisticsResponse.
        :rtype: int
        """
        return self._repository_scan_num

    @repository_scan_num.setter
    def repository_scan_num(self, repository_scan_num):
        r"""Sets the repository_scan_num of this ShowImagePayPerScanStatisticsResponse.

        仓库镜像扫描成功次数

        :param repository_scan_num: The repository_scan_num of this ShowImagePayPerScanStatisticsResponse.
        :type repository_scan_num: int
        """
        self._repository_scan_num = repository_scan_num

    @property
    def cicd_scan_num(self):
        r"""Gets the cicd_scan_num of this ShowImagePayPerScanStatisticsResponse.

        CICD镜像扫描成功次数

        :return: The cicd_scan_num of this ShowImagePayPerScanStatisticsResponse.
        :rtype: int
        """
        return self._cicd_scan_num

    @cicd_scan_num.setter
    def cicd_scan_num(self, cicd_scan_num):
        r"""Sets the cicd_scan_num of this ShowImagePayPerScanStatisticsResponse.

        CICD镜像扫描成功次数

        :param cicd_scan_num: The cicd_scan_num of this ShowImagePayPerScanStatisticsResponse.
        :type cicd_scan_num: int
        """
        self._cicd_scan_num = cicd_scan_num

    @property
    def free_quota_num(self):
        r"""Gets the free_quota_num of this ShowImagePayPerScanStatisticsResponse.

        免费扫描次数

        :return: The free_quota_num of this ShowImagePayPerScanStatisticsResponse.
        :rtype: int
        """
        return self._free_quota_num

    @free_quota_num.setter
    def free_quota_num(self, free_quota_num):
        r"""Sets the free_quota_num of this ShowImagePayPerScanStatisticsResponse.

        免费扫描次数

        :param free_quota_num: The free_quota_num of this ShowImagePayPerScanStatisticsResponse.
        :type free_quota_num: int
        """
        self._free_quota_num = free_quota_num

    @property
    def already_given(self):
        r"""Gets the already_given of this ShowImagePayPerScanStatisticsResponse.

        是否赠送过免费次数

        :return: The already_given of this ShowImagePayPerScanStatisticsResponse.
        :rtype: bool
        """
        return self._already_given

    @already_given.setter
    def already_given(self, already_given):
        r"""Sets the already_given of this ShowImagePayPerScanStatisticsResponse.

        是否赠送过免费次数

        :param already_given: The already_given of this ShowImagePayPerScanStatisticsResponse.
        :type already_given: bool
        """
        self._already_given = already_given

    @property
    def image_free_quota(self):
        r"""Gets the image_free_quota of this ShowImagePayPerScanStatisticsResponse.

        登录容器镜像界面赠送的次数

        :return: The image_free_quota of this ShowImagePayPerScanStatisticsResponse.
        :rtype: int
        """
        return self._image_free_quota

    @image_free_quota.setter
    def image_free_quota(self, image_free_quota):
        r"""Sets the image_free_quota of this ShowImagePayPerScanStatisticsResponse.

        登录容器镜像界面赠送的次数

        :param image_free_quota: The image_free_quota of this ShowImagePayPerScanStatisticsResponse.
        :type image_free_quota: int
        """
        self._image_free_quota = image_free_quota

    @property
    def high_risk(self):
        r"""Gets the high_risk of this ShowImagePayPerScanStatisticsResponse.

        :return: The high_risk of this ShowImagePayPerScanStatisticsResponse.
        :rtype: :class:`huaweicloudsdkhss.v5.ImageTypeRiskInfo`
        """
        return self._high_risk

    @high_risk.setter
    def high_risk(self, high_risk):
        r"""Sets the high_risk of this ShowImagePayPerScanStatisticsResponse.

        :param high_risk: The high_risk of this ShowImagePayPerScanStatisticsResponse.
        :type high_risk: :class:`huaweicloudsdkhss.v5.ImageTypeRiskInfo`
        """
        self._high_risk = high_risk

    @property
    def has_risk(self):
        r"""Gets the has_risk of this ShowImagePayPerScanStatisticsResponse.

        :return: The has_risk of this ShowImagePayPerScanStatisticsResponse.
        :rtype: :class:`huaweicloudsdkhss.v5.ImageTypeRiskInfo`
        """
        return self._has_risk

    @has_risk.setter
    def has_risk(self, has_risk):
        r"""Sets the has_risk of this ShowImagePayPerScanStatisticsResponse.

        :param has_risk: The has_risk of this ShowImagePayPerScanStatisticsResponse.
        :type has_risk: :class:`huaweicloudsdkhss.v5.ImageTypeRiskInfo`
        """
        self._has_risk = has_risk

    @property
    def total(self):
        r"""Gets the total of this ShowImagePayPerScanStatisticsResponse.

        :return: The total of this ShowImagePayPerScanStatisticsResponse.
        :rtype: :class:`huaweicloudsdkhss.v5.ImageTypeRiskInfo`
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ShowImagePayPerScanStatisticsResponse.

        :param total: The total of this ShowImagePayPerScanStatisticsResponse.
        :type total: :class:`huaweicloudsdkhss.v5.ImageTypeRiskInfo`
        """
        self._total = total

    @property
    def unscan(self):
        r"""Gets the unscan of this ShowImagePayPerScanStatisticsResponse.

        :return: The unscan of this ShowImagePayPerScanStatisticsResponse.
        :rtype: :class:`huaweicloudsdkhss.v5.ImageTypeRiskInfo`
        """
        return self._unscan

    @unscan.setter
    def unscan(self, unscan):
        r"""Sets the unscan of this ShowImagePayPerScanStatisticsResponse.

        :param unscan: The unscan of this ShowImagePayPerScanStatisticsResponse.
        :type unscan: :class:`huaweicloudsdkhss.v5.ImageTypeRiskInfo`
        """
        self._unscan = unscan

    def to_dict(self):
        import warnings
        warnings.warn("ShowImagePayPerScanStatisticsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowImagePayPerScanStatisticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
