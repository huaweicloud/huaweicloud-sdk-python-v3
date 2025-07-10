# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSimAlgorithmsResponse(SdkResponse):

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
        'compilation': 'CompilationUpdateSrlz',
        'build': 'BuildUpdateSrlz',
        'run': 'RunSrlz',
        'keys_reset': 'bool',
        'category': 'str',
        'name': 'str',
        'description': 'str',
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
        'keys_reset': 'keys_reset',
        'category': 'category',
        'name': 'name',
        'description': 'description',
        'mount_dir': 'mount_dir',
        'image_repo_id': 'image_repo_id'
    }

    def __init__(self, url=None, id=None, created_at=None, updated_at=None, compilation=None, build=None, run=None, keys_reset=None, category=None, name=None, description=None, mount_dir=None, image_repo_id=None):
        r"""UpdateSimAlgorithmsResponse

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
        :type compilation: :class:`huaweicloudsdkoctopus.v2.CompilationUpdateSrlz`
        :param build: 
        :type build: :class:`huaweicloudsdkoctopus.v2.BuildUpdateSrlz`
        :param run: 
        :type run: :class:`huaweicloudsdkoctopus.v2.RunSrlz`
        :param keys_reset: 
        :type keys_reset: bool
        :param category: 算法类型，如image
        :type category: str
        :param name: 名称
        :type name: str
        :param description: 描述
        :type description: str
        :param mount_dir: 挂载目录，需绝对路径
        :type mount_dir: str
        :param image_repo_id: 镜像id
        :type image_repo_id: int
        """
        
        super(UpdateSimAlgorithmsResponse, self).__init__()

        self._url = None
        self._id = None
        self._created_at = None
        self._updated_at = None
        self._compilation = None
        self._build = None
        self._run = None
        self._keys_reset = None
        self._category = None
        self._name = None
        self._description = None
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
        if compilation is not None:
            self.compilation = compilation
        if build is not None:
            self.build = build
        if run is not None:
            self.run = run
        if keys_reset is not None:
            self.keys_reset = keys_reset
        if category is not None:
            self.category = category
        if name is not None:
            self.name = name
        self.description = description
        if mount_dir is not None:
            self.mount_dir = mount_dir
        if image_repo_id is not None:
            self.image_repo_id = image_repo_id

    @property
    def url(self):
        r"""Gets the url of this UpdateSimAlgorithmsResponse.

        :return: The url of this UpdateSimAlgorithmsResponse.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this UpdateSimAlgorithmsResponse.

        :param url: The url of this UpdateSimAlgorithmsResponse.
        :type url: str
        """
        self._url = url

    @property
    def id(self):
        r"""Gets the id of this UpdateSimAlgorithmsResponse.

        :return: The id of this UpdateSimAlgorithmsResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UpdateSimAlgorithmsResponse.

        :param id: The id of this UpdateSimAlgorithmsResponse.
        :type id: int
        """
        self._id = id

    @property
    def created_at(self):
        r"""Gets the created_at of this UpdateSimAlgorithmsResponse.

        :return: The created_at of this UpdateSimAlgorithmsResponse.
        :rtype: float
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this UpdateSimAlgorithmsResponse.

        :param created_at: The created_at of this UpdateSimAlgorithmsResponse.
        :type created_at: float
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this UpdateSimAlgorithmsResponse.

        :return: The updated_at of this UpdateSimAlgorithmsResponse.
        :rtype: float
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this UpdateSimAlgorithmsResponse.

        :param updated_at: The updated_at of this UpdateSimAlgorithmsResponse.
        :type updated_at: float
        """
        self._updated_at = updated_at

    @property
    def compilation(self):
        r"""Gets the compilation of this UpdateSimAlgorithmsResponse.

        :return: The compilation of this UpdateSimAlgorithmsResponse.
        :rtype: :class:`huaweicloudsdkoctopus.v2.CompilationUpdateSrlz`
        """
        return self._compilation

    @compilation.setter
    def compilation(self, compilation):
        r"""Sets the compilation of this UpdateSimAlgorithmsResponse.

        :param compilation: The compilation of this UpdateSimAlgorithmsResponse.
        :type compilation: :class:`huaweicloudsdkoctopus.v2.CompilationUpdateSrlz`
        """
        self._compilation = compilation

    @property
    def build(self):
        r"""Gets the build of this UpdateSimAlgorithmsResponse.

        :return: The build of this UpdateSimAlgorithmsResponse.
        :rtype: :class:`huaweicloudsdkoctopus.v2.BuildUpdateSrlz`
        """
        return self._build

    @build.setter
    def build(self, build):
        r"""Sets the build of this UpdateSimAlgorithmsResponse.

        :param build: The build of this UpdateSimAlgorithmsResponse.
        :type build: :class:`huaweicloudsdkoctopus.v2.BuildUpdateSrlz`
        """
        self._build = build

    @property
    def run(self):
        r"""Gets the run of this UpdateSimAlgorithmsResponse.

        :return: The run of this UpdateSimAlgorithmsResponse.
        :rtype: :class:`huaweicloudsdkoctopus.v2.RunSrlz`
        """
        return self._run

    @run.setter
    def run(self, run):
        r"""Sets the run of this UpdateSimAlgorithmsResponse.

        :param run: The run of this UpdateSimAlgorithmsResponse.
        :type run: :class:`huaweicloudsdkoctopus.v2.RunSrlz`
        """
        self._run = run

    @property
    def keys_reset(self):
        r"""Gets the keys_reset of this UpdateSimAlgorithmsResponse.

        :return: The keys_reset of this UpdateSimAlgorithmsResponse.
        :rtype: bool
        """
        return self._keys_reset

    @keys_reset.setter
    def keys_reset(self, keys_reset):
        r"""Sets the keys_reset of this UpdateSimAlgorithmsResponse.

        :param keys_reset: The keys_reset of this UpdateSimAlgorithmsResponse.
        :type keys_reset: bool
        """
        self._keys_reset = keys_reset

    @property
    def category(self):
        r"""Gets the category of this UpdateSimAlgorithmsResponse.

        算法类型，如image

        :return: The category of this UpdateSimAlgorithmsResponse.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this UpdateSimAlgorithmsResponse.

        算法类型，如image

        :param category: The category of this UpdateSimAlgorithmsResponse.
        :type category: str
        """
        self._category = category

    @property
    def name(self):
        r"""Gets the name of this UpdateSimAlgorithmsResponse.

        名称

        :return: The name of this UpdateSimAlgorithmsResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateSimAlgorithmsResponse.

        名称

        :param name: The name of this UpdateSimAlgorithmsResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this UpdateSimAlgorithmsResponse.

        描述

        :return: The description of this UpdateSimAlgorithmsResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateSimAlgorithmsResponse.

        描述

        :param description: The description of this UpdateSimAlgorithmsResponse.
        :type description: str
        """
        self._description = description

    @property
    def mount_dir(self):
        r"""Gets the mount_dir of this UpdateSimAlgorithmsResponse.

        挂载目录，需绝对路径

        :return: The mount_dir of this UpdateSimAlgorithmsResponse.
        :rtype: str
        """
        return self._mount_dir

    @mount_dir.setter
    def mount_dir(self, mount_dir):
        r"""Sets the mount_dir of this UpdateSimAlgorithmsResponse.

        挂载目录，需绝对路径

        :param mount_dir: The mount_dir of this UpdateSimAlgorithmsResponse.
        :type mount_dir: str
        """
        self._mount_dir = mount_dir

    @property
    def image_repo_id(self):
        r"""Gets the image_repo_id of this UpdateSimAlgorithmsResponse.

        镜像id

        :return: The image_repo_id of this UpdateSimAlgorithmsResponse.
        :rtype: int
        """
        return self._image_repo_id

    @image_repo_id.setter
    def image_repo_id(self, image_repo_id):
        r"""Sets the image_repo_id of this UpdateSimAlgorithmsResponse.

        镜像id

        :param image_repo_id: The image_repo_id of this UpdateSimAlgorithmsResponse.
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
        if not isinstance(other, UpdateSimAlgorithmsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
