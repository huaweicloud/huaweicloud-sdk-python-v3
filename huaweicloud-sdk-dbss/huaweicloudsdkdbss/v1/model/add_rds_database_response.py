# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddRdsDatabaseResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ret_list': 'list[RdsDbResponseRetList]'
    }

    attribute_map = {
        'ret_list': 'ret_list'
    }

    def __init__(self, ret_list=None):
        r"""AddRdsDatabaseResponse

        The model defined in huaweicloud sdk

        :param ret_list: 结果列表
        :type ret_list: list[:class:`huaweicloudsdkdbss.v1.RdsDbResponseRetList`]
        """
        
        super(AddRdsDatabaseResponse, self).__init__()

        self._ret_list = None
        self.discriminator = None

        if ret_list is not None:
            self.ret_list = ret_list

    @property
    def ret_list(self):
        r"""Gets the ret_list of this AddRdsDatabaseResponse.

        结果列表

        :return: The ret_list of this AddRdsDatabaseResponse.
        :rtype: list[:class:`huaweicloudsdkdbss.v1.RdsDbResponseRetList`]
        """
        return self._ret_list

    @ret_list.setter
    def ret_list(self, ret_list):
        r"""Sets the ret_list of this AddRdsDatabaseResponse.

        结果列表

        :param ret_list: The ret_list of this AddRdsDatabaseResponse.
        :type ret_list: list[:class:`huaweicloudsdkdbss.v1.RdsDbResponseRetList`]
        """
        self._ret_list = ret_list

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
        if not isinstance(other, AddRdsDatabaseResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
