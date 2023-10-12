# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOrganizationConformancePackDetailedStatusesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'organization_id': 'str',
        'conformance_pack_name': 'str',
        'state': 'str',
        'limit': 'int',
        'marker': 'str'
    }

    attribute_map = {
        'organization_id': 'organization_id',
        'conformance_pack_name': 'conformance_pack_name',
        'state': 'state',
        'limit': 'limit',
        'marker': 'marker'
    }

    def __init__(self, organization_id=None, conformance_pack_name=None, state=None, limit=None, marker=None):
        """ShowOrganizationConformancePackDetailedStatusesRequest

        The model defined in huaweicloud sdk

        :param organization_id: 组织ID。
        :type organization_id: str
        :param conformance_pack_name: 合规规则包名称。
        :type conformance_pack_name: str
        :param state: 部署状态，区分大小写
        :type state: str
        :param limit: 最大的返回数量
        :type limit: int
        :param marker: 分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页
        :type marker: str
        """
        
        

        self._organization_id = None
        self._conformance_pack_name = None
        self._state = None
        self._limit = None
        self._marker = None
        self.discriminator = None

        self.organization_id = organization_id
        self.conformance_pack_name = conformance_pack_name
        if state is not None:
            self.state = state
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker

    @property
    def organization_id(self):
        """Gets the organization_id of this ShowOrganizationConformancePackDetailedStatusesRequest.

        组织ID。

        :return: The organization_id of this ShowOrganizationConformancePackDetailedStatusesRequest.
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this ShowOrganizationConformancePackDetailedStatusesRequest.

        组织ID。

        :param organization_id: The organization_id of this ShowOrganizationConformancePackDetailedStatusesRequest.
        :type organization_id: str
        """
        self._organization_id = organization_id

    @property
    def conformance_pack_name(self):
        """Gets the conformance_pack_name of this ShowOrganizationConformancePackDetailedStatusesRequest.

        合规规则包名称。

        :return: The conformance_pack_name of this ShowOrganizationConformancePackDetailedStatusesRequest.
        :rtype: str
        """
        return self._conformance_pack_name

    @conformance_pack_name.setter
    def conformance_pack_name(self, conformance_pack_name):
        """Sets the conformance_pack_name of this ShowOrganizationConformancePackDetailedStatusesRequest.

        合规规则包名称。

        :param conformance_pack_name: The conformance_pack_name of this ShowOrganizationConformancePackDetailedStatusesRequest.
        :type conformance_pack_name: str
        """
        self._conformance_pack_name = conformance_pack_name

    @property
    def state(self):
        """Gets the state of this ShowOrganizationConformancePackDetailedStatusesRequest.

        部署状态，区分大小写

        :return: The state of this ShowOrganizationConformancePackDetailedStatusesRequest.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ShowOrganizationConformancePackDetailedStatusesRequest.

        部署状态，区分大小写

        :param state: The state of this ShowOrganizationConformancePackDetailedStatusesRequest.
        :type state: str
        """
        self._state = state

    @property
    def limit(self):
        """Gets the limit of this ShowOrganizationConformancePackDetailedStatusesRequest.

        最大的返回数量

        :return: The limit of this ShowOrganizationConformancePackDetailedStatusesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowOrganizationConformancePackDetailedStatusesRequest.

        最大的返回数量

        :param limit: The limit of this ShowOrganizationConformancePackDetailedStatusesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ShowOrganizationConformancePackDetailedStatusesRequest.

        分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页

        :return: The marker of this ShowOrganizationConformancePackDetailedStatusesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ShowOrganizationConformancePackDetailedStatusesRequest.

        分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页

        :param marker: The marker of this ShowOrganizationConformancePackDetailedStatusesRequest.
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
        if not isinstance(other, ShowOrganizationConformancePackDetailedStatusesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
