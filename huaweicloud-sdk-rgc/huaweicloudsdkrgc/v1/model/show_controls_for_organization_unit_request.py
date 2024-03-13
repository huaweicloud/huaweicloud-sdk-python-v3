# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowControlsForOrganizationUnitRequest:

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
        'control_id': 'str'
    }

    attribute_map = {
        'managed_organization_unit_id': 'managed_organization_unit_id',
        'control_id': 'control_id'
    }

    def __init__(self, managed_organization_unit_id=None, control_id=None):
        """ShowControlsForOrganizationUnitRequest

        The model defined in huaweicloud sdk

        :param managed_organization_unit_id: 注册OU ID。
        :type managed_organization_unit_id: str
        :param control_id: 控制策略ID。
        :type control_id: str
        """
        
        

        self._managed_organization_unit_id = None
        self._control_id = None
        self.discriminator = None

        self.managed_organization_unit_id = managed_organization_unit_id
        self.control_id = control_id

    @property
    def managed_organization_unit_id(self):
        """Gets the managed_organization_unit_id of this ShowControlsForOrganizationUnitRequest.

        注册OU ID。

        :return: The managed_organization_unit_id of this ShowControlsForOrganizationUnitRequest.
        :rtype: str
        """
        return self._managed_organization_unit_id

    @managed_organization_unit_id.setter
    def managed_organization_unit_id(self, managed_organization_unit_id):
        """Sets the managed_organization_unit_id of this ShowControlsForOrganizationUnitRequest.

        注册OU ID。

        :param managed_organization_unit_id: The managed_organization_unit_id of this ShowControlsForOrganizationUnitRequest.
        :type managed_organization_unit_id: str
        """
        self._managed_organization_unit_id = managed_organization_unit_id

    @property
    def control_id(self):
        """Gets the control_id of this ShowControlsForOrganizationUnitRequest.

        控制策略ID。

        :return: The control_id of this ShowControlsForOrganizationUnitRequest.
        :rtype: str
        """
        return self._control_id

    @control_id.setter
    def control_id(self, control_id):
        """Sets the control_id of this ShowControlsForOrganizationUnitRequest.

        控制策略ID。

        :param control_id: The control_id of this ShowControlsForOrganizationUnitRequest.
        :type control_id: str
        """
        self._control_id = control_id

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
        if not isinstance(other, ShowControlsForOrganizationUnitRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
