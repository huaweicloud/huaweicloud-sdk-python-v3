# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PythonJobConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'main_file_name': 'str',
        'main_arguments': 'list[str]',
        'python_packages': 'list[str]',
        'working_dir': 'str',
        'resource_spec': 'str',
        'user_log_path': 'str'
    }

    attribute_map = {
        'main_file_name': 'main_file_name',
        'main_arguments': 'main_arguments',
        'python_packages': 'python_packages',
        'working_dir': 'working_dir',
        'resource_spec': 'resource_spec',
        'user_log_path': 'user_log_path'
    }

    def __init__(self, main_file_name=None, main_arguments=None, python_packages=None, working_dir=None, resource_spec=None, user_log_path=None):
        r"""PythonJobConfig

        The model defined in huaweicloud sdk

        :param main_file_name: Job主文件，python文件，拼接在working_dir后可以是相对路径
        :type main_file_name: str
        :param main_arguments: Python主文件的运行参数
        :type main_arguments: list[str]
        :param python_packages: 依赖的python包列表
        :type python_packages: list[str]
        :param working_dir: 代码目录，obs目录
        :type working_dir: str
        :param resource_spec: 资源规格
        :type resource_spec: str
        :param user_log_path: 用户日志obs存储位置
        :type user_log_path: str
        """
        
        

        self._main_file_name = None
        self._main_arguments = None
        self._python_packages = None
        self._working_dir = None
        self._resource_spec = None
        self._user_log_path = None
        self.discriminator = None

        if main_file_name is not None:
            self.main_file_name = main_file_name
        if main_arguments is not None:
            self.main_arguments = main_arguments
        if python_packages is not None:
            self.python_packages = python_packages
        if working_dir is not None:
            self.working_dir = working_dir
        self.resource_spec = resource_spec
        if user_log_path is not None:
            self.user_log_path = user_log_path

    @property
    def main_file_name(self):
        r"""Gets the main_file_name of this PythonJobConfig.

        Job主文件，python文件，拼接在working_dir后可以是相对路径

        :return: The main_file_name of this PythonJobConfig.
        :rtype: str
        """
        return self._main_file_name

    @main_file_name.setter
    def main_file_name(self, main_file_name):
        r"""Sets the main_file_name of this PythonJobConfig.

        Job主文件，python文件，拼接在working_dir后可以是相对路径

        :param main_file_name: The main_file_name of this PythonJobConfig.
        :type main_file_name: str
        """
        self._main_file_name = main_file_name

    @property
    def main_arguments(self):
        r"""Gets the main_arguments of this PythonJobConfig.

        Python主文件的运行参数

        :return: The main_arguments of this PythonJobConfig.
        :rtype: list[str]
        """
        return self._main_arguments

    @main_arguments.setter
    def main_arguments(self, main_arguments):
        r"""Sets the main_arguments of this PythonJobConfig.

        Python主文件的运行参数

        :param main_arguments: The main_arguments of this PythonJobConfig.
        :type main_arguments: list[str]
        """
        self._main_arguments = main_arguments

    @property
    def python_packages(self):
        r"""Gets the python_packages of this PythonJobConfig.

        依赖的python包列表

        :return: The python_packages of this PythonJobConfig.
        :rtype: list[str]
        """
        return self._python_packages

    @python_packages.setter
    def python_packages(self, python_packages):
        r"""Sets the python_packages of this PythonJobConfig.

        依赖的python包列表

        :param python_packages: The python_packages of this PythonJobConfig.
        :type python_packages: list[str]
        """
        self._python_packages = python_packages

    @property
    def working_dir(self):
        r"""Gets the working_dir of this PythonJobConfig.

        代码目录，obs目录

        :return: The working_dir of this PythonJobConfig.
        :rtype: str
        """
        return self._working_dir

    @working_dir.setter
    def working_dir(self, working_dir):
        r"""Sets the working_dir of this PythonJobConfig.

        代码目录，obs目录

        :param working_dir: The working_dir of this PythonJobConfig.
        :type working_dir: str
        """
        self._working_dir = working_dir

    @property
    def resource_spec(self):
        r"""Gets the resource_spec of this PythonJobConfig.

        资源规格

        :return: The resource_spec of this PythonJobConfig.
        :rtype: str
        """
        return self._resource_spec

    @resource_spec.setter
    def resource_spec(self, resource_spec):
        r"""Sets the resource_spec of this PythonJobConfig.

        资源规格

        :param resource_spec: The resource_spec of this PythonJobConfig.
        :type resource_spec: str
        """
        self._resource_spec = resource_spec

    @property
    def user_log_path(self):
        r"""Gets the user_log_path of this PythonJobConfig.

        用户日志obs存储位置

        :return: The user_log_path of this PythonJobConfig.
        :rtype: str
        """
        return self._user_log_path

    @user_log_path.setter
    def user_log_path(self, user_log_path):
        r"""Sets the user_log_path of this PythonJobConfig.

        用户日志obs存储位置

        :param user_log_path: The user_log_path of this PythonJobConfig.
        :type user_log_path: str
        """
        self._user_log_path = user_log_path

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
        if not isinstance(other, PythonJobConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
