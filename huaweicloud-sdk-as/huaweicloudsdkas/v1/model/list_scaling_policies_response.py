# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListScalingPoliciesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_number': 'int',
        'start_number': 'int',
        'limit': 'int',
        'scaling_policies': 'list[ScalingV1PolicyDetail]'
    }

    attribute_map = {
        'total_number': 'total_number',
        'start_number': 'start_number',
        'limit': 'limit',
        'scaling_policies': 'scaling_policies'
    }

    def __init__(self, total_number=None, start_number=None, limit=None, scaling_policies=None):
        r"""ListScalingPoliciesResponse

        The model defined in huaweicloud sdk

        :param total_number: 总记录数。
        :type total_number: int
        :param start_number: 查询的起始行号。
        :type start_number: int
        :param limit: 查询记录数。
        :type limit: int
        :param scaling_policies: 伸缩策略列表
        :type scaling_policies: list[:class:`huaweicloudsdkas.v1.ScalingV1PolicyDetail`]
        """
        
        super(ListScalingPoliciesResponse, self).__init__()

        self._total_number = None
        self._start_number = None
        self._limit = None
        self._scaling_policies = None
        self.discriminator = None

        if total_number is not None:
            self.total_number = total_number
        if start_number is not None:
            self.start_number = start_number
        if limit is not None:
            self.limit = limit
        if scaling_policies is not None:
            self.scaling_policies = scaling_policies

    @property
    def total_number(self):
        r"""Gets the total_number of this ListScalingPoliciesResponse.

        总记录数。

        :return: The total_number of this ListScalingPoliciesResponse.
        :rtype: int
        """
        return self._total_number

    @total_number.setter
    def total_number(self, total_number):
        r"""Sets the total_number of this ListScalingPoliciesResponse.

        总记录数。

        :param total_number: The total_number of this ListScalingPoliciesResponse.
        :type total_number: int
        """
        self._total_number = total_number

    @property
    def start_number(self):
        r"""Gets the start_number of this ListScalingPoliciesResponse.

        查询的起始行号。

        :return: The start_number of this ListScalingPoliciesResponse.
        :rtype: int
        """
        return self._start_number

    @start_number.setter
    def start_number(self, start_number):
        r"""Sets the start_number of this ListScalingPoliciesResponse.

        查询的起始行号。

        :param start_number: The start_number of this ListScalingPoliciesResponse.
        :type start_number: int
        """
        self._start_number = start_number

    @property
    def limit(self):
        r"""Gets the limit of this ListScalingPoliciesResponse.

        查询记录数。

        :return: The limit of this ListScalingPoliciesResponse.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListScalingPoliciesResponse.

        查询记录数。

        :param limit: The limit of this ListScalingPoliciesResponse.
        :type limit: int
        """
        self._limit = limit

    @property
    def scaling_policies(self):
        r"""Gets the scaling_policies of this ListScalingPoliciesResponse.

        伸缩策略列表

        :return: The scaling_policies of this ListScalingPoliciesResponse.
        :rtype: list[:class:`huaweicloudsdkas.v1.ScalingV1PolicyDetail`]
        """
        return self._scaling_policies

    @scaling_policies.setter
    def scaling_policies(self, scaling_policies):
        r"""Sets the scaling_policies of this ListScalingPoliciesResponse.

        伸缩策略列表

        :param scaling_policies: The scaling_policies of this ListScalingPoliciesResponse.
        :type scaling_policies: list[:class:`huaweicloudsdkas.v1.ScalingV1PolicyDetail`]
        """
        self._scaling_policies = scaling_policies

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
        if not isinstance(other, ListScalingPoliciesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
