# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GrantData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'uuid': 'str',
        'resource_id': 'str',
        'type': 'str',
        'grantee_user': 'str',
        'create_time': 'int',
        'update_time': 'int',
        'validity_time': 'int',
        'state': 'int',
        'signature': 'str'
    }

    attribute_map = {
        'uuid': 'uuid',
        'resource_id': 'resourceId',
        'type': 'type',
        'grantee_user': 'granteeUser',
        'create_time': 'createTime',
        'update_time': 'updateTime',
        'validity_time': 'validityTime',
        'state': 'state',
        'signature': 'signature'
    }

    def __init__(self, uuid=None, resource_id=None, type=None, grantee_user=None, create_time=None, update_time=None, validity_time=None, state=None, signature=None):
        r"""GrantData

        The model defined in huaweicloud sdk

        :param uuid: 授权id，授权给个人时存在
        :type uuid: str
        :param resource_id: 资源id
        :type resource_id: str
        :param type: 授权类型（SECRET，GROUP）
        :type type: str
        :param grantee_user: 授权目标用户id
        :type grantee_user: str
        :param create_time: 创建时间
        :type create_time: int
        :param update_time: 更新时间
        :type update_time: int
        :param validity_time: 有效期
        :type validity_time: int
        :param state: 状态
        :type state: int
        :param signature: 签名
        :type signature: str
        """
        
        

        self._uuid = None
        self._resource_id = None
        self._type = None
        self._grantee_user = None
        self._create_time = None
        self._update_time = None
        self._validity_time = None
        self._state = None
        self._signature = None
        self.discriminator = None

        self.uuid = uuid
        self.resource_id = resource_id
        self.type = type
        self.grantee_user = grantee_user
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if validity_time is not None:
            self.validity_time = validity_time
        if state is not None:
            self.state = state
        if signature is not None:
            self.signature = signature

    @property
    def uuid(self):
        r"""Gets the uuid of this GrantData.

        授权id，授权给个人时存在

        :return: The uuid of this GrantData.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        r"""Sets the uuid of this GrantData.

        授权id，授权给个人时存在

        :param uuid: The uuid of this GrantData.
        :type uuid: str
        """
        self._uuid = uuid

    @property
    def resource_id(self):
        r"""Gets the resource_id of this GrantData.

        资源id

        :return: The resource_id of this GrantData.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this GrantData.

        资源id

        :param resource_id: The resource_id of this GrantData.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def type(self):
        r"""Gets the type of this GrantData.

        授权类型（SECRET，GROUP）

        :return: The type of this GrantData.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this GrantData.

        授权类型（SECRET，GROUP）

        :param type: The type of this GrantData.
        :type type: str
        """
        self._type = type

    @property
    def grantee_user(self):
        r"""Gets the grantee_user of this GrantData.

        授权目标用户id

        :return: The grantee_user of this GrantData.
        :rtype: str
        """
        return self._grantee_user

    @grantee_user.setter
    def grantee_user(self, grantee_user):
        r"""Sets the grantee_user of this GrantData.

        授权目标用户id

        :param grantee_user: The grantee_user of this GrantData.
        :type grantee_user: str
        """
        self._grantee_user = grantee_user

    @property
    def create_time(self):
        r"""Gets the create_time of this GrantData.

        创建时间

        :return: The create_time of this GrantData.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this GrantData.

        创建时间

        :param create_time: The create_time of this GrantData.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this GrantData.

        更新时间

        :return: The update_time of this GrantData.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this GrantData.

        更新时间

        :param update_time: The update_time of this GrantData.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def validity_time(self):
        r"""Gets the validity_time of this GrantData.

        有效期

        :return: The validity_time of this GrantData.
        :rtype: int
        """
        return self._validity_time

    @validity_time.setter
    def validity_time(self, validity_time):
        r"""Sets the validity_time of this GrantData.

        有效期

        :param validity_time: The validity_time of this GrantData.
        :type validity_time: int
        """
        self._validity_time = validity_time

    @property
    def state(self):
        r"""Gets the state of this GrantData.

        状态

        :return: The state of this GrantData.
        :rtype: int
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this GrantData.

        状态

        :param state: The state of this GrantData.
        :type state: int
        """
        self._state = state

    @property
    def signature(self):
        r"""Gets the signature of this GrantData.

        签名

        :return: The signature of this GrantData.
        :rtype: str
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        r"""Sets the signature of this GrantData.

        签名

        :param signature: The signature of this GrantData.
        :type signature: str
        """
        self._signature = signature

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
        if not isinstance(other, GrantData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
