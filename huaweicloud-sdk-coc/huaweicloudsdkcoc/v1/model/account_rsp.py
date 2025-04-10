# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccountRsp:

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
        'name': 'str',
        'type': 'str',
        'delegatee': 'str',
        'agency_id': 'str',
        'delegator': 'str',
        'create_user_name': 'str',
        'status': 'str',
        'create_user_id': 'str',
        'create_time': 'str',
        'update_user_name': 'str',
        'update_user_id': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'delegatee': 'delegatee',
        'agency_id': 'agency_id',
        'delegator': 'delegator',
        'create_user_name': 'create_user_name',
        'status': 'status',
        'create_user_id': 'create_user_id',
        'create_time': 'create_time',
        'update_user_name': 'update_user_name',
        'update_user_id': 'update_user_id',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, name=None, type=None, delegatee=None, agency_id=None, delegator=None, create_user_name=None, status=None, create_user_id=None, create_time=None, update_user_name=None, update_user_id=None, update_time=None):
        r"""AccountRsp

        The model defined in huaweicloud sdk

        :param id: id
        :type id: str
        :param name: 名称
        :type name: str
        :param type: 账号类型 NORMAL 普通账号，停用状态 DELEGATOR 委托人 DELEGATEE 被委托人
        :type type: str
        :param delegatee: 被委托人id
        :type delegatee: str
        :param agency_id: 委托id
        :type agency_id: str
        :param delegator: 托管账号Id
        :type delegator: str
        :param create_user_name: 创建人
        :type create_user_name: str
        :param status: PENDING_AUTHORIZATION, 待授权,ENABLED 启用, DISABLED 停用
        :type status: str
        :param create_user_id: 创建userId
        :type create_user_id: str
        :param create_time: 创建时间
        :type create_time: str
        :param update_user_name: 编辑人
        :type update_user_name: str
        :param update_user_id: 编辑人user_id
        :type update_user_id: str
        :param update_time: 编辑时间，期初和创建时间一样
        :type update_time: str
        """
        
        

        self._id = None
        self._name = None
        self._type = None
        self._delegatee = None
        self._agency_id = None
        self._delegator = None
        self._create_user_name = None
        self._status = None
        self._create_user_id = None
        self._create_time = None
        self._update_user_name = None
        self._update_user_id = None
        self._update_time = None
        self.discriminator = None

        self.id = id
        self.name = name
        if type is not None:
            self.type = type
        if delegatee is not None:
            self.delegatee = delegatee
        if agency_id is not None:
            self.agency_id = agency_id
        if delegator is not None:
            self.delegator = delegator
        self.create_user_name = create_user_name
        self.status = status
        self.create_user_id = create_user_id
        self.create_time = create_time
        if update_user_name is not None:
            self.update_user_name = update_user_name
        if update_user_id is not None:
            self.update_user_id = update_user_id
        self.update_time = update_time

    @property
    def id(self):
        r"""Gets the id of this AccountRsp.

        id

        :return: The id of this AccountRsp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AccountRsp.

        id

        :param id: The id of this AccountRsp.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this AccountRsp.

        名称

        :return: The name of this AccountRsp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AccountRsp.

        名称

        :param name: The name of this AccountRsp.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this AccountRsp.

        账号类型 NORMAL 普通账号，停用状态 DELEGATOR 委托人 DELEGATEE 被委托人

        :return: The type of this AccountRsp.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this AccountRsp.

        账号类型 NORMAL 普通账号，停用状态 DELEGATOR 委托人 DELEGATEE 被委托人

        :param type: The type of this AccountRsp.
        :type type: str
        """
        self._type = type

    @property
    def delegatee(self):
        r"""Gets the delegatee of this AccountRsp.

        被委托人id

        :return: The delegatee of this AccountRsp.
        :rtype: str
        """
        return self._delegatee

    @delegatee.setter
    def delegatee(self, delegatee):
        r"""Sets the delegatee of this AccountRsp.

        被委托人id

        :param delegatee: The delegatee of this AccountRsp.
        :type delegatee: str
        """
        self._delegatee = delegatee

    @property
    def agency_id(self):
        r"""Gets the agency_id of this AccountRsp.

        委托id

        :return: The agency_id of this AccountRsp.
        :rtype: str
        """
        return self._agency_id

    @agency_id.setter
    def agency_id(self, agency_id):
        r"""Sets the agency_id of this AccountRsp.

        委托id

        :param agency_id: The agency_id of this AccountRsp.
        :type agency_id: str
        """
        self._agency_id = agency_id

    @property
    def delegator(self):
        r"""Gets the delegator of this AccountRsp.

        托管账号Id

        :return: The delegator of this AccountRsp.
        :rtype: str
        """
        return self._delegator

    @delegator.setter
    def delegator(self, delegator):
        r"""Sets the delegator of this AccountRsp.

        托管账号Id

        :param delegator: The delegator of this AccountRsp.
        :type delegator: str
        """
        self._delegator = delegator

    @property
    def create_user_name(self):
        r"""Gets the create_user_name of this AccountRsp.

        创建人

        :return: The create_user_name of this AccountRsp.
        :rtype: str
        """
        return self._create_user_name

    @create_user_name.setter
    def create_user_name(self, create_user_name):
        r"""Sets the create_user_name of this AccountRsp.

        创建人

        :param create_user_name: The create_user_name of this AccountRsp.
        :type create_user_name: str
        """
        self._create_user_name = create_user_name

    @property
    def status(self):
        r"""Gets the status of this AccountRsp.

        PENDING_AUTHORIZATION, 待授权,ENABLED 启用, DISABLED 停用

        :return: The status of this AccountRsp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this AccountRsp.

        PENDING_AUTHORIZATION, 待授权,ENABLED 启用, DISABLED 停用

        :param status: The status of this AccountRsp.
        :type status: str
        """
        self._status = status

    @property
    def create_user_id(self):
        r"""Gets the create_user_id of this AccountRsp.

        创建userId

        :return: The create_user_id of this AccountRsp.
        :rtype: str
        """
        return self._create_user_id

    @create_user_id.setter
    def create_user_id(self, create_user_id):
        r"""Sets the create_user_id of this AccountRsp.

        创建userId

        :param create_user_id: The create_user_id of this AccountRsp.
        :type create_user_id: str
        """
        self._create_user_id = create_user_id

    @property
    def create_time(self):
        r"""Gets the create_time of this AccountRsp.

        创建时间

        :return: The create_time of this AccountRsp.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this AccountRsp.

        创建时间

        :param create_time: The create_time of this AccountRsp.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_user_name(self):
        r"""Gets the update_user_name of this AccountRsp.

        编辑人

        :return: The update_user_name of this AccountRsp.
        :rtype: str
        """
        return self._update_user_name

    @update_user_name.setter
    def update_user_name(self, update_user_name):
        r"""Sets the update_user_name of this AccountRsp.

        编辑人

        :param update_user_name: The update_user_name of this AccountRsp.
        :type update_user_name: str
        """
        self._update_user_name = update_user_name

    @property
    def update_user_id(self):
        r"""Gets the update_user_id of this AccountRsp.

        编辑人user_id

        :return: The update_user_id of this AccountRsp.
        :rtype: str
        """
        return self._update_user_id

    @update_user_id.setter
    def update_user_id(self, update_user_id):
        r"""Sets the update_user_id of this AccountRsp.

        编辑人user_id

        :param update_user_id: The update_user_id of this AccountRsp.
        :type update_user_id: str
        """
        self._update_user_id = update_user_id

    @property
    def update_time(self):
        r"""Gets the update_time of this AccountRsp.

        编辑时间，期初和创建时间一样

        :return: The update_time of this AccountRsp.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this AccountRsp.

        编辑时间，期初和创建时间一样

        :param update_time: The update_time of this AccountRsp.
        :type update_time: str
        """
        self._update_time = update_time

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
        if not isinstance(other, AccountRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
