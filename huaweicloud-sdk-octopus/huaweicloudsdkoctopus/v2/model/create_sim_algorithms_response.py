# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSimAlgorithmsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'url': 'str',
        'id': 'int',
        'created_at': 'float',
        'updated_at': 'float',
        'compilation': 'CompilationCreateSrlz',
        'build': 'BuildCreateSrlz',
        'run': 'RunSrlz',
        'name': 'str',
        'description': 'str',
        'category': 'CategoryF62Enum',
        'mount_dir': 'str',
        'image_repo_id': 'int'
    }

    attribute_map = {
        'url': 'url',
        'id': 'id',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'compilation': 'compilation',
        'build': 'build',
        'run': 'run',
        'name': 'name',
        'description': 'description',
        'category': 'category',
        'mount_dir': 'mount_dir',
        'image_repo_id': 'image_repo_id'
    }

    def __init__(self, url=None, id=None, created_at=None, updated_at=None, compilation=None, build=None, run=None, name=None, description=None, category=None, mount_dir=None, image_repo_id=None):
        r"""CreateSimAlgorithmsResponse

        The model defined in huaweicloud sdk

        :param url: 
        :type url: str
        :param id: 
        :type id: int
        :param created_at: 
        :type created_at: float
        :param updated_at: 
        :type updated_at: float
        :param compilation: 
        :type compilation: :class:`huaweicloudsdkoctopus.v2.CompilationCreateSrlz`
        :param build: 
        :type build: :class:`huaweicloudsdkoctopus.v2.BuildCreateSrlz`
        :param run: 
        :type run: :class:`huaweicloudsdkoctopus.v2.RunSrlz`
        :param name: 名称
        :type name: str
        :param description: 描述
        :type description: str
        :param category: 算法类型  * &#x60;code&#x60; - Code * &#x60;artifact&#x60; - Artifact * &#x60;image&#x60; - Image
        :type category: :class:`huaweicloudsdkoctopus.v2.CategoryF62Enum`
        :param mount_dir: 挂载目录，需绝对路径
        :type mount_dir: str
        :param image_repo_id: 镜像id
        :type image_repo_id: int
        """
        
        super(CreateSimAlgorithmsResponse, self).__init__()

        self._url = None
        self._id = None
        self._created_at = None
        self._updated_at = None
        self._compilation = None
        self._build = None
        self._run = None
        self._name = None
        self._description = None
        self._category = None
        self._mount_dir = None
        self._image_repo_id = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if id is not None:
            self.id = id
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        self.compilation = compilation
        self.build = build
        if run is not None:
            self.run = run
        if name is not None:
            self.name = name
        self.description = description
        if category is not None:
            self.category = category
        if mount_dir is not None:
            self.mount_dir = mount_dir
        if image_repo_id is not None:
            self.image_repo_id = image_repo_id

    @property
    def url(self):
        r"""Gets the url of this CreateSimAlgorithmsResponse.

        :return: The url of this CreateSimAlgorithmsResponse.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this CreateSimAlgorithmsResponse.

        :param url: The url of this CreateSimAlgorithmsResponse.
        :type url: str
        """
        self._url = url

    @property
    def id(self):
        r"""Gets the id of this CreateSimAlgorithmsResponse.

        :return: The id of this CreateSimAlgorithmsResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CreateSimAlgorithmsResponse.

        :param id: The id of this CreateSimAlgorithmsResponse.
        :type id: int
        """
        self._id = id

    @property
    def created_at(self):
        r"""Gets the created_at of this CreateSimAlgorithmsResponse.

        :return: The created_at of this CreateSimAlgorithmsResponse.
        :rtype: float
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this CreateSimAlgorithmsResponse.

        :param created_at: The created_at of this CreateSimAlgorithmsResponse.
        :type created_at: float
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this CreateSimAlgorithmsResponse.

        :return: The updated_at of this CreateSimAlgorithmsResponse.
        :rtype: float
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this CreateSimAlgorithmsResponse.

        :param updated_at: The updated_at of this CreateSimAlgorithmsResponse.
        :type updated_at: float
        """
        self._updated_at = updated_at

    @property
    def compilation(self):
        r"""Gets the compilation of this CreateSimAlgorithmsResponse.

        :return: The compilation of this CreateSimAlgorithmsResponse.
        :rtype: :class:`huaweicloudsdkoctopus.v2.CompilationCreateSrlz`
        """
        return self._compilation

    @compilation.setter
    def compilation(self, compilation):
        r"""Sets the compilation of this CreateSimAlgorithmsResponse.

        :param compilation: The compilation of this CreateSimAlgorithmsResponse.
        :type compilation: :class:`huaweicloudsdkoctopus.v2.CompilationCreateSrlz`
        """
        self._compilation = compilation

    @property
    def build(self):
        r"""Gets the build of this CreateSimAlgorithmsResponse.

        :return: The build of this CreateSimAlgorithmsResponse.
        :rtype: :class:`huaweicloudsdkoctopus.v2.BuildCreateSrlz`
        """
        return self._build

    @build.setter
    def build(self, build):
        r"""Sets the build of this CreateSimAlgorithmsResponse.

        :param build: The build of this CreateSimAlgorithmsResponse.
        :type build: :class:`huaweicloudsdkoctopus.v2.BuildCreateSrlz`
        """
        self._build = build

    @property
    def run(self):
        r"""Gets the run of this CreateSimAlgorithmsResponse.

        :return: The run of this CreateSimAlgorithmsResponse.
        :rtype: :class:`huaweicloudsdkoctopus.v2.RunSrlz`
        """
        return self._run

    @run.setter
    def run(self, run):
        r"""Sets the run of this CreateSimAlgorithmsResponse.

        :param run: The run of this CreateSimAlgorithmsResponse.
        :type run: :class:`huaweicloudsdkoctopus.v2.RunSrlz`
        """
        self._run = run

    @property
    def name(self):
        r"""Gets the name of this CreateSimAlgorithmsResponse.

        名称

        :return: The name of this CreateSimAlgorithmsResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateSimAlgorithmsResponse.

        名称

        :param name: The name of this CreateSimAlgorithmsResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateSimAlgorithmsResponse.

        描述

        :return: The description of this CreateSimAlgorithmsResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateSimAlgorithmsResponse.

        描述

        :param description: The description of this CreateSimAlgorithmsResponse.
        :type description: str
        """
        self._description = description

    @property
    def category(self):
        r"""Gets the category of this CreateSimAlgorithmsResponse.

        算法类型  * `code` - Code * `artifact` - Artifact * `image` - Image

        :return: The category of this CreateSimAlgorithmsResponse.
        :rtype: :class:`huaweicloudsdkoctopus.v2.CategoryF62Enum`
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this CreateSimAlgorithmsResponse.

        算法类型  * `code` - Code * `artifact` - Artifact * `image` - Image

        :param category: The category of this CreateSimAlgorithmsResponse.
        :type category: :class:`huaweicloudsdkoctopus.v2.CategoryF62Enum`
        """
        self._category = category

    @property
    def mount_dir(self):
        r"""Gets the mount_dir of this CreateSimAlgorithmsResponse.

        挂载目录，需绝对路径

        :return: The mount_dir of this CreateSimAlgorithmsResponse.
        :rtype: str
        """
        return self._mount_dir

    @mount_dir.setter
    def mount_dir(self, mount_dir):
        r"""Sets the mount_dir of this CreateSimAlgorithmsResponse.

        挂载目录，需绝对路径

        :param mount_dir: The mount_dir of this CreateSimAlgorithmsResponse.
        :type mount_dir: str
        """
        self._mount_dir = mount_dir

    @property
    def image_repo_id(self):
        r"""Gets the image_repo_id of this CreateSimAlgorithmsResponse.

        镜像id

        :return: The image_repo_id of this CreateSimAlgorithmsResponse.
        :rtype: int
        """
        return self._image_repo_id

    @image_repo_id.setter
    def image_repo_id(self, image_repo_id):
        r"""Sets the image_repo_id of this CreateSimAlgorithmsResponse.

        镜像id

        :param image_repo_id: The image_repo_id of this CreateSimAlgorithmsResponse.
        :type image_repo_id: int
        """
        self._image_repo_id = image_repo_id

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
        if not isinstance(other, CreateSimAlgorithmsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
