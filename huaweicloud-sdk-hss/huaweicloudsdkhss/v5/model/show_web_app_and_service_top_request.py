# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowWebAppAndServiceTopRequest:

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
        'catalogue': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'catalogue': 'catalogue'
    }

    def __init__(self, enterprise_project_id=None, catalogue=None):
        r"""ShowWebAppAndServiceTopRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param catalogue: **参数解释**: web类型 **约束限制**: 不涉及 **取值范围**: - web_cms：web应用 - web_service：web服务 - database：数据库 **默认取值**: 不涉及 
        :type catalogue: str
        """
        
        

        self._enterprise_project_id = None
        self._catalogue = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.catalogue = catalogue

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ShowWebAppAndServiceTopRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ShowWebAppAndServiceTopRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ShowWebAppAndServiceTopRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ShowWebAppAndServiceTopRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def catalogue(self):
        r"""Gets the catalogue of this ShowWebAppAndServiceTopRequest.

        **参数解释**: web类型 **约束限制**: 不涉及 **取值范围**: - web_cms：web应用 - web_service：web服务 - database：数据库 **默认取值**: 不涉及 

        :return: The catalogue of this ShowWebAppAndServiceTopRequest.
        :rtype: str
        """
        return self._catalogue

    @catalogue.setter
    def catalogue(self, catalogue):
        r"""Sets the catalogue of this ShowWebAppAndServiceTopRequest.

        **参数解释**: web类型 **约束限制**: 不涉及 **取值范围**: - web_cms：web应用 - web_service：web服务 - database：数据库 **默认取值**: 不涉及 

        :param catalogue: The catalogue of this ShowWebAppAndServiceTopRequest.
        :type catalogue: str
        """
        self._catalogue = catalogue

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
        if not isinstance(other, ShowWebAppAndServiceTopRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
