# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchWriteKvResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'unprocessed_opers': 'list[TableOperIds]'
    }

    attribute_map = {
        'unprocessed_opers': 'unprocessed_opers'
    }

    def __init__(self, unprocessed_opers=None):
        r"""BatchWriteKvResponse

        The model defined in huaweicloud sdk

        :param unprocessed_opers: 未处理的操作列表。
        :type unprocessed_opers: list[:class:`huaweicloudsdkkvs.v1.TableOperIds`]
        """
        
        super(BatchWriteKvResponse, self).__init__()

        self._unprocessed_opers = None
        self.discriminator = None

        if unprocessed_opers is not None:
            self.unprocessed_opers = unprocessed_opers

    @property
    def unprocessed_opers(self):
        r"""Gets the unprocessed_opers of this BatchWriteKvResponse.

        未处理的操作列表。

        :return: The unprocessed_opers of this BatchWriteKvResponse.
        :rtype: list[:class:`huaweicloudsdkkvs.v1.TableOperIds`]
        """
        return self._unprocessed_opers

    @unprocessed_opers.setter
    def unprocessed_opers(self, unprocessed_opers):
        r"""Sets the unprocessed_opers of this BatchWriteKvResponse.

        未处理的操作列表。

        :param unprocessed_opers: The unprocessed_opers of this BatchWriteKvResponse.
        :type unprocessed_opers: list[:class:`huaweicloudsdkkvs.v1.TableOperIds`]
        """
        self._unprocessed_opers = unprocessed_opers

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
        if not isinstance(other, BatchWriteKvResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
