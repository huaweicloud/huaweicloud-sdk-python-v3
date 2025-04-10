# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateInstanceUserRequest:

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
        'instance_id': 'str',
        'user_name': 'str',
        'body': 'UpdateUserReq'
    }

    attribute_map = {
        'engine': 'engine',
        'instance_id': 'instance_id',
        'user_name': 'user_name',
        'body': 'body'
    }

    def __init__(self, engine=None, instance_id=None, user_name=None, body=None):
        r"""UpdateInstanceUserRequest

        The model defined in huaweicloud sdk

        :param engine: 消息引擎的类型。
        :type engine: str
        :param instance_id: 实例ID。
        :type instance_id: str
        :param user_name: 用户名称。
        :type user_name: str
        :param body: Body of the UpdateInstanceUserRequest
        :type body: :class:`huaweicloudsdkkafka.v2.UpdateUserReq`
        """
        
        

        self._engine = None
        self._instance_id = None
        self._user_name = None
        self._body = None
        self.discriminator = None

        self.engine = engine
        self.instance_id = instance_id
        self.user_name = user_name
        if body is not None:
            self.body = body

    @property
    def engine(self):
        r"""Gets the engine of this UpdateInstanceUserRequest.

        消息引擎的类型。

        :return: The engine of this UpdateInstanceUserRequest.
        :rtype: str
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        r"""Sets the engine of this UpdateInstanceUserRequest.

        消息引擎的类型。

        :param engine: The engine of this UpdateInstanceUserRequest.
        :type engine: str
        """
        self._engine = engine

    @property
    def instance_id(self):
        r"""Gets the instance_id of this UpdateInstanceUserRequest.

        实例ID。

        :return: The instance_id of this UpdateInstanceUserRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this UpdateInstanceUserRequest.

        实例ID。

        :param instance_id: The instance_id of this UpdateInstanceUserRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def user_name(self):
        r"""Gets the user_name of this UpdateInstanceUserRequest.

        用户名称。

        :return: The user_name of this UpdateInstanceUserRequest.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this UpdateInstanceUserRequest.

        用户名称。

        :param user_name: The user_name of this UpdateInstanceUserRequest.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def body(self):
        r"""Gets the body of this UpdateInstanceUserRequest.

        :return: The body of this UpdateInstanceUserRequest.
        :rtype: :class:`huaweicloudsdkkafka.v2.UpdateUserReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateInstanceUserRequest.

        :param body: The body of this UpdateInstanceUserRequest.
        :type body: :class:`huaweicloudsdkkafka.v2.UpdateUserReq`
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
        if not isinstance(other, UpdateInstanceUserRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
