# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListNetworkSwitchPoliciesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_name': 'str',
        'version': 'int',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'policy_name': 'policy_name',
        'version': 'version',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, policy_name=None, version=None, limit=None, offset=None):
        r"""ListNetworkSwitchPoliciesRequest

        The model defined in huaweicloud sdk

        :param policy_name: 策略名称
        :type policy_name: str
        :param version: 三网卡版本信息
        :type version: int
        :param limit: 分页查询时每页显示的记录数，默认值为10，取值范围为10-500的整数
        :type limit: int
        :param offset: 分页查询时的页码数，默认值为1，取值范围为1-1000000的整数
        :type offset: int
        """
        
        

        self._policy_name = None
        self._version = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if policy_name is not None:
            self.policy_name = policy_name
        if version is not None:
            self.version = version
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def policy_name(self):
        r"""Gets the policy_name of this ListNetworkSwitchPoliciesRequest.

        策略名称

        :return: The policy_name of this ListNetworkSwitchPoliciesRequest.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        r"""Sets the policy_name of this ListNetworkSwitchPoliciesRequest.

        策略名称

        :param policy_name: The policy_name of this ListNetworkSwitchPoliciesRequest.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def version(self):
        r"""Gets the version of this ListNetworkSwitchPoliciesRequest.

        三网卡版本信息

        :return: The version of this ListNetworkSwitchPoliciesRequest.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ListNetworkSwitchPoliciesRequest.

        三网卡版本信息

        :param version: The version of this ListNetworkSwitchPoliciesRequest.
        :type version: int
        """
        self._version = version

    @property
    def limit(self):
        r"""Gets the limit of this ListNetworkSwitchPoliciesRequest.

        分页查询时每页显示的记录数，默认值为10，取值范围为10-500的整数

        :return: The limit of this ListNetworkSwitchPoliciesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListNetworkSwitchPoliciesRequest.

        分页查询时每页显示的记录数，默认值为10，取值范围为10-500的整数

        :param limit: The limit of this ListNetworkSwitchPoliciesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListNetworkSwitchPoliciesRequest.

        分页查询时的页码数，默认值为1，取值范围为1-1000000的整数

        :return: The offset of this ListNetworkSwitchPoliciesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListNetworkSwitchPoliciesRequest.

        分页查询时的页码数，默认值为1，取值范围为1-1000000的整数

        :param offset: The offset of this ListNetworkSwitchPoliciesRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListNetworkSwitchPoliciesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
