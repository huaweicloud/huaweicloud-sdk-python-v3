# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MigrateResultsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'db_name': 'str',
        'job_id': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'db_name': 'db_name',
        'job_id': 'job_id'
    }

    def __init__(self, instance_id=None, db_name=None, job_id=None):
        r"""MigrateResultsRequest

        The model defined in huaweicloud sdk

        :param instance_id: DDM实例ID
        :type instance_id: str
        :param db_name: 逻辑库名称
        :type db_name: str
        :param job_id: 任务流id
        :type job_id: str
        """
        
        

        self._instance_id = None
        self._db_name = None
        self._job_id = None
        self.discriminator = None

        self.instance_id = instance_id
        self.db_name = db_name
        self.job_id = job_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this MigrateResultsRequest.

        DDM实例ID

        :return: The instance_id of this MigrateResultsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this MigrateResultsRequest.

        DDM实例ID

        :param instance_id: The instance_id of this MigrateResultsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def db_name(self):
        r"""Gets the db_name of this MigrateResultsRequest.

        逻辑库名称

        :return: The db_name of this MigrateResultsRequest.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        r"""Sets the db_name of this MigrateResultsRequest.

        逻辑库名称

        :param db_name: The db_name of this MigrateResultsRequest.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def job_id(self):
        r"""Gets the job_id of this MigrateResultsRequest.

        任务流id

        :return: The job_id of this MigrateResultsRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this MigrateResultsRequest.

        任务流id

        :param job_id: The job_id of this MigrateResultsRequest.
        :type job_id: str
        """
        self._job_id = job_id

    def to_dict(self):
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
        if not isinstance(other, MigrateResultsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
