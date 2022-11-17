# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MigrateCompositeHostsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_ids': 'list[str]',
        'policy_id': 'str',
        'certificate_id': 'str'
    }

    attribute_map = {
        'host_ids': 'host_ids',
        'policy_id': 'policy_id',
        'certificate_id': 'certificate_id'
    }

    def __init__(self, host_ids=None, policy_id=None, certificate_id=None):
        """MigrateCompositeHostsResponse

        The model defined in huaweicloud sdk

        :param host_ids: host_id列表
        :type host_ids: list[str]
        :param policy_id: 策略ID（目标企业项目下的策略ID）
        :type policy_id: str
        :param certificate_id: 证书ID（目标企业项目下的证书ID）
        :type certificate_id: str
        """
        
        super(MigrateCompositeHostsResponse, self).__init__()

        self._host_ids = None
        self._policy_id = None
        self._certificate_id = None
        self.discriminator = None

        if host_ids is not None:
            self.host_ids = host_ids
        if policy_id is not None:
            self.policy_id = policy_id
        if certificate_id is not None:
            self.certificate_id = certificate_id

    @property
    def host_ids(self):
        """Gets the host_ids of this MigrateCompositeHostsResponse.

        host_id列表

        :return: The host_ids of this MigrateCompositeHostsResponse.
        :rtype: list[str]
        """
        return self._host_ids

    @host_ids.setter
    def host_ids(self, host_ids):
        """Sets the host_ids of this MigrateCompositeHostsResponse.

        host_id列表

        :param host_ids: The host_ids of this MigrateCompositeHostsResponse.
        :type host_ids: list[str]
        """
        self._host_ids = host_ids

    @property
    def policy_id(self):
        """Gets the policy_id of this MigrateCompositeHostsResponse.

        策略ID（目标企业项目下的策略ID）

        :return: The policy_id of this MigrateCompositeHostsResponse.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        """Sets the policy_id of this MigrateCompositeHostsResponse.

        策略ID（目标企业项目下的策略ID）

        :param policy_id: The policy_id of this MigrateCompositeHostsResponse.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def certificate_id(self):
        """Gets the certificate_id of this MigrateCompositeHostsResponse.

        证书ID（目标企业项目下的证书ID）

        :return: The certificate_id of this MigrateCompositeHostsResponse.
        :rtype: str
        """
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, certificate_id):
        """Sets the certificate_id of this MigrateCompositeHostsResponse.

        证书ID（目标企业项目下的证书ID）

        :param certificate_id: The certificate_id of this MigrateCompositeHostsResponse.
        :type certificate_id: str
        """
        self._certificate_id = certificate_id

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
        if not isinstance(other, MigrateCompositeHostsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
