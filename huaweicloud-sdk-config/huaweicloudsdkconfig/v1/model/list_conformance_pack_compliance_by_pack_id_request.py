# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListConformancePackComplianceByPackIdRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'conformance_pack_id': 'str',
        'limit': 'int',
        'marker': 'str',
        'policy_assignment_name': 'str'
    }

    attribute_map = {
        'conformance_pack_id': 'conformance_pack_id',
        'limit': 'limit',
        'marker': 'marker',
        'policy_assignment_name': 'policy_assignment_name'
    }

    def __init__(self, conformance_pack_id=None, limit=None, marker=None, policy_assignment_name=None):
        r"""ListConformancePackComplianceByPackIdRequest

        The model defined in huaweicloud sdk

        :param conformance_pack_id: 合规规则包ID。
        :type conformance_pack_id: str
        :param limit: 最大的返回数量
        :type limit: int
        :param marker: 分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页
        :type marker: str
        :param policy_assignment_name: 合规规则名称。
        :type policy_assignment_name: str
        """
        
        

        self._conformance_pack_id = None
        self._limit = None
        self._marker = None
        self._policy_assignment_name = None
        self.discriminator = None

        self.conformance_pack_id = conformance_pack_id
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if policy_assignment_name is not None:
            self.policy_assignment_name = policy_assignment_name

    @property
    def conformance_pack_id(self):
        r"""Gets the conformance_pack_id of this ListConformancePackComplianceByPackIdRequest.

        合规规则包ID。

        :return: The conformance_pack_id of this ListConformancePackComplianceByPackIdRequest.
        :rtype: str
        """
        return self._conformance_pack_id

    @conformance_pack_id.setter
    def conformance_pack_id(self, conformance_pack_id):
        r"""Sets the conformance_pack_id of this ListConformancePackComplianceByPackIdRequest.

        合规规则包ID。

        :param conformance_pack_id: The conformance_pack_id of this ListConformancePackComplianceByPackIdRequest.
        :type conformance_pack_id: str
        """
        self._conformance_pack_id = conformance_pack_id

    @property
    def limit(self):
        r"""Gets the limit of this ListConformancePackComplianceByPackIdRequest.

        最大的返回数量

        :return: The limit of this ListConformancePackComplianceByPackIdRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListConformancePackComplianceByPackIdRequest.

        最大的返回数量

        :param limit: The limit of this ListConformancePackComplianceByPackIdRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListConformancePackComplianceByPackIdRequest.

        分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页

        :return: The marker of this ListConformancePackComplianceByPackIdRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListConformancePackComplianceByPackIdRequest.

        分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页

        :param marker: The marker of this ListConformancePackComplianceByPackIdRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def policy_assignment_name(self):
        r"""Gets the policy_assignment_name of this ListConformancePackComplianceByPackIdRequest.

        合规规则名称。

        :return: The policy_assignment_name of this ListConformancePackComplianceByPackIdRequest.
        :rtype: str
        """
        return self._policy_assignment_name

    @policy_assignment_name.setter
    def policy_assignment_name(self, policy_assignment_name):
        r"""Sets the policy_assignment_name of this ListConformancePackComplianceByPackIdRequest.

        合规规则名称。

        :param policy_assignment_name: The policy_assignment_name of this ListConformancePackComplianceByPackIdRequest.
        :type policy_assignment_name: str
        """
        self._policy_assignment_name = policy_assignment_name

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
        if not isinstance(other, ListConformancePackComplianceByPackIdRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
