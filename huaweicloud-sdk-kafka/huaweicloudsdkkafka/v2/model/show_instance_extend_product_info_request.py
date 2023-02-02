# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowInstanceExtendProductInfoRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'type': 'str',
        'engine': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'type': 'type',
        'engine': 'engine'
    }

    def __init__(self, instance_id=None, type=None, engine=None):
        """ShowInstanceExtendProductInfoRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID。
        :type instance_id: str
        :param type: [产品的类型。 - advanced: 专享版 - platinum: 铂金版 - dec: 专属云版 - exp: 体验版](tag:hc,hk,hws,hws_hk,ctc,sbc,hk_sbc,cmcc,hws_eu)
        :type type: str
        :param engine: 消息引擎的类型。当前支持的类型为kafka。
        :type engine: str
        """
        
        

        self._instance_id = None
        self._type = None
        self._engine = None
        self.discriminator = None

        self.instance_id = instance_id
        self.type = type
        self.engine = engine

    @property
    def instance_id(self):
        """Gets the instance_id of this ShowInstanceExtendProductInfoRequest.

        实例ID。

        :return: The instance_id of this ShowInstanceExtendProductInfoRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ShowInstanceExtendProductInfoRequest.

        实例ID。

        :param instance_id: The instance_id of this ShowInstanceExtendProductInfoRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def type(self):
        """Gets the type of this ShowInstanceExtendProductInfoRequest.

        [产品的类型。 - advanced: 专享版 - platinum: 铂金版 - dec: 专属云版 - exp: 体验版](tag:hc,hk,hws,hws_hk,ctc,sbc,hk_sbc,cmcc,hws_eu)

        :return: The type of this ShowInstanceExtendProductInfoRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShowInstanceExtendProductInfoRequest.

        [产品的类型。 - advanced: 专享版 - platinum: 铂金版 - dec: 专属云版 - exp: 体验版](tag:hc,hk,hws,hws_hk,ctc,sbc,hk_sbc,cmcc,hws_eu)

        :param type: The type of this ShowInstanceExtendProductInfoRequest.
        :type type: str
        """
        self._type = type

    @property
    def engine(self):
        """Gets the engine of this ShowInstanceExtendProductInfoRequest.

        消息引擎的类型。当前支持的类型为kafka。

        :return: The engine of this ShowInstanceExtendProductInfoRequest.
        :rtype: str
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        """Sets the engine of this ShowInstanceExtendProductInfoRequest.

        消息引擎的类型。当前支持的类型为kafka。

        :param engine: The engine of this ShowInstanceExtendProductInfoRequest.
        :type engine: str
        """
        self._engine = engine

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
        if not isinstance(other, ShowInstanceExtendProductInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
