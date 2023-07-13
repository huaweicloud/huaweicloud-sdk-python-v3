# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateShareRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'share': 'Share',
        'bss_param': 'BssInfo'
    }

    attribute_map = {
        'share': 'share',
        'bss_param': 'bss_param'
    }

    def __init__(self, share=None, bss_param=None):
        """CreateShareRequestBody

        The model defined in huaweicloud sdk

        :param share: 
        :type share: :class:`huaweicloudsdksfsturbo.v1.Share`
        :param bss_param: 
        :type bss_param: :class:`huaweicloudsdksfsturbo.v1.BssInfo`
        """
        
        

        self._share = None
        self._bss_param = None
        self.discriminator = None

        self.share = share
        if bss_param is not None:
            self.bss_param = bss_param

    @property
    def share(self):
        """Gets the share of this CreateShareRequestBody.

        :return: The share of this CreateShareRequestBody.
        :rtype: :class:`huaweicloudsdksfsturbo.v1.Share`
        """
        return self._share

    @share.setter
    def share(self, share):
        """Sets the share of this CreateShareRequestBody.

        :param share: The share of this CreateShareRequestBody.
        :type share: :class:`huaweicloudsdksfsturbo.v1.Share`
        """
        self._share = share

    @property
    def bss_param(self):
        """Gets the bss_param of this CreateShareRequestBody.

        :return: The bss_param of this CreateShareRequestBody.
        :rtype: :class:`huaweicloudsdksfsturbo.v1.BssInfo`
        """
        return self._bss_param

    @bss_param.setter
    def bss_param(self, bss_param):
        """Sets the bss_param of this CreateShareRequestBody.

        :param bss_param: The bss_param of this CreateShareRequestBody.
        :type bss_param: :class:`huaweicloudsdksfsturbo.v1.BssInfo`
        """
        self._bss_param = bss_param

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
        if not isinstance(other, CreateShareRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
