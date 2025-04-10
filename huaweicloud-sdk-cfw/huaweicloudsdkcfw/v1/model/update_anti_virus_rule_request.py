# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAntiVirusRuleRequest:

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
        'body': 'AntiVirusRuleDto'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'body': 'body'
    }

    def __init__(self, enterprise_project_id=None, body=None):
        r"""UpdateAntiVirusRuleRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 企业项目ID，用户根据组织规划企业项目，对应的ID为企业项目ID，可通过[如何获取企业项目ID](cfw_02_0027.xml)获取，用户未开启企业项目时为0
        :type enterprise_project_id: str
        :param body: Body of the UpdateAntiVirusRuleRequest
        :type body: :class:`huaweicloudsdkcfw.v1.AntiVirusRuleDto`
        """
        
        

        self._enterprise_project_id = None
        self._body = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if body is not None:
            self.body = body

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this UpdateAntiVirusRuleRequest.

        企业项目ID，用户根据组织规划企业项目，对应的ID为企业项目ID，可通过[如何获取企业项目ID](cfw_02_0027.xml)获取，用户未开启企业项目时为0

        :return: The enterprise_project_id of this UpdateAntiVirusRuleRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this UpdateAntiVirusRuleRequest.

        企业项目ID，用户根据组织规划企业项目，对应的ID为企业项目ID，可通过[如何获取企业项目ID](cfw_02_0027.xml)获取，用户未开启企业项目时为0

        :param enterprise_project_id: The enterprise_project_id of this UpdateAntiVirusRuleRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def body(self):
        r"""Gets the body of this UpdateAntiVirusRuleRequest.

        :return: The body of this UpdateAntiVirusRuleRequest.
        :rtype: :class:`huaweicloudsdkcfw.v1.AntiVirusRuleDto`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateAntiVirusRuleRequest.

        :param body: The body of this UpdateAntiVirusRuleRequest.
        :type body: :class:`huaweicloudsdkcfw.v1.AntiVirusRuleDto`
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
        if not isinstance(other, UpdateAntiVirusRuleRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
