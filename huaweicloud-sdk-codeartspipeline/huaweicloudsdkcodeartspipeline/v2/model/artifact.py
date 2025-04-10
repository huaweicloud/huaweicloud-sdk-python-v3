# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Artifact:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'name': 'str',
        'artifact_version': 'str',
        'upload_target': 'str',
        'artifact_package_type': 'str',
        'artifact_uri': 'str',
        'artifact_download_url_with_id': 'str',
        'artifact_type': 'str',
        'hash_code': 'list[ArtifactHashCode]',
        'job_id': 'str',
        'build_no': 'int',
        'daily_build_number': 'str',
        'file_size': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'name': 'name',
        'artifact_version': 'artifact_version',
        'upload_target': 'upload_target',
        'artifact_package_type': 'artifact_package_type',
        'artifact_uri': 'artifact_uri',
        'artifact_download_url_with_id': 'artifact_download_url_with_id',
        'artifact_type': 'artifact_type',
        'hash_code': 'hash_code',
        'job_id': 'job_id',
        'build_no': 'build_no',
        'daily_build_number': 'daily_build_number',
        'file_size': 'file_size'
    }

    def __init__(self, project_id=None, name=None, artifact_version=None, upload_target=None, artifact_package_type=None, artifact_uri=None, artifact_download_url_with_id=None, artifact_type=None, hash_code=None, job_id=None, build_no=None, daily_build_number=None, file_size=None):
        r"""Artifact

        The model defined in huaweicloud sdk

        :param project_id: 项目ID
        :type project_id: str
        :param name: 名称
        :type name: str
        :param artifact_version: 版本
        :type artifact_version: str
        :param upload_target: 存放平台类型
        :type upload_target: str
        :param artifact_package_type: 产物包类型
        :type artifact_package_type: str
        :param artifact_uri: 制品仓路径
        :type artifact_uri: str
        :param artifact_download_url_with_id: 制品仓下载链接
        :type artifact_download_url_with_id: str
        :param artifact_type: 产物类型
        :type artifact_type: str
        :param hash_code: 哈希码
        :type hash_code: list[:class:`huaweicloudsdkcodeartspipeline.v2.ArtifactHashCode`]
        :param job_id: 构建任务ID
        :type job_id: str
        :param build_no: 构建任务编号
        :type build_no: int
        :param daily_build_number: 构建任务序号
        :type daily_build_number: str
        :param file_size: 产物大小
        :type file_size: str
        """
        
        

        self._project_id = None
        self._name = None
        self._artifact_version = None
        self._upload_target = None
        self._artifact_package_type = None
        self._artifact_uri = None
        self._artifact_download_url_with_id = None
        self._artifact_type = None
        self._hash_code = None
        self._job_id = None
        self._build_no = None
        self._daily_build_number = None
        self._file_size = None
        self.discriminator = None

        if project_id is not None:
            self.project_id = project_id
        if name is not None:
            self.name = name
        if artifact_version is not None:
            self.artifact_version = artifact_version
        if upload_target is not None:
            self.upload_target = upload_target
        if artifact_package_type is not None:
            self.artifact_package_type = artifact_package_type
        if artifact_uri is not None:
            self.artifact_uri = artifact_uri
        if artifact_download_url_with_id is not None:
            self.artifact_download_url_with_id = artifact_download_url_with_id
        if artifact_type is not None:
            self.artifact_type = artifact_type
        if hash_code is not None:
            self.hash_code = hash_code
        if job_id is not None:
            self.job_id = job_id
        if build_no is not None:
            self.build_no = build_no
        if daily_build_number is not None:
            self.daily_build_number = daily_build_number
        if file_size is not None:
            self.file_size = file_size

    @property
    def project_id(self):
        r"""Gets the project_id of this Artifact.

        项目ID

        :return: The project_id of this Artifact.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this Artifact.

        项目ID

        :param project_id: The project_id of this Artifact.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def name(self):
        r"""Gets the name of this Artifact.

        名称

        :return: The name of this Artifact.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Artifact.

        名称

        :param name: The name of this Artifact.
        :type name: str
        """
        self._name = name

    @property
    def artifact_version(self):
        r"""Gets the artifact_version of this Artifact.

        版本

        :return: The artifact_version of this Artifact.
        :rtype: str
        """
        return self._artifact_version

    @artifact_version.setter
    def artifact_version(self, artifact_version):
        r"""Sets the artifact_version of this Artifact.

        版本

        :param artifact_version: The artifact_version of this Artifact.
        :type artifact_version: str
        """
        self._artifact_version = artifact_version

    @property
    def upload_target(self):
        r"""Gets the upload_target of this Artifact.

        存放平台类型

        :return: The upload_target of this Artifact.
        :rtype: str
        """
        return self._upload_target

    @upload_target.setter
    def upload_target(self, upload_target):
        r"""Sets the upload_target of this Artifact.

        存放平台类型

        :param upload_target: The upload_target of this Artifact.
        :type upload_target: str
        """
        self._upload_target = upload_target

    @property
    def artifact_package_type(self):
        r"""Gets the artifact_package_type of this Artifact.

        产物包类型

        :return: The artifact_package_type of this Artifact.
        :rtype: str
        """
        return self._artifact_package_type

    @artifact_package_type.setter
    def artifact_package_type(self, artifact_package_type):
        r"""Sets the artifact_package_type of this Artifact.

        产物包类型

        :param artifact_package_type: The artifact_package_type of this Artifact.
        :type artifact_package_type: str
        """
        self._artifact_package_type = artifact_package_type

    @property
    def artifact_uri(self):
        r"""Gets the artifact_uri of this Artifact.

        制品仓路径

        :return: The artifact_uri of this Artifact.
        :rtype: str
        """
        return self._artifact_uri

    @artifact_uri.setter
    def artifact_uri(self, artifact_uri):
        r"""Sets the artifact_uri of this Artifact.

        制品仓路径

        :param artifact_uri: The artifact_uri of this Artifact.
        :type artifact_uri: str
        """
        self._artifact_uri = artifact_uri

    @property
    def artifact_download_url_with_id(self):
        r"""Gets the artifact_download_url_with_id of this Artifact.

        制品仓下载链接

        :return: The artifact_download_url_with_id of this Artifact.
        :rtype: str
        """
        return self._artifact_download_url_with_id

    @artifact_download_url_with_id.setter
    def artifact_download_url_with_id(self, artifact_download_url_with_id):
        r"""Sets the artifact_download_url_with_id of this Artifact.

        制品仓下载链接

        :param artifact_download_url_with_id: The artifact_download_url_with_id of this Artifact.
        :type artifact_download_url_with_id: str
        """
        self._artifact_download_url_with_id = artifact_download_url_with_id

    @property
    def artifact_type(self):
        r"""Gets the artifact_type of this Artifact.

        产物类型

        :return: The artifact_type of this Artifact.
        :rtype: str
        """
        return self._artifact_type

    @artifact_type.setter
    def artifact_type(self, artifact_type):
        r"""Sets the artifact_type of this Artifact.

        产物类型

        :param artifact_type: The artifact_type of this Artifact.
        :type artifact_type: str
        """
        self._artifact_type = artifact_type

    @property
    def hash_code(self):
        r"""Gets the hash_code of this Artifact.

        哈希码

        :return: The hash_code of this Artifact.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.ArtifactHashCode`]
        """
        return self._hash_code

    @hash_code.setter
    def hash_code(self, hash_code):
        r"""Sets the hash_code of this Artifact.

        哈希码

        :param hash_code: The hash_code of this Artifact.
        :type hash_code: list[:class:`huaweicloudsdkcodeartspipeline.v2.ArtifactHashCode`]
        """
        self._hash_code = hash_code

    @property
    def job_id(self):
        r"""Gets the job_id of this Artifact.

        构建任务ID

        :return: The job_id of this Artifact.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this Artifact.

        构建任务ID

        :param job_id: The job_id of this Artifact.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def build_no(self):
        r"""Gets the build_no of this Artifact.

        构建任务编号

        :return: The build_no of this Artifact.
        :rtype: int
        """
        return self._build_no

    @build_no.setter
    def build_no(self, build_no):
        r"""Sets the build_no of this Artifact.

        构建任务编号

        :param build_no: The build_no of this Artifact.
        :type build_no: int
        """
        self._build_no = build_no

    @property
    def daily_build_number(self):
        r"""Gets the daily_build_number of this Artifact.

        构建任务序号

        :return: The daily_build_number of this Artifact.
        :rtype: str
        """
        return self._daily_build_number

    @daily_build_number.setter
    def daily_build_number(self, daily_build_number):
        r"""Sets the daily_build_number of this Artifact.

        构建任务序号

        :param daily_build_number: The daily_build_number of this Artifact.
        :type daily_build_number: str
        """
        self._daily_build_number = daily_build_number

    @property
    def file_size(self):
        r"""Gets the file_size of this Artifact.

        产物大小

        :return: The file_size of this Artifact.
        :rtype: str
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        r"""Sets the file_size of this Artifact.

        产物大小

        :param file_size: The file_size of this Artifact.
        :type file_size: str
        """
        self._file_size = file_size

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
        if not isinstance(other, Artifact):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
