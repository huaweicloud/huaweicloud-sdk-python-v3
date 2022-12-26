# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LiveDomainModifyReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain': 'str',
        'status': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'domain': 'domain',
        'status': 'status',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, domain=None, status=None, enterprise_project_id=None):
        """LiveDomainModifyReq

        The model defined in huaweicloud sdk

        :param domain: 直播域名，不允许修改
        :type domain: str
        :param status: 直播域名状态，通过修改此字段，实现域名的启用和停用。注意：域名处于“配置中”状态时，不允对该域名执行启停操作。
        :type status: str
        :param enterprise_project_id: 企业项目ID
        :type enterprise_project_id: str
        """
        
        

        self._domain = None
        self._status = None
        self._enterprise_project_id = None
        self.discriminator = None

        self.domain = domain
        if status is not None:
            self.status = status
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def domain(self):
        """Gets the domain of this LiveDomainModifyReq.

        直播域名，不允许修改

        :return: The domain of this LiveDomainModifyReq.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this LiveDomainModifyReq.

        直播域名，不允许修改

        :param domain: The domain of this LiveDomainModifyReq.
        :type domain: str
        """
        self._domain = domain

    @property
    def status(self):
        """Gets the status of this LiveDomainModifyReq.

        直播域名状态，通过修改此字段，实现域名的启用和停用。注意：域名处于“配置中”状态时，不允对该域名执行启停操作。

        :return: The status of this LiveDomainModifyReq.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this LiveDomainModifyReq.

        直播域名状态，通过修改此字段，实现域名的启用和停用。注意：域名处于“配置中”状态时，不允对该域名执行启停操作。

        :param status: The status of this LiveDomainModifyReq.
        :type status: str
        """
        self._status = status

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this LiveDomainModifyReq.

        企业项目ID

        :return: The enterprise_project_id of this LiveDomainModifyReq.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this LiveDomainModifyReq.

        企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this LiveDomainModifyReq.
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
        if not isinstance(other, LiveDomainModifyReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
