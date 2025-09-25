# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVulAffectImageAppsRequest:

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
        'is_handled': 'bool',
        'image_type': 'str',
        'vul_id': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'offset': 'offset',
        'limit': 'limit',
        'image_id': 'image_id',
        'is_handled': 'is_handled',
        'image_type': 'image_type',
        'vul_id': 'vul_id'
    }

    def __init__(self, enterprise_project_id=None, offset=None, limit=None, image_id=None, is_handled=None, image_type=None, vul_id=None):
        r"""ListVulAffectImageAppsRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 
        :type offset: int
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        :param image_id: 镜像id
        :type image_id: str
        :param is_handled: 是否已处理
        :type is_handled: bool
        :param image_type: 镜像类型，包含如下：   -local : 本地镜像   -registry : 仓库镜像   -cicd : CI/CD镜像   -cluster : 集群镜像
        :type image_type: str
        :param vul_id: 漏洞id
        :type vul_id: str
        """
        
        

        self._enterprise_project_id = None
        self._offset = None
        self._limit = None
        self._image_id = None
        self._is_handled = None
        self._image_type = None
        self._vul_id = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        self.image_id = image_id
        self.is_handled = is_handled
        self.image_type = image_type
        self.vul_id = vul_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListVulAffectImageAppsRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListVulAffectImageAppsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListVulAffectImageAppsRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListVulAffectImageAppsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def offset(self):
        r"""Gets the offset of this ListVulAffectImageAppsRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :return: The offset of this ListVulAffectImageAppsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListVulAffectImageAppsRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :param offset: The offset of this ListVulAffectImageAppsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListVulAffectImageAppsRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListVulAffectImageAppsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListVulAffectImageAppsRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListVulAffectImageAppsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def image_id(self):
        r"""Gets the image_id of this ListVulAffectImageAppsRequest.

        镜像id

        :return: The image_id of this ListVulAffectImageAppsRequest.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this ListVulAffectImageAppsRequest.

        镜像id

        :param image_id: The image_id of this ListVulAffectImageAppsRequest.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def is_handled(self):
        r"""Gets the is_handled of this ListVulAffectImageAppsRequest.

        是否已处理

        :return: The is_handled of this ListVulAffectImageAppsRequest.
        :rtype: bool
        """
        return self._is_handled

    @is_handled.setter
    def is_handled(self, is_handled):
        r"""Sets the is_handled of this ListVulAffectImageAppsRequest.

        是否已处理

        :param is_handled: The is_handled of this ListVulAffectImageAppsRequest.
        :type is_handled: bool
        """
        self._is_handled = is_handled

    @property
    def image_type(self):
        r"""Gets the image_type of this ListVulAffectImageAppsRequest.

        镜像类型，包含如下：   -local : 本地镜像   -registry : 仓库镜像   -cicd : CI/CD镜像   -cluster : 集群镜像

        :return: The image_type of this ListVulAffectImageAppsRequest.
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        r"""Sets the image_type of this ListVulAffectImageAppsRequest.

        镜像类型，包含如下：   -local : 本地镜像   -registry : 仓库镜像   -cicd : CI/CD镜像   -cluster : 集群镜像

        :param image_type: The image_type of this ListVulAffectImageAppsRequest.
        :type image_type: str
        """
        self._image_type = image_type

    @property
    def vul_id(self):
        r"""Gets the vul_id of this ListVulAffectImageAppsRequest.

        漏洞id

        :return: The vul_id of this ListVulAffectImageAppsRequest.
        :rtype: str
        """
        return self._vul_id

    @vul_id.setter
    def vul_id(self, vul_id):
        r"""Sets the vul_id of this ListVulAffectImageAppsRequest.

        漏洞id

        :param vul_id: The vul_id of this ListVulAffectImageAppsRequest.
        :type vul_id: str
        """
        self._vul_id = vul_id

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
        if not isinstance(other, ListVulAffectImageAppsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
