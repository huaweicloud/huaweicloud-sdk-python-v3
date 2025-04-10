# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateGdgwRouteTableRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'gdgw_id': 'str',
        'body': 'UpdateGdgwRoutetableRequestBody'
    }

    attribute_map = {
        'gdgw_id': 'gdgw_id',
        'body': 'body'
    }

    def __init__(self, gdgw_id=None, body=None):
        r"""UpdateGdgwRouteTableRequest

        The model defined in huaweicloud sdk

        :param gdgw_id: 全域接入网关ID
        :type gdgw_id: str
        :param body: Body of the UpdateGdgwRouteTableRequest
        :type body: :class:`huaweicloudsdkdc.v3.UpdateGdgwRoutetableRequestBody`
        """
        
        

        self._gdgw_id = None
        self._body = None
        self.discriminator = None

        self.gdgw_id = gdgw_id
        if body is not None:
            self.body = body

    @property
    def gdgw_id(self):
        r"""Gets the gdgw_id of this UpdateGdgwRouteTableRequest.

        全域接入网关ID

        :return: The gdgw_id of this UpdateGdgwRouteTableRequest.
        :rtype: str
        """
        return self._gdgw_id

    @gdgw_id.setter
    def gdgw_id(self, gdgw_id):
        r"""Sets the gdgw_id of this UpdateGdgwRouteTableRequest.

        全域接入网关ID

        :param gdgw_id: The gdgw_id of this UpdateGdgwRouteTableRequest.
        :type gdgw_id: str
        """
        self._gdgw_id = gdgw_id

    @property
    def body(self):
        r"""Gets the body of this UpdateGdgwRouteTableRequest.

        :return: The body of this UpdateGdgwRouteTableRequest.
        :rtype: :class:`huaweicloudsdkdc.v3.UpdateGdgwRoutetableRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateGdgwRouteTableRequest.

        :param body: The body of this UpdateGdgwRouteTableRequest.
        :type body: :class:`huaweicloudsdkdc.v3.UpdateGdgwRoutetableRequestBody`
        """
        self._body = body

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
        if not isinstance(other, UpdateGdgwRouteTableRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
