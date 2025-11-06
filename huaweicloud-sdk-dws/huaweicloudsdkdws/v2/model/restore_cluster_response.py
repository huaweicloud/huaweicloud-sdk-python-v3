# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RestoreClusterResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster': 'Cluster',
        'job_id': 'str'
    }

    attribute_map = {
        'cluster': 'cluster',
        'job_id': 'job_id'
    }

    def __init__(self, cluster=None, job_id=None):
        r"""RestoreClusterResponse

        The model defined in huaweicloud sdk

        :param cluster: 
        :type cluster: :class:`huaweicloudsdkdws.v2.Cluster`
        :param job_id: **参数解释**： 异步任务ID。 **取值范围**： 不涉及。
        :type job_id: str
        """
        
        super().__init__()

        self._cluster = None
        self._job_id = None
        self.discriminator = None

        if cluster is not None:
            self.cluster = cluster
        if job_id is not None:
            self.job_id = job_id

    @property
    def cluster(self):
        r"""Gets the cluster of this RestoreClusterResponse.

        :return: The cluster of this RestoreClusterResponse.
        :rtype: :class:`huaweicloudsdkdws.v2.Cluster`
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        r"""Sets the cluster of this RestoreClusterResponse.

        :param cluster: The cluster of this RestoreClusterResponse.
        :type cluster: :class:`huaweicloudsdkdws.v2.Cluster`
        """
        self._cluster = cluster

    @property
    def job_id(self):
        r"""Gets the job_id of this RestoreClusterResponse.

        **参数解释**： 异步任务ID。 **取值范围**： 不涉及。

        :return: The job_id of this RestoreClusterResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this RestoreClusterResponse.

        **参数解释**： 异步任务ID。 **取值范围**： 不涉及。

        :param job_id: The job_id of this RestoreClusterResponse.
        :type job_id: str
        """
        self._job_id = job_id

    def to_dict(self):
        import warnings
        warnings.warn("RestoreClusterResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, RestoreClusterResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
