# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAntivirusFreeQuotaResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'free_quota': 'int',
        'occupied_free_quota': 'int',
        'antivirus_already_given': 'bool',
        'antivirus_free_quota': 'int',
        'report_already_given': 'bool',
        'report_free_quota': 'int'
    }

    attribute_map = {
        'free_quota': 'free_quota',
        'occupied_free_quota': 'occupied_free_quota',
        'antivirus_already_given': 'antivirus_already_given',
        'antivirus_free_quota': 'antivirus_free_quota',
        'report_already_given': 'report_already_given',
        'report_free_quota': 'report_free_quota'
    }

    def __init__(self, free_quota=None, occupied_free_quota=None, antivirus_already_given=None, antivirus_free_quota=None, report_already_given=None, report_free_quota=None):
        r"""ShowAntivirusFreeQuotaResponse

        The model defined in huaweicloud sdk

        :param free_quota: 病毒查杀免费扫描次数
        :type free_quota: int
        :param occupied_free_quota: 当前扫描任务占用的免费扫描次数
        :type occupied_free_quota: int
        :param antivirus_already_given: 病毒查杀界面是否已经赠送过免费次数
        :type antivirus_already_given: bool
        :param antivirus_free_quota: 病毒查杀界面应该赠送的免费次数
        :type antivirus_free_quota: int
        :param report_already_given: 月度报告界面是否已经赠送过免费次数
        :type report_already_given: bool
        :param report_free_quota: 月度报告界面应该赠送的免费次数
        :type report_free_quota: int
        """
        
        super(ShowAntivirusFreeQuotaResponse, self).__init__()

        self._free_quota = None
        self._occupied_free_quota = None
        self._antivirus_already_given = None
        self._antivirus_free_quota = None
        self._report_already_given = None
        self._report_free_quota = None
        self.discriminator = None

        if free_quota is not None:
            self.free_quota = free_quota
        if occupied_free_quota is not None:
            self.occupied_free_quota = occupied_free_quota
        if antivirus_already_given is not None:
            self.antivirus_already_given = antivirus_already_given
        if antivirus_free_quota is not None:
            self.antivirus_free_quota = antivirus_free_quota
        if report_already_given is not None:
            self.report_already_given = report_already_given
        if report_free_quota is not None:
            self.report_free_quota = report_free_quota

    @property
    def free_quota(self):
        r"""Gets the free_quota of this ShowAntivirusFreeQuotaResponse.

        病毒查杀免费扫描次数

        :return: The free_quota of this ShowAntivirusFreeQuotaResponse.
        :rtype: int
        """
        return self._free_quota

    @free_quota.setter
    def free_quota(self, free_quota):
        r"""Sets the free_quota of this ShowAntivirusFreeQuotaResponse.

        病毒查杀免费扫描次数

        :param free_quota: The free_quota of this ShowAntivirusFreeQuotaResponse.
        :type free_quota: int
        """
        self._free_quota = free_quota

    @property
    def occupied_free_quota(self):
        r"""Gets the occupied_free_quota of this ShowAntivirusFreeQuotaResponse.

        当前扫描任务占用的免费扫描次数

        :return: The occupied_free_quota of this ShowAntivirusFreeQuotaResponse.
        :rtype: int
        """
        return self._occupied_free_quota

    @occupied_free_quota.setter
    def occupied_free_quota(self, occupied_free_quota):
        r"""Sets the occupied_free_quota of this ShowAntivirusFreeQuotaResponse.

        当前扫描任务占用的免费扫描次数

        :param occupied_free_quota: The occupied_free_quota of this ShowAntivirusFreeQuotaResponse.
        :type occupied_free_quota: int
        """
        self._occupied_free_quota = occupied_free_quota

    @property
    def antivirus_already_given(self):
        r"""Gets the antivirus_already_given of this ShowAntivirusFreeQuotaResponse.

        病毒查杀界面是否已经赠送过免费次数

        :return: The antivirus_already_given of this ShowAntivirusFreeQuotaResponse.
        :rtype: bool
        """
        return self._antivirus_already_given

    @antivirus_already_given.setter
    def antivirus_already_given(self, antivirus_already_given):
        r"""Sets the antivirus_already_given of this ShowAntivirusFreeQuotaResponse.

        病毒查杀界面是否已经赠送过免费次数

        :param antivirus_already_given: The antivirus_already_given of this ShowAntivirusFreeQuotaResponse.
        :type antivirus_already_given: bool
        """
        self._antivirus_already_given = antivirus_already_given

    @property
    def antivirus_free_quota(self):
        r"""Gets the antivirus_free_quota of this ShowAntivirusFreeQuotaResponse.

        病毒查杀界面应该赠送的免费次数

        :return: The antivirus_free_quota of this ShowAntivirusFreeQuotaResponse.
        :rtype: int
        """
        return self._antivirus_free_quota

    @antivirus_free_quota.setter
    def antivirus_free_quota(self, antivirus_free_quota):
        r"""Sets the antivirus_free_quota of this ShowAntivirusFreeQuotaResponse.

        病毒查杀界面应该赠送的免费次数

        :param antivirus_free_quota: The antivirus_free_quota of this ShowAntivirusFreeQuotaResponse.
        :type antivirus_free_quota: int
        """
        self._antivirus_free_quota = antivirus_free_quota

    @property
    def report_already_given(self):
        r"""Gets the report_already_given of this ShowAntivirusFreeQuotaResponse.

        月度报告界面是否已经赠送过免费次数

        :return: The report_already_given of this ShowAntivirusFreeQuotaResponse.
        :rtype: bool
        """
        return self._report_already_given

    @report_already_given.setter
    def report_already_given(self, report_already_given):
        r"""Sets the report_already_given of this ShowAntivirusFreeQuotaResponse.

        月度报告界面是否已经赠送过免费次数

        :param report_already_given: The report_already_given of this ShowAntivirusFreeQuotaResponse.
        :type report_already_given: bool
        """
        self._report_already_given = report_already_given

    @property
    def report_free_quota(self):
        r"""Gets the report_free_quota of this ShowAntivirusFreeQuotaResponse.

        月度报告界面应该赠送的免费次数

        :return: The report_free_quota of this ShowAntivirusFreeQuotaResponse.
        :rtype: int
        """
        return self._report_free_quota

    @report_free_quota.setter
    def report_free_quota(self, report_free_quota):
        r"""Sets the report_free_quota of this ShowAntivirusFreeQuotaResponse.

        月度报告界面应该赠送的免费次数

        :param report_free_quota: The report_free_quota of this ShowAntivirusFreeQuotaResponse.
        :type report_free_quota: int
        """
        self._report_free_quota = report_free_quota

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
        if not isinstance(other, ShowAntivirusFreeQuotaResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
