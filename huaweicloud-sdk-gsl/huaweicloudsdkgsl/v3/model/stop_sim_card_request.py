# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StopSimCardRequest:

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
        'body': 'DownUpTimeForSimCardReq'
    }

    attribute_map = {
        'sim_card_id': 'sim_card_id',
        'body': 'body'
    }

    def __init__(self, sim_card_id=None, body=None):
        """StopSimCardRequest

        The model defined in huaweicloud sdk

        :param sim_card_id: SIM卡标识，如果SIM卡标识传0则表示需要根据iccid处理。可通过[查询SIM卡列表接口](https://support.huaweicloud.com/api-ocgsl/gsl_07_0008.html)获取
        :type sim_card_id: int
        :param body: Body of the StopSimCardRequest
        :type body: :class:`huaweicloudsdkgsl.v3.DownUpTimeForSimCardReq`
        """
        
        

        self._sim_card_id = None
        self._body = None
        self.discriminator = None

        self.sim_card_id = sim_card_id
        if body is not None:
            self.body = body

    @property
    def sim_card_id(self):
        """Gets the sim_card_id of this StopSimCardRequest.

        SIM卡标识，如果SIM卡标识传0则表示需要根据iccid处理。可通过[查询SIM卡列表接口](https://support.huaweicloud.com/api-ocgsl/gsl_07_0008.html)获取

        :return: The sim_card_id of this StopSimCardRequest.
        :rtype: int
        """
        return self._sim_card_id

    @sim_card_id.setter
    def sim_card_id(self, sim_card_id):
        """Sets the sim_card_id of this StopSimCardRequest.

        SIM卡标识，如果SIM卡标识传0则表示需要根据iccid处理。可通过[查询SIM卡列表接口](https://support.huaweicloud.com/api-ocgsl/gsl_07_0008.html)获取

        :param sim_card_id: The sim_card_id of this StopSimCardRequest.
        :type sim_card_id: int
        """
        self._sim_card_id = sim_card_id

    @property
    def body(self):
        """Gets the body of this StopSimCardRequest.

        :return: The body of this StopSimCardRequest.
        :rtype: :class:`huaweicloudsdkgsl.v3.DownUpTimeForSimCardReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this StopSimCardRequest.

        :param body: The body of this StopSimCardRequest.
        :type body: :class:`huaweicloudsdkgsl.v3.DownUpTimeForSimCardReq`
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
        if not isinstance(other, StopSimCardRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
