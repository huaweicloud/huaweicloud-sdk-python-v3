# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAvailableFlavorInfosResponse(SdkResponse):

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
        'instance_name': 'str',
        'current_flavor': 'ComputeFlavor',
        'optional_flavors': 'OptionalFlavorsInfo'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'instance_name': 'instance_name',
        'current_flavor': 'current_flavor',
        'optional_flavors': 'optional_flavors'
    }

    def __init__(self, instance_id=None, instance_name=None, current_flavor=None, optional_flavors=None):
        """ListAvailableFlavorInfosResponse

        The model defined in huaweicloud sdk

        :param instance_id: 实例id。
        :type instance_id: str
        :param instance_name: 实例名称。
        :type instance_name: str
        :param current_flavor: 
        :type current_flavor: :class:`huaweicloudsdkgaussdbfornosql.v3.ComputeFlavor`
        :param optional_flavors: 
        :type optional_flavors: :class:`huaweicloudsdkgaussdbfornosql.v3.OptionalFlavorsInfo`
        """
        
        super(ListAvailableFlavorInfosResponse, self).__init__()

        self._instance_id = None
        self._instance_name = None
        self._current_flavor = None
        self._optional_flavors = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name
        if current_flavor is not None:
            self.current_flavor = current_flavor
        if optional_flavors is not None:
            self.optional_flavors = optional_flavors

    @property
    def instance_id(self):
        """Gets the instance_id of this ListAvailableFlavorInfosResponse.

        实例id。

        :return: The instance_id of this ListAvailableFlavorInfosResponse.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListAvailableFlavorInfosResponse.

        实例id。

        :param instance_id: The instance_id of this ListAvailableFlavorInfosResponse.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        """Gets the instance_name of this ListAvailableFlavorInfosResponse.

        实例名称。

        :return: The instance_name of this ListAvailableFlavorInfosResponse.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this ListAvailableFlavorInfosResponse.

        实例名称。

        :param instance_name: The instance_name of this ListAvailableFlavorInfosResponse.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def current_flavor(self):
        """Gets the current_flavor of this ListAvailableFlavorInfosResponse.

        :return: The current_flavor of this ListAvailableFlavorInfosResponse.
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ComputeFlavor`
        """
        return self._current_flavor

    @current_flavor.setter
    def current_flavor(self, current_flavor):
        """Sets the current_flavor of this ListAvailableFlavorInfosResponse.

        :param current_flavor: The current_flavor of this ListAvailableFlavorInfosResponse.
        :type current_flavor: :class:`huaweicloudsdkgaussdbfornosql.v3.ComputeFlavor`
        """
        self._current_flavor = current_flavor

    @property
    def optional_flavors(self):
        """Gets the optional_flavors of this ListAvailableFlavorInfosResponse.

        :return: The optional_flavors of this ListAvailableFlavorInfosResponse.
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.OptionalFlavorsInfo`
        """
        return self._optional_flavors

    @optional_flavors.setter
    def optional_flavors(self, optional_flavors):
        """Sets the optional_flavors of this ListAvailableFlavorInfosResponse.

        :param optional_flavors: The optional_flavors of this ListAvailableFlavorInfosResponse.
        :type optional_flavors: :class:`huaweicloudsdkgaussdbfornosql.v3.OptionalFlavorsInfo`
        """
        self._optional_flavors = optional_flavors

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
        if not isinstance(other, ListAvailableFlavorInfosResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
