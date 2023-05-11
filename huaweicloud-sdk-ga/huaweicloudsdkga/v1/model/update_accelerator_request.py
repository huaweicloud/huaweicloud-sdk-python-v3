# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAcceleratorRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'accelerator_id': 'str',
        'body': 'UpdateAcceleratorRequestBody'
    }

    attribute_map = {
        'accelerator_id': 'accelerator_id',
        'body': 'body'
    }

    def __init__(self, accelerator_id=None, body=None):
        """UpdateAcceleratorRequest

        The model defined in huaweicloud sdk

        :param accelerator_id: 全球加速器ID。
        :type accelerator_id: str
        :param body: Body of the UpdateAcceleratorRequest
        :type body: :class:`huaweicloudsdkga.v1.UpdateAcceleratorRequestBody`
        """
        
        

        self._accelerator_id = None
        self._body = None
        self.discriminator = None

        self.accelerator_id = accelerator_id
        if body is not None:
            self.body = body

    @property
    def accelerator_id(self):
        """Gets the accelerator_id of this UpdateAcceleratorRequest.

        全球加速器ID。

        :return: The accelerator_id of this UpdateAcceleratorRequest.
        :rtype: str
        """
        return self._accelerator_id

    @accelerator_id.setter
    def accelerator_id(self, accelerator_id):
        """Sets the accelerator_id of this UpdateAcceleratorRequest.

        全球加速器ID。

        :param accelerator_id: The accelerator_id of this UpdateAcceleratorRequest.
        :type accelerator_id: str
        """
        self._accelerator_id = accelerator_id

    @property
    def body(self):
        """Gets the body of this UpdateAcceleratorRequest.

        :return: The body of this UpdateAcceleratorRequest.
        :rtype: :class:`huaweicloudsdkga.v1.UpdateAcceleratorRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateAcceleratorRequest.

        :param body: The body of this UpdateAcceleratorRequest.
        :type body: :class:`huaweicloudsdkga.v1.UpdateAcceleratorRequestBody`
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
        if not isinstance(other, UpdateAcceleratorRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
