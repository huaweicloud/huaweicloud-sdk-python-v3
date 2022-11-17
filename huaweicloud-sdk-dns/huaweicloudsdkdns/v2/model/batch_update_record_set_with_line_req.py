# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchUpdateRecordSetWithLineReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'recordsets': 'list[BatchUpdateRecordSet]'
    }

    attribute_map = {
        'recordsets': 'recordsets'
    }

    def __init__(self, recordsets=None):
        """BatchUpdateRecordSetWithLineReq

        The model defined in huaweicloud sdk

        :param recordsets: RecordSet 列表。
        :type recordsets: list[:class:`huaweicloudsdkdns.v2.BatchUpdateRecordSet`]
        """
        
        

        self._recordsets = None
        self.discriminator = None

        self.recordsets = recordsets

    @property
    def recordsets(self):
        """Gets the recordsets of this BatchUpdateRecordSetWithLineReq.

        RecordSet 列表。

        :return: The recordsets of this BatchUpdateRecordSetWithLineReq.
        :rtype: list[:class:`huaweicloudsdkdns.v2.BatchUpdateRecordSet`]
        """
        return self._recordsets

    @recordsets.setter
    def recordsets(self, recordsets):
        """Sets the recordsets of this BatchUpdateRecordSetWithLineReq.

        RecordSet 列表。

        :param recordsets: The recordsets of this BatchUpdateRecordSetWithLineReq.
        :type recordsets: list[:class:`huaweicloudsdkdns.v2.BatchUpdateRecordSet`]
        """
        self._recordsets = recordsets

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
        if not isinstance(other, BatchUpdateRecordSetWithLineReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
