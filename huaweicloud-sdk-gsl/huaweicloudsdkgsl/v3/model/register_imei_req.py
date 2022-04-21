# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RegisterImeiReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'bind_type': 'int',
        'imei': 'str'
    }

    attribute_map = {
        'bind_type': 'bind_type',
        'imei': 'imei'
    }

    def __init__(self, bind_type=None, imei=None):
        """RegisterImeiReq

        The model defined in huaweicloud sdk

        :param bind_type: 绑定类型(1:普通机卡重绑，2：固定机卡重绑)
        :type bind_type: int
        :param imei: 设备IMEI,84584xxxxxx
        :type imei: str
        """
        
        

        self._bind_type = None
        self._imei = None
        self.discriminator = None

        self.bind_type = bind_type
        if imei is not None:
            self.imei = imei

    @property
    def bind_type(self):
        """Gets the bind_type of this RegisterImeiReq.

        绑定类型(1:普通机卡重绑，2：固定机卡重绑)

        :return: The bind_type of this RegisterImeiReq.
        :rtype: int
        """
        return self._bind_type

    @bind_type.setter
    def bind_type(self, bind_type):
        """Sets the bind_type of this RegisterImeiReq.

        绑定类型(1:普通机卡重绑，2：固定机卡重绑)

        :param bind_type: The bind_type of this RegisterImeiReq.
        :type bind_type: int
        """
        self._bind_type = bind_type

    @property
    def imei(self):
        """Gets the imei of this RegisterImeiReq.

        设备IMEI,84584xxxxxx

        :return: The imei of this RegisterImeiReq.
        :rtype: str
        """
        return self._imei

    @imei.setter
    def imei(self, imei):
        """Sets the imei of this RegisterImeiReq.

        设备IMEI,84584xxxxxx

        :param imei: The imei of this RegisterImeiReq.
        :type imei: str
        """
        self._imei = imei

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
        if not isinstance(other, RegisterImeiReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
