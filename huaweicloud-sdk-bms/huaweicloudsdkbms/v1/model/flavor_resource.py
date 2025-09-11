# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FlavorResource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'flavor_id': 'str',
        'count': 'int',
        'status': 'str'
    }

    attribute_map = {
        'flavor_id': 'flavor_id',
        'count': 'count',
        'status': 'status'
    }

    def __init__(self, flavor_id=None, count=None, status=None):
        r"""FlavorResource

        The model defined in huaweicloud sdk

        :param flavor_id: 
        :type flavor_id: str
        :param count: 
        :type count: int
        :param status: 
        :type status: str
        """
        
        

        self._flavor_id = None
        self._count = None
        self._status = None
        self.discriminator = None

        if flavor_id is not None:
            self.flavor_id = flavor_id
        if count is not None:
            self.count = count
        if status is not None:
            self.status = status

    @property
    def flavor_id(self):
        r"""Gets the flavor_id of this FlavorResource.

        :return: The flavor_id of this FlavorResource.
        :rtype: str
        """
        return self._flavor_id

    @flavor_id.setter
    def flavor_id(self, flavor_id):
        r"""Sets the flavor_id of this FlavorResource.

        :param flavor_id: The flavor_id of this FlavorResource.
        :type flavor_id: str
        """
        self._flavor_id = flavor_id

    @property
    def count(self):
        r"""Gets the count of this FlavorResource.

        :return: The count of this FlavorResource.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this FlavorResource.

        :param count: The count of this FlavorResource.
        :type count: int
        """
        self._count = count

    @property
    def status(self):
        r"""Gets the status of this FlavorResource.

        :return: The status of this FlavorResource.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this FlavorResource.

        :param status: The status of this FlavorResource.
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
        if not isinstance(other, FlavorResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
