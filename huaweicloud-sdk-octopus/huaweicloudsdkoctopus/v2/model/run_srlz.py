# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RunSrlz:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'command': 'str',
        'keyword': 'str',
        'cpu': 'float',
        'memory': 'int',
        'gpu': 'int',
        'pkg_log_dir': 'str'
    }

    attribute_map = {
        'command': 'command',
        'keyword': 'keyword',
        'cpu': 'cpu',
        'memory': 'memory',
        'gpu': 'gpu',
        'pkg_log_dir': 'pkg_log_dir'
    }

    def __init__(self, command=None, keyword=None, cpu=None, memory=None, gpu=None, pkg_log_dir=None):
        r"""RunSrlz

        The model defined in huaweicloud sdk

        :param command: 运行命令
        :type command: str
        :param keyword: 算法关键字
        :type keyword: str
        :param cpu: cpu配额
        :type cpu: float
        :param memory: 内存配额
        :type memory: int
        :param gpu: gpu配额
        :type gpu: int
        :param pkg_log_dir: 日志目录打包路径
        :type pkg_log_dir: str
        """
        
        

        self._command = None
        self._keyword = None
        self._cpu = None
        self._memory = None
        self._gpu = None
        self._pkg_log_dir = None
        self.discriminator = None

        self.command = command
        self.keyword = keyword
        self.cpu = cpu
        self.memory = memory
        self.gpu = gpu
        self.pkg_log_dir = pkg_log_dir

    @property
    def command(self):
        r"""Gets the command of this RunSrlz.

        运行命令

        :return: The command of this RunSrlz.
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        r"""Sets the command of this RunSrlz.

        运行命令

        :param command: The command of this RunSrlz.
        :type command: str
        """
        self._command = command

    @property
    def keyword(self):
        r"""Gets the keyword of this RunSrlz.

        算法关键字

        :return: The keyword of this RunSrlz.
        :rtype: str
        """
        return self._keyword

    @keyword.setter
    def keyword(self, keyword):
        r"""Sets the keyword of this RunSrlz.

        算法关键字

        :param keyword: The keyword of this RunSrlz.
        :type keyword: str
        """
        self._keyword = keyword

    @property
    def cpu(self):
        r"""Gets the cpu of this RunSrlz.

        cpu配额

        :return: The cpu of this RunSrlz.
        :rtype: float
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        r"""Sets the cpu of this RunSrlz.

        cpu配额

        :param cpu: The cpu of this RunSrlz.
        :type cpu: float
        """
        self._cpu = cpu

    @property
    def memory(self):
        r"""Gets the memory of this RunSrlz.

        内存配额

        :return: The memory of this RunSrlz.
        :rtype: int
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        r"""Sets the memory of this RunSrlz.

        内存配额

        :param memory: The memory of this RunSrlz.
        :type memory: int
        """
        self._memory = memory

    @property
    def gpu(self):
        r"""Gets the gpu of this RunSrlz.

        gpu配额

        :return: The gpu of this RunSrlz.
        :rtype: int
        """
        return self._gpu

    @gpu.setter
    def gpu(self, gpu):
        r"""Sets the gpu of this RunSrlz.

        gpu配额

        :param gpu: The gpu of this RunSrlz.
        :type gpu: int
        """
        self._gpu = gpu

    @property
    def pkg_log_dir(self):
        r"""Gets the pkg_log_dir of this RunSrlz.

        日志目录打包路径

        :return: The pkg_log_dir of this RunSrlz.
        :rtype: str
        """
        return self._pkg_log_dir

    @pkg_log_dir.setter
    def pkg_log_dir(self, pkg_log_dir):
        r"""Sets the pkg_log_dir of this RunSrlz.

        日志目录打包路径

        :param pkg_log_dir: The pkg_log_dir of this RunSrlz.
        :type pkg_log_dir: str
        """
        self._pkg_log_dir = pkg_log_dir

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
        if not isinstance(other, RunSrlz):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
