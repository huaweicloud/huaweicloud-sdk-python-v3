# coding: utf-8

import re
import six


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
        'cluster_log_record': 'list[ClusterLogRecord]'
    }

    attribute_map = {
        'cluster_log_record': 'clusterLogRecord'
    }

    def __init__(self, cluster_log_record=None):
        """ListLogsJobResponse

        The model defined in huaweicloud sdk

        :param cluster_log_record: 
        :type cluster_log_record: list[:class:`huaweicloudsdkcss.v1.ClusterLogRecord`]
        """
        
        super(ListLogsJobResponse, self).__init__()

        self._cluster_log_record = None
        self.discriminator = None

        if cluster_log_record is not None:
            self.cluster_log_record = cluster_log_record

    @property
    def cluster_log_record(self):
        """Gets the cluster_log_record of this ListLogsJobResponse.


        :return: The cluster_log_record of this ListLogsJobResponse.
        :rtype: list[:class:`huaweicloudsdkcss.v1.ClusterLogRecord`]
        """
        return self._cluster_log_record

    @cluster_log_record.setter
    def cluster_log_record(self, cluster_log_record):
        """Sets the cluster_log_record of this ListLogsJobResponse.


        :param cluster_log_record: The cluster_log_record of this ListLogsJobResponse.
        :type cluster_log_record: list[:class:`huaweicloudsdkcss.v1.ClusterLogRecord`]
        """
        self._cluster_log_record = cluster_log_record

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
        if not isinstance(other, ListLogsJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
