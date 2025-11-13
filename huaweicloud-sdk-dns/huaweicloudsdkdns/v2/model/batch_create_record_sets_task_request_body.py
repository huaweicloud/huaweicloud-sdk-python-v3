# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCreateRecordSetsTaskRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'recordsets': 'list[BatchCreateRecordSetsTaskItem]'
    }

    attribute_map = {
        'recordsets': 'recordsets'
    }

    def __init__(self, recordsets=None):
        r"""BatchCreateRecordSetsTaskRequestBody

        The model defined in huaweicloud sdk

        :param recordsets: 批量创建记录集列表。
        :type recordsets: list[:class:`huaweicloudsdkdns.v2.BatchCreateRecordSetsTaskItem`]
        """
        
        

        self._recordsets = None
        self.discriminator = None

        self.recordsets = recordsets

    @property
    def recordsets(self):
        r"""Gets the recordsets of this BatchCreateRecordSetsTaskRequestBody.

        批量创建记录集列表。

        :return: The recordsets of this BatchCreateRecordSetsTaskRequestBody.
        :rtype: list[:class:`huaweicloudsdkdns.v2.BatchCreateRecordSetsTaskItem`]
        """
        return self._recordsets

    @recordsets.setter
    def recordsets(self, recordsets):
        r"""Sets the recordsets of this BatchCreateRecordSetsTaskRequestBody.

        批量创建记录集列表。

        :param recordsets: The recordsets of this BatchCreateRecordSetsTaskRequestBody.
        :type recordsets: list[:class:`huaweicloudsdkdns.v2.BatchCreateRecordSetsTaskItem`]
        """
        self._recordsets = recordsets

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BatchCreateRecordSetsTaskRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
