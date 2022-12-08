# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAssetNameResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'msg': 'str',
        'status': 'str'
    }

    attribute_map = {
        'msg': 'msg',
        'status': 'status'
    }

    def __init__(self, msg=None, status=None):
        """UpdateAssetNameResponse

        The model defined in huaweicloud sdk

        :param msg: 返回消息
        :type msg: str
        :param status: 返回状态，如&#39;200&#39;,&#39;400&#39;
        :type status: str
        """
        
        super(UpdateAssetNameResponse, self).__init__()

        self._msg = None
        self._status = None
        self.discriminator = None

        if msg is not None:
            self.msg = msg
        if status is not None:
            self.status = status

    @property
    def msg(self):
        """Gets the msg of this UpdateAssetNameResponse.

        返回消息

        :return: The msg of this UpdateAssetNameResponse.
        :rtype: str
        """
        return self._msg

    @msg.setter
    def msg(self, msg):
        """Sets the msg of this UpdateAssetNameResponse.

        返回消息

        :param msg: The msg of this UpdateAssetNameResponse.
        :type msg: str
        """
        self._msg = msg

    @property
    def status(self):
        """Gets the status of this UpdateAssetNameResponse.

        返回状态，如'200','400'

        :return: The status of this UpdateAssetNameResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UpdateAssetNameResponse.

        返回状态，如'200','400'

        :param status: The status of this UpdateAssetNameResponse.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, UpdateAssetNameResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
