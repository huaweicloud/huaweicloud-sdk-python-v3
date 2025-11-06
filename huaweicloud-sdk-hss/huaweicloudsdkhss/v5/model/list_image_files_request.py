# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListImageFilesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'limit': 'int',
        'offset': 'int',
        'image_type': 'str',
        'image_id': 'str',
        'namespace': 'str',
        'image_name': 'str',
        'tag_name': 'str',
        'file_name': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'limit': 'limit',
        'offset': 'offset',
        'image_type': 'image_type',
        'image_id': 'image_id',
        'namespace': 'namespace',
        'image_name': 'image_name',
        'tag_name': 'tag_name',
        'file_name': 'file_name'
    }

    def __init__(self, enterprise_project_id=None, limit=None, offset=None, image_type=None, image_id=None, namespace=None, image_name=None, tag_name=None, file_name=None):
        r"""ListImageFilesRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 
        :type offset: int
        :param image_type: **参数解释**: 镜像类型 **取值范围**: - private_image : 私有镜像仓库 - shared_image : 共享镜像仓库 - instance_image : 企业镜像 - cicd : cicd镜像 - harbor ：Harbor仓库镜像 **默认取值**: 不涉及 
        :type image_type: str
        :param image_id: **参数解释**: 镜像id **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 
        :type image_id: str
        :param namespace: **参数解释**: 组织名称 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 
        :type namespace: str
        :param image_name: **参数解释**: 镜像名称 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 
        :type image_name: str
        :param tag_name: **参数解释**: 镜像版本名称 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 
        :type tag_name: str
        :param file_name: **参数解释**: 文件名称过滤查询(支持模糊匹配) **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 
        :type file_name: str
        """
        
        

        self._enterprise_project_id = None
        self._limit = None
        self._offset = None
        self._image_type = None
        self._image_id = None
        self._namespace = None
        self._image_name = None
        self._tag_name = None
        self._file_name = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        self.image_type = image_type
        self.image_id = image_id
        if namespace is not None:
            self.namespace = namespace
        if image_name is not None:
            self.image_name = image_name
        if tag_name is not None:
            self.tag_name = tag_name
        if file_name is not None:
            self.file_name = file_name

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListImageFilesRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListImageFilesRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListImageFilesRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListImageFilesRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def limit(self):
        r"""Gets the limit of this ListImageFilesRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListImageFilesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListImageFilesRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListImageFilesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListImageFilesRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :return: The offset of this ListImageFilesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListImageFilesRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :param offset: The offset of this ListImageFilesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def image_type(self):
        r"""Gets the image_type of this ListImageFilesRequest.

        **参数解释**: 镜像类型 **取值范围**: - private_image : 私有镜像仓库 - shared_image : 共享镜像仓库 - instance_image : 企业镜像 - cicd : cicd镜像 - harbor ：Harbor仓库镜像 **默认取值**: 不涉及 

        :return: The image_type of this ListImageFilesRequest.
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        r"""Sets the image_type of this ListImageFilesRequest.

        **参数解释**: 镜像类型 **取值范围**: - private_image : 私有镜像仓库 - shared_image : 共享镜像仓库 - instance_image : 企业镜像 - cicd : cicd镜像 - harbor ：Harbor仓库镜像 **默认取值**: 不涉及 

        :param image_type: The image_type of this ListImageFilesRequest.
        :type image_type: str
        """
        self._image_type = image_type

    @property
    def image_id(self):
        r"""Gets the image_id of this ListImageFilesRequest.

        **参数解释**: 镜像id **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :return: The image_id of this ListImageFilesRequest.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this ListImageFilesRequest.

        **参数解释**: 镜像id **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :param image_id: The image_id of this ListImageFilesRequest.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def namespace(self):
        r"""Gets the namespace of this ListImageFilesRequest.

        **参数解释**: 组织名称 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :return: The namespace of this ListImageFilesRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this ListImageFilesRequest.

        **参数解释**: 组织名称 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :param namespace: The namespace of this ListImageFilesRequest.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def image_name(self):
        r"""Gets the image_name of this ListImageFilesRequest.

        **参数解释**: 镜像名称 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :return: The image_name of this ListImageFilesRequest.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this ListImageFilesRequest.

        **参数解释**: 镜像名称 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :param image_name: The image_name of this ListImageFilesRequest.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def tag_name(self):
        r"""Gets the tag_name of this ListImageFilesRequest.

        **参数解释**: 镜像版本名称 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :return: The tag_name of this ListImageFilesRequest.
        :rtype: str
        """
        return self._tag_name

    @tag_name.setter
    def tag_name(self, tag_name):
        r"""Sets the tag_name of this ListImageFilesRequest.

        **参数解释**: 镜像版本名称 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :param tag_name: The tag_name of this ListImageFilesRequest.
        :type tag_name: str
        """
        self._tag_name = tag_name

    @property
    def file_name(self):
        r"""Gets the file_name of this ListImageFilesRequest.

        **参数解释**: 文件名称过滤查询(支持模糊匹配) **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :return: The file_name of this ListImageFilesRequest.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this ListImageFilesRequest.

        **参数解释**: 文件名称过滤查询(支持模糊匹配) **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :param file_name: The file_name of this ListImageFilesRequest.
        :type file_name: str
        """
        self._file_name = file_name

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
        if not isinstance(other, ListImageFilesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
