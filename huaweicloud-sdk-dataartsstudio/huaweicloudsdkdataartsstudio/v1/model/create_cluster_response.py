# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateClusterResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_success': 'bool',
        'message': 'str',
        'cluster_name': 'str',
        'job_id': 'str'
    }

    attribute_map = {
        'is_success': 'is_success',
        'message': 'message',
        'cluster_name': 'cluster_name',
        'job_id': 'job_id'
    }

    def __init__(self, is_success=None, message=None, cluster_name=None, job_id=None):
        r"""CreateClusterResponse

        The model defined in huaweicloud sdk

        :param is_success: 请求执行是否成功。\&quot;true\&quot;表示请求执行成功。
        :type is_success: bool
        :param message: 系统提示信息，执行成功时，信息可能为空。
        :type message: str
        :param cluster_name: 新增集群的名称。
        :type cluster_name: str
        :param job_id: 异步作业id，用于查询作业状态。
        :type job_id: str
        """
        
        super().__init__()

        self._is_success = None
        self._message = None
        self._cluster_name = None
        self._job_id = None
        self.discriminator = None

        if is_success is not None:
            self.is_success = is_success
        if message is not None:
            self.message = message
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if job_id is not None:
            self.job_id = job_id

    @property
    def is_success(self):
        r"""Gets the is_success of this CreateClusterResponse.

        请求执行是否成功。\"true\"表示请求执行成功。

        :return: The is_success of this CreateClusterResponse.
        :rtype: bool
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        r"""Sets the is_success of this CreateClusterResponse.

        请求执行是否成功。\"true\"表示请求执行成功。

        :param is_success: The is_success of this CreateClusterResponse.
        :type is_success: bool
        """
        self._is_success = is_success

    @property
    def message(self):
        r"""Gets the message of this CreateClusterResponse.

        系统提示信息，执行成功时，信息可能为空。

        :return: The message of this CreateClusterResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this CreateClusterResponse.

        系统提示信息，执行成功时，信息可能为空。

        :param message: The message of this CreateClusterResponse.
        :type message: str
        """
        self._message = message

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this CreateClusterResponse.

        新增集群的名称。

        :return: The cluster_name of this CreateClusterResponse.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this CreateClusterResponse.

        新增集群的名称。

        :param cluster_name: The cluster_name of this CreateClusterResponse.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def job_id(self):
        r"""Gets the job_id of this CreateClusterResponse.

        异步作业id，用于查询作业状态。

        :return: The job_id of this CreateClusterResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this CreateClusterResponse.

        异步作业id，用于查询作业状态。

        :param job_id: The job_id of this CreateClusterResponse.
        :type job_id: str
        """
        self._job_id = job_id

    def to_dict(self):
        import warnings
        warnings.warn("CreateClusterResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, CreateClusterResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
