# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeletePremiumHostRequest:

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
        'host_id': 'str',
        'keep_policy': 'bool'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'host_id': 'host_id',
        'keep_policy': 'keepPolicy'
    }

    def __init__(self, enterprise_project_id=None, host_id=None, keep_policy=None):
        r"""DeletePremiumHostRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id
        :type enterprise_project_id: str
        :param host_id: 独享模式域名ID
        :type host_id: str
        :param keep_policy: 是否保留规则。false表示不保留该域名的防护策略；true表示保留该域名的防护策略。当要删除的防护域名的防护策略防护多个防护域名时，该参数不传。
        :type keep_policy: bool
        """
        
        

        self._enterprise_project_id = None
        self._host_id = None
        self._keep_policy = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.host_id = host_id
        if keep_policy is not None:
            self.keep_policy = keep_policy

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this DeletePremiumHostRequest.

        您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id

        :return: The enterprise_project_id of this DeletePremiumHostRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this DeletePremiumHostRequest.

        您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id

        :param enterprise_project_id: The enterprise_project_id of this DeletePremiumHostRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def host_id(self):
        r"""Gets the host_id of this DeletePremiumHostRequest.

        独享模式域名ID

        :return: The host_id of this DeletePremiumHostRequest.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this DeletePremiumHostRequest.

        独享模式域名ID

        :param host_id: The host_id of this DeletePremiumHostRequest.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def keep_policy(self):
        r"""Gets the keep_policy of this DeletePremiumHostRequest.

        是否保留规则。false表示不保留该域名的防护策略；true表示保留该域名的防护策略。当要删除的防护域名的防护策略防护多个防护域名时，该参数不传。

        :return: The keep_policy of this DeletePremiumHostRequest.
        :rtype: bool
        """
        return self._keep_policy

    @keep_policy.setter
    def keep_policy(self, keep_policy):
        r"""Sets the keep_policy of this DeletePremiumHostRequest.

        是否保留规则。false表示不保留该域名的防护策略；true表示保留该域名的防护策略。当要删除的防护域名的防护策略防护多个防护域名时，该参数不传。

        :param keep_policy: The keep_policy of this DeletePremiumHostRequest.
        :type keep_policy: bool
        """
        self._keep_policy = keep_policy

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
        if not isinstance(other, DeletePremiumHostRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
