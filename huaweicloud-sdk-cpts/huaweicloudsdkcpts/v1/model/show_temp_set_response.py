# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTempSetResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'code': 'str',
        'message': 'str',
        'temps': 'list[TempDetailInfo]'
    }

    attribute_map = {
        'code': 'code',
        'message': 'message',
        'temps': 'temps'
    }

    def __init__(self, code=None, message=None, temps=None):
        """ShowTempSetResponse

        The model defined in huaweicloud sdk

        :param code: code
        :type code: str
        :param message: message
        :type message: str
        :param temps: temps
        :type temps: list[:class:`huaweicloudsdkcpts.v1.TempDetailInfo`]
        """
        
        super(ShowTempSetResponse, self).__init__()

        self._code = None
        self._message = None
        self._temps = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if message is not None:
            self.message = message
        if temps is not None:
            self.temps = temps

    @property
    def code(self):
        """Gets the code of this ShowTempSetResponse.

        code

        :return: The code of this ShowTempSetResponse.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ShowTempSetResponse.

        code

        :param code: The code of this ShowTempSetResponse.
        :type code: str
        """
        self._code = code

    @property
    def message(self):
        """Gets the message of this ShowTempSetResponse.

        message

        :return: The message of this ShowTempSetResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ShowTempSetResponse.

        message

        :param message: The message of this ShowTempSetResponse.
        :type message: str
        """
        self._message = message

    @property
    def temps(self):
        """Gets the temps of this ShowTempSetResponse.

        temps

        :return: The temps of this ShowTempSetResponse.
        :rtype: list[:class:`huaweicloudsdkcpts.v1.TempDetailInfo`]
        """
        return self._temps

    @temps.setter
    def temps(self, temps):
        """Sets the temps of this ShowTempSetResponse.

        temps

        :param temps: The temps of this ShowTempSetResponse.
        :type temps: list[:class:`huaweicloudsdkcpts.v1.TempDetailInfo`]
        """
        self._temps = temps

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
        if not isinstance(other, ShowTempSetResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
