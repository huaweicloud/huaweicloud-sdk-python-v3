# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOrganizationConformancePacksRequest:

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
        'organization_conformance_pack_id': 'str',
        'conformance_pack_name': 'str'
    }

    attribute_map = {
        'organization_id': 'organization_id',
        'limit': 'limit',
        'marker': 'marker',
        'organization_conformance_pack_id': 'organization_conformance_pack_id',
        'conformance_pack_name': 'conformance_pack_name'
    }

    def __init__(self, organization_id=None, limit=None, marker=None, organization_conformance_pack_id=None, conformance_pack_name=None):
        r"""ListOrganizationConformancePacksRequest

        The model defined in huaweicloud sdk

        :param organization_id: 组织ID。
        :type organization_id: str
        :param limit: 最大的返回数量
        :type limit: int
        :param marker: 分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页
        :type marker: str
        :param organization_conformance_pack_id: 组织合规规则包ID。
        :type organization_conformance_pack_id: str
        :param conformance_pack_name: 合规规则包名称。
        :type conformance_pack_name: str
        """
        
        

        self._organization_id = None
        self._limit = None
        self._marker = None
        self._organization_conformance_pack_id = None
        self._conformance_pack_name = None
        self.discriminator = None

        self.organization_id = organization_id
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if organization_conformance_pack_id is not None:
            self.organization_conformance_pack_id = organization_conformance_pack_id
        if conformance_pack_name is not None:
            self.conformance_pack_name = conformance_pack_name

    @property
    def organization_id(self):
        r"""Gets the organization_id of this ListOrganizationConformancePacksRequest.

        组织ID。

        :return: The organization_id of this ListOrganizationConformancePacksRequest.
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        r"""Sets the organization_id of this ListOrganizationConformancePacksRequest.

        组织ID。

        :param organization_id: The organization_id of this ListOrganizationConformancePacksRequest.
        :type organization_id: str
        """
        self._organization_id = organization_id

    @property
    def limit(self):
        r"""Gets the limit of this ListOrganizationConformancePacksRequest.

        最大的返回数量

        :return: The limit of this ListOrganizationConformancePacksRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListOrganizationConformancePacksRequest.

        最大的返回数量

        :param limit: The limit of this ListOrganizationConformancePacksRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListOrganizationConformancePacksRequest.

        分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页

        :return: The marker of this ListOrganizationConformancePacksRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListOrganizationConformancePacksRequest.

        分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页

        :param marker: The marker of this ListOrganizationConformancePacksRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def organization_conformance_pack_id(self):
        r"""Gets the organization_conformance_pack_id of this ListOrganizationConformancePacksRequest.

        组织合规规则包ID。

        :return: The organization_conformance_pack_id of this ListOrganizationConformancePacksRequest.
        :rtype: str
        """
        return self._organization_conformance_pack_id

    @organization_conformance_pack_id.setter
    def organization_conformance_pack_id(self, organization_conformance_pack_id):
        r"""Sets the organization_conformance_pack_id of this ListOrganizationConformancePacksRequest.

        组织合规规则包ID。

        :param organization_conformance_pack_id: The organization_conformance_pack_id of this ListOrganizationConformancePacksRequest.
        :type organization_conformance_pack_id: str
        """
        self._organization_conformance_pack_id = organization_conformance_pack_id

    @property
    def conformance_pack_name(self):
        r"""Gets the conformance_pack_name of this ListOrganizationConformancePacksRequest.

        合规规则包名称。

        :return: The conformance_pack_name of this ListOrganizationConformancePacksRequest.
        :rtype: str
        """
        return self._conformance_pack_name

    @conformance_pack_name.setter
    def conformance_pack_name(self, conformance_pack_name):
        r"""Sets the conformance_pack_name of this ListOrganizationConformancePacksRequest.

        合规规则包名称。

        :param conformance_pack_name: The conformance_pack_name of this ListOrganizationConformancePacksRequest.
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
        if not isinstance(other, ListOrganizationConformancePacksRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
