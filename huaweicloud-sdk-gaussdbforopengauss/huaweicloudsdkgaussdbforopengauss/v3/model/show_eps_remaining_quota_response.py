# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowEpsRemainingQuotaResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'eps_quota_remaining': 'list[EpsRemainingQuotaResult]',
        'job_id': 'str',
        'total_count': 'int'
    }

    attribute_map = {
        'eps_quota_remaining': 'eps_quota_remaining',
        'job_id': 'job_id',
        'total_count': 'total_count'
    }

    def __init__(self, eps_quota_remaining=None, job_id=None, total_count=None):
        r"""ShowEpsRemainingQuotaResponse

        The model defined in huaweicloud sdk

        :param eps_quota_remaining: **参数解释**: 剩余企业项目配额组。
        :type eps_quota_remaining: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.EpsRemainingQuotaResult`]
        :param job_id: **参数解释**: 任务ID。 **取值范围**: 不涉及。
        :type job_id: str
        :param total_count: **参数解释**: 返回的企业项目个数。 **取值范围**: 不涉及。
        :type total_count: int
        """
        
        super(ShowEpsRemainingQuotaResponse, self).__init__()

        self._eps_quota_remaining = None
        self._job_id = None
        self._total_count = None
        self.discriminator = None

        if eps_quota_remaining is not None:
            self.eps_quota_remaining = eps_quota_remaining
        if job_id is not None:
            self.job_id = job_id
        if total_count is not None:
            self.total_count = total_count

    @property
    def eps_quota_remaining(self):
        r"""Gets the eps_quota_remaining of this ShowEpsRemainingQuotaResponse.

        **参数解释**: 剩余企业项目配额组。

        :return: The eps_quota_remaining of this ShowEpsRemainingQuotaResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.EpsRemainingQuotaResult`]
        """
        return self._eps_quota_remaining

    @eps_quota_remaining.setter
    def eps_quota_remaining(self, eps_quota_remaining):
        r"""Sets the eps_quota_remaining of this ShowEpsRemainingQuotaResponse.

        **参数解释**: 剩余企业项目配额组。

        :param eps_quota_remaining: The eps_quota_remaining of this ShowEpsRemainingQuotaResponse.
        :type eps_quota_remaining: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.EpsRemainingQuotaResult`]
        """
        self._eps_quota_remaining = eps_quota_remaining

    @property
    def job_id(self):
        r"""Gets the job_id of this ShowEpsRemainingQuotaResponse.

        **参数解释**: 任务ID。 **取值范围**: 不涉及。

        :return: The job_id of this ShowEpsRemainingQuotaResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ShowEpsRemainingQuotaResponse.

        **参数解释**: 任务ID。 **取值范围**: 不涉及。

        :param job_id: The job_id of this ShowEpsRemainingQuotaResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def total_count(self):
        r"""Gets the total_count of this ShowEpsRemainingQuotaResponse.

        **参数解释**: 返回的企业项目个数。 **取值范围**: 不涉及。

        :return: The total_count of this ShowEpsRemainingQuotaResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ShowEpsRemainingQuotaResponse.

        **参数解释**: 返回的企业项目个数。 **取值范围**: 不涉及。

        :param total_count: The total_count of this ShowEpsRemainingQuotaResponse.
        :type total_count: int
        """
        self._total_count = total_count

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
        if not isinstance(other, ShowEpsRemainingQuotaResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
