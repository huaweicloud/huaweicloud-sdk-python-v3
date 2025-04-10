# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSubscriptionResources:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_id': 'str',
        'resource_spec_code': 'str',
        'resource_type': 'str',
        'resource_size': 'int',
        'expire_time': 'str',
        'status': 'int'
    }

    attribute_map = {
        'resource_id': 'resourceId',
        'resource_spec_code': 'resourceSpecCode',
        'resource_type': 'resourceType',
        'resource_size': 'resourceSize',
        'expire_time': 'expireTime',
        'status': 'status'
    }

    def __init__(self, resource_id=None, resource_spec_code=None, resource_type=None, resource_size=None, expire_time=None, status=None):
        r"""ShowSubscriptionResources

        The model defined in huaweicloud sdk

        :param resource_id: resourceId
        :type resource_id: str
        :param resource_spec_code: resourceSpecCode
        :type resource_spec_code: str
        :param resource_type: resourceType
        :type resource_type: str
        :param resource_size: resourceSize
        :type resource_size: int
        :param expire_time: expireTime
        :type expire_time: str
        :param status: status
        :type status: int
        """
        
        

        self._resource_id = None
        self._resource_spec_code = None
        self._resource_type = None
        self._resource_size = None
        self._expire_time = None
        self._status = None
        self.discriminator = None

        if resource_id is not None:
            self.resource_id = resource_id
        if resource_spec_code is not None:
            self.resource_spec_code = resource_spec_code
        if resource_type is not None:
            self.resource_type = resource_type
        if resource_size is not None:
            self.resource_size = resource_size
        if expire_time is not None:
            self.expire_time = expire_time
        if status is not None:
            self.status = status

    @property
    def resource_id(self):
        r"""Gets the resource_id of this ShowSubscriptionResources.

        resourceId

        :return: The resource_id of this ShowSubscriptionResources.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this ShowSubscriptionResources.

        resourceId

        :param resource_id: The resource_id of this ShowSubscriptionResources.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_spec_code(self):
        r"""Gets the resource_spec_code of this ShowSubscriptionResources.

        resourceSpecCode

        :return: The resource_spec_code of this ShowSubscriptionResources.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        r"""Sets the resource_spec_code of this ShowSubscriptionResources.

        resourceSpecCode

        :param resource_spec_code: The resource_spec_code of this ShowSubscriptionResources.
        :type resource_spec_code: str
        """
        self._resource_spec_code = resource_spec_code

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ShowSubscriptionResources.

        resourceType

        :return: The resource_type of this ShowSubscriptionResources.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ShowSubscriptionResources.

        resourceType

        :param resource_type: The resource_type of this ShowSubscriptionResources.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_size(self):
        r"""Gets the resource_size of this ShowSubscriptionResources.

        resourceSize

        :return: The resource_size of this ShowSubscriptionResources.
        :rtype: int
        """
        return self._resource_size

    @resource_size.setter
    def resource_size(self, resource_size):
        r"""Sets the resource_size of this ShowSubscriptionResources.

        resourceSize

        :param resource_size: The resource_size of this ShowSubscriptionResources.
        :type resource_size: int
        """
        self._resource_size = resource_size

    @property
    def expire_time(self):
        r"""Gets the expire_time of this ShowSubscriptionResources.

        expireTime

        :return: The expire_time of this ShowSubscriptionResources.
        :rtype: str
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        r"""Sets the expire_time of this ShowSubscriptionResources.

        expireTime

        :param expire_time: The expire_time of this ShowSubscriptionResources.
        :type expire_time: str
        """
        self._expire_time = expire_time

    @property
    def status(self):
        r"""Gets the status of this ShowSubscriptionResources.

        status

        :return: The status of this ShowSubscriptionResources.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowSubscriptionResources.

        status

        :param status: The status of this ShowSubscriptionResources.
        :type status: int
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
        if not isinstance(other, ShowSubscriptionResources):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
