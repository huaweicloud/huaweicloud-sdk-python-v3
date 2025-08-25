# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image_id': 'str',
        'image_name': 'str',
        'service_type': 'str',
        'arch_type': 'str',
        'specification_id': 'str',
        'create_time': 'str',
        'version_type': 'str',
        'trust_domain': 'str',
        'vendor_name': 'str',
        'vendor_image_version': 'str',
        'ccsp_version_need': 'str',
        'hw_image_version': 'str',
        'description': 'str'
    }

    attribute_map = {
        'image_id': 'image_id',
        'image_name': 'image_name',
        'service_type': 'service_type',
        'arch_type': 'arch_type',
        'specification_id': 'specification_id',
        'create_time': 'create_time',
        'version_type': 'version_type',
        'trust_domain': 'trust_domain',
        'vendor_name': 'vendor_name',
        'vendor_image_version': 'vendor_image_version',
        'ccsp_version_need': 'ccsp_version_need',
        'hw_image_version': 'hw_image_version',
        'description': 'description'
    }

    def __init__(self, image_id=None, image_name=None, service_type=None, arch_type=None, specification_id=None, create_time=None, version_type=None, trust_domain=None, vendor_name=None, vendor_image_version=None, ccsp_version_need=None, hw_image_version=None, description=None):
        r"""ImageInfo

        The model defined in huaweicloud sdk

        :param image_id: 镜像ID
        :type image_id: str
        :param image_name: 镜像名称
        :type image_name: str
        :param service_type: 镜像所属的服务
        :type service_type: str
        :param arch_type: 镜像的系统架构： - **X86_64** : X86 - **ARRCH** : ARM
        :type arch_type: str
        :param specification_id: 规格ID
        :type specification_id: str
        :param create_time: 镜像的录入时间，UNIX时间戳，单位毫秒
        :type create_time: str
        :param version_type: 版本类型
        :type version_type: str
        :param trust_domain: domain白名单列表，多个之间用逗号分隔
        :type trust_domain: str
        :param vendor_name: 厂商名称
        :type vendor_name: str
        :param vendor_image_version: 厂商版本号
        :type vendor_image_version: str
        :param ccsp_version_need: 密码服务依赖的(厂商)平台版本号
        :type ccsp_version_need: str
        :param hw_image_version: 华为版本号
        :type hw_image_version: str
        :param description: 描述
        :type description: str
        """
        
        

        self._image_id = None
        self._image_name = None
        self._service_type = None
        self._arch_type = None
        self._specification_id = None
        self._create_time = None
        self._version_type = None
        self._trust_domain = None
        self._vendor_name = None
        self._vendor_image_version = None
        self._ccsp_version_need = None
        self._hw_image_version = None
        self._description = None
        self.discriminator = None

        self.image_id = image_id
        self.image_name = image_name
        self.service_type = service_type
        self.arch_type = arch_type
        self.specification_id = specification_id
        self.create_time = create_time
        self.version_type = version_type
        self.trust_domain = trust_domain
        self.vendor_name = vendor_name
        self.vendor_image_version = vendor_image_version
        self.ccsp_version_need = ccsp_version_need
        self.hw_image_version = hw_image_version
        self.description = description

    @property
    def image_id(self):
        r"""Gets the image_id of this ImageInfo.

        镜像ID

        :return: The image_id of this ImageInfo.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this ImageInfo.

        镜像ID

        :param image_id: The image_id of this ImageInfo.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def image_name(self):
        r"""Gets the image_name of this ImageInfo.

        镜像名称

        :return: The image_name of this ImageInfo.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this ImageInfo.

        镜像名称

        :param image_name: The image_name of this ImageInfo.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def service_type(self):
        r"""Gets the service_type of this ImageInfo.

        镜像所属的服务

        :return: The service_type of this ImageInfo.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        r"""Sets the service_type of this ImageInfo.

        镜像所属的服务

        :param service_type: The service_type of this ImageInfo.
        :type service_type: str
        """
        self._service_type = service_type

    @property
    def arch_type(self):
        r"""Gets the arch_type of this ImageInfo.

        镜像的系统架构： - **X86_64** : X86 - **ARRCH** : ARM

        :return: The arch_type of this ImageInfo.
        :rtype: str
        """
        return self._arch_type

    @arch_type.setter
    def arch_type(self, arch_type):
        r"""Sets the arch_type of this ImageInfo.

        镜像的系统架构： - **X86_64** : X86 - **ARRCH** : ARM

        :param arch_type: The arch_type of this ImageInfo.
        :type arch_type: str
        """
        self._arch_type = arch_type

    @property
    def specification_id(self):
        r"""Gets the specification_id of this ImageInfo.

        规格ID

        :return: The specification_id of this ImageInfo.
        :rtype: str
        """
        return self._specification_id

    @specification_id.setter
    def specification_id(self, specification_id):
        r"""Sets the specification_id of this ImageInfo.

        规格ID

        :param specification_id: The specification_id of this ImageInfo.
        :type specification_id: str
        """
        self._specification_id = specification_id

    @property
    def create_time(self):
        r"""Gets the create_time of this ImageInfo.

        镜像的录入时间，UNIX时间戳，单位毫秒

        :return: The create_time of this ImageInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ImageInfo.

        镜像的录入时间，UNIX时间戳，单位毫秒

        :param create_time: The create_time of this ImageInfo.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def version_type(self):
        r"""Gets the version_type of this ImageInfo.

        版本类型

        :return: The version_type of this ImageInfo.
        :rtype: str
        """
        return self._version_type

    @version_type.setter
    def version_type(self, version_type):
        r"""Sets the version_type of this ImageInfo.

        版本类型

        :param version_type: The version_type of this ImageInfo.
        :type version_type: str
        """
        self._version_type = version_type

    @property
    def trust_domain(self):
        r"""Gets the trust_domain of this ImageInfo.

        domain白名单列表，多个之间用逗号分隔

        :return: The trust_domain of this ImageInfo.
        :rtype: str
        """
        return self._trust_domain

    @trust_domain.setter
    def trust_domain(self, trust_domain):
        r"""Sets the trust_domain of this ImageInfo.

        domain白名单列表，多个之间用逗号分隔

        :param trust_domain: The trust_domain of this ImageInfo.
        :type trust_domain: str
        """
        self._trust_domain = trust_domain

    @property
    def vendor_name(self):
        r"""Gets the vendor_name of this ImageInfo.

        厂商名称

        :return: The vendor_name of this ImageInfo.
        :rtype: str
        """
        return self._vendor_name

    @vendor_name.setter
    def vendor_name(self, vendor_name):
        r"""Sets the vendor_name of this ImageInfo.

        厂商名称

        :param vendor_name: The vendor_name of this ImageInfo.
        :type vendor_name: str
        """
        self._vendor_name = vendor_name

    @property
    def vendor_image_version(self):
        r"""Gets the vendor_image_version of this ImageInfo.

        厂商版本号

        :return: The vendor_image_version of this ImageInfo.
        :rtype: str
        """
        return self._vendor_image_version

    @vendor_image_version.setter
    def vendor_image_version(self, vendor_image_version):
        r"""Sets the vendor_image_version of this ImageInfo.

        厂商版本号

        :param vendor_image_version: The vendor_image_version of this ImageInfo.
        :type vendor_image_version: str
        """
        self._vendor_image_version = vendor_image_version

    @property
    def ccsp_version_need(self):
        r"""Gets the ccsp_version_need of this ImageInfo.

        密码服务依赖的(厂商)平台版本号

        :return: The ccsp_version_need of this ImageInfo.
        :rtype: str
        """
        return self._ccsp_version_need

    @ccsp_version_need.setter
    def ccsp_version_need(self, ccsp_version_need):
        r"""Sets the ccsp_version_need of this ImageInfo.

        密码服务依赖的(厂商)平台版本号

        :param ccsp_version_need: The ccsp_version_need of this ImageInfo.
        :type ccsp_version_need: str
        """
        self._ccsp_version_need = ccsp_version_need

    @property
    def hw_image_version(self):
        r"""Gets the hw_image_version of this ImageInfo.

        华为版本号

        :return: The hw_image_version of this ImageInfo.
        :rtype: str
        """
        return self._hw_image_version

    @hw_image_version.setter
    def hw_image_version(self, hw_image_version):
        r"""Sets the hw_image_version of this ImageInfo.

        华为版本号

        :param hw_image_version: The hw_image_version of this ImageInfo.
        :type hw_image_version: str
        """
        self._hw_image_version = hw_image_version

    @property
    def description(self):
        r"""Gets the description of this ImageInfo.

        描述

        :return: The description of this ImageInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ImageInfo.

        描述

        :param description: The description of this ImageInfo.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, ImageInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
