# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceJob:

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
        'server_ids': 'list[str]'
    }

    attribute_map = {
        'job_id': 'job_id',
        'server_ids': 'server_ids'
    }

    def __init__(self, job_id=None, server_ids=None):
        r"""InstanceJob

        The model defined in huaweicloud sdk

        :param job_id: 
        :type job_id: str
        :param server_ids: 
        :type server_ids: list[str]
        """
        
        

        self._job_id = None
        self._server_ids = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if server_ids is not None:
            self.server_ids = server_ids

    @property
    def job_id(self):
        r"""Gets the job_id of this InstanceJob.

        :return: The job_id of this InstanceJob.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this InstanceJob.

        :param job_id: The job_id of this InstanceJob.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def server_ids(self):
        r"""Gets the server_ids of this InstanceJob.

        :return: The server_ids of this InstanceJob.
        :rtype: list[str]
        """
        return self._server_ids

    @server_ids.setter
    def server_ids(self, server_ids):
        r"""Sets the server_ids of this InstanceJob.

        :param server_ids: The server_ids of this InstanceJob.
        :type server_ids: list[str]
        """
        self._server_ids = server_ids

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
        if not isinstance(other, InstanceJob):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
