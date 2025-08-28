# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListImageHandleAffectVulnerabilitiesRequest:

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
        'image_name': 'str',
        'vul_name': 'str',
        'body': 'HandleImageVulnerabilityRequestBody'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'offset': 'offset',
        'limit': 'limit',
        'image_name': 'image_name',
        'vul_name': 'vul_name',
        'body': 'body'
    }

    def __init__(self, enterprise_project_id=None, offset=None, limit=None, image_name=None, vul_name=None, body=None):
        r"""ListImageHandleAffectVulnerabilitiesRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 不涉及 
        :type offset: int
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        :param image_name: **参数解释**: 镜像名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-512 **默认取值**: 不涉及 
        :type image_name: str
        :param vul_name: **参数解释**: 漏洞名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-512 **默认取值**: 不涉及 
        :type vul_name: str
        :param body: Body of the ListImageHandleAffectVulnerabilitiesRequest
        :type body: :class:`huaweicloudsdkhss.v5.HandleImageVulnerabilityRequestBody`
        """
        
        

        self._enterprise_project_id = None
        self._offset = None
        self._limit = None
        self._image_name = None
        self._vul_name = None
        self._body = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.offset = offset
        self.limit = limit
        if image_name is not None:
            self.image_name = image_name
        if vul_name is not None:
            self.vul_name = vul_name
        if body is not None:
            self.body = body

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListImageHandleAffectVulnerabilitiesRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListImageHandleAffectVulnerabilitiesRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListImageHandleAffectVulnerabilitiesRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListImageHandleAffectVulnerabilitiesRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def offset(self):
        r"""Gets the offset of this ListImageHandleAffectVulnerabilitiesRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 不涉及 

        :return: The offset of this ListImageHandleAffectVulnerabilitiesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListImageHandleAffectVulnerabilitiesRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 不涉及 

        :param offset: The offset of this ListImageHandleAffectVulnerabilitiesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListImageHandleAffectVulnerabilitiesRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListImageHandleAffectVulnerabilitiesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListImageHandleAffectVulnerabilitiesRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListImageHandleAffectVulnerabilitiesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def image_name(self):
        r"""Gets the image_name of this ListImageHandleAffectVulnerabilitiesRequest.

        **参数解释**: 镜像名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-512 **默认取值**: 不涉及 

        :return: The image_name of this ListImageHandleAffectVulnerabilitiesRequest.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this ListImageHandleAffectVulnerabilitiesRequest.

        **参数解释**: 镜像名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-512 **默认取值**: 不涉及 

        :param image_name: The image_name of this ListImageHandleAffectVulnerabilitiesRequest.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def vul_name(self):
        r"""Gets the vul_name of this ListImageHandleAffectVulnerabilitiesRequest.

        **参数解释**: 漏洞名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-512 **默认取值**: 不涉及 

        :return: The vul_name of this ListImageHandleAffectVulnerabilitiesRequest.
        :rtype: str
        """
        return self._vul_name

    @vul_name.setter
    def vul_name(self, vul_name):
        r"""Sets the vul_name of this ListImageHandleAffectVulnerabilitiesRequest.

        **参数解释**: 漏洞名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-512 **默认取值**: 不涉及 

        :param vul_name: The vul_name of this ListImageHandleAffectVulnerabilitiesRequest.
        :type vul_name: str
        """
        self._vul_name = vul_name

    @property
    def body(self):
        r"""Gets the body of this ListImageHandleAffectVulnerabilitiesRequest.

        :return: The body of this ListImageHandleAffectVulnerabilitiesRequest.
        :rtype: :class:`huaweicloudsdkhss.v5.HandleImageVulnerabilityRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this ListImageHandleAffectVulnerabilitiesRequest.

        :param body: The body of this ListImageHandleAffectVulnerabilitiesRequest.
        :type body: :class:`huaweicloudsdkhss.v5.HandleImageVulnerabilityRequestBody`
        """
        self._body = body

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
        if not isinstance(other, ListImageHandleAffectVulnerabilitiesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
