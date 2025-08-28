# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageScanTaskInfoFailedImages:

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
        'registry_id': 'str',
        'registry_name': 'str',
        'image_name': 'str',
        'image_version': 'str',
        'namespace': 'str',
        'registry_type': 'str',
        'failed_reason': 'str'
    }

    attribute_map = {
        'id': 'id',
        'registry_id': 'registry_id',
        'registry_name': 'registry_name',
        'image_name': 'image_name',
        'image_version': 'image_version',
        'namespace': 'namespace',
        'registry_type': 'registry_type',
        'failed_reason': 'failed_reason'
    }

    def __init__(self, id=None, registry_id=None, registry_name=None, image_name=None, image_version=None, namespace=None, registry_type=None, failed_reason=None):
        r"""ImageScanTaskInfoFailedImages

        The model defined in huaweicloud sdk

        :param id: **参数解释**： 失败镜像ID **取值范围**： 最小值0，最大值9223372036854775807 
        :type id: int
        :param registry_id: **参数解释**： 镜像仓库ID **取值范围**： 字符长度0-128位 
        :type registry_id: str
        :param registry_name: **参数解释**： 镜像仓库名称 **取值范围**： 字符长度0-128位 
        :type registry_name: str
        :param image_name: **参数解释**： 镜像名称 **取值范围**： 字符长度0-128位 
        :type image_name: str
        :param image_version: **参数解释**： 镜像版本 **取值范围**： 字符长度0-128位 
        :type image_version: str
        :param namespace: **参数解释**： 命名空间 **取值范围**： 字符长度0-128位 
        :type namespace: str
        :param registry_type: **参数解释**： 镜像仓库类型 **取值范围**： - SwrPrivate：swr私有。 - SwrShared：swr共享。 - SwrEnterprise：swr企业。 - Harbor：harbor仓库。 - Jfrog：jfrog仓库。 - Other：其他仓库。 
        :type registry_type: str
        :param failed_reason: **参数解释**： 失败原因 **取值范围**： 字符长度0-128位 
        :type failed_reason: str
        """
        
        

        self._id = None
        self._registry_id = None
        self._registry_name = None
        self._image_name = None
        self._image_version = None
        self._namespace = None
        self._registry_type = None
        self._failed_reason = None
        self.discriminator = None

        if id is not None:
            self.id = id
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
        if registry_type is not None:
            self.registry_type = registry_type
        if failed_reason is not None:
            self.failed_reason = failed_reason

    @property
    def id(self):
        r"""Gets the id of this ImageScanTaskInfoFailedImages.

        **参数解释**： 失败镜像ID **取值范围**： 最小值0，最大值9223372036854775807 

        :return: The id of this ImageScanTaskInfoFailedImages.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ImageScanTaskInfoFailedImages.

        **参数解释**： 失败镜像ID **取值范围**： 最小值0，最大值9223372036854775807 

        :param id: The id of this ImageScanTaskInfoFailedImages.
        :type id: int
        """
        self._id = id

    @property
    def registry_id(self):
        r"""Gets the registry_id of this ImageScanTaskInfoFailedImages.

        **参数解释**： 镜像仓库ID **取值范围**： 字符长度0-128位 

        :return: The registry_id of this ImageScanTaskInfoFailedImages.
        :rtype: str
        """
        return self._registry_id

    @registry_id.setter
    def registry_id(self, registry_id):
        r"""Sets the registry_id of this ImageScanTaskInfoFailedImages.

        **参数解释**： 镜像仓库ID **取值范围**： 字符长度0-128位 

        :param registry_id: The registry_id of this ImageScanTaskInfoFailedImages.
        :type registry_id: str
        """
        self._registry_id = registry_id

    @property
    def registry_name(self):
        r"""Gets the registry_name of this ImageScanTaskInfoFailedImages.

        **参数解释**： 镜像仓库名称 **取值范围**： 字符长度0-128位 

        :return: The registry_name of this ImageScanTaskInfoFailedImages.
        :rtype: str
        """
        return self._registry_name

    @registry_name.setter
    def registry_name(self, registry_name):
        r"""Sets the registry_name of this ImageScanTaskInfoFailedImages.

        **参数解释**： 镜像仓库名称 **取值范围**： 字符长度0-128位 

        :param registry_name: The registry_name of this ImageScanTaskInfoFailedImages.
        :type registry_name: str
        """
        self._registry_name = registry_name

    @property
    def image_name(self):
        r"""Gets the image_name of this ImageScanTaskInfoFailedImages.

        **参数解释**： 镜像名称 **取值范围**： 字符长度0-128位 

        :return: The image_name of this ImageScanTaskInfoFailedImages.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this ImageScanTaskInfoFailedImages.

        **参数解释**： 镜像名称 **取值范围**： 字符长度0-128位 

        :param image_name: The image_name of this ImageScanTaskInfoFailedImages.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def image_version(self):
        r"""Gets the image_version of this ImageScanTaskInfoFailedImages.

        **参数解释**： 镜像版本 **取值范围**： 字符长度0-128位 

        :return: The image_version of this ImageScanTaskInfoFailedImages.
        :rtype: str
        """
        return self._image_version

    @image_version.setter
    def image_version(self, image_version):
        r"""Sets the image_version of this ImageScanTaskInfoFailedImages.

        **参数解释**： 镜像版本 **取值范围**： 字符长度0-128位 

        :param image_version: The image_version of this ImageScanTaskInfoFailedImages.
        :type image_version: str
        """
        self._image_version = image_version

    @property
    def namespace(self):
        r"""Gets the namespace of this ImageScanTaskInfoFailedImages.

        **参数解释**： 命名空间 **取值范围**： 字符长度0-128位 

        :return: The namespace of this ImageScanTaskInfoFailedImages.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this ImageScanTaskInfoFailedImages.

        **参数解释**： 命名空间 **取值范围**： 字符长度0-128位 

        :param namespace: The namespace of this ImageScanTaskInfoFailedImages.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def registry_type(self):
        r"""Gets the registry_type of this ImageScanTaskInfoFailedImages.

        **参数解释**： 镜像仓库类型 **取值范围**： - SwrPrivate：swr私有。 - SwrShared：swr共享。 - SwrEnterprise：swr企业。 - Harbor：harbor仓库。 - Jfrog：jfrog仓库。 - Other：其他仓库。 

        :return: The registry_type of this ImageScanTaskInfoFailedImages.
        :rtype: str
        """
        return self._registry_type

    @registry_type.setter
    def registry_type(self, registry_type):
        r"""Sets the registry_type of this ImageScanTaskInfoFailedImages.

        **参数解释**： 镜像仓库类型 **取值范围**： - SwrPrivate：swr私有。 - SwrShared：swr共享。 - SwrEnterprise：swr企业。 - Harbor：harbor仓库。 - Jfrog：jfrog仓库。 - Other：其他仓库。 

        :param registry_type: The registry_type of this ImageScanTaskInfoFailedImages.
        :type registry_type: str
        """
        self._registry_type = registry_type

    @property
    def failed_reason(self):
        r"""Gets the failed_reason of this ImageScanTaskInfoFailedImages.

        **参数解释**： 失败原因 **取值范围**： 字符长度0-128位 

        :return: The failed_reason of this ImageScanTaskInfoFailedImages.
        :rtype: str
        """
        return self._failed_reason

    @failed_reason.setter
    def failed_reason(self, failed_reason):
        r"""Sets the failed_reason of this ImageScanTaskInfoFailedImages.

        **参数解释**： 失败原因 **取值范围**： 字符长度0-128位 

        :param failed_reason: The failed_reason of this ImageScanTaskInfoFailedImages.
        :type failed_reason: str
        """
        self._failed_reason = failed_reason

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
        if not isinstance(other, ImageScanTaskInfoFailedImages):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
