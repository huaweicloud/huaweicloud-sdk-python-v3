# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowEdgeWafDomainsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domainid': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'domainid': 'domainid',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, domainid=None, enterprise_project_id=None):
        """ShowEdgeWafDomainsRequest

        The model defined in huaweicloud sdk

        :param domainid: 防护域名id
        :type domainid: str
        :param enterprise_project_id: 您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id
        :type enterprise_project_id: str
        """
        
        

        self._domainid = None
        self._enterprise_project_id = None
        self.discriminator = None

        self.domainid = domainid
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def domainid(self):
        """Gets the domainid of this ShowEdgeWafDomainsRequest.

        防护域名id

        :return: The domainid of this ShowEdgeWafDomainsRequest.
        :rtype: str
        """
        return self._domainid

    @domainid.setter
    def domainid(self, domainid):
        """Sets the domainid of this ShowEdgeWafDomainsRequest.

        防护域名id

        :param domainid: The domainid of this ShowEdgeWafDomainsRequest.
        :type domainid: str
        """
        self._domainid = domainid

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ShowEdgeWafDomainsRequest.

        您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id

        :return: The enterprise_project_id of this ShowEdgeWafDomainsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ShowEdgeWafDomainsRequest.

        您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id

        :param enterprise_project_id: The enterprise_project_id of this ShowEdgeWafDomainsRequest.
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
        if not isinstance(other, ShowEdgeWafDomainsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
