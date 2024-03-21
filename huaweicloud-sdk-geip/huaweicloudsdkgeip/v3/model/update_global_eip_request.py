# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateGlobalEipRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'global_eip_id': 'str',
        'body': 'UpdateGlobalEipRequestBody'
    }

    attribute_map = {
        'global_eip_id': 'global_eip_id',
        'body': 'body'
    }

    def __init__(self, global_eip_id=None, body=None):
        """UpdateGlobalEipRequest

        The model defined in huaweicloud sdk

        :param global_eip_id: 
        :type global_eip_id: str
        :param body: Body of the UpdateGlobalEipRequest
        :type body: :class:`huaweicloudsdkgeip.v3.UpdateGlobalEipRequestBody`
        """
        
        

        self._global_eip_id = None
        self._body = None
        self.discriminator = None

        self.global_eip_id = global_eip_id
        if body is not None:
            self.body = body

    @property
    def global_eip_id(self):
        """Gets the global_eip_id of this UpdateGlobalEipRequest.

        :return: The global_eip_id of this UpdateGlobalEipRequest.
        :rtype: str
        """
        return self._global_eip_id

    @global_eip_id.setter
    def global_eip_id(self, global_eip_id):
        """Sets the global_eip_id of this UpdateGlobalEipRequest.

        :param global_eip_id: The global_eip_id of this UpdateGlobalEipRequest.
        :type global_eip_id: str
        """
        self._global_eip_id = global_eip_id

    @property
    def body(self):
        """Gets the body of this UpdateGlobalEipRequest.

        :return: The body of this UpdateGlobalEipRequest.
        :rtype: :class:`huaweicloudsdkgeip.v3.UpdateGlobalEipRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateGlobalEipRequest.

        :param body: The body of this UpdateGlobalEipRequest.
        :type body: :class:`huaweicloudsdkgeip.v3.UpdateGlobalEipRequestBody`
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
        if not isinstance(other, UpdateGlobalEipRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
