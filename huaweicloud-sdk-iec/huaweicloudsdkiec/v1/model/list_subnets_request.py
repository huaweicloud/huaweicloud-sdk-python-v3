# coding: utf-8

import pprint
import re

import six





class ListSubnetsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'vpc_id': 'str',
        'limit': 'int',
        'offset': 'int',
        'site_id': 'str'
    }

    attribute_map = {
        'vpc_id': 'vpc_id',
        'limit': 'limit',
        'offset': 'offset',
        'site_id': 'site_id'
    }

    def __init__(self, vpc_id=None, limit=None, offset=None, site_id=None):
        """ListSubnetsRequest - a model defined in huaweicloud sdk"""
        
        

        self._vpc_id = None
        self._limit = None
        self._offset = None
        self._site_id = None
        self.discriminator = None

        if vpc_id is not None:
            self.vpc_id = vpc_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if site_id is not None:
            self.site_id = site_id

    @property
    def vpc_id(self):
        """Gets the vpc_id of this ListSubnetsRequest.

        虚拟私有云ID。

        :return: The vpc_id of this ListSubnetsRequest.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this ListSubnetsRequest.

        虚拟私有云ID。

        :param vpc_id: The vpc_id of this ListSubnetsRequest.
        :type: str
        """
        self._vpc_id = vpc_id

    @property
    def limit(self):
        """Gets the limit of this ListSubnetsRequest.

        查询返回边缘子网列表数量。取值范围：0~1000。

        :return: The limit of this ListSubnetsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListSubnetsRequest.

        查询返回边缘子网列表数量。取值范围：0~1000。

        :param limit: The limit of this ListSubnetsRequest.
        :type: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListSubnetsRequest.

        查询的偏移量。

        :return: The offset of this ListSubnetsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListSubnetsRequest.

        查询的偏移量。

        :param offset: The offset of this ListSubnetsRequest.
        :type: int
        """
        self._offset = offset

    @property
    def site_id(self):
        """Gets the site_id of this ListSubnetsRequest.

        站点ID。

        :return: The site_id of this ListSubnetsRequest.
        :rtype: str
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """Sets the site_id of this ListSubnetsRequest.

        站点ID。

        :param site_id: The site_id of this ListSubnetsRequest.
        :type: str
        """
        self._site_id = site_id

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListSubnetsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
