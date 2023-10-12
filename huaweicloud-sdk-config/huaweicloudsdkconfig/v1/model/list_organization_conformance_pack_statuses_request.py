# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOrganizationConformancePackStatusesRequest:

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
        'limit': 'int',
        'marker': 'str',
        'conformance_pack_name': 'str'
    }

    attribute_map = {
        'organization_id': 'organization_id',
        'limit': 'limit',
        'marker': 'marker',
        'conformance_pack_name': 'conformance_pack_name'
    }

    def __init__(self, organization_id=None, limit=None, marker=None, conformance_pack_name=None):
        """ListOrganizationConformancePackStatusesRequest

        The model defined in huaweicloud sdk

        :param organization_id: 组织ID。
        :type organization_id: str
        :param limit: 最大的返回数量
        :type limit: int
        :param marker: 分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页
        :type marker: str
        :param conformance_pack_name: 合规规则包名称。
        :type conformance_pack_name: str
        """
        
        

        self._organization_id = None
        self._limit = None
        self._marker = None
        self._conformance_pack_name = None
        self.discriminator = None

        self.organization_id = organization_id
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if conformance_pack_name is not None:
            self.conformance_pack_name = conformance_pack_name

    @property
    def organization_id(self):
        """Gets the organization_id of this ListOrganizationConformancePackStatusesRequest.

        组织ID。

        :return: The organization_id of this ListOrganizationConformancePackStatusesRequest.
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this ListOrganizationConformancePackStatusesRequest.

        组织ID。

        :param organization_id: The organization_id of this ListOrganizationConformancePackStatusesRequest.
        :type organization_id: str
        """
        self._organization_id = organization_id

    @property
    def limit(self):
        """Gets the limit of this ListOrganizationConformancePackStatusesRequest.

        最大的返回数量

        :return: The limit of this ListOrganizationConformancePackStatusesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListOrganizationConformancePackStatusesRequest.

        最大的返回数量

        :param limit: The limit of this ListOrganizationConformancePackStatusesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListOrganizationConformancePackStatusesRequest.

        分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页

        :return: The marker of this ListOrganizationConformancePackStatusesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListOrganizationConformancePackStatusesRequest.

        分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页

        :param marker: The marker of this ListOrganizationConformancePackStatusesRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def conformance_pack_name(self):
        """Gets the conformance_pack_name of this ListOrganizationConformancePackStatusesRequest.

        合规规则包名称。

        :return: The conformance_pack_name of this ListOrganizationConformancePackStatusesRequest.
        :rtype: str
        """
        return self._conformance_pack_name

    @conformance_pack_name.setter
    def conformance_pack_name(self, conformance_pack_name):
        """Sets the conformance_pack_name of this ListOrganizationConformancePackStatusesRequest.

        合规规则包名称。

        :param conformance_pack_name: The conformance_pack_name of this ListOrganizationConformancePackStatusesRequest.
        :type conformance_pack_name: str
        """
        self._conformance_pack_name = conformance_pack_name

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
        if not isinstance(other, ListOrganizationConformancePackStatusesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
