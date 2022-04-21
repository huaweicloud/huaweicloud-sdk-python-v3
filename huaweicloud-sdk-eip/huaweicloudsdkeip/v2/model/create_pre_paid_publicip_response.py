# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePrePaidPublicipResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'publicip': 'PublicipCreateResp',
        'order_id': 'str',
        'publicip_id': 'str'
    }

    attribute_map = {
        'publicip': 'publicip',
        'order_id': 'order_id',
        'publicip_id': 'publicip_id'
    }

    def __init__(self, publicip=None, order_id=None, publicip_id=None):
        """CreatePrePaidPublicipResponse

        The model defined in huaweicloud sdk

        :param publicip: 
        :type publicip: :class:`huaweicloudsdkeip.v2.PublicipCreateResp`
        :param order_id: 订单号（预付费场景返回该字段）
        :type order_id: str
        :param publicip_id: 弹性公网IP的ID（预付费场景返回该字段）
        :type publicip_id: str
        """
        
        super(CreatePrePaidPublicipResponse, self).__init__()

        self._publicip = None
        self._order_id = None
        self._publicip_id = None
        self.discriminator = None

        if publicip is not None:
            self.publicip = publicip
        if order_id is not None:
            self.order_id = order_id
        if publicip_id is not None:
            self.publicip_id = publicip_id

    @property
    def publicip(self):
        """Gets the publicip of this CreatePrePaidPublicipResponse.


        :return: The publicip of this CreatePrePaidPublicipResponse.
        :rtype: :class:`huaweicloudsdkeip.v2.PublicipCreateResp`
        """
        return self._publicip

    @publicip.setter
    def publicip(self, publicip):
        """Sets the publicip of this CreatePrePaidPublicipResponse.


        :param publicip: The publicip of this CreatePrePaidPublicipResponse.
        :type publicip: :class:`huaweicloudsdkeip.v2.PublicipCreateResp`
        """
        self._publicip = publicip

    @property
    def order_id(self):
        """Gets the order_id of this CreatePrePaidPublicipResponse.

        订单号（预付费场景返回该字段）

        :return: The order_id of this CreatePrePaidPublicipResponse.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this CreatePrePaidPublicipResponse.

        订单号（预付费场景返回该字段）

        :param order_id: The order_id of this CreatePrePaidPublicipResponse.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def publicip_id(self):
        """Gets the publicip_id of this CreatePrePaidPublicipResponse.

        弹性公网IP的ID（预付费场景返回该字段）

        :return: The publicip_id of this CreatePrePaidPublicipResponse.
        :rtype: str
        """
        return self._publicip_id

    @publicip_id.setter
    def publicip_id(self, publicip_id):
        """Sets the publicip_id of this CreatePrePaidPublicipResponse.

        弹性公网IP的ID（预付费场景返回该字段）

        :param publicip_id: The publicip_id of this CreatePrePaidPublicipResponse.
        :type publicip_id: str
        """
        self._publicip_id = publicip_id

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
        if not isinstance(other, CreatePrePaidPublicipResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
