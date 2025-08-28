# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportRisksRequest:

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
        'risk_type': 'str',
        'export_size': 'int',
        'body': 'ExportRisksRequestBody'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'risk_type': 'risk_type',
        'export_size': 'export_size',
        'body': 'body'
    }

    def __init__(self, enterprise_project_id=None, risk_type=None, export_size=None, body=None):
        r"""ExportRisksRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param risk_type: **参数解释**: 风险类型 **约束限制**: 不涉及 **取值范围**: - iac_risk: IaC风险。  **默认取值**: 不涉及 
        :type risk_type: str
        :param export_size: **参数解释**: 导出数据条数 **约束限制**: 不涉及 **取值范围**: 不涉及 **默认取值**: 不涉及 
        :type export_size: int
        :param body: Body of the ExportRisksRequest
        :type body: :class:`huaweicloudsdkhss.v5.ExportRisksRequestBody`
        """
        
        

        self._enterprise_project_id = None
        self._risk_type = None
        self._export_size = None
        self._body = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.risk_type = risk_type
        self.export_size = export_size
        if body is not None:
            self.body = body

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ExportRisksRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ExportRisksRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ExportRisksRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ExportRisksRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def risk_type(self):
        r"""Gets the risk_type of this ExportRisksRequest.

        **参数解释**: 风险类型 **约束限制**: 不涉及 **取值范围**: - iac_risk: IaC风险。  **默认取值**: 不涉及 

        :return: The risk_type of this ExportRisksRequest.
        :rtype: str
        """
        return self._risk_type

    @risk_type.setter
    def risk_type(self, risk_type):
        r"""Sets the risk_type of this ExportRisksRequest.

        **参数解释**: 风险类型 **约束限制**: 不涉及 **取值范围**: - iac_risk: IaC风险。  **默认取值**: 不涉及 

        :param risk_type: The risk_type of this ExportRisksRequest.
        :type risk_type: str
        """
        self._risk_type = risk_type

    @property
    def export_size(self):
        r"""Gets the export_size of this ExportRisksRequest.

        **参数解释**: 导出数据条数 **约束限制**: 不涉及 **取值范围**: 不涉及 **默认取值**: 不涉及 

        :return: The export_size of this ExportRisksRequest.
        :rtype: int
        """
        return self._export_size

    @export_size.setter
    def export_size(self, export_size):
        r"""Sets the export_size of this ExportRisksRequest.

        **参数解释**: 导出数据条数 **约束限制**: 不涉及 **取值范围**: 不涉及 **默认取值**: 不涉及 

        :param export_size: The export_size of this ExportRisksRequest.
        :type export_size: int
        """
        self._export_size = export_size

    @property
    def body(self):
        r"""Gets the body of this ExportRisksRequest.

        :return: The body of this ExportRisksRequest.
        :rtype: :class:`huaweicloudsdkhss.v5.ExportRisksRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this ExportRisksRequest.

        :param body: The body of this ExportRisksRequest.
        :type body: :class:`huaweicloudsdkhss.v5.ExportRisksRequestBody`
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
        if not isinstance(other, ExportRisksRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
