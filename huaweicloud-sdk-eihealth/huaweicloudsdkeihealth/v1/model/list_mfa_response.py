# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMfaResponse(SdkResponse):

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
        'methods': 'list[MfaRsp]'
    }

    attribute_map = {
        'count': 'count',
        'methods': 'methods'
    }

    def __init__(self, count=None, methods=None):
        """ListMfaResponse

        The model defined in huaweicloud sdk

        :param count: mfa方式个数
        :type count: int
        :param methods: mfa方式列表
        :type methods: list[:class:`huaweicloudsdkeihealth.v1.MfaRsp`]
        """
        
        super(ListMfaResponse, self).__init__()

        self._count = None
        self._methods = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if methods is not None:
            self.methods = methods

    @property
    def count(self):
        """Gets the count of this ListMfaResponse.

        mfa方式个数

        :return: The count of this ListMfaResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListMfaResponse.

        mfa方式个数

        :param count: The count of this ListMfaResponse.
        :type count: int
        """
        self._count = count

    @property
    def methods(self):
        """Gets the methods of this ListMfaResponse.

        mfa方式列表

        :return: The methods of this ListMfaResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.MfaRsp`]
        """
        return self._methods

    @methods.setter
    def methods(self, methods):
        """Sets the methods of this ListMfaResponse.

        mfa方式列表

        :param methods: The methods of this ListMfaResponse.
        :type methods: list[:class:`huaweicloudsdkeihealth.v1.MfaRsp`]
        """
        self._methods = methods

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
        if not isinstance(other, ListMfaResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
