# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'type': 'str',
        'location': 'str',
        'depend_files': 'list[str]',
        'desc': 'str',
        'directory': 'str',
        'depend_packages': 'list[DependPackage]',
        'job_relation': 'list[Relation]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'location': 'location',
        'depend_files': 'dependFiles',
        'desc': 'desc',
        'directory': 'directory',
        'depend_packages': 'dependPackages',
        'job_relation': 'jobRelation'
    }

    def __init__(self, id=None, name=None, type=None, location=None, depend_files=None, desc=None, directory=None, depend_packages=None, job_relation=None):
        r"""ResourceInfo

        The model defined in huaweicloud sdk

        :param id: 资源id
        :type id: str
        :param name: 资源名称，只能包含英文字母、数字、中文字符、下划线或中划线。
        :type name: str
        :param type: 资源类型:   - archive: 压缩包   - file: 文件   - jar: jar文件   - pyFile：python文件
        :type type: str
        :param location: 资源文件所在OBS路径
        :type location: str
        :param depend_files: 主Jar包所依赖的JAR包、properties文件
        :type depend_files: list[str]
        :param desc: 资源描述
        :type desc: str
        :param directory: 资源所在目录
        :type directory: str
        :param depend_packages: 主Jar包所依赖的JAR包、properties文件。同时存在dependFiles和dependPackages时，优先解析该字段。
        :type depend_packages: list[:class:`huaweicloudsdkdgc.v1.DependPackage`]
        :param job_relation: 通过jar包名称查询相关的job
        :type job_relation: list[:class:`huaweicloudsdkdgc.v1.Relation`]
        """
        
        

        self._id = None
        self._name = None
        self._type = None
        self._location = None
        self._depend_files = None
        self._desc = None
        self._directory = None
        self._depend_packages = None
        self._job_relation = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if location is not None:
            self.location = location
        if depend_files is not None:
            self.depend_files = depend_files
        if desc is not None:
            self.desc = desc
        if directory is not None:
            self.directory = directory
        if depend_packages is not None:
            self.depend_packages = depend_packages
        if job_relation is not None:
            self.job_relation = job_relation

    @property
    def id(self):
        r"""Gets the id of this ResourceInfo.

        资源id

        :return: The id of this ResourceInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ResourceInfo.

        资源id

        :param id: The id of this ResourceInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ResourceInfo.

        资源名称，只能包含英文字母、数字、中文字符、下划线或中划线。

        :return: The name of this ResourceInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ResourceInfo.

        资源名称，只能包含英文字母、数字、中文字符、下划线或中划线。

        :param name: The name of this ResourceInfo.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this ResourceInfo.

        资源类型:   - archive: 压缩包   - file: 文件   - jar: jar文件   - pyFile：python文件

        :return: The type of this ResourceInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ResourceInfo.

        资源类型:   - archive: 压缩包   - file: 文件   - jar: jar文件   - pyFile：python文件

        :param type: The type of this ResourceInfo.
        :type type: str
        """
        self._type = type

    @property
    def location(self):
        r"""Gets the location of this ResourceInfo.

        资源文件所在OBS路径

        :return: The location of this ResourceInfo.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        r"""Sets the location of this ResourceInfo.

        资源文件所在OBS路径

        :param location: The location of this ResourceInfo.
        :type location: str
        """
        self._location = location

    @property
    def depend_files(self):
        r"""Gets the depend_files of this ResourceInfo.

        主Jar包所依赖的JAR包、properties文件

        :return: The depend_files of this ResourceInfo.
        :rtype: list[str]
        """
        return self._depend_files

    @depend_files.setter
    def depend_files(self, depend_files):
        r"""Sets the depend_files of this ResourceInfo.

        主Jar包所依赖的JAR包、properties文件

        :param depend_files: The depend_files of this ResourceInfo.
        :type depend_files: list[str]
        """
        self._depend_files = depend_files

    @property
    def desc(self):
        r"""Gets the desc of this ResourceInfo.

        资源描述

        :return: The desc of this ResourceInfo.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        r"""Sets the desc of this ResourceInfo.

        资源描述

        :param desc: The desc of this ResourceInfo.
        :type desc: str
        """
        self._desc = desc

    @property
    def directory(self):
        r"""Gets the directory of this ResourceInfo.

        资源所在目录

        :return: The directory of this ResourceInfo.
        :rtype: str
        """
        return self._directory

    @directory.setter
    def directory(self, directory):
        r"""Sets the directory of this ResourceInfo.

        资源所在目录

        :param directory: The directory of this ResourceInfo.
        :type directory: str
        """
        self._directory = directory

    @property
    def depend_packages(self):
        r"""Gets the depend_packages of this ResourceInfo.

        主Jar包所依赖的JAR包、properties文件。同时存在dependFiles和dependPackages时，优先解析该字段。

        :return: The depend_packages of this ResourceInfo.
        :rtype: list[:class:`huaweicloudsdkdgc.v1.DependPackage`]
        """
        return self._depend_packages

    @depend_packages.setter
    def depend_packages(self, depend_packages):
        r"""Sets the depend_packages of this ResourceInfo.

        主Jar包所依赖的JAR包、properties文件。同时存在dependFiles和dependPackages时，优先解析该字段。

        :param depend_packages: The depend_packages of this ResourceInfo.
        :type depend_packages: list[:class:`huaweicloudsdkdgc.v1.DependPackage`]
        """
        self._depend_packages = depend_packages

    @property
    def job_relation(self):
        r"""Gets the job_relation of this ResourceInfo.

        通过jar包名称查询相关的job

        :return: The job_relation of this ResourceInfo.
        :rtype: list[:class:`huaweicloudsdkdgc.v1.Relation`]
        """
        return self._job_relation

    @job_relation.setter
    def job_relation(self, job_relation):
        r"""Sets the job_relation of this ResourceInfo.

        通过jar包名称查询相关的job

        :param job_relation: The job_relation of this ResourceInfo.
        :type job_relation: list[:class:`huaweicloudsdkdgc.v1.Relation`]
        """
        self._job_relation = job_relation

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
        if not isinstance(other, ResourceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
