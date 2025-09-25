# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListImageBasicImageRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region': 'str',
        'enterprise_project_id': 'str',
        'limit': 'int',
        'offset': 'int',
        'image_id': 'str',
        'image_type': 'str',
        'namespace': 'str',
        'image_name': 'str',
        'image_version': 'str',
        'os_name': 'str'
    }

    attribute_map = {
        'region': 'region',
        'enterprise_project_id': 'enterprise_project_id',
        'limit': 'limit',
        'offset': 'offset',
        'image_id': 'image_id',
        'image_type': 'image_type',
        'namespace': 'namespace',
        'image_name': 'image_name',
        'image_version': 'image_version',
        'os_name': 'os_name'
    }

    def __init__(self, region=None, enterprise_project_id=None, limit=None, offset=None, image_id=None, image_type=None, namespace=None, image_name=None, image_version=None, os_name=None):
        r"""ListImageBasicImageRequest

        The model defined in huaweicloud sdk

        :param region: Region ID
        :type region: str
        :param enterprise_project_id: 主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。
        :type enterprise_project_id: str
        :param limit: 每页显示个数
        :type limit: int
        :param offset: 偏移量：指定返回记录的开始位置
        :type offset: int
        :param image_id: 镜像id
        :type image_id: str
        :param image_type: 镜像类型，包含如下:   - private_image : 私有镜像仓库   - shared_image : 共享镜像仓库   - instance_image : 企业镜像   - cicd : cicd镜像   - harbor ：Harbor仓库镜像
        :type image_type: str
        :param namespace: 组织名称
        :type namespace: str
        :param image_name: 镜像名称
        :type image_name: str
        :param image_version: 镜像版本名称
        :type image_version: str
        :param os_name: os名称
        :type os_name: str
        """
        
        

        self._region = None
        self._enterprise_project_id = None
        self._limit = None
        self._offset = None
        self._image_id = None
        self._image_type = None
        self._namespace = None
        self._image_name = None
        self._image_version = None
        self._os_name = None
        self.discriminator = None

        self.region = region
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        self.image_id = image_id
        self.image_type = image_type
        if namespace is not None:
            self.namespace = namespace
        if image_name is not None:
            self.image_name = image_name
        if image_version is not None:
            self.image_version = image_version
        if os_name is not None:
            self.os_name = os_name

    @property
    def region(self):
        r"""Gets the region of this ListImageBasicImageRequest.

        Region ID

        :return: The region of this ListImageBasicImageRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ListImageBasicImageRequest.

        Region ID

        :param region: The region of this ListImageBasicImageRequest.
        :type region: str
        """
        self._region = region

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListImageBasicImageRequest.

        主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。

        :return: The enterprise_project_id of this ListImageBasicImageRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListImageBasicImageRequest.

        主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。

        :param enterprise_project_id: The enterprise_project_id of this ListImageBasicImageRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def limit(self):
        r"""Gets the limit of this ListImageBasicImageRequest.

        每页显示个数

        :return: The limit of this ListImageBasicImageRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListImageBasicImageRequest.

        每页显示个数

        :param limit: The limit of this ListImageBasicImageRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListImageBasicImageRequest.

        偏移量：指定返回记录的开始位置

        :return: The offset of this ListImageBasicImageRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListImageBasicImageRequest.

        偏移量：指定返回记录的开始位置

        :param offset: The offset of this ListImageBasicImageRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def image_id(self):
        r"""Gets the image_id of this ListImageBasicImageRequest.

        镜像id

        :return: The image_id of this ListImageBasicImageRequest.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this ListImageBasicImageRequest.

        镜像id

        :param image_id: The image_id of this ListImageBasicImageRequest.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def image_type(self):
        r"""Gets the image_type of this ListImageBasicImageRequest.

        镜像类型，包含如下:   - private_image : 私有镜像仓库   - shared_image : 共享镜像仓库   - instance_image : 企业镜像   - cicd : cicd镜像   - harbor ：Harbor仓库镜像

        :return: The image_type of this ListImageBasicImageRequest.
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        r"""Sets the image_type of this ListImageBasicImageRequest.

        镜像类型，包含如下:   - private_image : 私有镜像仓库   - shared_image : 共享镜像仓库   - instance_image : 企业镜像   - cicd : cicd镜像   - harbor ：Harbor仓库镜像

        :param image_type: The image_type of this ListImageBasicImageRequest.
        :type image_type: str
        """
        self._image_type = image_type

    @property
    def namespace(self):
        r"""Gets the namespace of this ListImageBasicImageRequest.

        组织名称

        :return: The namespace of this ListImageBasicImageRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this ListImageBasicImageRequest.

        组织名称

        :param namespace: The namespace of this ListImageBasicImageRequest.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def image_name(self):
        r"""Gets the image_name of this ListImageBasicImageRequest.

        镜像名称

        :return: The image_name of this ListImageBasicImageRequest.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this ListImageBasicImageRequest.

        镜像名称

        :param image_name: The image_name of this ListImageBasicImageRequest.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def image_version(self):
        r"""Gets the image_version of this ListImageBasicImageRequest.

        镜像版本名称

        :return: The image_version of this ListImageBasicImageRequest.
        :rtype: str
        """
        return self._image_version

    @image_version.setter
    def image_version(self, image_version):
        r"""Sets the image_version of this ListImageBasicImageRequest.

        镜像版本名称

        :param image_version: The image_version of this ListImageBasicImageRequest.
        :type image_version: str
        """
        self._image_version = image_version

    @property
    def os_name(self):
        r"""Gets the os_name of this ListImageBasicImageRequest.

        os名称

        :return: The os_name of this ListImageBasicImageRequest.
        :rtype: str
        """
        return self._os_name

    @os_name.setter
    def os_name(self, os_name):
        r"""Sets the os_name of this ListImageBasicImageRequest.

        os名称

        :param os_name: The os_name of this ListImageBasicImageRequest.
        :type os_name: str
        """
        self._os_name = os_name

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
        if not isinstance(other, ListImageBasicImageRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
