# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDatasetRequest:

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
        'run_id': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'job_id': 'job_id',
        'run_id': 'run_id',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, job_id=None, run_id=None, offset=None, limit=None):
        """ShowDatasetRequest

        The model defined in huaweicloud sdk

        :param job_id: 作业ID。
        :type job_id: str
        :param run_id: 作业运行ID。
        :type run_id: str
        :param offset: 当前偏移量，默认为0。
        :type offset: int
        :param limit: 每页显示的最大作业个数，范围: [1, 100]。默认值：10。
        :type limit: int
        """
        
        

        self._job_id = None
        self._run_id = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.job_id = job_id
        self.run_id = run_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def job_id(self):
        """Gets the job_id of this ShowDatasetRequest.

        作业ID。

        :return: The job_id of this ShowDatasetRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ShowDatasetRequest.

        作业ID。

        :param job_id: The job_id of this ShowDatasetRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def run_id(self):
        """Gets the run_id of this ShowDatasetRequest.

        作业运行ID。

        :return: The run_id of this ShowDatasetRequest.
        :rtype: str
        """
        return self._run_id

    @run_id.setter
    def run_id(self, run_id):
        """Sets the run_id of this ShowDatasetRequest.

        作业运行ID。

        :param run_id: The run_id of this ShowDatasetRequest.
        :type run_id: str
        """
        self._run_id = run_id

    @property
    def offset(self):
        """Gets the offset of this ShowDatasetRequest.

        当前偏移量，默认为0。

        :return: The offset of this ShowDatasetRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ShowDatasetRequest.

        当前偏移量，默认为0。

        :param offset: The offset of this ShowDatasetRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ShowDatasetRequest.

        每页显示的最大作业个数，范围: [1, 100]。默认值：10。

        :return: The limit of this ShowDatasetRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowDatasetRequest.

        每页显示的最大作业个数，范围: [1, 100]。默认值：10。

        :param limit: The limit of this ShowDatasetRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ShowDatasetRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
