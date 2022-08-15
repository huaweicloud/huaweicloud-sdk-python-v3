# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePostPaidInstanceByEngineRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'engine': 'str',
        'body': 'CreateInstanceReq'
    }

    attribute_map = {
        'engine': 'engine',
        'body': 'body'
    }

    def __init__(self, engine=None, body=None):
        """CreatePostPaidInstanceByEngineRequest

        The model defined in huaweicloud sdk

        :param engine: 消息引擎。
        :type engine: str
        :param body: Body of the CreatePostPaidInstanceByEngineRequest
        :type body: :class:`huaweicloudsdkrabbitmq.v2.CreateInstanceReq`
        """
        
        

        self._engine = None
        self._body = None
        self.discriminator = None

        self.engine = engine
        if body is not None:
            self.body = body

    @property
    def engine(self):
        """Gets the engine of this CreatePostPaidInstanceByEngineRequest.

        消息引擎。

        :return: The engine of this CreatePostPaidInstanceByEngineRequest.
        :rtype: str
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        """Sets the engine of this CreatePostPaidInstanceByEngineRequest.

        消息引擎。

        :param engine: The engine of this CreatePostPaidInstanceByEngineRequest.
        :type engine: str
        """
        self._engine = engine

    @property
    def body(self):
        """Gets the body of this CreatePostPaidInstanceByEngineRequest.


        :return: The body of this CreatePostPaidInstanceByEngineRequest.
        :rtype: :class:`huaweicloudsdkrabbitmq.v2.CreateInstanceReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CreatePostPaidInstanceByEngineRequest.


        :param body: The body of this CreatePostPaidInstanceByEngineRequest.
        :type body: :class:`huaweicloudsdkrabbitmq.v2.CreateInstanceReq`
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
        if not isinstance(other, CreatePostPaidInstanceByEngineRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
