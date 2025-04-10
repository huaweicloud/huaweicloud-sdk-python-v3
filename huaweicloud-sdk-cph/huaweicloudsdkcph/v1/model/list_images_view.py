# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListImagesView:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_id': 'str',
        'image_name': 'str',
        'update_time': 'str',
        'create_time': 'str',
        'image_size': 'int',
        'project_id': 'str',
        'image_id': 'str',
        'image_version': 'str',
        'image_type': 'str',
        'status': 'int',
        'src_project_id': 'str'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'image_name': 'image_name',
        'update_time': 'update_time',
        'create_time': 'create_time',
        'image_size': 'image_size',
        'project_id': 'project_id',
        'image_id': 'image_id',
        'image_version': 'image_version',
        'image_type': 'image_type',
        'status': 'status',
        'src_project_id': 'src_project_id'
    }

    def __init__(self, domain_id=None, image_name=None, update_time=None, create_time=None, image_size=None, project_id=None, image_id=None, image_version=None, image_type=None, status=None, src_project_id=None):
        r"""ListImagesView

        The model defined in huaweicloud sdk

        :param domain_id: 镜像所属租户
        :type domain_id: str
        :param image_name: 镜像名称
        :type image_name: str
        :param update_time: 镜像更新时间
        :type update_time: str
        :param create_time: 镜像创建时间
        :type create_time: str
        :param image_size: 镜像大小，单位byte
        :type image_size: int
        :param project_id: project_id（当image_type为private时，才会返回此字段)
        :type project_id: str
        :param image_id: 镜像ID
        :type image_id: str
        :param image_version: 镜像AOSP版本
        :type image_version: str
        :param image_type: 镜像类型 私有镜像：private 共享镜像：share
        :type image_type: str
        :param status: 镜像状态。 - 0：CREATING 创建中 - 1：PRODUCTION 生产态，可使用 - 2：CREATE_FAILED 创建失败
        :type status: int
        :param src_project_id: 共享镜像账号的projectId（当image_type为share时，才会返回此字段)
        :type src_project_id: str
        """
        
        

        self._domain_id = None
        self._image_name = None
        self._update_time = None
        self._create_time = None
        self._image_size = None
        self._project_id = None
        self._image_id = None
        self._image_version = None
        self._image_type = None
        self._status = None
        self._src_project_id = None
        self.discriminator = None

        if domain_id is not None:
            self.domain_id = domain_id
        if image_name is not None:
            self.image_name = image_name
        if update_time is not None:
            self.update_time = update_time
        if create_time is not None:
            self.create_time = create_time
        if image_size is not None:
            self.image_size = image_size
        if project_id is not None:
            self.project_id = project_id
        if image_id is not None:
            self.image_id = image_id
        if image_version is not None:
            self.image_version = image_version
        if image_type is not None:
            self.image_type = image_type
        if status is not None:
            self.status = status
        if src_project_id is not None:
            self.src_project_id = src_project_id

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ListImagesView.

        镜像所属租户

        :return: The domain_id of this ListImagesView.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ListImagesView.

        镜像所属租户

        :param domain_id: The domain_id of this ListImagesView.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def image_name(self):
        r"""Gets the image_name of this ListImagesView.

        镜像名称

        :return: The image_name of this ListImagesView.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this ListImagesView.

        镜像名称

        :param image_name: The image_name of this ListImagesView.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def update_time(self):
        r"""Gets the update_time of this ListImagesView.

        镜像更新时间

        :return: The update_time of this ListImagesView.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ListImagesView.

        镜像更新时间

        :param update_time: The update_time of this ListImagesView.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def create_time(self):
        r"""Gets the create_time of this ListImagesView.

        镜像创建时间

        :return: The create_time of this ListImagesView.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ListImagesView.

        镜像创建时间

        :param create_time: The create_time of this ListImagesView.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def image_size(self):
        r"""Gets the image_size of this ListImagesView.

        镜像大小，单位byte

        :return: The image_size of this ListImagesView.
        :rtype: int
        """
        return self._image_size

    @image_size.setter
    def image_size(self, image_size):
        r"""Sets the image_size of this ListImagesView.

        镜像大小，单位byte

        :param image_size: The image_size of this ListImagesView.
        :type image_size: int
        """
        self._image_size = image_size

    @property
    def project_id(self):
        r"""Gets the project_id of this ListImagesView.

        project_id（当image_type为private时，才会返回此字段)

        :return: The project_id of this ListImagesView.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListImagesView.

        project_id（当image_type为private时，才会返回此字段)

        :param project_id: The project_id of this ListImagesView.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def image_id(self):
        r"""Gets the image_id of this ListImagesView.

        镜像ID

        :return: The image_id of this ListImagesView.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this ListImagesView.

        镜像ID

        :param image_id: The image_id of this ListImagesView.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def image_version(self):
        r"""Gets the image_version of this ListImagesView.

        镜像AOSP版本

        :return: The image_version of this ListImagesView.
        :rtype: str
        """
        return self._image_version

    @image_version.setter
    def image_version(self, image_version):
        r"""Sets the image_version of this ListImagesView.

        镜像AOSP版本

        :param image_version: The image_version of this ListImagesView.
        :type image_version: str
        """
        self._image_version = image_version

    @property
    def image_type(self):
        r"""Gets the image_type of this ListImagesView.

        镜像类型 私有镜像：private 共享镜像：share

        :return: The image_type of this ListImagesView.
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        r"""Sets the image_type of this ListImagesView.

        镜像类型 私有镜像：private 共享镜像：share

        :param image_type: The image_type of this ListImagesView.
        :type image_type: str
        """
        self._image_type = image_type

    @property
    def status(self):
        r"""Gets the status of this ListImagesView.

        镜像状态。 - 0：CREATING 创建中 - 1：PRODUCTION 生产态，可使用 - 2：CREATE_FAILED 创建失败

        :return: The status of this ListImagesView.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListImagesView.

        镜像状态。 - 0：CREATING 创建中 - 1：PRODUCTION 生产态，可使用 - 2：CREATE_FAILED 创建失败

        :param status: The status of this ListImagesView.
        :type status: int
        """
        self._status = status

    @property
    def src_project_id(self):
        r"""Gets the src_project_id of this ListImagesView.

        共享镜像账号的projectId（当image_type为share时，才会返回此字段)

        :return: The src_project_id of this ListImagesView.
        :rtype: str
        """
        return self._src_project_id

    @src_project_id.setter
    def src_project_id(self, src_project_id):
        r"""Sets the src_project_id of this ListImagesView.

        共享镜像账号的projectId（当image_type为share时，才会返回此字段)

        :param src_project_id: The src_project_id of this ListImagesView.
        :type src_project_id: str
        """
        self._src_project_id = src_project_id

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
        if not isinstance(other, ListImagesView):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
