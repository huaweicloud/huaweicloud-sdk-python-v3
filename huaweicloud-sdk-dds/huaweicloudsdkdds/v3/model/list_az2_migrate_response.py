# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAz2MigrateResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'az_list': 'list[Az2Migrate]'
    }

    attribute_map = {
        'az_list': 'az_list'
    }

    def __init__(self, az_list=None):
        r"""ListAz2MigrateResponse

        The model defined in huaweicloud sdk

        :param az_list: 可用区具体信息。
        :type az_list: list[:class:`huaweicloudsdkdds.v3.Az2Migrate`]
        """
        
        super(ListAz2MigrateResponse, self).__init__()

        self._az_list = None
        self.discriminator = None

        if az_list is not None:
            self.az_list = az_list

    @property
    def az_list(self):
        r"""Gets the az_list of this ListAz2MigrateResponse.

        可用区具体信息。

        :return: The az_list of this ListAz2MigrateResponse.
        :rtype: list[:class:`huaweicloudsdkdds.v3.Az2Migrate`]
        """
        return self._az_list

    @az_list.setter
    def az_list(self, az_list):
        r"""Sets the az_list of this ListAz2MigrateResponse.

        可用区具体信息。

        :param az_list: The az_list of this ListAz2MigrateResponse.
        :type az_list: list[:class:`huaweicloudsdkdds.v3.Az2Migrate`]
        """
        self._az_list = az_list

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
        if not isinstance(other, ListAz2MigrateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
