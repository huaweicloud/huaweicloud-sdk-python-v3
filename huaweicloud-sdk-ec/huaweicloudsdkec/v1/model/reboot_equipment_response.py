# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RebootEquipmentResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'success_msg': 'str'
    }

    attribute_map = {
        'success_msg': 'success_msg'
    }

    def __init__(self, success_msg=None):
        r"""RebootEquipmentResponse

        The model defined in huaweicloud sdk

        :param success_msg: 成功信息
        :type success_msg: str
        """
        
        super(RebootEquipmentResponse, self).__init__()

        self._success_msg = None
        self.discriminator = None

        if success_msg is not None:
            self.success_msg = success_msg

    @property
    def success_msg(self):
        r"""Gets the success_msg of this RebootEquipmentResponse.

        成功信息

        :return: The success_msg of this RebootEquipmentResponse.
        :rtype: str
        """
        return self._success_msg

    @success_msg.setter
    def success_msg(self, success_msg):
        r"""Sets the success_msg of this RebootEquipmentResponse.

        成功信息

        :param success_msg: The success_msg of this RebootEquipmentResponse.
        :type success_msg: str
        """
        self._success_msg = success_msg

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
        if not isinstance(other, RebootEquipmentResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
