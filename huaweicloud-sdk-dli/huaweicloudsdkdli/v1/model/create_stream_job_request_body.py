# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateStreamJobRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'transaction_id': 'str',
        'job_type': 'str',
        'description': 'str',
        'tags': 'list[Tag]',
        'environment_config': 'StreamEnvironmentConfig',
        'runtime_config': 'StreamRuntimeConfig',
        'flink_sql_parameter': 'FlinkSqlParameter',
        'flink_jar_parameter': 'FlinkJarParameter'
    }

    attribute_map = {
        'transaction_id': 'transaction_id',
        'job_type': 'job_type',
        'description': 'description',
        'tags': 'tags',
        'environment_config': 'environment_config',
        'runtime_config': 'runtime_config',
        'flink_sql_parameter': 'flink_sql_parameter',
        'flink_jar_parameter': 'flink_jar_parameter'
    }

    def __init__(self, transaction_id=None, job_type=None, description=None, tags=None, environment_config=None, runtime_config=None, flink_sql_parameter=None, flink_jar_parameter=None):
        """CreateStreamJobRequestBody

        The model defined in huaweicloud sdk

        :param transaction_id: 流作业事务 ID，防止重复提交。长度限制：0-64个字符。
        :type transaction_id: str
        :param job_type: 作业类型：flink_sql_job或flink_jar_job
        :type job_type: str
        :param description: 流作业描述。长度限制：0-512个字符。
        :type description: str
        :param tags: 标签。
        :type tags: list[:class:`huaweicloudsdkdli.v1.Tag`]
        :param environment_config: 
        :type environment_config: :class:`huaweicloudsdkdli.v1.StreamEnvironmentConfig`
        :param runtime_config: 
        :type runtime_config: :class:`huaweicloudsdkdli.v1.StreamRuntimeConfig`
        :param flink_sql_parameter: 
        :type flink_sql_parameter: :class:`huaweicloudsdkdli.v1.FlinkSqlParameter`
        :param flink_jar_parameter: 
        :type flink_jar_parameter: :class:`huaweicloudsdkdli.v1.FlinkJarParameter`
        """
        
        

        self._transaction_id = None
        self._job_type = None
        self._description = None
        self._tags = None
        self._environment_config = None
        self._runtime_config = None
        self._flink_sql_parameter = None
        self._flink_jar_parameter = None
        self.discriminator = None

        self.transaction_id = transaction_id
        if job_type is not None:
            self.job_type = job_type
        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags
        if environment_config is not None:
            self.environment_config = environment_config
        if runtime_config is not None:
            self.runtime_config = runtime_config
        if flink_sql_parameter is not None:
            self.flink_sql_parameter = flink_sql_parameter
        if flink_jar_parameter is not None:
            self.flink_jar_parameter = flink_jar_parameter

    @property
    def transaction_id(self):
        """Gets the transaction_id of this CreateStreamJobRequestBody.

        流作业事务 ID，防止重复提交。长度限制：0-64个字符。

        :return: The transaction_id of this CreateStreamJobRequestBody.
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """Sets the transaction_id of this CreateStreamJobRequestBody.

        流作业事务 ID，防止重复提交。长度限制：0-64个字符。

        :param transaction_id: The transaction_id of this CreateStreamJobRequestBody.
        :type transaction_id: str
        """
        self._transaction_id = transaction_id

    @property
    def job_type(self):
        """Gets the job_type of this CreateStreamJobRequestBody.

        作业类型：flink_sql_job或flink_jar_job

        :return: The job_type of this CreateStreamJobRequestBody.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this CreateStreamJobRequestBody.

        作业类型：flink_sql_job或flink_jar_job

        :param job_type: The job_type of this CreateStreamJobRequestBody.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def description(self):
        """Gets the description of this CreateStreamJobRequestBody.

        流作业描述。长度限制：0-512个字符。

        :return: The description of this CreateStreamJobRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateStreamJobRequestBody.

        流作业描述。长度限制：0-512个字符。

        :param description: The description of this CreateStreamJobRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def tags(self):
        """Gets the tags of this CreateStreamJobRequestBody.

        标签。

        :return: The tags of this CreateStreamJobRequestBody.
        :rtype: list[:class:`huaweicloudsdkdli.v1.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateStreamJobRequestBody.

        标签。

        :param tags: The tags of this CreateStreamJobRequestBody.
        :type tags: list[:class:`huaweicloudsdkdli.v1.Tag`]
        """
        self._tags = tags

    @property
    def environment_config(self):
        """Gets the environment_config of this CreateStreamJobRequestBody.

        :return: The environment_config of this CreateStreamJobRequestBody.
        :rtype: :class:`huaweicloudsdkdli.v1.StreamEnvironmentConfig`
        """
        return self._environment_config

    @environment_config.setter
    def environment_config(self, environment_config):
        """Sets the environment_config of this CreateStreamJobRequestBody.

        :param environment_config: The environment_config of this CreateStreamJobRequestBody.
        :type environment_config: :class:`huaweicloudsdkdli.v1.StreamEnvironmentConfig`
        """
        self._environment_config = environment_config

    @property
    def runtime_config(self):
        """Gets the runtime_config of this CreateStreamJobRequestBody.

        :return: The runtime_config of this CreateStreamJobRequestBody.
        :rtype: :class:`huaweicloudsdkdli.v1.StreamRuntimeConfig`
        """
        return self._runtime_config

    @runtime_config.setter
    def runtime_config(self, runtime_config):
        """Sets the runtime_config of this CreateStreamJobRequestBody.

        :param runtime_config: The runtime_config of this CreateStreamJobRequestBody.
        :type runtime_config: :class:`huaweicloudsdkdli.v1.StreamRuntimeConfig`
        """
        self._runtime_config = runtime_config

    @property
    def flink_sql_parameter(self):
        """Gets the flink_sql_parameter of this CreateStreamJobRequestBody.

        :return: The flink_sql_parameter of this CreateStreamJobRequestBody.
        :rtype: :class:`huaweicloudsdkdli.v1.FlinkSqlParameter`
        """
        return self._flink_sql_parameter

    @flink_sql_parameter.setter
    def flink_sql_parameter(self, flink_sql_parameter):
        """Sets the flink_sql_parameter of this CreateStreamJobRequestBody.

        :param flink_sql_parameter: The flink_sql_parameter of this CreateStreamJobRequestBody.
        :type flink_sql_parameter: :class:`huaweicloudsdkdli.v1.FlinkSqlParameter`
        """
        self._flink_sql_parameter = flink_sql_parameter

    @property
    def flink_jar_parameter(self):
        """Gets the flink_jar_parameter of this CreateStreamJobRequestBody.

        :return: The flink_jar_parameter of this CreateStreamJobRequestBody.
        :rtype: :class:`huaweicloudsdkdli.v1.FlinkJarParameter`
        """
        return self._flink_jar_parameter

    @flink_jar_parameter.setter
    def flink_jar_parameter(self, flink_jar_parameter):
        """Sets the flink_jar_parameter of this CreateStreamJobRequestBody.

        :param flink_jar_parameter: The flink_jar_parameter of this CreateStreamJobRequestBody.
        :type flink_jar_parameter: :class:`huaweicloudsdkdli.v1.FlinkJarParameter`
        """
        self._flink_jar_parameter = flink_jar_parameter

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
        if not isinstance(other, CreateStreamJobRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
