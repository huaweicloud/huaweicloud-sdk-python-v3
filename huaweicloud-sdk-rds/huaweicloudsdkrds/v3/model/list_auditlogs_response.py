# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListAuditlogsResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'auditlogs': 'list[Auditlog]',
        'total_record': 'int'
    }

    attribute_map = {
        'auditlogs': 'auditlogs',
        'total_record': 'total_record'
    }

    def __init__(self, auditlogs=None, total_record=None):
        """ListAuditlogsResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._auditlogs = None
        self._total_record = None
        self.discriminator = None

        if auditlogs is not None:
            self.auditlogs = auditlogs
        if total_record is not None:
            self.total_record = total_record

    @property
    def auditlogs(self):
        """Gets the auditlogs of this ListAuditlogsResponse.


        :return: The auditlogs of this ListAuditlogsResponse.
        :rtype: list[Auditlog]
        """
        return self._auditlogs

    @auditlogs.setter
    def auditlogs(self, auditlogs):
        """Sets the auditlogs of this ListAuditlogsResponse.


        :param auditlogs: The auditlogs of this ListAuditlogsResponse.
        :type: list[Auditlog]
        """
        self._auditlogs = auditlogs

    @property
    def total_record(self):
        """Gets the total_record of this ListAuditlogsResponse.

        总记录数。

        :return: The total_record of this ListAuditlogsResponse.
        :rtype: int
        """
        return self._total_record

    @total_record.setter
    def total_record(self, total_record):
        """Sets the total_record of this ListAuditlogsResponse.

        总记录数。

        :param total_record: The total_record of this ListAuditlogsResponse.
        :type: int
        """
        self._total_record = total_record

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
        if not isinstance(other, ListAuditlogsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
