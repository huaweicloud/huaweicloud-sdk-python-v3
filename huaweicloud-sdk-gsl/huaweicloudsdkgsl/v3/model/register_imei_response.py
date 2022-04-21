# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RegisterImeiResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'work_order_id': 'int'
    }

    attribute_map = {
        'work_order_id': 'work_order_id'
    }

    def __init__(self, work_order_id=None):
        """RegisterImeiResponse

        The model defined in huaweicloud sdk

        :param work_order_id: 业务受理单号
        :type work_order_id: int
        """
        
        super(RegisterImeiResponse, self).__init__()

        self._work_order_id = None
        self.discriminator = None

        if work_order_id is not None:
            self.work_order_id = work_order_id

    @property
    def work_order_id(self):
        """Gets the work_order_id of this RegisterImeiResponse.

        业务受理单号

        :return: The work_order_id of this RegisterImeiResponse.
        :rtype: int
        """
        return self._work_order_id

    @work_order_id.setter
    def work_order_id(self, work_order_id):
        """Sets the work_order_id of this RegisterImeiResponse.

        业务受理单号

        :param work_order_id: The work_order_id of this RegisterImeiResponse.
        :type work_order_id: int
        """
        self._work_order_id = work_order_id

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
        if not isinstance(other, RegisterImeiResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
