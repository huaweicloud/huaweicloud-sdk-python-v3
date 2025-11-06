# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VulRepoImageInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'namespace': 'str',
        'image_id': 'str',
        'image_name': 'str',
        'app_name': 'str',
        'version': 'str',
        'tag_count': 'int',
        'image_type': 'str',
        'data_list': 'list[VulRepoImagesTagInfo]'
    }

    attribute_map = {
        'namespace': 'namespace',
        'image_id': 'image_id',
        'image_name': 'image_name',
        'app_name': 'app_name',
        'version': 'version',
        'tag_count': 'tag_count',
        'image_type': 'image_type',
        'data_list': 'data_list'
    }

    def __init__(self, namespace=None, image_id=None, image_name=None, app_name=None, version=None, tag_count=None, image_type=None, data_list=None):
        r"""VulRepoImageInfo

        The model defined in huaweicloud sdk

        :param namespace: **参数解释**: 组织名称 **取值范围**: 字符长度0-65535位 
        :type namespace: str
        :param image_id: **参数解释**: 镜像id **取值范围**: 字符长度0-65535位 
        :type image_id: str
        :param image_name: **参数解释**: 镜像名称 **取值范围**: 字符长度0-65535位 
        :type image_name: str
        :param app_name: **参数解释**: 应用名称 **取值范围**: 字符长度0-65535位 
        :type app_name: str
        :param version: **参数解释**: 版本信息 **取值范围**: 字符长度0-65535位 
        :type version: str
        :param tag_count: **参数解释**: 镜像版本数 **取值范围**: 最小值0，最大值65535 
        :type tag_count: int
        :param image_type: **参数解释**: 镜像类型 **取值范围**: - private_image：私有镜像仓库。 - shared_image：共享镜像仓库。 
        :type image_type: str
        :param data_list: **参数解释**: tag版本总数 **取值范围**: 最小值0，最大值65535 
        :type data_list: list[:class:`huaweicloudsdkhss.v5.VulRepoImagesTagInfo`]
        """
        
        

        self._namespace = None
        self._image_id = None
        self._image_name = None
        self._app_name = None
        self._version = None
        self._tag_count = None
        self._image_type = None
        self._data_list = None
        self.discriminator = None

        if namespace is not None:
            self.namespace = namespace
        if image_id is not None:
            self.image_id = image_id
        if image_name is not None:
            self.image_name = image_name
        if app_name is not None:
            self.app_name = app_name
        if version is not None:
            self.version = version
        if tag_count is not None:
            self.tag_count = tag_count
        if image_type is not None:
            self.image_type = image_type
        if data_list is not None:
            self.data_list = data_list

    @property
    def namespace(self):
        r"""Gets the namespace of this VulRepoImageInfo.

        **参数解释**: 组织名称 **取值范围**: 字符长度0-65535位 

        :return: The namespace of this VulRepoImageInfo.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this VulRepoImageInfo.

        **参数解释**: 组织名称 **取值范围**: 字符长度0-65535位 

        :param namespace: The namespace of this VulRepoImageInfo.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def image_id(self):
        r"""Gets the image_id of this VulRepoImageInfo.

        **参数解释**: 镜像id **取值范围**: 字符长度0-65535位 

        :return: The image_id of this VulRepoImageInfo.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this VulRepoImageInfo.

        **参数解释**: 镜像id **取值范围**: 字符长度0-65535位 

        :param image_id: The image_id of this VulRepoImageInfo.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def image_name(self):
        r"""Gets the image_name of this VulRepoImageInfo.

        **参数解释**: 镜像名称 **取值范围**: 字符长度0-65535位 

        :return: The image_name of this VulRepoImageInfo.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this VulRepoImageInfo.

        **参数解释**: 镜像名称 **取值范围**: 字符长度0-65535位 

        :param image_name: The image_name of this VulRepoImageInfo.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def app_name(self):
        r"""Gets the app_name of this VulRepoImageInfo.

        **参数解释**: 应用名称 **取值范围**: 字符长度0-65535位 

        :return: The app_name of this VulRepoImageInfo.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this VulRepoImageInfo.

        **参数解释**: 应用名称 **取值范围**: 字符长度0-65535位 

        :param app_name: The app_name of this VulRepoImageInfo.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def version(self):
        r"""Gets the version of this VulRepoImageInfo.

        **参数解释**: 版本信息 **取值范围**: 字符长度0-65535位 

        :return: The version of this VulRepoImageInfo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this VulRepoImageInfo.

        **参数解释**: 版本信息 **取值范围**: 字符长度0-65535位 

        :param version: The version of this VulRepoImageInfo.
        :type version: str
        """
        self._version = version

    @property
    def tag_count(self):
        r"""Gets the tag_count of this VulRepoImageInfo.

        **参数解释**: 镜像版本数 **取值范围**: 最小值0，最大值65535 

        :return: The tag_count of this VulRepoImageInfo.
        :rtype: int
        """
        return self._tag_count

    @tag_count.setter
    def tag_count(self, tag_count):
        r"""Sets the tag_count of this VulRepoImageInfo.

        **参数解释**: 镜像版本数 **取值范围**: 最小值0，最大值65535 

        :param tag_count: The tag_count of this VulRepoImageInfo.
        :type tag_count: int
        """
        self._tag_count = tag_count

    @property
    def image_type(self):
        r"""Gets the image_type of this VulRepoImageInfo.

        **参数解释**: 镜像类型 **取值范围**: - private_image：私有镜像仓库。 - shared_image：共享镜像仓库。 

        :return: The image_type of this VulRepoImageInfo.
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        r"""Sets the image_type of this VulRepoImageInfo.

        **参数解释**: 镜像类型 **取值范围**: - private_image：私有镜像仓库。 - shared_image：共享镜像仓库。 

        :param image_type: The image_type of this VulRepoImageInfo.
        :type image_type: str
        """
        self._image_type = image_type

    @property
    def data_list(self):
        r"""Gets the data_list of this VulRepoImageInfo.

        **参数解释**: tag版本总数 **取值范围**: 最小值0，最大值65535 

        :return: The data_list of this VulRepoImageInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.VulRepoImagesTagInfo`]
        """
        return self._data_list

    @data_list.setter
    def data_list(self, data_list):
        r"""Sets the data_list of this VulRepoImageInfo.

        **参数解释**: tag版本总数 **取值范围**: 最小值0，最大值65535 

        :param data_list: The data_list of this VulRepoImageInfo.
        :type data_list: list[:class:`huaweicloudsdkhss.v5.VulRepoImagesTagInfo`]
        """
        self._data_list = data_list

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
        if not isinstance(other, VulRepoImageInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
