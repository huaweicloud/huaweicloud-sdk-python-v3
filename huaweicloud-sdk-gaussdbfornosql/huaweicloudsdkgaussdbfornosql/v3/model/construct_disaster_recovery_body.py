# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConstructDisasterRecoveryBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'alias': 'str',
        'password': 'str',
        'instance_role': 'str',
        'disaster_recovery_instance': 'ConstructDisasterRecoveryInstance'
    }

    attribute_map = {
        'id': 'id',
        'alias': 'alias',
        'password': 'password',
        'instance_role': 'instance_role',
        'disaster_recovery_instance': 'disaster_recovery_instance'
    }

    def __init__(self, id=None, alias=None, password=None, instance_role=None, disaster_recovery_instance=None):
        """ConstructDisasterRecoveryBody

        The model defined in huaweicloud sdk

        :param id: 容灾ID。 对容灾角色为主的实例下发搭建容灾接口时不传该参数，接口成功响应后返回生成的容灾ID。 对容灾角色为备的实例下发建容灾接口时必传该参数，且必须与上述生成的容灾ID保持一致。
        :type id: str
        :param alias: 搭建容灾关系的别名。
        :type alias: str
        :param password: 建立容灾关系所需要的容灾密码，搭建同一容灾关系的两次调用容灾密码必须保持一致。 容灾密码为容灾集群内部数据通信所用，不能用于客户端连接使用。
        :type password: str
        :param instance_role: 指定当前实例的容灾角色。取值为master或slave，表示在容灾关系中角色为主或备。
        :type instance_role: str
        :param disaster_recovery_instance: 
        :type disaster_recovery_instance: :class:`huaweicloudsdkgaussdbfornosql.v3.ConstructDisasterRecoveryInstance`
        """
        
        

        self._id = None
        self._alias = None
        self._password = None
        self._instance_role = None
        self._disaster_recovery_instance = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.alias = alias
        self.password = password
        self.instance_role = instance_role
        self.disaster_recovery_instance = disaster_recovery_instance

    @property
    def id(self):
        """Gets the id of this ConstructDisasterRecoveryBody.

        容灾ID。 对容灾角色为主的实例下发搭建容灾接口时不传该参数，接口成功响应后返回生成的容灾ID。 对容灾角色为备的实例下发建容灾接口时必传该参数，且必须与上述生成的容灾ID保持一致。

        :return: The id of this ConstructDisasterRecoveryBody.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ConstructDisasterRecoveryBody.

        容灾ID。 对容灾角色为主的实例下发搭建容灾接口时不传该参数，接口成功响应后返回生成的容灾ID。 对容灾角色为备的实例下发建容灾接口时必传该参数，且必须与上述生成的容灾ID保持一致。

        :param id: The id of this ConstructDisasterRecoveryBody.
        :type id: str
        """
        self._id = id

    @property
    def alias(self):
        """Gets the alias of this ConstructDisasterRecoveryBody.

        搭建容灾关系的别名。

        :return: The alias of this ConstructDisasterRecoveryBody.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this ConstructDisasterRecoveryBody.

        搭建容灾关系的别名。

        :param alias: The alias of this ConstructDisasterRecoveryBody.
        :type alias: str
        """
        self._alias = alias

    @property
    def password(self):
        """Gets the password of this ConstructDisasterRecoveryBody.

        建立容灾关系所需要的容灾密码，搭建同一容灾关系的两次调用容灾密码必须保持一致。 容灾密码为容灾集群内部数据通信所用，不能用于客户端连接使用。

        :return: The password of this ConstructDisasterRecoveryBody.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this ConstructDisasterRecoveryBody.

        建立容灾关系所需要的容灾密码，搭建同一容灾关系的两次调用容灾密码必须保持一致。 容灾密码为容灾集群内部数据通信所用，不能用于客户端连接使用。

        :param password: The password of this ConstructDisasterRecoveryBody.
        :type password: str
        """
        self._password = password

    @property
    def instance_role(self):
        """Gets the instance_role of this ConstructDisasterRecoveryBody.

        指定当前实例的容灾角色。取值为master或slave，表示在容灾关系中角色为主或备。

        :return: The instance_role of this ConstructDisasterRecoveryBody.
        :rtype: str
        """
        return self._instance_role

    @instance_role.setter
    def instance_role(self, instance_role):
        """Sets the instance_role of this ConstructDisasterRecoveryBody.

        指定当前实例的容灾角色。取值为master或slave，表示在容灾关系中角色为主或备。

        :param instance_role: The instance_role of this ConstructDisasterRecoveryBody.
        :type instance_role: str
        """
        self._instance_role = instance_role

    @property
    def disaster_recovery_instance(self):
        """Gets the disaster_recovery_instance of this ConstructDisasterRecoveryBody.


        :return: The disaster_recovery_instance of this ConstructDisasterRecoveryBody.
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ConstructDisasterRecoveryInstance`
        """
        return self._disaster_recovery_instance

    @disaster_recovery_instance.setter
    def disaster_recovery_instance(self, disaster_recovery_instance):
        """Sets the disaster_recovery_instance of this ConstructDisasterRecoveryBody.


        :param disaster_recovery_instance: The disaster_recovery_instance of this ConstructDisasterRecoveryBody.
        :type disaster_recovery_instance: :class:`huaweicloudsdkgaussdbfornosql.v3.ConstructDisasterRecoveryInstance`
        """
        self._disaster_recovery_instance = disaster_recovery_instance

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
        if not isinstance(other, ConstructDisasterRecoveryBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
