# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobExecution:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'job_type': 'str',
        'job_name': 'str',
        'arguments': 'list[str]',
        'properties': 'dict(str, str)'
    }

    attribute_map = {
        'job_type': 'job_type',
        'job_name': 'job_name',
        'arguments': 'arguments',
        'properties': 'properties'
    }

    def __init__(self, job_type=None, job_name=None, arguments=None, properties=None):
        """JobExecution

        The model defined in huaweicloud sdk

        :param job_type: 作业类型: - MapReduce - SparkSubmit - SparkPython：该类型作业将转换为SparkSubmit类型提交，MRS控制台界面的作业类型展示为SparkSubmit，通过接口查询作业列表信息时作业类型请选择SparkSubmit。 - HiveScript - HiveSql - DistCp，导入、导出数据。 - SparkScript - SparkSql - Flink
        :type job_type: str
        :param job_name: 作业名称，只能由字母、数字、中划线和下划线组成，并且长度为1～64个字符。 说明： 不同作业的名称允许相同，但不建议设置相同。
        :type job_name: str
        :param arguments: 程序执行的关键参数，该参数由用户程序内的函数指定，MRS只负责参数的传入。 最多为150000字符，不能包含;|&amp;&gt;&#39;&lt;$!\\\&quot;\\特殊字符，可为空。 说明： - 若输入带有敏感信息（如登录密码）的参数可能在作业详情展示和日志打印中存在暴露的风险，请谨慎操作。 - 提交HiveScript或HiveSql类型的作业时如需以“obs://”开头格式访问存储在OBS上的文件，请在Hive服务配置页面搜索参数“core.site.customized.configs”，新增OBS的endpoint配置项，参数为“fs.obs.endpoint”，值请输入OBS对应的endpoint，具体请参考[终端节点](https://support.huaweicloud.com/api-mrs/mrs_02_0003.html)。
        :type arguments: list[str]
        :param properties: 程序系统参数。 最多为2048字符，不能包含&gt;&lt;|&#39;&#x60;&amp;!\\特殊字符，可为空。
        :type properties: dict(str, str)
        """
        
        

        self._job_type = None
        self._job_name = None
        self._arguments = None
        self._properties = None
        self.discriminator = None

        self.job_type = job_type
        self.job_name = job_name
        if arguments is not None:
            self.arguments = arguments
        if properties is not None:
            self.properties = properties

    @property
    def job_type(self):
        """Gets the job_type of this JobExecution.

        作业类型: - MapReduce - SparkSubmit - SparkPython：该类型作业将转换为SparkSubmit类型提交，MRS控制台界面的作业类型展示为SparkSubmit，通过接口查询作业列表信息时作业类型请选择SparkSubmit。 - HiveScript - HiveSql - DistCp，导入、导出数据。 - SparkScript - SparkSql - Flink

        :return: The job_type of this JobExecution.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this JobExecution.

        作业类型: - MapReduce - SparkSubmit - SparkPython：该类型作业将转换为SparkSubmit类型提交，MRS控制台界面的作业类型展示为SparkSubmit，通过接口查询作业列表信息时作业类型请选择SparkSubmit。 - HiveScript - HiveSql - DistCp，导入、导出数据。 - SparkScript - SparkSql - Flink

        :param job_type: The job_type of this JobExecution.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def job_name(self):
        """Gets the job_name of this JobExecution.

        作业名称，只能由字母、数字、中划线和下划线组成，并且长度为1～64个字符。 说明： 不同作业的名称允许相同，但不建议设置相同。

        :return: The job_name of this JobExecution.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this JobExecution.

        作业名称，只能由字母、数字、中划线和下划线组成，并且长度为1～64个字符。 说明： 不同作业的名称允许相同，但不建议设置相同。

        :param job_name: The job_name of this JobExecution.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def arguments(self):
        """Gets the arguments of this JobExecution.

        程序执行的关键参数，该参数由用户程序内的函数指定，MRS只负责参数的传入。 最多为150000字符，不能包含;|&>'<$!\\\"\\特殊字符，可为空。 说明： - 若输入带有敏感信息（如登录密码）的参数可能在作业详情展示和日志打印中存在暴露的风险，请谨慎操作。 - 提交HiveScript或HiveSql类型的作业时如需以“obs://”开头格式访问存储在OBS上的文件，请在Hive服务配置页面搜索参数“core.site.customized.configs”，新增OBS的endpoint配置项，参数为“fs.obs.endpoint”，值请输入OBS对应的endpoint，具体请参考[终端节点](https://support.huaweicloud.com/api-mrs/mrs_02_0003.html)。

        :return: The arguments of this JobExecution.
        :rtype: list[str]
        """
        return self._arguments

    @arguments.setter
    def arguments(self, arguments):
        """Sets the arguments of this JobExecution.

        程序执行的关键参数，该参数由用户程序内的函数指定，MRS只负责参数的传入。 最多为150000字符，不能包含;|&>'<$!\\\"\\特殊字符，可为空。 说明： - 若输入带有敏感信息（如登录密码）的参数可能在作业详情展示和日志打印中存在暴露的风险，请谨慎操作。 - 提交HiveScript或HiveSql类型的作业时如需以“obs://”开头格式访问存储在OBS上的文件，请在Hive服务配置页面搜索参数“core.site.customized.configs”，新增OBS的endpoint配置项，参数为“fs.obs.endpoint”，值请输入OBS对应的endpoint，具体请参考[终端节点](https://support.huaweicloud.com/api-mrs/mrs_02_0003.html)。

        :param arguments: The arguments of this JobExecution.
        :type arguments: list[str]
        """
        self._arguments = arguments

    @property
    def properties(self):
        """Gets the properties of this JobExecution.

        程序系统参数。 最多为2048字符，不能包含><|'`&!\\特殊字符，可为空。

        :return: The properties of this JobExecution.
        :rtype: dict(str, str)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this JobExecution.

        程序系统参数。 最多为2048字符，不能包含><|'`&!\\特殊字符，可为空。

        :param properties: The properties of this JobExecution.
        :type properties: dict(str, str)
        """
        self._properties = properties

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
        if not isinstance(other, JobExecution):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
