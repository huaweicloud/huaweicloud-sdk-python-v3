# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateOuInfoRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ou_id': 'str',
        'body': 'ModifyOuNameInfoV2Req'
    }

    attribute_map = {
        'ou_id': 'ou_id',
        'body': 'body'
    }

    def __init__(self, ou_id=None, body=None):
        r"""UpdateOuInfoRequest

        The model defined in huaweicloud sdk

        :param ou_id: OU的id。
        :type ou_id: str
        :param body: Body of the UpdateOuInfoRequest
        :type body: :class:`huaweicloudsdkworkspace.v2.ModifyOuNameInfoV2Req`
        """
        
        

        self._ou_id = None
        self._body = None
        self.discriminator = None

        self.ou_id = ou_id
        if body is not None:
            self.body = body

    @property
    def ou_id(self):
        r"""Gets the ou_id of this UpdateOuInfoRequest.

        OU的id。

        :return: The ou_id of this UpdateOuInfoRequest.
        :rtype: str
        """
        return self._ou_id

    @ou_id.setter
    def ou_id(self, ou_id):
        r"""Sets the ou_id of this UpdateOuInfoRequest.

        OU的id。

        :param ou_id: The ou_id of this UpdateOuInfoRequest.
        :type ou_id: str
        """
        self._ou_id = ou_id

    @property
    def body(self):
        r"""Gets the body of this UpdateOuInfoRequest.

        :return: The body of this UpdateOuInfoRequest.
        :rtype: :class:`huaweicloudsdkworkspace.v2.ModifyOuNameInfoV2Req`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateOuInfoRequest.

        :param body: The body of this UpdateOuInfoRequest.
        :type body: :class:`huaweicloudsdkworkspace.v2.ModifyOuNameInfoV2Req`
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
        if not isinstance(other, UpdateOuInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
