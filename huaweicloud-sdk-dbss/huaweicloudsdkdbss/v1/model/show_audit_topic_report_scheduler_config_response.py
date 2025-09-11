# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAuditTopicReportSchedulerConfigResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'scheduler': 'SchedulerConfigBase',
        'smn_effective': 'bool'
    }

    attribute_map = {
        'scheduler': 'scheduler',
        'smn_effective': 'smn_effective'
    }

    def __init__(self, scheduler=None, smn_effective=None):
        r"""ShowAuditTopicReportSchedulerConfigResponse

        The model defined in huaweicloud sdk

        :param scheduler: 
        :type scheduler: :class:`huaweicloudsdkdbss.v1.SchedulerConfigBase`
        :param smn_effective: 是否支持订阅  - true: 支持  - false: 不支持\&quot;
        :type smn_effective: bool
        """
        
        super(ShowAuditTopicReportSchedulerConfigResponse, self).__init__()

        self._scheduler = None
        self._smn_effective = None
        self.discriminator = None

        if scheduler is not None:
            self.scheduler = scheduler
        if smn_effective is not None:
            self.smn_effective = smn_effective

    @property
    def scheduler(self):
        r"""Gets the scheduler of this ShowAuditTopicReportSchedulerConfigResponse.

        :return: The scheduler of this ShowAuditTopicReportSchedulerConfigResponse.
        :rtype: :class:`huaweicloudsdkdbss.v1.SchedulerConfigBase`
        """
        return self._scheduler

    @scheduler.setter
    def scheduler(self, scheduler):
        r"""Sets the scheduler of this ShowAuditTopicReportSchedulerConfigResponse.

        :param scheduler: The scheduler of this ShowAuditTopicReportSchedulerConfigResponse.
        :type scheduler: :class:`huaweicloudsdkdbss.v1.SchedulerConfigBase`
        """
        self._scheduler = scheduler

    @property
    def smn_effective(self):
        r"""Gets the smn_effective of this ShowAuditTopicReportSchedulerConfigResponse.

        是否支持订阅  - true: 支持  - false: 不支持\"

        :return: The smn_effective of this ShowAuditTopicReportSchedulerConfigResponse.
        :rtype: bool
        """
        return self._smn_effective

    @smn_effective.setter
    def smn_effective(self, smn_effective):
        r"""Sets the smn_effective of this ShowAuditTopicReportSchedulerConfigResponse.

        是否支持订阅  - true: 支持  - false: 不支持\"

        :param smn_effective: The smn_effective of this ShowAuditTopicReportSchedulerConfigResponse.
        :type smn_effective: bool
        """
        self._smn_effective = smn_effective

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
        if not isinstance(other, ShowAuditTopicReportSchedulerConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
