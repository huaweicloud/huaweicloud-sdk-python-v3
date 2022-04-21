# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateJobRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'cluster_id': 'str',
        'job_name': 'str',
        'body': 'CdmUpdateJobJsonReq'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'job_name': 'job_name',
        'body': 'body'
    }

    def __init__(self, cluster_id=None, job_name=None, body=None):
        """UpdateJobRequest

        The model defined in huaweicloud sdk

        :param cluster_id: 集群ID
        :type cluster_id: str
        :param job_name: 作业名称。
        :type job_name: str
        :param body: Body of the UpdateJobRequest
        :type body: :class:`huaweicloudsdkcdm.v1.CdmUpdateJobJsonReq`
        """
        
        

        self._cluster_id = None
        self._job_name = None
        self._body = None
        self.discriminator = None

        self.cluster_id = cluster_id
        self.job_name = job_name
        if body is not None:
            self.body = body

    @property
    def cluster_id(self):
        """Gets the cluster_id of this UpdateJobRequest.

        集群ID

        :return: The cluster_id of this UpdateJobRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this UpdateJobRequest.

        集群ID

        :param cluster_id: The cluster_id of this UpdateJobRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def job_name(self):
        """Gets the job_name of this UpdateJobRequest.

        作业名称。

        :return: The job_name of this UpdateJobRequest.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this UpdateJobRequest.

        作业名称。

        :param job_name: The job_name of this UpdateJobRequest.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def body(self):
        """Gets the body of this UpdateJobRequest.


        :return: The body of this UpdateJobRequest.
        :rtype: :class:`huaweicloudsdkcdm.v1.CdmUpdateJobJsonReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateJobRequest.


        :param body: The body of this UpdateJobRequest.
        :type body: :class:`huaweicloudsdkcdm.v1.CdmUpdateJobJsonReq`
        """
        self._body = body

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
        if not isinstance(other, UpdateJobRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
