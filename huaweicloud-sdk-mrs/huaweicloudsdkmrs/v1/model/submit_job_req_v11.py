# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubmitJobReqV11:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'job_name': 'str',
        'cluster_id': 'str',
        'jar_path': 'str',
        'input': 'str',
        'output': 'str',
        'job_log': 'str',
        'job_type': 'int',
        'file_action': 'str',
        'arguments': 'str',
        'hql': 'str',
        'hive_script_path': 'str'
    }

    attribute_map = {
        'job_name': 'job_name',
        'cluster_id': 'cluster_id',
        'jar_path': 'jar_path',
        'input': 'input',
        'output': 'output',
        'job_log': 'job_log',
        'job_type': 'job_type',
        'file_action': 'file_action',
        'arguments': 'arguments',
        'hql': 'hql',
        'hive_script_path': 'hive_script_path'
    }

    def __init__(self, job_name=None, cluster_id=None, jar_path=None, input=None, output=None, job_log=None, job_type=None, file_action=None, arguments=None, hql=None, hive_script_path=None):
        """SubmitJobReqV11

        The model defined in huaweicloud sdk

        :param job_name: 作业名称，只能由字母、数字、中划线和下划线组成，并且长度为1～64个字符。  说明： 不同作业的名称允许相同，但不建议设置相同。
        :type job_name: str
        :param cluster_id: 集群ID。
        :type cluster_id: str
        :param jar_path: 执行程序Jar包或sql文件地址，需要满足如下要求： - 最多为1023字符，不能包含;|&amp;&gt;&lt;&#39;$特殊字符，且不可为空或全空格。 - 需要以“/”或“s3a://”开头。OBS路径不支持KMS加密的文件或程序。 - Spark Script需要以“.sql”结尾，MapReduce和Spark Jar需要以“.jar”结尾，sql和jar不区分大小写。 说明： 作业类型为MapReduce或Spark时，jar_path参数为必选。
        :type jar_path: str
        :param input: 数据输入地址，必须以“/”或“s3a://”开头。请配置为正确的OBS路径，OBS路径不支持KMS加密的文件或程序。  最多为1023字符，不能包含;|&amp;&gt;&#39;&lt;$特殊字符，可为空。
        :type input: str
        :param output: 数据输出地址，必须以“/”或“s3a://”开头。请配置为正确的OBS路径，如果该路径不存在，系统会自动创建。  最多为1023字符，不能包含;|&amp;&gt;&#39;&lt;$特殊字符，可为空。
        :type output: str
        :param job_log: 作业日志存储地址，该日志信息记录作业运行状态。必须以“/”或“s3a://”开头，请配置为正确的OBS路径。  最多为1023字符，不能包含;|&amp;&gt;&#39;&lt;$特殊字符，可为空。
        :type job_log: str
        :param job_type: 作业类型码。  - 1：MapReduce - 2：Spark - 3：Hive Script - 4：HiveSQL（当前不支持） - 5：DistCp，导入、导出数据。 - 6：Spark Script - 7：Spark SQL，提交SQL语句（该接口当前不支持）
        :type job_type: int
        :param file_action: 文件操作类型，包括： - export：从HDFS导出数据至OBS - import：从OBS导入数据至HDFS
        :type file_action: str
        :param arguments: 程序执行的关键参数，该参数由用户程序内的函数指定，MRS只负责参数的传入。 最多为150000字符，不能包含;|&amp;&gt;&#39;&lt;$!\\\&quot;\\特殊字符，可为空。 说明： 用户输入带有敏感信息（如登录密码）的参数时，可通过在参数名前添加“@”的方式，为该参数值加密，以防止敏感信息被明文形式持久化。在查看作业信息时，敏感信息显示为“*”。 例如：username&#x3D;admin @password&#x3D;admin_123
        :type arguments: str
        :param hql: Spark SQL语句，该语句需要进行Base64编码和解码，“ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/”为标准的编码表，MRS使用“ABCDEFGHILKJMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/”进行Base64编码。在编码后所得字符串首位任意加上一个字母，即得到Hql参数的值。后台自动进行解码得到Spark SQL语句。 使用样例： 1) 在Web界面输入Spark SQL语句“show tables;”。 2) 使用“ABCDEFGHILKJMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/”编码后得到字符串“c2hvdyB0YWLsZXM7”。 3) 在“c2hvdyB0YWLsZXM7”首位任意加上一字母，例如“gc2hvdyB0YWLsZXM7”，即Hql参数的值。 4) 后台自动进行解码得到Spark SQL语句“show tables;”。 
        :type hql: str
        :param hive_script_path: sql程序路径，仅Spark Script和Hive Script作业需要使用此参数。需要满足如下要求：  - 最多为1023字符，不能包含;|&amp;&gt;&lt;&#39;$特殊字符，且不可为空或全空格。 - 需要以“/”或“s3a://”开头，OBS路径不支持KMS加密的文件或程序。 - 需要以“.sql”结尾，sql不区分大小写。
        :type hive_script_path: str
        """
        
        

        self._job_name = None
        self._cluster_id = None
        self._jar_path = None
        self._input = None
        self._output = None
        self._job_log = None
        self._job_type = None
        self._file_action = None
        self._arguments = None
        self._hql = None
        self._hive_script_path = None
        self.discriminator = None

        self.job_name = job_name
        self.cluster_id = cluster_id
        if jar_path is not None:
            self.jar_path = jar_path
        if input is not None:
            self.input = input
        if output is not None:
            self.output = output
        if job_log is not None:
            self.job_log = job_log
        self.job_type = job_type
        if file_action is not None:
            self.file_action = file_action
        if arguments is not None:
            self.arguments = arguments
        if hql is not None:
            self.hql = hql
        if hive_script_path is not None:
            self.hive_script_path = hive_script_path

    @property
    def job_name(self):
        """Gets the job_name of this SubmitJobReqV11.

        作业名称，只能由字母、数字、中划线和下划线组成，并且长度为1～64个字符。  说明： 不同作业的名称允许相同，但不建议设置相同。

        :return: The job_name of this SubmitJobReqV11.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this SubmitJobReqV11.

        作业名称，只能由字母、数字、中划线和下划线组成，并且长度为1～64个字符。  说明： 不同作业的名称允许相同，但不建议设置相同。

        :param job_name: The job_name of this SubmitJobReqV11.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def cluster_id(self):
        """Gets the cluster_id of this SubmitJobReqV11.

        集群ID。

        :return: The cluster_id of this SubmitJobReqV11.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this SubmitJobReqV11.

        集群ID。

        :param cluster_id: The cluster_id of this SubmitJobReqV11.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def jar_path(self):
        """Gets the jar_path of this SubmitJobReqV11.

        执行程序Jar包或sql文件地址，需要满足如下要求： - 最多为1023字符，不能包含;|&><'$特殊字符，且不可为空或全空格。 - 需要以“/”或“s3a://”开头。OBS路径不支持KMS加密的文件或程序。 - Spark Script需要以“.sql”结尾，MapReduce和Spark Jar需要以“.jar”结尾，sql和jar不区分大小写。 说明： 作业类型为MapReduce或Spark时，jar_path参数为必选。

        :return: The jar_path of this SubmitJobReqV11.
        :rtype: str
        """
        return self._jar_path

    @jar_path.setter
    def jar_path(self, jar_path):
        """Sets the jar_path of this SubmitJobReqV11.

        执行程序Jar包或sql文件地址，需要满足如下要求： - 最多为1023字符，不能包含;|&><'$特殊字符，且不可为空或全空格。 - 需要以“/”或“s3a://”开头。OBS路径不支持KMS加密的文件或程序。 - Spark Script需要以“.sql”结尾，MapReduce和Spark Jar需要以“.jar”结尾，sql和jar不区分大小写。 说明： 作业类型为MapReduce或Spark时，jar_path参数为必选。

        :param jar_path: The jar_path of this SubmitJobReqV11.
        :type jar_path: str
        """
        self._jar_path = jar_path

    @property
    def input(self):
        """Gets the input of this SubmitJobReqV11.

        数据输入地址，必须以“/”或“s3a://”开头。请配置为正确的OBS路径，OBS路径不支持KMS加密的文件或程序。  最多为1023字符，不能包含;|&>'<$特殊字符，可为空。

        :return: The input of this SubmitJobReqV11.
        :rtype: str
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this SubmitJobReqV11.

        数据输入地址，必须以“/”或“s3a://”开头。请配置为正确的OBS路径，OBS路径不支持KMS加密的文件或程序。  最多为1023字符，不能包含;|&>'<$特殊字符，可为空。

        :param input: The input of this SubmitJobReqV11.
        :type input: str
        """
        self._input = input

    @property
    def output(self):
        """Gets the output of this SubmitJobReqV11.

        数据输出地址，必须以“/”或“s3a://”开头。请配置为正确的OBS路径，如果该路径不存在，系统会自动创建。  最多为1023字符，不能包含;|&>'<$特殊字符，可为空。

        :return: The output of this SubmitJobReqV11.
        :rtype: str
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this SubmitJobReqV11.

        数据输出地址，必须以“/”或“s3a://”开头。请配置为正确的OBS路径，如果该路径不存在，系统会自动创建。  最多为1023字符，不能包含;|&>'<$特殊字符，可为空。

        :param output: The output of this SubmitJobReqV11.
        :type output: str
        """
        self._output = output

    @property
    def job_log(self):
        """Gets the job_log of this SubmitJobReqV11.

        作业日志存储地址，该日志信息记录作业运行状态。必须以“/”或“s3a://”开头，请配置为正确的OBS路径。  最多为1023字符，不能包含;|&>'<$特殊字符，可为空。

        :return: The job_log of this SubmitJobReqV11.
        :rtype: str
        """
        return self._job_log

    @job_log.setter
    def job_log(self, job_log):
        """Sets the job_log of this SubmitJobReqV11.

        作业日志存储地址，该日志信息记录作业运行状态。必须以“/”或“s3a://”开头，请配置为正确的OBS路径。  最多为1023字符，不能包含;|&>'<$特殊字符，可为空。

        :param job_log: The job_log of this SubmitJobReqV11.
        :type job_log: str
        """
        self._job_log = job_log

    @property
    def job_type(self):
        """Gets the job_type of this SubmitJobReqV11.

        作业类型码。  - 1：MapReduce - 2：Spark - 3：Hive Script - 4：HiveSQL（当前不支持） - 5：DistCp，导入、导出数据。 - 6：Spark Script - 7：Spark SQL，提交SQL语句（该接口当前不支持）

        :return: The job_type of this SubmitJobReqV11.
        :rtype: int
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this SubmitJobReqV11.

        作业类型码。  - 1：MapReduce - 2：Spark - 3：Hive Script - 4：HiveSQL（当前不支持） - 5：DistCp，导入、导出数据。 - 6：Spark Script - 7：Spark SQL，提交SQL语句（该接口当前不支持）

        :param job_type: The job_type of this SubmitJobReqV11.
        :type job_type: int
        """
        self._job_type = job_type

    @property
    def file_action(self):
        """Gets the file_action of this SubmitJobReqV11.

        文件操作类型，包括： - export：从HDFS导出数据至OBS - import：从OBS导入数据至HDFS

        :return: The file_action of this SubmitJobReqV11.
        :rtype: str
        """
        return self._file_action

    @file_action.setter
    def file_action(self, file_action):
        """Sets the file_action of this SubmitJobReqV11.

        文件操作类型，包括： - export：从HDFS导出数据至OBS - import：从OBS导入数据至HDFS

        :param file_action: The file_action of this SubmitJobReqV11.
        :type file_action: str
        """
        self._file_action = file_action

    @property
    def arguments(self):
        """Gets the arguments of this SubmitJobReqV11.

        程序执行的关键参数，该参数由用户程序内的函数指定，MRS只负责参数的传入。 最多为150000字符，不能包含;|&>'<$!\\\"\\特殊字符，可为空。 说明： 用户输入带有敏感信息（如登录密码）的参数时，可通过在参数名前添加“@”的方式，为该参数值加密，以防止敏感信息被明文形式持久化。在查看作业信息时，敏感信息显示为“*”。 例如：username=admin @password=admin_123

        :return: The arguments of this SubmitJobReqV11.
        :rtype: str
        """
        return self._arguments

    @arguments.setter
    def arguments(self, arguments):
        """Sets the arguments of this SubmitJobReqV11.

        程序执行的关键参数，该参数由用户程序内的函数指定，MRS只负责参数的传入。 最多为150000字符，不能包含;|&>'<$!\\\"\\特殊字符，可为空。 说明： 用户输入带有敏感信息（如登录密码）的参数时，可通过在参数名前添加“@”的方式，为该参数值加密，以防止敏感信息被明文形式持久化。在查看作业信息时，敏感信息显示为“*”。 例如：username=admin @password=admin_123

        :param arguments: The arguments of this SubmitJobReqV11.
        :type arguments: str
        """
        self._arguments = arguments

    @property
    def hql(self):
        """Gets the hql of this SubmitJobReqV11.

        Spark SQL语句，该语句需要进行Base64编码和解码，“ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/”为标准的编码表，MRS使用“ABCDEFGHILKJMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/”进行Base64编码。在编码后所得字符串首位任意加上一个字母，即得到Hql参数的值。后台自动进行解码得到Spark SQL语句。 使用样例： 1) 在Web界面输入Spark SQL语句“show tables;”。 2) 使用“ABCDEFGHILKJMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/”编码后得到字符串“c2hvdyB0YWLsZXM7”。 3) 在“c2hvdyB0YWLsZXM7”首位任意加上一字母，例如“gc2hvdyB0YWLsZXM7”，即Hql参数的值。 4) 后台自动进行解码得到Spark SQL语句“show tables;”。 

        :return: The hql of this SubmitJobReqV11.
        :rtype: str
        """
        return self._hql

    @hql.setter
    def hql(self, hql):
        """Sets the hql of this SubmitJobReqV11.

        Spark SQL语句，该语句需要进行Base64编码和解码，“ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/”为标准的编码表，MRS使用“ABCDEFGHILKJMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/”进行Base64编码。在编码后所得字符串首位任意加上一个字母，即得到Hql参数的值。后台自动进行解码得到Spark SQL语句。 使用样例： 1) 在Web界面输入Spark SQL语句“show tables;”。 2) 使用“ABCDEFGHILKJMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/”编码后得到字符串“c2hvdyB0YWLsZXM7”。 3) 在“c2hvdyB0YWLsZXM7”首位任意加上一字母，例如“gc2hvdyB0YWLsZXM7”，即Hql参数的值。 4) 后台自动进行解码得到Spark SQL语句“show tables;”。 

        :param hql: The hql of this SubmitJobReqV11.
        :type hql: str
        """
        self._hql = hql

    @property
    def hive_script_path(self):
        """Gets the hive_script_path of this SubmitJobReqV11.

        sql程序路径，仅Spark Script和Hive Script作业需要使用此参数。需要满足如下要求：  - 最多为1023字符，不能包含;|&><'$特殊字符，且不可为空或全空格。 - 需要以“/”或“s3a://”开头，OBS路径不支持KMS加密的文件或程序。 - 需要以“.sql”结尾，sql不区分大小写。

        :return: The hive_script_path of this SubmitJobReqV11.
        :rtype: str
        """
        return self._hive_script_path

    @hive_script_path.setter
    def hive_script_path(self, hive_script_path):
        """Sets the hive_script_path of this SubmitJobReqV11.

        sql程序路径，仅Spark Script和Hive Script作业需要使用此参数。需要满足如下要求：  - 最多为1023字符，不能包含;|&><'$特殊字符，且不可为空或全空格。 - 需要以“/”或“s3a://”开头，OBS路径不支持KMS加密的文件或程序。 - 需要以“.sql”结尾，sql不区分大小写。

        :param hive_script_path: The hive_script_path of this SubmitJobReqV11.
        :type hive_script_path: str
        """
        self._hive_script_path = hive_script_path

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
        if not isinstance(other, SubmitJobReqV11):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
