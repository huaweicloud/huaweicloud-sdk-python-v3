# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInternetResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'internet_infos': 'list[InternetInfo]'
    }

    attribute_map = {
        'internet_infos': 'internet_infos'
    }

    def __init__(self, internet_infos=None):
        r"""ListInternetResponse

        The model defined in huaweicloud sdk

        :param internet_infos: 上网信息。
        :type internet_infos: list[:class:`huaweicloudsdkworkspace.v2.InternetInfo`]
        """
        
        super(ListInternetResponse, self).__init__()

        self._internet_infos = None
        self.discriminator = None

        if internet_infos is not None:
            self.internet_infos = internet_infos

    @property
    def internet_infos(self):
        r"""Gets the internet_infos of this ListInternetResponse.

        上网信息。

        :return: The internet_infos of this ListInternetResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.InternetInfo`]
        """
        return self._internet_infos

    @internet_infos.setter
    def internet_infos(self, internet_infos):
        r"""Sets the internet_infos of this ListInternetResponse.

        上网信息。

        :param internet_infos: The internet_infos of this ListInternetResponse.
        :type internet_infos: list[:class:`huaweicloudsdkworkspace.v2.InternetInfo`]
        """
        self._internet_infos = internet_infos

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
        if not isinstance(other, ListInternetResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
