# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteScreenRecordsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'screen_records': 'list[BatchDeleteScreenRecordsRequestBodyScreenRecords]'
    }

    attribute_map = {
        'screen_records': 'screen_records'
    }

    def __init__(self, screen_records=None):
        r"""BatchDeleteScreenRecordsRequestBody

        The model defined in huaweicloud sdk

        :param screen_records: 待删除的录屏ID列表。
        :type screen_records: list[:class:`huaweicloudsdkworkspace.v2.BatchDeleteScreenRecordsRequestBodyScreenRecords`]
        """
        
        

        self._screen_records = None
        self.discriminator = None

        if screen_records is not None:
            self.screen_records = screen_records

    @property
    def screen_records(self):
        r"""Gets the screen_records of this BatchDeleteScreenRecordsRequestBody.

        待删除的录屏ID列表。

        :return: The screen_records of this BatchDeleteScreenRecordsRequestBody.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.BatchDeleteScreenRecordsRequestBodyScreenRecords`]
        """
        return self._screen_records

    @screen_records.setter
    def screen_records(self, screen_records):
        r"""Sets the screen_records of this BatchDeleteScreenRecordsRequestBody.

        待删除的录屏ID列表。

        :param screen_records: The screen_records of this BatchDeleteScreenRecordsRequestBody.
        :type screen_records: list[:class:`huaweicloudsdkworkspace.v2.BatchDeleteScreenRecordsRequestBodyScreenRecords`]
        """
        self._screen_records = screen_records

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
        if not isinstance(other, BatchDeleteScreenRecordsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
