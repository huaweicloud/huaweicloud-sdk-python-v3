# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateCloudTableClusterResponse(SdkResponse):

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
        'job_id': 'str',
        'get_job_endpoint': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'job_id': 'jobId',
        'get_job_endpoint': 'getJobEndpoint'
    }

    def __init__(self, cluster_id=None, job_id=None, get_job_endpoint=None):
        """CreateCloudTableClusterResponse

        The model defined in huaweicloud sdk

        :param cluster_id: 集群ID
        :type cluster_id: str
        :param job_id: 
        :type job_id: str
        :param get_job_endpoint: 
        :type get_job_endpoint: str
        """
        
        super(CreateCloudTableClusterResponse, self).__init__()

        self._cluster_id = None
        self._job_id = None
        self._get_job_endpoint = None
        self.discriminator = None

        if cluster_id is not None:
            self.cluster_id = cluster_id
        if job_id is not None:
            self.job_id = job_id
        if get_job_endpoint is not None:
            self.get_job_endpoint = get_job_endpoint

    @property
    def cluster_id(self):
        """Gets the cluster_id of this CreateCloudTableClusterResponse.

        集群ID

        :return: The cluster_id of this CreateCloudTableClusterResponse.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this CreateCloudTableClusterResponse.

        集群ID

        :param cluster_id: The cluster_id of this CreateCloudTableClusterResponse.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def job_id(self):
        """Gets the job_id of this CreateCloudTableClusterResponse.

        :return: The job_id of this CreateCloudTableClusterResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this CreateCloudTableClusterResponse.

        :param job_id: The job_id of this CreateCloudTableClusterResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def get_job_endpoint(self):
        """Gets the get_job_endpoint of this CreateCloudTableClusterResponse.

        :return: The get_job_endpoint of this CreateCloudTableClusterResponse.
        :rtype: str
        """
        return self._get_job_endpoint

    @get_job_endpoint.setter
    def get_job_endpoint(self, get_job_endpoint):
        """Sets the get_job_endpoint of this CreateCloudTableClusterResponse.

        :param get_job_endpoint: The get_job_endpoint of this CreateCloudTableClusterResponse.
        :type get_job_endpoint: str
        """
        self._get_job_endpoint = get_job_endpoint

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
        if not isinstance(other, CreateCloudTableClusterResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
