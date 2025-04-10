# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateBatchJobResponse(SdkResponse):

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
        'job_name': 'str',
        'created_at': 'int'
    }

    attribute_map = {
        'job_id': 'job_id',
        'job_name': 'job_name',
        'created_at': 'created_at'
    }

    def __init__(self, job_id=None, job_name=None, created_at=None):
        r"""CreateBatchJobResponse

        The model defined in huaweicloud sdk

        :param job_id: 批量处理作业ID
        :type job_id: str
        :param job_name: 批量处理作业名称
        :type job_name: str
        :param created_at: 批量处理作业创建时间戳
        :type created_at: int
        """
        
        super(CreateBatchJobResponse, self).__init__()

        self._job_id = None
        self._job_name = None
        self._created_at = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if job_name is not None:
            self.job_name = job_name
        if created_at is not None:
            self.created_at = created_at

    @property
    def job_id(self):
        r"""Gets the job_id of this CreateBatchJobResponse.

        批量处理作业ID

        :return: The job_id of this CreateBatchJobResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this CreateBatchJobResponse.

        批量处理作业ID

        :param job_id: The job_id of this CreateBatchJobResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def job_name(self):
        r"""Gets the job_name of this CreateBatchJobResponse.

        批量处理作业名称

        :return: The job_name of this CreateBatchJobResponse.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        r"""Sets the job_name of this CreateBatchJobResponse.

        批量处理作业名称

        :param job_name: The job_name of this CreateBatchJobResponse.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def created_at(self):
        r"""Gets the created_at of this CreateBatchJobResponse.

        批量处理作业创建时间戳

        :return: The created_at of this CreateBatchJobResponse.
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this CreateBatchJobResponse.

        批量处理作业创建时间戳

        :param created_at: The created_at of this CreateBatchJobResponse.
        :type created_at: int
        """
        self._created_at = created_at

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
        if not isinstance(other, CreateBatchJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
