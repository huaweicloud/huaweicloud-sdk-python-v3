# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StartJobReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_params': 'list[JobParam]'
    }

    attribute_map = {
        'job_params': 'jobParams'
    }

    def __init__(self, job_params=None):
        r"""StartJobReq

        The model defined in huaweicloud sdk

        :param job_params: 
        :type job_params: list[:class:`huaweicloudsdkdgc.v1.JobParam`]
        """
        
        

        self._job_params = None
        self.discriminator = None

        if job_params is not None:
            self.job_params = job_params

    @property
    def job_params(self):
        r"""Gets the job_params of this StartJobReq.

        :return: The job_params of this StartJobReq.
        :rtype: list[:class:`huaweicloudsdkdgc.v1.JobParam`]
        """
        return self._job_params

    @job_params.setter
    def job_params(self, job_params):
        r"""Sets the job_params of this StartJobReq.

        :param job_params: The job_params of this StartJobReq.
        :type job_params: list[:class:`huaweicloudsdkdgc.v1.JobParam`]
        """
        self._job_params = job_params

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
        if not isinstance(other, StartJobReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
