# coding: utf-8

import pprint
import re

import six





class ListIssuedCouponQuotasRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'quota_id': 'str',
        'indirect_partner_id': 'str',
        'parent_quota_id': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'quota_id': 'quota_id',
        'indirect_partner_id': 'indirect_partner_id',
        'parent_quota_id': 'parent_quota_id',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, quota_id=None, indirect_partner_id=None, parent_quota_id=None, offset=None, limit=None):
        """ListIssuedCouponQuotasRequest - a model defined in huaweicloud sdk"""
        
        

        self._quota_id = None
        self._indirect_partner_id = None
        self._parent_quota_id = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if quota_id is not None:
            self.quota_id = quota_id
        if indirect_partner_id is not None:
            self.indirect_partner_id = indirect_partner_id
        if parent_quota_id is not None:
            self.parent_quota_id = parent_quota_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def quota_id(self):
        """Gets the quota_id of this ListIssuedCouponQuotasRequest.


        :return: The quota_id of this ListIssuedCouponQuotasRequest.
        :rtype: str
        """
        return self._quota_id

    @quota_id.setter
    def quota_id(self, quota_id):
        """Sets the quota_id of this ListIssuedCouponQuotasRequest.


        :param quota_id: The quota_id of this ListIssuedCouponQuotasRequest.
        :type: str
        """
        self._quota_id = quota_id

    @property
    def indirect_partner_id(self):
        """Gets the indirect_partner_id of this ListIssuedCouponQuotasRequest.


        :return: The indirect_partner_id of this ListIssuedCouponQuotasRequest.
        :rtype: str
        """
        return self._indirect_partner_id

    @indirect_partner_id.setter
    def indirect_partner_id(self, indirect_partner_id):
        """Sets the indirect_partner_id of this ListIssuedCouponQuotasRequest.


        :param indirect_partner_id: The indirect_partner_id of this ListIssuedCouponQuotasRequest.
        :type: str
        """
        self._indirect_partner_id = indirect_partner_id

    @property
    def parent_quota_id(self):
        """Gets the parent_quota_id of this ListIssuedCouponQuotasRequest.


        :return: The parent_quota_id of this ListIssuedCouponQuotasRequest.
        :rtype: str
        """
        return self._parent_quota_id

    @parent_quota_id.setter
    def parent_quota_id(self, parent_quota_id):
        """Sets the parent_quota_id of this ListIssuedCouponQuotasRequest.


        :param parent_quota_id: The parent_quota_id of this ListIssuedCouponQuotasRequest.
        :type: str
        """
        self._parent_quota_id = parent_quota_id

    @property
    def offset(self):
        """Gets the offset of this ListIssuedCouponQuotasRequest.


        :return: The offset of this ListIssuedCouponQuotasRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListIssuedCouponQuotasRequest.


        :param offset: The offset of this ListIssuedCouponQuotasRequest.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListIssuedCouponQuotasRequest.


        :return: The limit of this ListIssuedCouponQuotasRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListIssuedCouponQuotasRequest.


        :param limit: The limit of this ListIssuedCouponQuotasRequest.
        :type: int
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListIssuedCouponQuotasRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
