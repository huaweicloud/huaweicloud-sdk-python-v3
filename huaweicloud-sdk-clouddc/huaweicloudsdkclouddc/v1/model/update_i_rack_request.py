# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateIRackRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'irack_id': 'str',
        'body': 'IRackRequest'
    }

    attribute_map = {
        'irack_id': 'irack_id',
        'body': 'body'
    }

    def __init__(self, irack_id=None, body=None):
        r"""UpdateIRackRequest

        The model defined in huaweicloud sdk

        :param irack_id: iRack 唯一标识符
        :type irack_id: str
        :param body: Body of the UpdateIRackRequest
        :type body: :class:`huaweicloudsdkclouddc.v1.IRackRequest`
        """
        
        

        self._irack_id = None
        self._body = None
        self.discriminator = None

        self.irack_id = irack_id
        if body is not None:
            self.body = body

    @property
    def irack_id(self):
        r"""Gets the irack_id of this UpdateIRackRequest.

        iRack 唯一标识符

        :return: The irack_id of this UpdateIRackRequest.
        :rtype: str
        """
        return self._irack_id

    @irack_id.setter
    def irack_id(self, irack_id):
        r"""Sets the irack_id of this UpdateIRackRequest.

        iRack 唯一标识符

        :param irack_id: The irack_id of this UpdateIRackRequest.
        :type irack_id: str
        """
        self._irack_id = irack_id

    @property
    def body(self):
        r"""Gets the body of this UpdateIRackRequest.

        :return: The body of this UpdateIRackRequest.
        :rtype: :class:`huaweicloudsdkclouddc.v1.IRackRequest`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateIRackRequest.

        :param body: The body of this UpdateIRackRequest.
        :type body: :class:`huaweicloudsdkclouddc.v1.IRackRequest`
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
        if not isinstance(other, UpdateIRackRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
