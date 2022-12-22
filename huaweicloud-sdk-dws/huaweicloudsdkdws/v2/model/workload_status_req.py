# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkloadStatusReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workload_status': 'WorkloadStatus'
    }

    attribute_map = {
        'workload_status': 'workload_status'
    }

    def __init__(self, workload_status=None):
        """WorkloadStatusReq

        The model defined in huaweicloud sdk

        :param workload_status: 
        :type workload_status: :class:`huaweicloudsdkdws.v2.WorkloadStatus`
        """
        
        

        self._workload_status = None
        self.discriminator = None

        if workload_status is not None:
            self.workload_status = workload_status

    @property
    def workload_status(self):
        """Gets the workload_status of this WorkloadStatusReq.

        :return: The workload_status of this WorkloadStatusReq.
        :rtype: :class:`huaweicloudsdkdws.v2.WorkloadStatus`
        """
        return self._workload_status

    @workload_status.setter
    def workload_status(self, workload_status):
        """Sets the workload_status of this WorkloadStatusReq.

        :param workload_status: The workload_status of this WorkloadStatusReq.
        :type workload_status: :class:`huaweicloudsdkdws.v2.WorkloadStatus`
        """
        self._workload_status = workload_status

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
        if not isinstance(other, WorkloadStatusReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
