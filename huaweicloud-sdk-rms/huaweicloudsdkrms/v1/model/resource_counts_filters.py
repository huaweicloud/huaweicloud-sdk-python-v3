# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceCountsFilters:

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
        'resource_type': 'str',
        'region_id': 'str'
    }

    attribute_map = {
        'account_id': 'account_id',
        'resource_type': 'resource_type',
        'region_id': 'region_id'
    }

    def __init__(self, account_id=None, resource_type=None, region_id=None):
        r"""ResourceCountsFilters

        The model defined in huaweicloud sdk

        :param account_id: 帐号ID。
        :type account_id: str
        :param resource_type: 资源类型。
        :type resource_type: str
        :param region_id: 区域ID。
        :type region_id: str
        """
        
        

        self._account_id = None
        self._resource_type = None
        self._region_id = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if resource_type is not None:
            self.resource_type = resource_type
        if region_id is not None:
            self.region_id = region_id

    @property
    def account_id(self):
        r"""Gets the account_id of this ResourceCountsFilters.

        帐号ID。

        :return: The account_id of this ResourceCountsFilters.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        r"""Sets the account_id of this ResourceCountsFilters.

        帐号ID。

        :param account_id: The account_id of this ResourceCountsFilters.
        :type account_id: str
        """
        self._account_id = account_id

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ResourceCountsFilters.

        资源类型。

        :return: The resource_type of this ResourceCountsFilters.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ResourceCountsFilters.

        资源类型。

        :param resource_type: The resource_type of this ResourceCountsFilters.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def region_id(self):
        r"""Gets the region_id of this ResourceCountsFilters.

        区域ID。

        :return: The region_id of this ResourceCountsFilters.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this ResourceCountsFilters.

        区域ID。

        :param region_id: The region_id of this ResourceCountsFilters.
        :type region_id: str
        """
        self._region_id = region_id

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
        if not isinstance(other, ResourceCountsFilters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
