# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDomainSetDetailRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'fw_instance_id': 'str',
        'domain_set_id': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'fw_instance_id': 'fw_instance_id',
        'domain_set_id': 'domain_set_id',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, fw_instance_id=None, domain_set_id=None, enterprise_project_id=None):
        r"""ShowDomainSetDetailRequest

        The model defined in huaweicloud sdk

        :param fw_instance_id: 防火墙ID，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取
        :type fw_instance_id: str
        :param domain_set_id: 域名组ID，可通过[查询域名组列表接口](ListDomainSets.xml)查询获得，通过返回值中的data.records.set_id（.表示各对象之间层级的区分）获取
        :type domain_set_id: str
        :param enterprise_project_id: 企业项目ID，用户根据组织规划企业项目，对应的ID为企业项目ID，可通过[如何获取企业项目ID](cfw_02_0027.xml)获取，用户未开启企业项目时为0
        :type enterprise_project_id: str
        """
        
        

        self._fw_instance_id = None
        self._domain_set_id = None
        self._enterprise_project_id = None
        self.discriminator = None

        self.fw_instance_id = fw_instance_id
        self.domain_set_id = domain_set_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def fw_instance_id(self):
        r"""Gets the fw_instance_id of this ShowDomainSetDetailRequest.

        防火墙ID，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取

        :return: The fw_instance_id of this ShowDomainSetDetailRequest.
        :rtype: str
        """
        return self._fw_instance_id

    @fw_instance_id.setter
    def fw_instance_id(self, fw_instance_id):
        r"""Sets the fw_instance_id of this ShowDomainSetDetailRequest.

        防火墙ID，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取

        :param fw_instance_id: The fw_instance_id of this ShowDomainSetDetailRequest.
        :type fw_instance_id: str
        """
        self._fw_instance_id = fw_instance_id

    @property
    def domain_set_id(self):
        r"""Gets the domain_set_id of this ShowDomainSetDetailRequest.

        域名组ID，可通过[查询域名组列表接口](ListDomainSets.xml)查询获得，通过返回值中的data.records.set_id（.表示各对象之间层级的区分）获取

        :return: The domain_set_id of this ShowDomainSetDetailRequest.
        :rtype: str
        """
        return self._domain_set_id

    @domain_set_id.setter
    def domain_set_id(self, domain_set_id):
        r"""Sets the domain_set_id of this ShowDomainSetDetailRequest.

        域名组ID，可通过[查询域名组列表接口](ListDomainSets.xml)查询获得，通过返回值中的data.records.set_id（.表示各对象之间层级的区分）获取

        :param domain_set_id: The domain_set_id of this ShowDomainSetDetailRequest.
        :type domain_set_id: str
        """
        self._domain_set_id = domain_set_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ShowDomainSetDetailRequest.

        企业项目ID，用户根据组织规划企业项目，对应的ID为企业项目ID，可通过[如何获取企业项目ID](cfw_02_0027.xml)获取，用户未开启企业项目时为0

        :return: The enterprise_project_id of this ShowDomainSetDetailRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ShowDomainSetDetailRequest.

        企业项目ID，用户根据组织规划企业项目，对应的ID为企业项目ID，可通过[如何获取企业项目ID](cfw_02_0027.xml)获取，用户未开启企业项目时为0

        :param enterprise_project_id: The enterprise_project_id of this ShowDomainSetDetailRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, ShowDomainSetDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
