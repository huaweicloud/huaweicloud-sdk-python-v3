# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVulRepoImageRequest:

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
        'vul_id': 'str',
        'namespace': 'str',
        'image_name': 'str',
        'image_id': 'str',
        'app_name': 'str'
    }

    attribute_map = {
        'region': 'region',
        'enterprise_project_id': 'enterprise_project_id',
        'limit': 'limit',
        'offset': 'offset',
        'vul_id': 'vul_id',
        'namespace': 'namespace',
        'image_name': 'image_name',
        'image_id': 'image_id',
        'app_name': 'app_name'
    }

    def __init__(self, region=None, enterprise_project_id=None, limit=None, offset=None, vul_id=None, namespace=None, image_name=None, image_id=None, app_name=None):
        r"""ListVulRepoImageRequest

        The model defined in huaweicloud sdk

        :param region: **参数解释**: 区域ID，用于查询目的区域内的资产。获取方式请参见[获取区域ID](hss_02_0026.xml)。 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 
        :type region: str
        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 
        :type offset: int
        :param vul_id: **参数解释**: 漏洞ID **约束限制**: 不涉及 **取值范围**: 字符长度0-65535位 **默认取值**: 不涉及 
        :type vul_id: str
        :param namespace: **参数解释**: 组织名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-65535位 **默认取值**: 不涉及 
        :type namespace: str
        :param image_name: **参数解释**: 镜像名称（支持模糊匹配） **约束限制**: 不涉及 **取值范围**: 字符长度0-65535位 **默认取值**: 不涉及 
        :type image_name: str
        :param image_id: **参数解释**: 镜像id **约束限制**: 不涉及 **取值范围**: 字符长度0-65535位 **默认取值**: 不涉及 
        :type image_id: str
        :param app_name: **参数解释**: 软件名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-65535位 **默认取值**: 不涉及 
        :type app_name: str
        """
        
        

        self._region = None
        self._enterprise_project_id = None
        self._limit = None
        self._offset = None
        self._vul_id = None
        self._namespace = None
        self._image_name = None
        self._image_id = None
        self._app_name = None
        self.discriminator = None

        if region is not None:
            self.region = region
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        self.vul_id = vul_id
        if namespace is not None:
            self.namespace = namespace
        if image_name is not None:
            self.image_name = image_name
        if image_id is not None:
            self.image_id = image_id
        if app_name is not None:
            self.app_name = app_name

    @property
    def region(self):
        r"""Gets the region of this ListVulRepoImageRequest.

        **参数解释**: 区域ID，用于查询目的区域内的资产。获取方式请参见[获取区域ID](hss_02_0026.xml)。 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :return: The region of this ListVulRepoImageRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ListVulRepoImageRequest.

        **参数解释**: 区域ID，用于查询目的区域内的资产。获取方式请参见[获取区域ID](hss_02_0026.xml)。 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :param region: The region of this ListVulRepoImageRequest.
        :type region: str
        """
        self._region = region

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListVulRepoImageRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListVulRepoImageRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListVulRepoImageRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListVulRepoImageRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def limit(self):
        r"""Gets the limit of this ListVulRepoImageRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListVulRepoImageRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListVulRepoImageRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListVulRepoImageRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListVulRepoImageRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :return: The offset of this ListVulRepoImageRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListVulRepoImageRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :param offset: The offset of this ListVulRepoImageRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def vul_id(self):
        r"""Gets the vul_id of this ListVulRepoImageRequest.

        **参数解释**: 漏洞ID **约束限制**: 不涉及 **取值范围**: 字符长度0-65535位 **默认取值**: 不涉及 

        :return: The vul_id of this ListVulRepoImageRequest.
        :rtype: str
        """
        return self._vul_id

    @vul_id.setter
    def vul_id(self, vul_id):
        r"""Sets the vul_id of this ListVulRepoImageRequest.

        **参数解释**: 漏洞ID **约束限制**: 不涉及 **取值范围**: 字符长度0-65535位 **默认取值**: 不涉及 

        :param vul_id: The vul_id of this ListVulRepoImageRequest.
        :type vul_id: str
        """
        self._vul_id = vul_id

    @property
    def namespace(self):
        r"""Gets the namespace of this ListVulRepoImageRequest.

        **参数解释**: 组织名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-65535位 **默认取值**: 不涉及 

        :return: The namespace of this ListVulRepoImageRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this ListVulRepoImageRequest.

        **参数解释**: 组织名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-65535位 **默认取值**: 不涉及 

        :param namespace: The namespace of this ListVulRepoImageRequest.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def image_name(self):
        r"""Gets the image_name of this ListVulRepoImageRequest.

        **参数解释**: 镜像名称（支持模糊匹配） **约束限制**: 不涉及 **取值范围**: 字符长度0-65535位 **默认取值**: 不涉及 

        :return: The image_name of this ListVulRepoImageRequest.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this ListVulRepoImageRequest.

        **参数解释**: 镜像名称（支持模糊匹配） **约束限制**: 不涉及 **取值范围**: 字符长度0-65535位 **默认取值**: 不涉及 

        :param image_name: The image_name of this ListVulRepoImageRequest.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def image_id(self):
        r"""Gets the image_id of this ListVulRepoImageRequest.

        **参数解释**: 镜像id **约束限制**: 不涉及 **取值范围**: 字符长度0-65535位 **默认取值**: 不涉及 

        :return: The image_id of this ListVulRepoImageRequest.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this ListVulRepoImageRequest.

        **参数解释**: 镜像id **约束限制**: 不涉及 **取值范围**: 字符长度0-65535位 **默认取值**: 不涉及 

        :param image_id: The image_id of this ListVulRepoImageRequest.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def app_name(self):
        r"""Gets the app_name of this ListVulRepoImageRequest.

        **参数解释**: 软件名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-65535位 **默认取值**: 不涉及 

        :return: The app_name of this ListVulRepoImageRequest.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this ListVulRepoImageRequest.

        **参数解释**: 软件名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-65535位 **默认取值**: 不涉及 

        :param app_name: The app_name of this ListVulRepoImageRequest.
        :type app_name: str
        """
        self._app_name = app_name

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
        if not isinstance(other, ListVulRepoImageRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
