# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPolicyStatesByDomainIdRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'compliance_state': 'str',
        'resource_id': 'str',
        'resource_name': 'str',
        'limit': 'int',
        'marker': 'str'
    }

    attribute_map = {
        'compliance_state': 'compliance_state',
        'resource_id': 'resource_id',
        'resource_name': 'resource_name',
        'limit': 'limit',
        'marker': 'marker'
    }

    def __init__(self, compliance_state=None, resource_id=None, resource_name=None, limit=None, marker=None):
        r"""ListPolicyStatesByDomainIdRequest

        The model defined in huaweicloud sdk

        :param compliance_state: 合规状态
        :type compliance_state: str
        :param resource_id: 资源ID
        :type resource_id: str
        :param resource_name: 资源名称
        :type resource_name: str
        :param limit: 最大的返回数量
        :type limit: int
        :param marker: 分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页
        :type marker: str
        """
        
        

        self._compliance_state = None
        self._resource_id = None
        self._resource_name = None
        self._limit = None
        self._marker = None
        self.discriminator = None

        if compliance_state is not None:
            self.compliance_state = compliance_state
        if resource_id is not None:
            self.resource_id = resource_id
        if resource_name is not None:
            self.resource_name = resource_name
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker

    @property
    def compliance_state(self):
        r"""Gets the compliance_state of this ListPolicyStatesByDomainIdRequest.

        合规状态

        :return: The compliance_state of this ListPolicyStatesByDomainIdRequest.
        :rtype: str
        """
        return self._compliance_state

    @compliance_state.setter
    def compliance_state(self, compliance_state):
        r"""Sets the compliance_state of this ListPolicyStatesByDomainIdRequest.

        合规状态

        :param compliance_state: The compliance_state of this ListPolicyStatesByDomainIdRequest.
        :type compliance_state: str
        """
        self._compliance_state = compliance_state

    @property
    def resource_id(self):
        r"""Gets the resource_id of this ListPolicyStatesByDomainIdRequest.

        资源ID

        :return: The resource_id of this ListPolicyStatesByDomainIdRequest.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this ListPolicyStatesByDomainIdRequest.

        资源ID

        :param resource_id: The resource_id of this ListPolicyStatesByDomainIdRequest.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        r"""Gets the resource_name of this ListPolicyStatesByDomainIdRequest.

        资源名称

        :return: The resource_name of this ListPolicyStatesByDomainIdRequest.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this ListPolicyStatesByDomainIdRequest.

        资源名称

        :param resource_name: The resource_name of this ListPolicyStatesByDomainIdRequest.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def limit(self):
        r"""Gets the limit of this ListPolicyStatesByDomainIdRequest.

        最大的返回数量

        :return: The limit of this ListPolicyStatesByDomainIdRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListPolicyStatesByDomainIdRequest.

        最大的返回数量

        :param limit: The limit of this ListPolicyStatesByDomainIdRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListPolicyStatesByDomainIdRequest.

        分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页

        :return: The marker of this ListPolicyStatesByDomainIdRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListPolicyStatesByDomainIdRequest.

        分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页

        :param marker: The marker of this ListPolicyStatesByDomainIdRequest.
        :type marker: str
        """
        self._marker = marker

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
        if not isinstance(other, ListPolicyStatesByDomainIdRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
