# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateManualImageScanTaskReqInfoImageInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'image_id': 'str',
        'image_digest': 'str',
        'registry_id': 'str',
        'registry_name': 'str',
        'image_name': 'str',
        'image_version': 'str',
        'namespace': 'str',
        'instance_id': 'str',
        'instance_url': 'str',
        'registry_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'image_id': 'image_id',
        'image_digest': 'image_digest',
        'registry_id': 'registry_id',
        'registry_name': 'registry_name',
        'image_name': 'image_name',
        'image_version': 'image_version',
        'namespace': 'namespace',
        'instance_id': 'instance_id',
        'instance_url': 'instance_url',
        'registry_type': 'registry_type'
    }

    def __init__(self, id=None, image_id=None, image_digest=None, registry_id=None, registry_name=None, image_name=None, image_version=None, namespace=None, instance_id=None, instance_url=None, registry_type=None):
        r"""CreateManualImageScanTaskReqInfoImageInfo

        The model defined in huaweicloud sdk

        :param id: id
        :type id: int
        :param image_id: image id
        :type image_id: str
        :param image_digest: 镜像digest
        :type image_digest: str
        :param registry_id: 镜像仓库ID
        :type registry_id: str
        :param registry_name: 镜像仓库名称
        :type registry_name: str
        :param image_name: 镜像名称
        :type image_name: str
        :param image_version: 镜像版本
        :type image_version: str
        :param namespace: 命名空间
        :type namespace: str
        :param instance_id: 企业实例ID
        :type instance_id: str
        :param instance_url: 下载企业镜像URL
        :type instance_url: str
        :param registry_type: **参数解释**: 镜像仓库类型 **约束限制**: 不涉及 **取值范围**: - SwrPrivate：swr私有。 - SwrShared：swr共享。 - SwrEnterprise：swr企业。 - Harbor：harbor仓库。 - Jfrog：jfrog仓库。 - Other：其他仓库。  **默认取值**: 不涉及 
        :type registry_type: str
        """
        
        

        self._id = None
        self._image_id = None
        self._image_digest = None
        self._registry_id = None
        self._registry_name = None
        self._image_name = None
        self._image_version = None
        self._namespace = None
        self._instance_id = None
        self._instance_url = None
        self._registry_type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if image_id is not None:
            self.image_id = image_id
        if image_digest is not None:
            self.image_digest = image_digest
        if registry_id is not None:
            self.registry_id = registry_id
        if registry_name is not None:
            self.registry_name = registry_name
        if image_name is not None:
            self.image_name = image_name
        if image_version is not None:
            self.image_version = image_version
        if namespace is not None:
            self.namespace = namespace
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_url is not None:
            self.instance_url = instance_url
        if registry_type is not None:
            self.registry_type = registry_type

    @property
    def id(self):
        r"""Gets the id of this CreateManualImageScanTaskReqInfoImageInfo.

        id

        :return: The id of this CreateManualImageScanTaskReqInfoImageInfo.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CreateManualImageScanTaskReqInfoImageInfo.

        id

        :param id: The id of this CreateManualImageScanTaskReqInfoImageInfo.
        :type id: int
        """
        self._id = id

    @property
    def image_id(self):
        r"""Gets the image_id of this CreateManualImageScanTaskReqInfoImageInfo.

        image id

        :return: The image_id of this CreateManualImageScanTaskReqInfoImageInfo.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this CreateManualImageScanTaskReqInfoImageInfo.

        image id

        :param image_id: The image_id of this CreateManualImageScanTaskReqInfoImageInfo.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def image_digest(self):
        r"""Gets the image_digest of this CreateManualImageScanTaskReqInfoImageInfo.

        镜像digest

        :return: The image_digest of this CreateManualImageScanTaskReqInfoImageInfo.
        :rtype: str
        """
        return self._image_digest

    @image_digest.setter
    def image_digest(self, image_digest):
        r"""Sets the image_digest of this CreateManualImageScanTaskReqInfoImageInfo.

        镜像digest

        :param image_digest: The image_digest of this CreateManualImageScanTaskReqInfoImageInfo.
        :type image_digest: str
        """
        self._image_digest = image_digest

    @property
    def registry_id(self):
        r"""Gets the registry_id of this CreateManualImageScanTaskReqInfoImageInfo.

        镜像仓库ID

        :return: The registry_id of this CreateManualImageScanTaskReqInfoImageInfo.
        :rtype: str
        """
        return self._registry_id

    @registry_id.setter
    def registry_id(self, registry_id):
        r"""Sets the registry_id of this CreateManualImageScanTaskReqInfoImageInfo.

        镜像仓库ID

        :param registry_id: The registry_id of this CreateManualImageScanTaskReqInfoImageInfo.
        :type registry_id: str
        """
        self._registry_id = registry_id

    @property
    def registry_name(self):
        r"""Gets the registry_name of this CreateManualImageScanTaskReqInfoImageInfo.

        镜像仓库名称

        :return: The registry_name of this CreateManualImageScanTaskReqInfoImageInfo.
        :rtype: str
        """
        return self._registry_name

    @registry_name.setter
    def registry_name(self, registry_name):
        r"""Sets the registry_name of this CreateManualImageScanTaskReqInfoImageInfo.

        镜像仓库名称

        :param registry_name: The registry_name of this CreateManualImageScanTaskReqInfoImageInfo.
        :type registry_name: str
        """
        self._registry_name = registry_name

    @property
    def image_name(self):
        r"""Gets the image_name of this CreateManualImageScanTaskReqInfoImageInfo.

        镜像名称

        :return: The image_name of this CreateManualImageScanTaskReqInfoImageInfo.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this CreateManualImageScanTaskReqInfoImageInfo.

        镜像名称

        :param image_name: The image_name of this CreateManualImageScanTaskReqInfoImageInfo.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def image_version(self):
        r"""Gets the image_version of this CreateManualImageScanTaskReqInfoImageInfo.

        镜像版本

        :return: The image_version of this CreateManualImageScanTaskReqInfoImageInfo.
        :rtype: str
        """
        return self._image_version

    @image_version.setter
    def image_version(self, image_version):
        r"""Sets the image_version of this CreateManualImageScanTaskReqInfoImageInfo.

        镜像版本

        :param image_version: The image_version of this CreateManualImageScanTaskReqInfoImageInfo.
        :type image_version: str
        """
        self._image_version = image_version

    @property
    def namespace(self):
        r"""Gets the namespace of this CreateManualImageScanTaskReqInfoImageInfo.

        命名空间

        :return: The namespace of this CreateManualImageScanTaskReqInfoImageInfo.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this CreateManualImageScanTaskReqInfoImageInfo.

        命名空间

        :param namespace: The namespace of this CreateManualImageScanTaskReqInfoImageInfo.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def instance_id(self):
        r"""Gets the instance_id of this CreateManualImageScanTaskReqInfoImageInfo.

        企业实例ID

        :return: The instance_id of this CreateManualImageScanTaskReqInfoImageInfo.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this CreateManualImageScanTaskReqInfoImageInfo.

        企业实例ID

        :param instance_id: The instance_id of this CreateManualImageScanTaskReqInfoImageInfo.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_url(self):
        r"""Gets the instance_url of this CreateManualImageScanTaskReqInfoImageInfo.

        下载企业镜像URL

        :return: The instance_url of this CreateManualImageScanTaskReqInfoImageInfo.
        :rtype: str
        """
        return self._instance_url

    @instance_url.setter
    def instance_url(self, instance_url):
        r"""Sets the instance_url of this CreateManualImageScanTaskReqInfoImageInfo.

        下载企业镜像URL

        :param instance_url: The instance_url of this CreateManualImageScanTaskReqInfoImageInfo.
        :type instance_url: str
        """
        self._instance_url = instance_url

    @property
    def registry_type(self):
        r"""Gets the registry_type of this CreateManualImageScanTaskReqInfoImageInfo.

        **参数解释**: 镜像仓库类型 **约束限制**: 不涉及 **取值范围**: - SwrPrivate：swr私有。 - SwrShared：swr共享。 - SwrEnterprise：swr企业。 - Harbor：harbor仓库。 - Jfrog：jfrog仓库。 - Other：其他仓库。  **默认取值**: 不涉及 

        :return: The registry_type of this CreateManualImageScanTaskReqInfoImageInfo.
        :rtype: str
        """
        return self._registry_type

    @registry_type.setter
    def registry_type(self, registry_type):
        r"""Sets the registry_type of this CreateManualImageScanTaskReqInfoImageInfo.

        **参数解释**: 镜像仓库类型 **约束限制**: 不涉及 **取值范围**: - SwrPrivate：swr私有。 - SwrShared：swr共享。 - SwrEnterprise：swr企业。 - Harbor：harbor仓库。 - Jfrog：jfrog仓库。 - Other：其他仓库。  **默认取值**: 不涉及 

        :param registry_type: The registry_type of this CreateManualImageScanTaskReqInfoImageInfo.
        :type registry_type: str
        """
        self._registry_type = registry_type

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
        if not isinstance(other, CreateManualImageScanTaskReqInfoImageInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
