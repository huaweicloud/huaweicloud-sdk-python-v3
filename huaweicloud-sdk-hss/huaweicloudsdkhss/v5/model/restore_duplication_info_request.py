# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RestoreDuplicationInfoRequest:

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
        'backup_id': 'str',
        'body': 'RestoreDuplicationRequestInfo'
    }

    attribute_map = {
        'region': 'region',
        'enterprise_project_id': 'enterprise_project_id',
        'backup_id': 'backup_id',
        'body': 'body'
    }

    def __init__(self, region=None, enterprise_project_id=None, backup_id=None, body=None):
        r"""RestoreDuplicationInfoRequest

        The model defined in huaweicloud sdk

        :param region: **参数解释**: 区域ID，用于查询目的区域内的资产。获取方式请参见[获取区域ID](hss_02_0026.xml)。 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 
        :type region: str
        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param backup_id: **参数解释**: 备份ID **约束限制**: 不涉及 **取值范围**: 字符串大小0-64 **默认取值**: 不涉及 
        :type backup_id: str
        :param body: Body of the RestoreDuplicationInfoRequest
        :type body: :class:`huaweicloudsdkhss.v5.RestoreDuplicationRequestInfo`
        """
        
        

        self._region = None
        self._enterprise_project_id = None
        self._backup_id = None
        self._body = None
        self.discriminator = None

        if region is not None:
            self.region = region
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.backup_id = backup_id
        if body is not None:
            self.body = body

    @property
    def region(self):
        r"""Gets the region of this RestoreDuplicationInfoRequest.

        **参数解释**: 区域ID，用于查询目的区域内的资产。获取方式请参见[获取区域ID](hss_02_0026.xml)。 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :return: The region of this RestoreDuplicationInfoRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this RestoreDuplicationInfoRequest.

        **参数解释**: 区域ID，用于查询目的区域内的资产。获取方式请参见[获取区域ID](hss_02_0026.xml)。 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :param region: The region of this RestoreDuplicationInfoRequest.
        :type region: str
        """
        self._region = region

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this RestoreDuplicationInfoRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this RestoreDuplicationInfoRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this RestoreDuplicationInfoRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this RestoreDuplicationInfoRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def backup_id(self):
        r"""Gets the backup_id of this RestoreDuplicationInfoRequest.

        **参数解释**: 备份ID **约束限制**: 不涉及 **取值范围**: 字符串大小0-64 **默认取值**: 不涉及 

        :return: The backup_id of this RestoreDuplicationInfoRequest.
        :rtype: str
        """
        return self._backup_id

    @backup_id.setter
    def backup_id(self, backup_id):
        r"""Sets the backup_id of this RestoreDuplicationInfoRequest.

        **参数解释**: 备份ID **约束限制**: 不涉及 **取值范围**: 字符串大小0-64 **默认取值**: 不涉及 

        :param backup_id: The backup_id of this RestoreDuplicationInfoRequest.
        :type backup_id: str
        """
        self._backup_id = backup_id

    @property
    def body(self):
        r"""Gets the body of this RestoreDuplicationInfoRequest.

        :return: The body of this RestoreDuplicationInfoRequest.
        :rtype: :class:`huaweicloudsdkhss.v5.RestoreDuplicationRequestInfo`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this RestoreDuplicationInfoRequest.

        :param body: The body of this RestoreDuplicationInfoRequest.
        :type body: :class:`huaweicloudsdkhss.v5.RestoreDuplicationRequestInfo`
        """
        self._body = body

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
        if not isinstance(other, RestoreDuplicationInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
