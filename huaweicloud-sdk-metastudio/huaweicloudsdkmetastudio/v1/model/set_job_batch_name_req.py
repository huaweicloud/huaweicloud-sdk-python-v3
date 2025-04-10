# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetJobBatchNameReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'batch_name': 'str',
        'job_ids': 'list[str]'
    }

    attribute_map = {
        'batch_name': 'batch_name',
        'job_ids': 'job_ids'
    }

    def __init__(self, batch_name=None, job_ids=None):
        r"""SetJobBatchNameReq

        The model defined in huaweicloud sdk

        :param batch_name: 批次名称
        :type batch_name: str
        :param job_ids: 任务id列表
        :type job_ids: list[str]
        """
        
        

        self._batch_name = None
        self._job_ids = None
        self.discriminator = None

        if batch_name is not None:
            self.batch_name = batch_name
        if job_ids is not None:
            self.job_ids = job_ids

    @property
    def batch_name(self):
        r"""Gets the batch_name of this SetJobBatchNameReq.

        批次名称

        :return: The batch_name of this SetJobBatchNameReq.
        :rtype: str
        """
        return self._batch_name

    @batch_name.setter
    def batch_name(self, batch_name):
        r"""Sets the batch_name of this SetJobBatchNameReq.

        批次名称

        :param batch_name: The batch_name of this SetJobBatchNameReq.
        :type batch_name: str
        """
        self._batch_name = batch_name

    @property
    def job_ids(self):
        r"""Gets the job_ids of this SetJobBatchNameReq.

        任务id列表

        :return: The job_ids of this SetJobBatchNameReq.
        :rtype: list[str]
        """
        return self._job_ids

    @job_ids.setter
    def job_ids(self, job_ids):
        r"""Sets the job_ids of this SetJobBatchNameReq.

        任务id列表

        :param job_ids: The job_ids of this SetJobBatchNameReq.
        :type job_ids: list[str]
        """
        self._job_ids = job_ids

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
        if not isinstance(other, SetJobBatchNameReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
