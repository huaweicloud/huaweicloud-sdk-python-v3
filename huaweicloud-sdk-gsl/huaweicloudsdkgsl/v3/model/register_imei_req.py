# coding: utf-8

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
        'imei': 'str',
        'iccid': 'str'
    }

    attribute_map = {
        'bind_type': 'bind_type',
        'imei': 'imei',
        'iccid': 'iccid'
    }

    def __init__(self, bind_type=None, imei=None, iccid=None):
        r"""RegisterImeiReq

        The model defined in huaweicloud sdk

        :param bind_type: 绑定类型(1:普通机卡重绑，2：固定机卡重绑)
        :type bind_type: int
        :param imei: 设备IMEI,84584xxxxxx
        :type imei: str
        :param iccid: iccid，传入的sim_card_id为0,则根据iccid进行处理
        :type iccid: str
        """
        
        

        self._bind_type = None
        self._imei = None
        self._iccid = None
        self.discriminator = None

        self.bind_type = bind_type
        if imei is not None:
            self.imei = imei
        if iccid is not None:
            self.iccid = iccid

    @property
    def bind_type(self):
        r"""Gets the bind_type of this RegisterImeiReq.

        绑定类型(1:普通机卡重绑，2：固定机卡重绑)

        :return: The bind_type of this RegisterImeiReq.
        :rtype: int
        """
        return self._bind_type

    @bind_type.setter
    def bind_type(self, bind_type):
        r"""Sets the bind_type of this RegisterImeiReq.

        绑定类型(1:普通机卡重绑，2：固定机卡重绑)

        :param bind_type: The bind_type of this RegisterImeiReq.
        :type bind_type: int
        """
        self._bind_type = bind_type

    @property
    def imei(self):
        r"""Gets the imei of this RegisterImeiReq.

        设备IMEI,84584xxxxxx

        :return: The imei of this RegisterImeiReq.
        :rtype: str
        """
        return self._imei

    @imei.setter
    def imei(self, imei):
        r"""Sets the imei of this RegisterImeiReq.

        设备IMEI,84584xxxxxx

        :param imei: The imei of this RegisterImeiReq.
        :type imei: str
        """
        self._imei = imei

    @property
    def iccid(self):
        r"""Gets the iccid of this RegisterImeiReq.

        iccid，传入的sim_card_id为0,则根据iccid进行处理

        :return: The iccid of this RegisterImeiReq.
        :rtype: str
        """
        return self._iccid

    @iccid.setter
    def iccid(self, iccid):
        r"""Sets the iccid of this RegisterImeiReq.

        iccid，传入的sim_card_id为0,则根据iccid进行处理

        :param iccid: The iccid of this RegisterImeiReq.
        :type iccid: str
        """
        self._iccid = iccid

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
