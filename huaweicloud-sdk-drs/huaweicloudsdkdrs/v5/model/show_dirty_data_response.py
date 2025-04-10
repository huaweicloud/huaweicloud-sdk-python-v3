# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDirtyDataResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'dirty_data_list': 'list[DirtyData]'
    }

    attribute_map = {
        'count': 'count',
        'dirty_data_list': 'dirty_data_list'
    }

    def __init__(self, count=None, dirty_data_list=None):
        r"""ShowDirtyDataResponse

        The model defined in huaweicloud sdk

        :param count: 总数。
        :type count: int
        :param dirty_data_list: 异常数据列表。
        :type dirty_data_list: list[:class:`huaweicloudsdkdrs.v5.DirtyData`]
        """
        
        super(ShowDirtyDataResponse, self).__init__()

        self._count = None
        self._dirty_data_list = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if dirty_data_list is not None:
            self.dirty_data_list = dirty_data_list

    @property
    def count(self):
        r"""Gets the count of this ShowDirtyDataResponse.

        总数。

        :return: The count of this ShowDirtyDataResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ShowDirtyDataResponse.

        总数。

        :param count: The count of this ShowDirtyDataResponse.
        :type count: int
        """
        self._count = count

    @property
    def dirty_data_list(self):
        r"""Gets the dirty_data_list of this ShowDirtyDataResponse.

        异常数据列表。

        :return: The dirty_data_list of this ShowDirtyDataResponse.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.DirtyData`]
        """
        return self._dirty_data_list

    @dirty_data_list.setter
    def dirty_data_list(self, dirty_data_list):
        r"""Sets the dirty_data_list of this ShowDirtyDataResponse.

        异常数据列表。

        :param dirty_data_list: The dirty_data_list of this ShowDirtyDataResponse.
        :type dirty_data_list: list[:class:`huaweicloudsdkdrs.v5.DirtyData`]
        """
        self._dirty_data_list = dirty_data_list

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
        if not isinstance(other, ShowDirtyDataResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
