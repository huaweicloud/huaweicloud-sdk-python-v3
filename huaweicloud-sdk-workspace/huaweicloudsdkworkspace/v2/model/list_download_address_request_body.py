# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDownloadAddressRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'record_ids': 'list[str]'
    }

    attribute_map = {
        'record_ids': 'record_ids'
    }

    def __init__(self, record_ids=None):
        r"""ListDownloadAddressRequestBody

        The model defined in huaweicloud sdk

        :param record_ids: 录屏记录UUID列表。
        :type record_ids: list[str]
        """
        
        

        self._record_ids = None
        self.discriminator = None

        if record_ids is not None:
            self.record_ids = record_ids

    @property
    def record_ids(self):
        r"""Gets the record_ids of this ListDownloadAddressRequestBody.

        录屏记录UUID列表。

        :return: The record_ids of this ListDownloadAddressRequestBody.
        :rtype: list[str]
        """
        return self._record_ids

    @record_ids.setter
    def record_ids(self, record_ids):
        r"""Sets the record_ids of this ListDownloadAddressRequestBody.

        录屏记录UUID列表。

        :param record_ids: The record_ids of this ListDownloadAddressRequestBody.
        :type record_ids: list[str]
        """
        self._record_ids = record_ids

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
        if not isinstance(other, ListDownloadAddressRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
