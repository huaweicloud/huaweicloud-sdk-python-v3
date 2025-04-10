# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFirmwaresResponse(SdkResponse):

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
        'firmwares': 'list[ListFirmwaresResponseData]'
    }

    attribute_map = {
        'count': 'count',
        'firmwares': 'firmwares'
    }

    def __init__(self, count=None, firmwares=None):
        r"""ListFirmwaresResponse

        The model defined in huaweicloud sdk

        :param count: 固件数
        :type count: int
        :param firmwares: 固件列表
        :type firmwares: list[:class:`huaweicloudsdkhilens.v3.ListFirmwaresResponseData`]
        """
        
        super(ListFirmwaresResponse, self).__init__()

        self._count = None
        self._firmwares = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if firmwares is not None:
            self.firmwares = firmwares

    @property
    def count(self):
        r"""Gets the count of this ListFirmwaresResponse.

        固件数

        :return: The count of this ListFirmwaresResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListFirmwaresResponse.

        固件数

        :param count: The count of this ListFirmwaresResponse.
        :type count: int
        """
        self._count = count

    @property
    def firmwares(self):
        r"""Gets the firmwares of this ListFirmwaresResponse.

        固件列表

        :return: The firmwares of this ListFirmwaresResponse.
        :rtype: list[:class:`huaweicloudsdkhilens.v3.ListFirmwaresResponseData`]
        """
        return self._firmwares

    @firmwares.setter
    def firmwares(self, firmwares):
        r"""Sets the firmwares of this ListFirmwaresResponse.

        固件列表

        :param firmwares: The firmwares of this ListFirmwaresResponse.
        :type firmwares: list[:class:`huaweicloudsdkhilens.v3.ListFirmwaresResponseData`]
        """
        self._firmwares = firmwares

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
        if not isinstance(other, ListFirmwaresResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
