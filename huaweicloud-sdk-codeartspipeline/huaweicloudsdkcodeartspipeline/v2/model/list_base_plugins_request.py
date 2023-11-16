# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBasePluginsRequest:

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
        'attribution': 'str',
        'offset': 'str',
        'limit': 'str'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'attribution': 'attribution',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, domain_id=None, attribution=None, offset=None, limit=None):
        """ListBasePluginsRequest

        The model defined in huaweicloud sdk

        :param domain_id: 租户ID
        :type domain_id: str
        :param attribution: 属性
        :type attribution: str
        :param offset: 偏移
        :type offset: str
        :param limit: 大小
        :type limit: str
        """
        
        

        self._domain_id = None
        self._attribution = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.domain_id = domain_id
        if attribution is not None:
            self.attribution = attribution
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def domain_id(self):
        """Gets the domain_id of this ListBasePluginsRequest.

        租户ID

        :return: The domain_id of this ListBasePluginsRequest.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this ListBasePluginsRequest.

        租户ID

        :param domain_id: The domain_id of this ListBasePluginsRequest.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def attribution(self):
        """Gets the attribution of this ListBasePluginsRequest.

        属性

        :return: The attribution of this ListBasePluginsRequest.
        :rtype: str
        """
        return self._attribution

    @attribution.setter
    def attribution(self, attribution):
        """Sets the attribution of this ListBasePluginsRequest.

        属性

        :param attribution: The attribution of this ListBasePluginsRequest.
        :type attribution: str
        """
        self._attribution = attribution

    @property
    def offset(self):
        """Gets the offset of this ListBasePluginsRequest.

        偏移

        :return: The offset of this ListBasePluginsRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListBasePluginsRequest.

        偏移

        :param offset: The offset of this ListBasePluginsRequest.
        :type offset: str
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListBasePluginsRequest.

        大小

        :return: The limit of this ListBasePluginsRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListBasePluginsRequest.

        大小

        :param limit: The limit of this ListBasePluginsRequest.
        :type limit: str
        """
        self._limit = limit

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
        if not isinstance(other, ListBasePluginsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
