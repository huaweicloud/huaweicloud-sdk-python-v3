# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddJobsReqV11:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'job_type': 'int',
        'job_name': 'str',
        'jar_path': 'str',
        'arguments': 'str',
        'input': 'str',
        'output': 'str',
        'job_log': 'str',
        'hive_script_path': 'str',
        'hql': 'str',
        'shutdown_cluster': 'bool',
        'submit_job_once_cluster_run': 'bool',
        'file_action': 'str'
    }

    attribute_map = {
        'job_type': 'job_type',
        'job_name': 'job_name',
        'jar_path': 'jar_path',
        'arguments': 'arguments',
        'input': 'input',
        'output': 'output',
        'job_log': 'job_log',
        'hive_script_path': 'hive_script_path',
        'hql': 'hql',
        'shutdown_cluster': 'shutdown_cluster',
        'submit_job_once_cluster_run': 'submit_job_once_cluster_run',
        'file_action': 'file_action'
    }

    def __init__(self, job_type=None, job_name=None, jar_path=None, arguments=None, input=None, output=None, job_log=None, hive_script_path=None, hql=None, shutdown_cluster=None, submit_job_once_cluster_run=None, file_action=None):
        """AddJobsReqV11

        The model defined in huaweicloud sdk

        :param job_type: 作业类型码。 - 1：MapReduce - 2：Spark - 3：Hive Script - 4：HiveSQL（当前不支持） - 5：DistCp，导入、导出数据，（当前不支持）。 - 6：Spark Script - 7：Spark SQL，提交SQL语句，（当前不支持）。
        :type job_type: int
        :param job_name: 作业名称。 只能由字母、数字、中划线和下划线组成，并且长度为1～64个字符。 说明： 不同作业的名称允许相同，但不建议设置相同。
        :type job_name: str
        :param jar_path: 执行程序Jar包或sql文件地址，需要满足如下要求： - 最多为1023字符，不能包含;|&amp;&gt;,&lt;&#39;$特殊字符，且不可为空或全空格。 - 文件可存储于HDFS或者OBS中，不同的文件系统对应的路径存在差异。    - OBS：以“obs://”开头。不支持KMS加密的文件或程序。    - HDFS：以“/”开头。 - Spark Script需要以“.sql”结尾，MapReduce和Spark Jar需要以“.jar”结尾，sql和jar不区分大小写。
        :type jar_path: str
        :param arguments: 程序执行的关键参数，该参数由用户程序内的函数指定，MRS只负责参数的传入。 最多为150000字符，不能包含;|&amp;&gt;&#39;&lt;$特殊字符，可为空。
        :type arguments: str
        :param input: 数据输入地址。 文件可存储于HDFS或者OBS中，不同的文件系统对应的路径存在差异。 - OBS：以“obs://”开头。不支持KMS加密的文件或程序。 - HDFS：以“/”开头。 最多为1023字符，不能包含;|&amp;&gt;&#39;&lt;$特殊字符，可为空。
        :type input: str
        :param output: 数据输出地址。 文件可存储于HDFS或者OBS中，不同的文件系统对应的路径存在差异。 - OBS：以“obs://”开头。 - HDFS：以“/”开头。 如果该路径不存在，系统会自动创建。 最多为1023字符，不能包含;|&amp;&gt;&#39;&lt;$特殊字符，可为空。
        :type output: str
        :param job_log: 作业日志存储地址，该日志信息记录作业运行状态。 文件可存储于HDFS或者OBS中，不同的文件系统对应的路径存在差异。 - OBS：以“obs://”开头。 - HDFS：以“/”开头。 最多为1023字符，不能包含;|&amp;&gt;&#39;&lt;$特殊字符，可为空。
        :type job_log: str
        :param hive_script_path: sql程序路径，仅Spark Script和Hive Script作业需要使用此参数。需要满足如下要求： - 最多为1023字符，不能包含;|&amp;&gt;&lt;&#39;$特殊字符，且不可为空或全空格。 - 文件可存储于HDFS或者OBS中，不同的文件系统对应的路径存在差异。     - OBS：以“obs://”开头。不支持KMS加密的文件或程序。     - HDFS：以“/”开头。 - 需要以“.sql”结尾，sql不区分大小写。
        :type hive_script_path: str
        :param hql: HQL脚本语句。
        :type hql: str
        :param shutdown_cluster: 作业执行完成后，是否删除集群。 - true：是 - false：否
        :type shutdown_cluster: bool
        :param submit_job_once_cluster_run: - true：创建集群同时提交作业 - false：单独提交作业 此处应设置为true。
        :type submit_job_once_cluster_run: bool
        :param file_action: 数据导入导出。 - import - export
        :type file_action: str
        """
        
        

        self._job_type = None
        self._job_name = None
        self._jar_path = None
        self._arguments = None
        self._input = None
        self._output = None
        self._job_log = None
        self._hive_script_path = None
        self._hql = None
        self._shutdown_cluster = None
        self._submit_job_once_cluster_run = None
        self._file_action = None
        self.discriminator = None

        self.job_type = job_type
        self.job_name = job_name
        if jar_path is not None:
            self.jar_path = jar_path
        if arguments is not None:
            self.arguments = arguments
        if input is not None:
            self.input = input
        if output is not None:
            self.output = output
        if job_log is not None:
            self.job_log = job_log
        if hive_script_path is not None:
            self.hive_script_path = hive_script_path
        if hql is not None:
            self.hql = hql
        if shutdown_cluster is not None:
            self.shutdown_cluster = shutdown_cluster
        self.submit_job_once_cluster_run = submit_job_once_cluster_run
        if file_action is not None:
            self.file_action = file_action

    @property
    def job_type(self):
        """Gets the job_type of this AddJobsReqV11.

        作业类型码。 - 1：MapReduce - 2：Spark - 3：Hive Script - 4：HiveSQL（当前不支持） - 5：DistCp，导入、导出数据，（当前不支持）。 - 6：Spark Script - 7：Spark SQL，提交SQL语句，（当前不支持）。

        :return: The job_type of this AddJobsReqV11.
        :rtype: int
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this AddJobsReqV11.

        作业类型码。 - 1：MapReduce - 2：Spark - 3：Hive Script - 4：HiveSQL（当前不支持） - 5：DistCp，导入、导出数据，（当前不支持）。 - 6：Spark Script - 7：Spark SQL，提交SQL语句，（当前不支持）。

        :param job_type: The job_type of this AddJobsReqV11.
        :type job_type: int
        """
        self._job_type = job_type

    @property
    def job_name(self):
        """Gets the job_name of this AddJobsReqV11.

        作业名称。 只能由字母、数字、中划线和下划线组成，并且长度为1～64个字符。 说明： 不同作业的名称允许相同，但不建议设置相同。

        :return: The job_name of this AddJobsReqV11.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this AddJobsReqV11.

        作业名称。 只能由字母、数字、中划线和下划线组成，并且长度为1～64个字符。 说明： 不同作业的名称允许相同，但不建议设置相同。

        :param job_name: The job_name of this AddJobsReqV11.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def jar_path(self):
        """Gets the jar_path of this AddJobsReqV11.

        执行程序Jar包或sql文件地址，需要满足如下要求： - 最多为1023字符，不能包含;|&>,<'$特殊字符，且不可为空或全空格。 - 文件可存储于HDFS或者OBS中，不同的文件系统对应的路径存在差异。    - OBS：以“obs://”开头。不支持KMS加密的文件或程序。    - HDFS：以“/”开头。 - Spark Script需要以“.sql”结尾，MapReduce和Spark Jar需要以“.jar”结尾，sql和jar不区分大小写。

        :return: The jar_path of this AddJobsReqV11.
        :rtype: str
        """
        return self._jar_path

    @jar_path.setter
    def jar_path(self, jar_path):
        """Sets the jar_path of this AddJobsReqV11.

        执行程序Jar包或sql文件地址，需要满足如下要求： - 最多为1023字符，不能包含;|&>,<'$特殊字符，且不可为空或全空格。 - 文件可存储于HDFS或者OBS中，不同的文件系统对应的路径存在差异。    - OBS：以“obs://”开头。不支持KMS加密的文件或程序。    - HDFS：以“/”开头。 - Spark Script需要以“.sql”结尾，MapReduce和Spark Jar需要以“.jar”结尾，sql和jar不区分大小写。

        :param jar_path: The jar_path of this AddJobsReqV11.
        :type jar_path: str
        """
        self._jar_path = jar_path

    @property
    def arguments(self):
        """Gets the arguments of this AddJobsReqV11.

        程序执行的关键参数，该参数由用户程序内的函数指定，MRS只负责参数的传入。 最多为150000字符，不能包含;|&>'<$特殊字符，可为空。

        :return: The arguments of this AddJobsReqV11.
        :rtype: str
        """
        return self._arguments

    @arguments.setter
    def arguments(self, arguments):
        """Sets the arguments of this AddJobsReqV11.

        程序执行的关键参数，该参数由用户程序内的函数指定，MRS只负责参数的传入。 最多为150000字符，不能包含;|&>'<$特殊字符，可为空。

        :param arguments: The arguments of this AddJobsReqV11.
        :type arguments: str
        """
        self._arguments = arguments

    @property
    def input(self):
        """Gets the input of this AddJobsReqV11.

        数据输入地址。 文件可存储于HDFS或者OBS中，不同的文件系统对应的路径存在差异。 - OBS：以“obs://”开头。不支持KMS加密的文件或程序。 - HDFS：以“/”开头。 最多为1023字符，不能包含;|&>'<$特殊字符，可为空。

        :return: The input of this AddJobsReqV11.
        :rtype: str
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this AddJobsReqV11.

        数据输入地址。 文件可存储于HDFS或者OBS中，不同的文件系统对应的路径存在差异。 - OBS：以“obs://”开头。不支持KMS加密的文件或程序。 - HDFS：以“/”开头。 最多为1023字符，不能包含;|&>'<$特殊字符，可为空。

        :param input: The input of this AddJobsReqV11.
        :type input: str
        """
        self._input = input

    @property
    def output(self):
        """Gets the output of this AddJobsReqV11.

        数据输出地址。 文件可存储于HDFS或者OBS中，不同的文件系统对应的路径存在差异。 - OBS：以“obs://”开头。 - HDFS：以“/”开头。 如果该路径不存在，系统会自动创建。 最多为1023字符，不能包含;|&>'<$特殊字符，可为空。

        :return: The output of this AddJobsReqV11.
        :rtype: str
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this AddJobsReqV11.

        数据输出地址。 文件可存储于HDFS或者OBS中，不同的文件系统对应的路径存在差异。 - OBS：以“obs://”开头。 - HDFS：以“/”开头。 如果该路径不存在，系统会自动创建。 最多为1023字符，不能包含;|&>'<$特殊字符，可为空。

        :param output: The output of this AddJobsReqV11.
        :type output: str
        """
        self._output = output

    @property
    def job_log(self):
        """Gets the job_log of this AddJobsReqV11.

        作业日志存储地址，该日志信息记录作业运行状态。 文件可存储于HDFS或者OBS中，不同的文件系统对应的路径存在差异。 - OBS：以“obs://”开头。 - HDFS：以“/”开头。 最多为1023字符，不能包含;|&>'<$特殊字符，可为空。

        :return: The job_log of this AddJobsReqV11.
        :rtype: str
        """
        return self._job_log

    @job_log.setter
    def job_log(self, job_log):
        """Sets the job_log of this AddJobsReqV11.

        作业日志存储地址，该日志信息记录作业运行状态。 文件可存储于HDFS或者OBS中，不同的文件系统对应的路径存在差异。 - OBS：以“obs://”开头。 - HDFS：以“/”开头。 最多为1023字符，不能包含;|&>'<$特殊字符，可为空。

        :param job_log: The job_log of this AddJobsReqV11.
        :type job_log: str
        """
        self._job_log = job_log

    @property
    def hive_script_path(self):
        """Gets the hive_script_path of this AddJobsReqV11.

        sql程序路径，仅Spark Script和Hive Script作业需要使用此参数。需要满足如下要求： - 最多为1023字符，不能包含;|&><'$特殊字符，且不可为空或全空格。 - 文件可存储于HDFS或者OBS中，不同的文件系统对应的路径存在差异。     - OBS：以“obs://”开头。不支持KMS加密的文件或程序。     - HDFS：以“/”开头。 - 需要以“.sql”结尾，sql不区分大小写。

        :return: The hive_script_path of this AddJobsReqV11.
        :rtype: str
        """
        return self._hive_script_path

    @hive_script_path.setter
    def hive_script_path(self, hive_script_path):
        """Sets the hive_script_path of this AddJobsReqV11.

        sql程序路径，仅Spark Script和Hive Script作业需要使用此参数。需要满足如下要求： - 最多为1023字符，不能包含;|&><'$特殊字符，且不可为空或全空格。 - 文件可存储于HDFS或者OBS中，不同的文件系统对应的路径存在差异。     - OBS：以“obs://”开头。不支持KMS加密的文件或程序。     - HDFS：以“/”开头。 - 需要以“.sql”结尾，sql不区分大小写。

        :param hive_script_path: The hive_script_path of this AddJobsReqV11.
        :type hive_script_path: str
        """
        self._hive_script_path = hive_script_path

    @property
    def hql(self):
        """Gets the hql of this AddJobsReqV11.

        HQL脚本语句。

        :return: The hql of this AddJobsReqV11.
        :rtype: str
        """
        return self._hql

    @hql.setter
    def hql(self, hql):
        """Sets the hql of this AddJobsReqV11.

        HQL脚本语句。

        :param hql: The hql of this AddJobsReqV11.
        :type hql: str
        """
        self._hql = hql

    @property
    def shutdown_cluster(self):
        """Gets the shutdown_cluster of this AddJobsReqV11.

        作业执行完成后，是否删除集群。 - true：是 - false：否

        :return: The shutdown_cluster of this AddJobsReqV11.
        :rtype: bool
        """
        return self._shutdown_cluster

    @shutdown_cluster.setter
    def shutdown_cluster(self, shutdown_cluster):
        """Sets the shutdown_cluster of this AddJobsReqV11.

        作业执行完成后，是否删除集群。 - true：是 - false：否

        :param shutdown_cluster: The shutdown_cluster of this AddJobsReqV11.
        :type shutdown_cluster: bool
        """
        self._shutdown_cluster = shutdown_cluster

    @property
    def submit_job_once_cluster_run(self):
        """Gets the submit_job_once_cluster_run of this AddJobsReqV11.

        - true：创建集群同时提交作业 - false：单独提交作业 此处应设置为true。

        :return: The submit_job_once_cluster_run of this AddJobsReqV11.
        :rtype: bool
        """
        return self._submit_job_once_cluster_run

    @submit_job_once_cluster_run.setter
    def submit_job_once_cluster_run(self, submit_job_once_cluster_run):
        """Sets the submit_job_once_cluster_run of this AddJobsReqV11.

        - true：创建集群同时提交作业 - false：单独提交作业 此处应设置为true。

        :param submit_job_once_cluster_run: The submit_job_once_cluster_run of this AddJobsReqV11.
        :type submit_job_once_cluster_run: bool
        """
        self._submit_job_once_cluster_run = submit_job_once_cluster_run

    @property
    def file_action(self):
        """Gets the file_action of this AddJobsReqV11.

        数据导入导出。 - import - export

        :return: The file_action of this AddJobsReqV11.
        :rtype: str
        """
        return self._file_action

    @file_action.setter
    def file_action(self, file_action):
        """Sets the file_action of this AddJobsReqV11.

        数据导入导出。 - import - export

        :param file_action: The file_action of this AddJobsReqV11.
        :type file_action: str
        """
        self._file_action = file_action

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
        if not isinstance(other, AddJobsReqV11):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
