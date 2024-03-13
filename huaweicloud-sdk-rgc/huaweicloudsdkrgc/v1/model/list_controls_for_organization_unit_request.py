# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListControlsForOrganizationUnitRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'managed_organization_unit_id': 'str',
        'limit': 'int',
        'marker': 'str'
    }

    attribute_map = {
        'managed_organization_unit_id': 'managed_organization_unit_id',
        'limit': 'limit',
        'marker': 'marker'
    }

    def __init__(self, managed_organization_unit_id=None, limit=None, marker=None):
        """ListControlsForOrganizationUnitRequest

        The model defined in huaweicloud sdk

        :param managed_organization_unit_id: 注册OU ID。
        :type managed_organization_unit_id: str
        :param limit: 分页页面的最大值。
        :type limit: int
        :param marker: 页面标记。
        :type marker: str
        """
        
        

        self._managed_organization_unit_id = None
        self._limit = None
        self._marker = None
        self.discriminator = None

        self.managed_organization_unit_id = managed_organization_unit_id
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker

    @property
    def managed_organization_unit_id(self):
        """Gets the managed_organization_unit_id of this ListControlsForOrganizationUnitRequest.

        注册OU ID。

        :return: The managed_organization_unit_id of this ListControlsForOrganizationUnitRequest.
        :rtype: str
        """
        return self._managed_organization_unit_id

    @managed_organization_unit_id.setter
    def managed_organization_unit_id(self, managed_organization_unit_id):
        """Sets the managed_organization_unit_id of this ListControlsForOrganizationUnitRequest.

        注册OU ID。

        :param managed_organization_unit_id: The managed_organization_unit_id of this ListControlsForOrganizationUnitRequest.
        :type managed_organization_unit_id: str
        """
        self._managed_organization_unit_id = managed_organization_unit_id

    @property
    def limit(self):
        """Gets the limit of this ListControlsForOrganizationUnitRequest.

        分页页面的最大值。

        :return: The limit of this ListControlsForOrganizationUnitRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListControlsForOrganizationUnitRequest.

        分页页面的最大值。

        :param limit: The limit of this ListControlsForOrganizationUnitRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListControlsForOrganizationUnitRequest.

        页面标记。

        :return: The marker of this ListControlsForOrganizationUnitRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListControlsForOrganizationUnitRequest.

        页面标记。

        :param marker: The marker of this ListControlsForOrganizationUnitRequest.
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
        if not isinstance(other, ListControlsForOrganizationUnitRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
