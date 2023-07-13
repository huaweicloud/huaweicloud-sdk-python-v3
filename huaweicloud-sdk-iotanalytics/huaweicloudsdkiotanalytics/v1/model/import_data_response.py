# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImportDataResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'table_id': 'str',
        'job_id': 'str',
        'run_id': 'str'
    }

    attribute_map = {
        'table_id': 'table_id',
        'job_id': 'job_id',
        'run_id': 'run_id'
    }

    def __init__(self, table_id=None, job_id=None, run_id=None):
        """ImportDataResponse

        The model defined in huaweicloud sdk

        :param table_id: 表ID。
        :type table_id: str
        :param job_id: 作业ID。
        :type job_id: str
        :param run_id: 作业运行ID。
        :type run_id: str
        """
        
        super(ImportDataResponse, self).__init__()

        self._table_id = None
        self._job_id = None
        self._run_id = None
        self.discriminator = None

        if table_id is not None:
            self.table_id = table_id
        if job_id is not None:
            self.job_id = job_id
        if run_id is not None:
            self.run_id = run_id

    @property
    def table_id(self):
        """Gets the table_id of this ImportDataResponse.

        表ID。

        :return: The table_id of this ImportDataResponse.
        :rtype: str
        """
        return self._table_id

    @table_id.setter
    def table_id(self, table_id):
        """Sets the table_id of this ImportDataResponse.

        表ID。

        :param table_id: The table_id of this ImportDataResponse.
        :type table_id: str
        """
        self._table_id = table_id

    @property
    def job_id(self):
        """Gets the job_id of this ImportDataResponse.

        作业ID。

        :return: The job_id of this ImportDataResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ImportDataResponse.

        作业ID。

        :param job_id: The job_id of this ImportDataResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def run_id(self):
        """Gets the run_id of this ImportDataResponse.

        作业运行ID。

        :return: The run_id of this ImportDataResponse.
        :rtype: str
        """
        return self._run_id

    @run_id.setter
    def run_id(self, run_id):
        """Sets the run_id of this ImportDataResponse.

        作业运行ID。

        :param run_id: The run_id of this ImportDataResponse.
        :type run_id: str
        """
        self._run_id = run_id

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
        if not isinstance(other, ImportDataResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
