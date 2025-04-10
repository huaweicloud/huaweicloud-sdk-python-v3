# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EnableSimCardRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sim_card_id': 'int',
        'iccid': 'str'
    }

    attribute_map = {
        'sim_card_id': 'sim_card_id',
        'iccid': 'iccid'
    }

    def __init__(self, sim_card_id=None, iccid=None):
        r"""EnableSimCardRequest

        The model defined in huaweicloud sdk

        :param sim_card_id: SIM卡标识，如果SIM卡标识传0则表示需要根据iccid处理。可通过[查询SIM卡列表接口](https://support.huaweicloud.com/api-ocgsl/gsl_07_0008.html)获取
        :type sim_card_id: int
        :param iccid: iccid，传入的sim_card_id为0,则根据iccid进行处理
        :type iccid: str
        """
        
        

        self._sim_card_id = None
        self._iccid = None
        self.discriminator = None

        self.sim_card_id = sim_card_id
        if iccid is not None:
            self.iccid = iccid

    @property
    def sim_card_id(self):
        r"""Gets the sim_card_id of this EnableSimCardRequest.

        SIM卡标识，如果SIM卡标识传0则表示需要根据iccid处理。可通过[查询SIM卡列表接口](https://support.huaweicloud.com/api-ocgsl/gsl_07_0008.html)获取

        :return: The sim_card_id of this EnableSimCardRequest.
        :rtype: int
        """
        return self._sim_card_id

    @sim_card_id.setter
    def sim_card_id(self, sim_card_id):
        r"""Sets the sim_card_id of this EnableSimCardRequest.

        SIM卡标识，如果SIM卡标识传0则表示需要根据iccid处理。可通过[查询SIM卡列表接口](https://support.huaweicloud.com/api-ocgsl/gsl_07_0008.html)获取

        :param sim_card_id: The sim_card_id of this EnableSimCardRequest.
        :type sim_card_id: int
        """
        self._sim_card_id = sim_card_id

    @property
    def iccid(self):
        r"""Gets the iccid of this EnableSimCardRequest.

        iccid，传入的sim_card_id为0,则根据iccid进行处理

        :return: The iccid of this EnableSimCardRequest.
        :rtype: str
        """
        return self._iccid

    @iccid.setter
    def iccid(self, iccid):
        r"""Sets the iccid of this EnableSimCardRequest.

        iccid，传入的sim_card_id为0,则根据iccid进行处理

        :param iccid: The iccid of this EnableSimCardRequest.
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
        if not isinstance(other, EnableSimCardRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
