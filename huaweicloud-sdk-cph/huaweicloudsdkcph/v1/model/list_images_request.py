# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListImagesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image_type': 'str',
        'status': 'int',
        'offset': 'int',
        'limit': 'int',
        'image_id': 'str',
        'image_name': 'str',
        'create_since': 'int',
        'create_until': 'int',
        'src_project_id': 'str'
    }

    attribute_map = {
        'image_type': 'image_type',
        'status': 'status',
        'offset': 'offset',
        'limit': 'limit',
        'image_id': 'image_id',
        'image_name': 'image_name',
        'create_since': 'create_since',
        'create_until': 'create_until',
        'src_project_id': 'src_project_id'
    }

    def __init__(self, image_type=None, status=None, offset=None, limit=None, image_id=None, image_name=None, create_since=None, create_until=None, src_project_id=None):
        r"""ListImagesRequest

        The model defined in huaweicloud sdk

        :param image_type: 镜像类型。 - private：私有镜像 - share：共享镜像
        :type image_type: str
        :param status: 镜像状态。 - 0：CREATING 创建中 - 1：PRODUCTION 生产态，可使用 - 2：CREATE_FAILED 创建失败
        :type status: int
        :param offset: 偏移量为一个大于等于0整数，表示查询该偏移量后面的所有的资源数，默认值为0。
        :type offset: int
        :param limit: 每页返回的资源个数。取值范围：1~100（默认值为100），一般设置为10、20、50。
        :type limit: int
        :param image_id: 镜像id
        :type image_id: str
        :param image_name: 镜像名称
        :type image_name: str
        :param create_since: 起始时间
        :type create_since: int
        :param create_until: 截止时间
        :type create_until: int
        :param src_project_id: 共享镜像账号的projectId
        :type src_project_id: str
        """
        
        

        self._image_type = None
        self._status = None
        self._offset = None
        self._limit = None
        self._image_id = None
        self._image_name = None
        self._create_since = None
        self._create_until = None
        self._src_project_id = None
        self.discriminator = None

        if image_type is not None:
            self.image_type = image_type
        if status is not None:
            self.status = status
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if image_id is not None:
            self.image_id = image_id
        if image_name is not None:
            self.image_name = image_name
        if create_since is not None:
            self.create_since = create_since
        if create_until is not None:
            self.create_until = create_until
        if src_project_id is not None:
            self.src_project_id = src_project_id

    @property
    def image_type(self):
        r"""Gets the image_type of this ListImagesRequest.

        镜像类型。 - private：私有镜像 - share：共享镜像

        :return: The image_type of this ListImagesRequest.
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        r"""Sets the image_type of this ListImagesRequest.

        镜像类型。 - private：私有镜像 - share：共享镜像

        :param image_type: The image_type of this ListImagesRequest.
        :type image_type: str
        """
        self._image_type = image_type

    @property
    def status(self):
        r"""Gets the status of this ListImagesRequest.

        镜像状态。 - 0：CREATING 创建中 - 1：PRODUCTION 生产态，可使用 - 2：CREATE_FAILED 创建失败

        :return: The status of this ListImagesRequest.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListImagesRequest.

        镜像状态。 - 0：CREATING 创建中 - 1：PRODUCTION 生产态，可使用 - 2：CREATE_FAILED 创建失败

        :param status: The status of this ListImagesRequest.
        :type status: int
        """
        self._status = status

    @property
    def offset(self):
        r"""Gets the offset of this ListImagesRequest.

        偏移量为一个大于等于0整数，表示查询该偏移量后面的所有的资源数，默认值为0。

        :return: The offset of this ListImagesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListImagesRequest.

        偏移量为一个大于等于0整数，表示查询该偏移量后面的所有的资源数，默认值为0。

        :param offset: The offset of this ListImagesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListImagesRequest.

        每页返回的资源个数。取值范围：1~100（默认值为100），一般设置为10、20、50。

        :return: The limit of this ListImagesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListImagesRequest.

        每页返回的资源个数。取值范围：1~100（默认值为100），一般设置为10、20、50。

        :param limit: The limit of this ListImagesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def image_id(self):
        r"""Gets the image_id of this ListImagesRequest.

        镜像id

        :return: The image_id of this ListImagesRequest.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this ListImagesRequest.

        镜像id

        :param image_id: The image_id of this ListImagesRequest.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def image_name(self):
        r"""Gets the image_name of this ListImagesRequest.

        镜像名称

        :return: The image_name of this ListImagesRequest.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this ListImagesRequest.

        镜像名称

        :param image_name: The image_name of this ListImagesRequest.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def create_since(self):
        r"""Gets the create_since of this ListImagesRequest.

        起始时间

        :return: The create_since of this ListImagesRequest.
        :rtype: int
        """
        return self._create_since

    @create_since.setter
    def create_since(self, create_since):
        r"""Sets the create_since of this ListImagesRequest.

        起始时间

        :param create_since: The create_since of this ListImagesRequest.
        :type create_since: int
        """
        self._create_since = create_since

    @property
    def create_until(self):
        r"""Gets the create_until of this ListImagesRequest.

        截止时间

        :return: The create_until of this ListImagesRequest.
        :rtype: int
        """
        return self._create_until

    @create_until.setter
    def create_until(self, create_until):
        r"""Sets the create_until of this ListImagesRequest.

        截止时间

        :param create_until: The create_until of this ListImagesRequest.
        :type create_until: int
        """
        self._create_until = create_until

    @property
    def src_project_id(self):
        r"""Gets the src_project_id of this ListImagesRequest.

        共享镜像账号的projectId

        :return: The src_project_id of this ListImagesRequest.
        :rtype: str
        """
        return self._src_project_id

    @src_project_id.setter
    def src_project_id(self, src_project_id):
        r"""Sets the src_project_id of this ListImagesRequest.

        共享镜像账号的projectId

        :param src_project_id: The src_project_id of this ListImagesRequest.
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
        if not isinstance(other, ListImagesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
