# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateNodeFirmwareResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'body': 'object',
        'firmware_name': 'str',
        'firmware_id': 'str'
    }

    attribute_map = {
        'body': 'body',
        'firmware_name': 'firmware_name',
        'firmware_id': 'firmware_id'
    }

    def __init__(self, body=None, firmware_name=None, firmware_id=None):
        r"""UpdateNodeFirmwareResponse

        The model defined in huaweicloud sdk

        :param body: 
        :type body: object
        :param firmware_name: 
        :type firmware_name: str
        :param firmware_id: 
        :type firmware_id: str
        """
        
        super(UpdateNodeFirmwareResponse, self).__init__()

        self._body = None
        self._firmware_name = None
        self._firmware_id = None
        self.discriminator = None

        if body is not None:
            self.body = body
        if firmware_name is not None:
            self.firmware_name = firmware_name
        if firmware_id is not None:
            self.firmware_id = firmware_id

    @property
    def body(self):
        r"""Gets the body of this UpdateNodeFirmwareResponse.

        :return: The body of this UpdateNodeFirmwareResponse.
        :rtype: object
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateNodeFirmwareResponse.

        :param body: The body of this UpdateNodeFirmwareResponse.
        :type body: object
        """
        self._body = body

    @property
    def firmware_name(self):
        r"""Gets the firmware_name of this UpdateNodeFirmwareResponse.

        :return: The firmware_name of this UpdateNodeFirmwareResponse.
        :rtype: str
        """
        return self._firmware_name

    @firmware_name.setter
    def firmware_name(self, firmware_name):
        r"""Sets the firmware_name of this UpdateNodeFirmwareResponse.

        :param firmware_name: The firmware_name of this UpdateNodeFirmwareResponse.
        :type firmware_name: str
        """
        self._firmware_name = firmware_name

    @property
    def firmware_id(self):
        r"""Gets the firmware_id of this UpdateNodeFirmwareResponse.

        :return: The firmware_id of this UpdateNodeFirmwareResponse.
        :rtype: str
        """
        return self._firmware_id

    @firmware_id.setter
    def firmware_id(self, firmware_id):
        r"""Sets the firmware_id of this UpdateNodeFirmwareResponse.

        :param firmware_id: The firmware_id of this UpdateNodeFirmwareResponse.
        :type firmware_id: str
        """
        self._firmware_id = firmware_id

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
        if not isinstance(other, UpdateNodeFirmwareResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
