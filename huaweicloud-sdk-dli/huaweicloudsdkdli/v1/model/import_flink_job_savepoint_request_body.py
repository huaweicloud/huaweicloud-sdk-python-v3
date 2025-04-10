# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImportFlinkJobSavepointRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'int',
        'savepoint_path': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'savepoint_path': 'savepoint_path'
    }

    def __init__(self, job_id=None, savepoint_path=None):
        r"""ImportFlinkJobSavepointRequestBody

        The model defined in huaweicloud sdk

        :param job_id: Flink作业的id
        :type job_id: int
        :param savepoint_path: Savepoint路径。需指定到_metaData文件的上级目录 例：\&quot;obs://bucket_name/file_name/\&quot;
        :type savepoint_path: str
        """
        
        

        self._job_id = None
        self._savepoint_path = None
        self.discriminator = None

        self.job_id = job_id
        self.savepoint_path = savepoint_path

    @property
    def job_id(self):
        r"""Gets the job_id of this ImportFlinkJobSavepointRequestBody.

        Flink作业的id

        :return: The job_id of this ImportFlinkJobSavepointRequestBody.
        :rtype: int
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ImportFlinkJobSavepointRequestBody.

        Flink作业的id

        :param job_id: The job_id of this ImportFlinkJobSavepointRequestBody.
        :type job_id: int
        """
        self._job_id = job_id

    @property
    def savepoint_path(self):
        r"""Gets the savepoint_path of this ImportFlinkJobSavepointRequestBody.

        Savepoint路径。需指定到_metaData文件的上级目录 例：\"obs://bucket_name/file_name/\"

        :return: The savepoint_path of this ImportFlinkJobSavepointRequestBody.
        :rtype: str
        """
        return self._savepoint_path

    @savepoint_path.setter
    def savepoint_path(self, savepoint_path):
        r"""Sets the savepoint_path of this ImportFlinkJobSavepointRequestBody.

        Savepoint路径。需指定到_metaData文件的上级目录 例：\"obs://bucket_name/file_name/\"

        :param savepoint_path: The savepoint_path of this ImportFlinkJobSavepointRequestBody.
        :type savepoint_path: str
        """
        self._savepoint_path = savepoint_path

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
        if not isinstance(other, ImportFlinkJobSavepointRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
