# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MicroServiceInfoCSEBase:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'engine_id': 'str',
        'service_id': 'str'
    }

    attribute_map = {
        'engine_id': 'engine_id',
        'service_id': 'service_id'
    }

    def __init__(self, engine_id=None, service_id=None):
        r"""MicroServiceInfoCSEBase

        The model defined in huaweicloud sdk

        :param engine_id: 微服务引擎编号
        :type engine_id: str
        :param service_id: 微服务编号
        :type service_id: str
        """
        
        

        self._engine_id = None
        self._service_id = None
        self.discriminator = None

        self.engine_id = engine_id
        self.service_id = service_id

    @property
    def engine_id(self):
        r"""Gets the engine_id of this MicroServiceInfoCSEBase.

        微服务引擎编号

        :return: The engine_id of this MicroServiceInfoCSEBase.
        :rtype: str
        """
        return self._engine_id

    @engine_id.setter
    def engine_id(self, engine_id):
        r"""Sets the engine_id of this MicroServiceInfoCSEBase.

        微服务引擎编号

        :param engine_id: The engine_id of this MicroServiceInfoCSEBase.
        :type engine_id: str
        """
        self._engine_id = engine_id

    @property
    def service_id(self):
        r"""Gets the service_id of this MicroServiceInfoCSEBase.

        微服务编号

        :return: The service_id of this MicroServiceInfoCSEBase.
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        r"""Sets the service_id of this MicroServiceInfoCSEBase.

        微服务编号

        :param service_id: The service_id of this MicroServiceInfoCSEBase.
        :type service_id: str
        """
        self._service_id = service_id

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
        if not isinstance(other, MicroServiceInfoCSEBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
