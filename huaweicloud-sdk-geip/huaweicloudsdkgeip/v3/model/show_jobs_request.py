# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowJobsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'fields': 'list[str]'
    }

    attribute_map = {
        'job_id': 'job_id',
        'fields': 'fields'
    }

    def __init__(self, job_id=None, fields=None):
        r"""ShowJobsRequest

        The model defined in huaweicloud sdk

        :param job_id: job_id
        :type job_id: str
        :param fields: 
        :type fields: list[str]
        """
        
        

        self._job_id = None
        self._fields = None
        self.discriminator = None

        self.job_id = job_id
        if fields is not None:
            self.fields = fields

    @property
    def job_id(self):
        r"""Gets the job_id of this ShowJobsRequest.

        job_id

        :return: The job_id of this ShowJobsRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ShowJobsRequest.

        job_id

        :param job_id: The job_id of this ShowJobsRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def fields(self):
        r"""Gets the fields of this ShowJobsRequest.

        :return: The fields of this ShowJobsRequest.
        :rtype: list[str]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        r"""Sets the fields of this ShowJobsRequest.

        :param fields: The fields of this ShowJobsRequest.
        :type fields: list[str]
        """
        self._fields = fields

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
        if not isinstance(other, ShowJobsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
