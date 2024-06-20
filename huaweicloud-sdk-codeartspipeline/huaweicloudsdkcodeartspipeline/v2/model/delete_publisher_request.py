# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeletePublisherRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_id': 'str',
        'publisher_unique_id': 'str'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'publisher_unique_id': 'publisher_unique_id'
    }

    def __init__(self, domain_id=None, publisher_unique_id=None):
        """DeletePublisherRequest

        The model defined in huaweicloud sdk

        :param domain_id: 租户ID
        :type domain_id: str
        :param publisher_unique_id: 发布商ID
        :type publisher_unique_id: str
        """
        
        

        self._domain_id = None
        self._publisher_unique_id = None
        self.discriminator = None

        self.domain_id = domain_id
        self.publisher_unique_id = publisher_unique_id

    @property
    def domain_id(self):
        """Gets the domain_id of this DeletePublisherRequest.

        租户ID

        :return: The domain_id of this DeletePublisherRequest.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this DeletePublisherRequest.

        租户ID

        :param domain_id: The domain_id of this DeletePublisherRequest.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def publisher_unique_id(self):
        """Gets the publisher_unique_id of this DeletePublisherRequest.

        发布商ID

        :return: The publisher_unique_id of this DeletePublisherRequest.
        :rtype: str
        """
        return self._publisher_unique_id

    @publisher_unique_id.setter
    def publisher_unique_id(self, publisher_unique_id):
        """Sets the publisher_unique_id of this DeletePublisherRequest.

        发布商ID

        :param publisher_unique_id: The publisher_unique_id of this DeletePublisherRequest.
        :type publisher_unique_id: str
        """
        self._publisher_unique_id = publisher_unique_id

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
        if not isinstance(other, DeletePublisherRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
