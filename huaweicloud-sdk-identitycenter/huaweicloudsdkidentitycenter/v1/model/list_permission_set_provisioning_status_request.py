# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPermissionSetProvisioningStatusRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'limit': 'int',
        'marker': 'str',
        'status': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'limit': 'limit',
        'marker': 'marker',
        'status': 'status'
    }

    def __init__(self, instance_id=None, limit=None, marker=None, status=None):
        """ListPermissionSetProvisioningStatusRequest

        The model defined in huaweicloud sdk

        :param instance_id: 
        :type instance_id: str
        :param limit: 
        :type limit: int
        :param marker: 
        :type marker: str
        :param status: Filters he operation status list based on the passed attribute value.
        :type status: str
        """
        
        

        self._instance_id = None
        self._limit = None
        self._marker = None
        self._status = None
        self.discriminator = None

        self.instance_id = instance_id
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if status is not None:
            self.status = status

    @property
    def instance_id(self):
        """Gets the instance_id of this ListPermissionSetProvisioningStatusRequest.

        :return: The instance_id of this ListPermissionSetProvisioningStatusRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListPermissionSetProvisioningStatusRequest.

        :param instance_id: The instance_id of this ListPermissionSetProvisioningStatusRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def limit(self):
        """Gets the limit of this ListPermissionSetProvisioningStatusRequest.

        :return: The limit of this ListPermissionSetProvisioningStatusRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListPermissionSetProvisioningStatusRequest.

        :param limit: The limit of this ListPermissionSetProvisioningStatusRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListPermissionSetProvisioningStatusRequest.

        :return: The marker of this ListPermissionSetProvisioningStatusRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListPermissionSetProvisioningStatusRequest.

        :param marker: The marker of this ListPermissionSetProvisioningStatusRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def status(self):
        """Gets the status of this ListPermissionSetProvisioningStatusRequest.

        Filters he operation status list based on the passed attribute value.

        :return: The status of this ListPermissionSetProvisioningStatusRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListPermissionSetProvisioningStatusRequest.

        Filters he operation status list based on the passed attribute value.

        :param status: The status of this ListPermissionSetProvisioningStatusRequest.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, ListPermissionSetProvisioningStatusRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
