# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVulAffectImageContainersRequest:

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
        'offset': 'int',
        'limit': 'int',
        'image_id': 'str',
        'image_digest': 'str',
        'image_name': 'str',
        'image_version': 'str',
        'agent_id': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'offset': 'offset',
        'limit': 'limit',
        'image_id': 'image_id',
        'image_digest': 'image_digest',
        'image_name': 'image_name',
        'image_version': 'image_version',
        'agent_id': 'agent_id'
    }

    def __init__(self, enterprise_project_id=None, offset=None, limit=None, image_id=None, image_digest=None, image_name=None, image_version=None, agent_id=None):
        r"""ListVulAffectImageContainersRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 
        :type offset: int
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        :param image_id: 镜像id
        :type image_id: str
        :param image_digest: 镜像标识
        :type image_digest: str
        :param image_name: 镜像名称
        :type image_name: str
        :param image_version: 镜像版本
        :type image_version: str
        :param agent_id: Agent ID
        :type agent_id: str
        """
        
        

        self._enterprise_project_id = None
        self._offset = None
        self._limit = None
        self._image_id = None
        self._image_digest = None
        self._image_name = None
        self._image_version = None
        self._agent_id = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        self.image_id = image_id
        self.image_digest = image_digest
        self.image_name = image_name
        self.image_version = image_version
        self.agent_id = agent_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListVulAffectImageContainersRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListVulAffectImageContainersRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListVulAffectImageContainersRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListVulAffectImageContainersRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def offset(self):
        r"""Gets the offset of this ListVulAffectImageContainersRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :return: The offset of this ListVulAffectImageContainersRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListVulAffectImageContainersRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :param offset: The offset of this ListVulAffectImageContainersRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListVulAffectImageContainersRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListVulAffectImageContainersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListVulAffectImageContainersRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListVulAffectImageContainersRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def image_id(self):
        r"""Gets the image_id of this ListVulAffectImageContainersRequest.

        镜像id

        :return: The image_id of this ListVulAffectImageContainersRequest.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this ListVulAffectImageContainersRequest.

        镜像id

        :param image_id: The image_id of this ListVulAffectImageContainersRequest.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def image_digest(self):
        r"""Gets the image_digest of this ListVulAffectImageContainersRequest.

        镜像标识

        :return: The image_digest of this ListVulAffectImageContainersRequest.
        :rtype: str
        """
        return self._image_digest

    @image_digest.setter
    def image_digest(self, image_digest):
        r"""Sets the image_digest of this ListVulAffectImageContainersRequest.

        镜像标识

        :param image_digest: The image_digest of this ListVulAffectImageContainersRequest.
        :type image_digest: str
        """
        self._image_digest = image_digest

    @property
    def image_name(self):
        r"""Gets the image_name of this ListVulAffectImageContainersRequest.

        镜像名称

        :return: The image_name of this ListVulAffectImageContainersRequest.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this ListVulAffectImageContainersRequest.

        镜像名称

        :param image_name: The image_name of this ListVulAffectImageContainersRequest.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def image_version(self):
        r"""Gets the image_version of this ListVulAffectImageContainersRequest.

        镜像版本

        :return: The image_version of this ListVulAffectImageContainersRequest.
        :rtype: str
        """
        return self._image_version

    @image_version.setter
    def image_version(self, image_version):
        r"""Sets the image_version of this ListVulAffectImageContainersRequest.

        镜像版本

        :param image_version: The image_version of this ListVulAffectImageContainersRequest.
        :type image_version: str
        """
        self._image_version = image_version

    @property
    def agent_id(self):
        r"""Gets the agent_id of this ListVulAffectImageContainersRequest.

        Agent ID

        :return: The agent_id of this ListVulAffectImageContainersRequest.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        r"""Sets the agent_id of this ListVulAffectImageContainersRequest.

        Agent ID

        :param agent_id: The agent_id of this ListVulAffectImageContainersRequest.
        :type agent_id: str
        """
        self._agent_id = agent_id

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
        if not isinstance(other, ListVulAffectImageContainersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
