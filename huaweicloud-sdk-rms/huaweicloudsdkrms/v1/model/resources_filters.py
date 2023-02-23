# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourcesFilters:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'account_id': 'str',
        'region_id': 'str',
        'resource_id': 'str',
        'resource_name': 'str'
    }

    attribute_map = {
        'account_id': 'account_id',
        'region_id': 'region_id',
        'resource_id': 'resource_id',
        'resource_name': 'resource_name'
    }

    def __init__(self, account_id=None, region_id=None, resource_id=None, resource_name=None):
        """ResourcesFilters

        The model defined in huaweicloud sdk

        :param account_id: 帐号ID。
        :type account_id: str
        :param region_id: 区域ID。
        :type region_id: str
        :param resource_id: 资源ID。
        :type resource_id: str
        :param resource_name: 资源名称。
        :type resource_name: str
        """
        
        

        self._account_id = None
        self._region_id = None
        self._resource_id = None
        self._resource_name = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if region_id is not None:
            self.region_id = region_id
        if resource_id is not None:
            self.resource_id = resource_id
        if resource_name is not None:
            self.resource_name = resource_name

    @property
    def account_id(self):
        """Gets the account_id of this ResourcesFilters.

        帐号ID。

        :return: The account_id of this ResourcesFilters.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this ResourcesFilters.

        帐号ID。

        :param account_id: The account_id of this ResourcesFilters.
        :type account_id: str
        """
        self._account_id = account_id

    @property
    def region_id(self):
        """Gets the region_id of this ResourcesFilters.

        区域ID。

        :return: The region_id of this ResourcesFilters.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this ResourcesFilters.

        区域ID。

        :param region_id: The region_id of this ResourcesFilters.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def resource_id(self):
        """Gets the resource_id of this ResourcesFilters.

        资源ID。

        :return: The resource_id of this ResourcesFilters.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this ResourcesFilters.

        资源ID。

        :param resource_id: The resource_id of this ResourcesFilters.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        """Gets the resource_name of this ResourcesFilters.

        资源名称。

        :return: The resource_name of this ResourcesFilters.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this ResourcesFilters.

        资源名称。

        :param resource_name: The resource_name of this ResourcesFilters.
        :type resource_name: str
        """
        self._resource_name = resource_name

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
        if not isinstance(other, ResourcesFilters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
