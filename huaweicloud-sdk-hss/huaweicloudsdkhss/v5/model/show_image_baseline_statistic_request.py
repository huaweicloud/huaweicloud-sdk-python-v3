# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowImageBaselineStatisticRequest:

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
        'image_type': 'str',
        'namespace': 'str',
        'image_name': 'str',
        'image_version': 'str',
        'instance_id': 'str',
        'image_id': 'str'
    }

    attribute_map = {
        'region': 'region',
        'enterprise_project_id': 'enterprise_project_id',
        'image_type': 'image_type',
        'namespace': 'namespace',
        'image_name': 'image_name',
        'image_version': 'image_version',
        'instance_id': 'instance_id',
        'image_id': 'image_id'
    }

    def __init__(self, region=None, enterprise_project_id=None, image_type=None, namespace=None, image_name=None, image_version=None, instance_id=None, image_id=None):
        r"""ShowImageBaselineStatisticRequest

        The model defined in huaweicloud sdk

        :param region: **参数解释**: 区域ID，用于查询目的区域内的资产。获取方式请参见[获取区域ID](hss_02_0026.xml)。 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 
        :type region: str
        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param image_type: **参数解释**: 镜像类型 **约束限制**: 不涉及 **取值范围**: - private_image：私有镜像仓库。 - shared_image：共享镜像仓库。 - local_image : 本地镜像。 - instance_image：企业镜像。 - registry : 仓库镜像。 - local : 本地镜像，用于查询全局数据。  **默认取值**: 不涉及 
        :type image_type: str
        :param namespace: **参数解释**: 组织名称（没有镜像相关信息时，表示查询所有镜像） **约束限制**: 不涉及 **取值范围**: 字符长度0-65535位 **默认取值**: 不涉及 
        :type namespace: str
        :param image_name: **参数解释**: 镜像名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-65535位 **默认取值**: 不涉及 
        :type image_name: str
        :param image_version: **参数解释**: 镜像版本名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-65535位 **默认取值**: 不涉及 
        :type image_version: str
        :param instance_id: **参数解释**: 企业仓库实例ID，swr共享版无需使用该参数 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 
        :type instance_id: str
        :param image_id: **参数解释**: 镜像id **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 
        :type image_id: str
        """
        
        

        self._region = None
        self._enterprise_project_id = None
        self._image_type = None
        self._namespace = None
        self._image_name = None
        self._image_version = None
        self._instance_id = None
        self._image_id = None
        self.discriminator = None

        if region is not None:
            self.region = region
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.image_type = image_type
        if namespace is not None:
            self.namespace = namespace
        if image_name is not None:
            self.image_name = image_name
        if image_version is not None:
            self.image_version = image_version
        if instance_id is not None:
            self.instance_id = instance_id
        if image_id is not None:
            self.image_id = image_id

    @property
    def region(self):
        r"""Gets the region of this ShowImageBaselineStatisticRequest.

        **参数解释**: 区域ID，用于查询目的区域内的资产。获取方式请参见[获取区域ID](hss_02_0026.xml)。 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :return: The region of this ShowImageBaselineStatisticRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ShowImageBaselineStatisticRequest.

        **参数解释**: 区域ID，用于查询目的区域内的资产。获取方式请参见[获取区域ID](hss_02_0026.xml)。 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :param region: The region of this ShowImageBaselineStatisticRequest.
        :type region: str
        """
        self._region = region

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ShowImageBaselineStatisticRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ShowImageBaselineStatisticRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ShowImageBaselineStatisticRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ShowImageBaselineStatisticRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def image_type(self):
        r"""Gets the image_type of this ShowImageBaselineStatisticRequest.

        **参数解释**: 镜像类型 **约束限制**: 不涉及 **取值范围**: - private_image：私有镜像仓库。 - shared_image：共享镜像仓库。 - local_image : 本地镜像。 - instance_image：企业镜像。 - registry : 仓库镜像。 - local : 本地镜像，用于查询全局数据。  **默认取值**: 不涉及 

        :return: The image_type of this ShowImageBaselineStatisticRequest.
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        r"""Sets the image_type of this ShowImageBaselineStatisticRequest.

        **参数解释**: 镜像类型 **约束限制**: 不涉及 **取值范围**: - private_image：私有镜像仓库。 - shared_image：共享镜像仓库。 - local_image : 本地镜像。 - instance_image：企业镜像。 - registry : 仓库镜像。 - local : 本地镜像，用于查询全局数据。  **默认取值**: 不涉及 

        :param image_type: The image_type of this ShowImageBaselineStatisticRequest.
        :type image_type: str
        """
        self._image_type = image_type

    @property
    def namespace(self):
        r"""Gets the namespace of this ShowImageBaselineStatisticRequest.

        **参数解释**: 组织名称（没有镜像相关信息时，表示查询所有镜像） **约束限制**: 不涉及 **取值范围**: 字符长度0-65535位 **默认取值**: 不涉及 

        :return: The namespace of this ShowImageBaselineStatisticRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this ShowImageBaselineStatisticRequest.

        **参数解释**: 组织名称（没有镜像相关信息时，表示查询所有镜像） **约束限制**: 不涉及 **取值范围**: 字符长度0-65535位 **默认取值**: 不涉及 

        :param namespace: The namespace of this ShowImageBaselineStatisticRequest.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def image_name(self):
        r"""Gets the image_name of this ShowImageBaselineStatisticRequest.

        **参数解释**: 镜像名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-65535位 **默认取值**: 不涉及 

        :return: The image_name of this ShowImageBaselineStatisticRequest.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this ShowImageBaselineStatisticRequest.

        **参数解释**: 镜像名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-65535位 **默认取值**: 不涉及 

        :param image_name: The image_name of this ShowImageBaselineStatisticRequest.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def image_version(self):
        r"""Gets the image_version of this ShowImageBaselineStatisticRequest.

        **参数解释**: 镜像版本名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-65535位 **默认取值**: 不涉及 

        :return: The image_version of this ShowImageBaselineStatisticRequest.
        :rtype: str
        """
        return self._image_version

    @image_version.setter
    def image_version(self, image_version):
        r"""Sets the image_version of this ShowImageBaselineStatisticRequest.

        **参数解释**: 镜像版本名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-65535位 **默认取值**: 不涉及 

        :param image_version: The image_version of this ShowImageBaselineStatisticRequest.
        :type image_version: str
        """
        self._image_version = image_version

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowImageBaselineStatisticRequest.

        **参数解释**: 企业仓库实例ID，swr共享版无需使用该参数 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :return: The instance_id of this ShowImageBaselineStatisticRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowImageBaselineStatisticRequest.

        **参数解释**: 企业仓库实例ID，swr共享版无需使用该参数 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :param instance_id: The instance_id of this ShowImageBaselineStatisticRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def image_id(self):
        r"""Gets the image_id of this ShowImageBaselineStatisticRequest.

        **参数解释**: 镜像id **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :return: The image_id of this ShowImageBaselineStatisticRequest.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this ShowImageBaselineStatisticRequest.

        **参数解释**: 镜像id **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :param image_id: The image_id of this ShowImageBaselineStatisticRequest.
        :type image_id: str
        """
        self._image_id = image_id

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
        if not isinstance(other, ShowImageBaselineStatisticRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
