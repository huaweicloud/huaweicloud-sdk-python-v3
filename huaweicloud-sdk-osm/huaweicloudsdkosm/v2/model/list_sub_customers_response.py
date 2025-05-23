# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSubCustomersResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sub_customer_infos': 'list[SubCutomerInfoV2]'
    }

    attribute_map = {
        'sub_customer_infos': 'sub_customer_infos'
    }

    def __init__(self, sub_customer_infos=None):
        r"""ListSubCustomersResponse

        The model defined in huaweicloud sdk

        :param sub_customer_infos: 子用户列表
        :type sub_customer_infos: list[:class:`huaweicloudsdkosm.v2.SubCutomerInfoV2`]
        """
        
        super(ListSubCustomersResponse, self).__init__()

        self._sub_customer_infos = None
        self.discriminator = None

        if sub_customer_infos is not None:
            self.sub_customer_infos = sub_customer_infos

    @property
    def sub_customer_infos(self):
        r"""Gets the sub_customer_infos of this ListSubCustomersResponse.

        子用户列表

        :return: The sub_customer_infos of this ListSubCustomersResponse.
        :rtype: list[:class:`huaweicloudsdkosm.v2.SubCutomerInfoV2`]
        """
        return self._sub_customer_infos

    @sub_customer_infos.setter
    def sub_customer_infos(self, sub_customer_infos):
        r"""Sets the sub_customer_infos of this ListSubCustomersResponse.

        子用户列表

        :param sub_customer_infos: The sub_customer_infos of this ListSubCustomersResponse.
        :type sub_customer_infos: list[:class:`huaweicloudsdkosm.v2.SubCutomerInfoV2`]
        """
        self._sub_customer_infos = sub_customer_infos

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
        if not isinstance(other, ListSubCustomersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
