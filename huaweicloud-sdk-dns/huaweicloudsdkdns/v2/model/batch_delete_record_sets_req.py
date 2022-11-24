# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteRecordSetsReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'zone_type': 'str',
        'recordset_ids': 'list[str]'
    }

    attribute_map = {
        'zone_type': 'zone_type',
        'recordset_ids': 'recordset_ids'
    }

    def __init__(self, zone_type=None, recordset_ids=None):
        """BatchDeleteRecordSetsReq

        The model defined in huaweicloud sdk

        :param zone_type: Zone的类型，取值为public或private。
        :type zone_type: str
        :param recordset_ids: 待删除的Record Set ID列表。 最多支持100个。
        :type recordset_ids: list[str]
        """
        
        

        self._zone_type = None
        self._recordset_ids = None
        self.discriminator = None

        if zone_type is not None:
            self.zone_type = zone_type
        if recordset_ids is not None:
            self.recordset_ids = recordset_ids

    @property
    def zone_type(self):
        """Gets the zone_type of this BatchDeleteRecordSetsReq.

        Zone的类型，取值为public或private。

        :return: The zone_type of this BatchDeleteRecordSetsReq.
        :rtype: str
        """
        return self._zone_type

    @zone_type.setter
    def zone_type(self, zone_type):
        """Sets the zone_type of this BatchDeleteRecordSetsReq.

        Zone的类型，取值为public或private。

        :param zone_type: The zone_type of this BatchDeleteRecordSetsReq.
        :type zone_type: str
        """
        self._zone_type = zone_type

    @property
    def recordset_ids(self):
        """Gets the recordset_ids of this BatchDeleteRecordSetsReq.

        待删除的Record Set ID列表。 最多支持100个。

        :return: The recordset_ids of this BatchDeleteRecordSetsReq.
        :rtype: list[str]
        """
        return self._recordset_ids

    @recordset_ids.setter
    def recordset_ids(self, recordset_ids):
        """Sets the recordset_ids of this BatchDeleteRecordSetsReq.

        待删除的Record Set ID列表。 最多支持100个。

        :param recordset_ids: The recordset_ids of this BatchDeleteRecordSetsReq.
        :type recordset_ids: list[str]
        """
        self._recordset_ids = recordset_ids

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
        if not isinstance(other, BatchDeleteRecordSetsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
