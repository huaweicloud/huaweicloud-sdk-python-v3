# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListLogsJobResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_log_record': 'list[ClusterLogRecord]',
        'total_size': 'int'
    }

    attribute_map = {
        'cluster_log_record': 'clusterLogRecord',
        'total_size': 'totalSize'
    }

    def __init__(self, cluster_log_record=None, total_size=None):
        r"""ListLogsJobResponse

        The model defined in huaweicloud sdk

        :param cluster_log_record: 
        :type cluster_log_record: list[:class:`huaweicloudsdkcss.v1.ClusterLogRecord`]
        :param total_size: **参数解释**： 日志记录总条数。 **取值范围**： 不涉及
        :type total_size: int
        """
        
        super().__init__()

        self._cluster_log_record = None
        self._total_size = None
        self.discriminator = None

        if cluster_log_record is not None:
            self.cluster_log_record = cluster_log_record
        if total_size is not None:
            self.total_size = total_size

    @property
    def cluster_log_record(self):
        r"""Gets the cluster_log_record of this ListLogsJobResponse.

        :return: The cluster_log_record of this ListLogsJobResponse.
        :rtype: list[:class:`huaweicloudsdkcss.v1.ClusterLogRecord`]
        """
        return self._cluster_log_record

    @cluster_log_record.setter
    def cluster_log_record(self, cluster_log_record):
        r"""Sets the cluster_log_record of this ListLogsJobResponse.

        :param cluster_log_record: The cluster_log_record of this ListLogsJobResponse.
        :type cluster_log_record: list[:class:`huaweicloudsdkcss.v1.ClusterLogRecord`]
        """
        self._cluster_log_record = cluster_log_record

    @property
    def total_size(self):
        r"""Gets the total_size of this ListLogsJobResponse.

        **参数解释**： 日志记录总条数。 **取值范围**： 不涉及

        :return: The total_size of this ListLogsJobResponse.
        :rtype: int
        """
        return self._total_size

    @total_size.setter
    def total_size(self, total_size):
        r"""Sets the total_size of this ListLogsJobResponse.

        **参数解释**： 日志记录总条数。 **取值范围**： 不涉及

        :param total_size: The total_size of this ListLogsJobResponse.
        :type total_size: int
        """
        self._total_size = total_size

    def to_dict(self):
        import warnings
        warnings.warn("ListLogsJobResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListLogsJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
