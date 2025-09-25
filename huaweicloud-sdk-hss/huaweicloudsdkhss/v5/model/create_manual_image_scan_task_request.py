# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateManualImageScanTaskRequest:

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
        'global_image_type': 'str',
        'body': 'CreateManualImageScanTaskReqInfo'
    }

    attribute_map = {
        'region': 'region',
        'enterprise_project_id': 'enterprise_project_id',
        'global_image_type': 'global_image_type',
        'body': 'body'
    }

    def __init__(self, region=None, enterprise_project_id=None, global_image_type=None, body=None):
        r"""CreateManualImageScanTaskRequest

        The model defined in huaweicloud sdk

        :param region: **参数解释**: 区域ID，用于查询目的区域内的资产。获取方式请参见[获取区域ID](hss_02_0026.xml)。 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 
        :type region: str
        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param global_image_type: **参数解释**: 镜像类型 **约束限制**: 不涉及 **取值范围**: - local：本地镜像。 - registry：仓库镜像。  **默认取值**: registry 
        :type global_image_type: str
        :param body: Body of the CreateManualImageScanTaskRequest
        :type body: :class:`huaweicloudsdkhss.v5.CreateManualImageScanTaskReqInfo`
        """
        
        

        self._region = None
        self._enterprise_project_id = None
        self._global_image_type = None
        self._body = None
        self.discriminator = None

        if region is not None:
            self.region = region
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if global_image_type is not None:
            self.global_image_type = global_image_type
        if body is not None:
            self.body = body

    @property
    def region(self):
        r"""Gets the region of this CreateManualImageScanTaskRequest.

        **参数解释**: 区域ID，用于查询目的区域内的资产。获取方式请参见[获取区域ID](hss_02_0026.xml)。 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :return: The region of this CreateManualImageScanTaskRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this CreateManualImageScanTaskRequest.

        **参数解释**: 区域ID，用于查询目的区域内的资产。获取方式请参见[获取区域ID](hss_02_0026.xml)。 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :param region: The region of this CreateManualImageScanTaskRequest.
        :type region: str
        """
        self._region = region

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CreateManualImageScanTaskRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this CreateManualImageScanTaskRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CreateManualImageScanTaskRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this CreateManualImageScanTaskRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def global_image_type(self):
        r"""Gets the global_image_type of this CreateManualImageScanTaskRequest.

        **参数解释**: 镜像类型 **约束限制**: 不涉及 **取值范围**: - local：本地镜像。 - registry：仓库镜像。  **默认取值**: registry 

        :return: The global_image_type of this CreateManualImageScanTaskRequest.
        :rtype: str
        """
        return self._global_image_type

    @global_image_type.setter
    def global_image_type(self, global_image_type):
        r"""Sets the global_image_type of this CreateManualImageScanTaskRequest.

        **参数解释**: 镜像类型 **约束限制**: 不涉及 **取值范围**: - local：本地镜像。 - registry：仓库镜像。  **默认取值**: registry 

        :param global_image_type: The global_image_type of this CreateManualImageScanTaskRequest.
        :type global_image_type: str
        """
        self._global_image_type = global_image_type

    @property
    def body(self):
        r"""Gets the body of this CreateManualImageScanTaskRequest.

        :return: The body of this CreateManualImageScanTaskRequest.
        :rtype: :class:`huaweicloudsdkhss.v5.CreateManualImageScanTaskReqInfo`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this CreateManualImageScanTaskRequest.

        :param body: The body of this CreateManualImageScanTaskRequest.
        :type body: :class:`huaweicloudsdkhss.v5.CreateManualImageScanTaskReqInfo`
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
        if not isinstance(other, CreateManualImageScanTaskRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
