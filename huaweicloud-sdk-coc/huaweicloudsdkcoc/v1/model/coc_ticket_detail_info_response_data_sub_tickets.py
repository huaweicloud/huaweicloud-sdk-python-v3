# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CocTicketDetailInfoResponseDataSubTickets:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'change_ticket_id': 'str',
        'change_ticket_id_sub': 'str',
        'whether_to_change': 'bool',
        'is_deleted': 'bool',
        'id': 'str',
        'main_ticket_id': 'str',
        'parent_ticket_id': 'str',
        'ticket_id': 'str',
        'real_ticket_id': 'str',
        'ticket_path': 'str',
        'target_value': 'str',
        'target_type': 'str',
        'create_time': 'int',
        'update_time': 'int',
        'creator': 'str',
        'operator': 'str'
    }

    attribute_map = {
        'change_ticket_id': 'change_ticket_id',
        'change_ticket_id_sub': 'change_ticket_id_sub',
        'whether_to_change': 'whether_to_change',
        'is_deleted': 'is_deleted',
        'id': 'id',
        'main_ticket_id': 'main_ticket_id',
        'parent_ticket_id': 'parent_ticket_id',
        'ticket_id': 'ticket_id',
        'real_ticket_id': 'real_ticket_id',
        'ticket_path': 'ticket_path',
        'target_value': 'target_value',
        'target_type': 'target_type',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'creator': 'creator',
        'operator': 'operator'
    }

    def __init__(self, change_ticket_id=None, change_ticket_id_sub=None, whether_to_change=None, is_deleted=None, id=None, main_ticket_id=None, parent_ticket_id=None, ticket_id=None, real_ticket_id=None, ticket_path=None, target_value=None, target_type=None, create_time=None, update_time=None, creator=None, operator=None):
        r"""CocTicketDetailInfoResponseDataSubTickets

        The model defined in huaweicloud sdk

        :param change_ticket_id: 变更单单号。
        :type change_ticket_id: str
        :param change_ticket_id_sub: 变更子单单号。
        :type change_ticket_id_sub: str
        :param whether_to_change: 是否需要变更。
        :type whether_to_change: bool
        :param is_deleted: 是否已删除。
        :type is_deleted: bool
        :param id: 变更工单ID
        :type id: str
        :param main_ticket_id: 变更工单主键ID。
        :type main_ticket_id: str
        :param parent_ticket_id: 父级工单ID。
        :type parent_ticket_id: str
        :param ticket_id: 问题单ID。
        :type ticket_id: str
        :param real_ticket_id: 问题单单号。
        :type real_ticket_id: str
        :param ticket_path: 工单路径。
        :type ticket_path: str
        :param target_value: region信息。
        :type target_value: str
        :param target_type: 子单类型。
        :type target_type: str
        :param create_time: 创建时间。
        :type create_time: int
        :param update_time: 更新时间。
        :type update_time: int
        :param creator: 创单人。
        :type creator: str
        :param operator: 操作人。
        :type operator: str
        """
        
        

        self._change_ticket_id = None
        self._change_ticket_id_sub = None
        self._whether_to_change = None
        self._is_deleted = None
        self._id = None
        self._main_ticket_id = None
        self._parent_ticket_id = None
        self._ticket_id = None
        self._real_ticket_id = None
        self._ticket_path = None
        self._target_value = None
        self._target_type = None
        self._create_time = None
        self._update_time = None
        self._creator = None
        self._operator = None
        self.discriminator = None

        if change_ticket_id is not None:
            self.change_ticket_id = change_ticket_id
        if change_ticket_id_sub is not None:
            self.change_ticket_id_sub = change_ticket_id_sub
        if whether_to_change is not None:
            self.whether_to_change = whether_to_change
        if is_deleted is not None:
            self.is_deleted = is_deleted
        if id is not None:
            self.id = id
        if main_ticket_id is not None:
            self.main_ticket_id = main_ticket_id
        if parent_ticket_id is not None:
            self.parent_ticket_id = parent_ticket_id
        if ticket_id is not None:
            self.ticket_id = ticket_id
        if real_ticket_id is not None:
            self.real_ticket_id = real_ticket_id
        if ticket_path is not None:
            self.ticket_path = ticket_path
        if target_value is not None:
            self.target_value = target_value
        if target_type is not None:
            self.target_type = target_type
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if creator is not None:
            self.creator = creator
        if operator is not None:
            self.operator = operator

    @property
    def change_ticket_id(self):
        r"""Gets the change_ticket_id of this CocTicketDetailInfoResponseDataSubTickets.

        变更单单号。

        :return: The change_ticket_id of this CocTicketDetailInfoResponseDataSubTickets.
        :rtype: str
        """
        return self._change_ticket_id

    @change_ticket_id.setter
    def change_ticket_id(self, change_ticket_id):
        r"""Sets the change_ticket_id of this CocTicketDetailInfoResponseDataSubTickets.

        变更单单号。

        :param change_ticket_id: The change_ticket_id of this CocTicketDetailInfoResponseDataSubTickets.
        :type change_ticket_id: str
        """
        self._change_ticket_id = change_ticket_id

    @property
    def change_ticket_id_sub(self):
        r"""Gets the change_ticket_id_sub of this CocTicketDetailInfoResponseDataSubTickets.

        变更子单单号。

        :return: The change_ticket_id_sub of this CocTicketDetailInfoResponseDataSubTickets.
        :rtype: str
        """
        return self._change_ticket_id_sub

    @change_ticket_id_sub.setter
    def change_ticket_id_sub(self, change_ticket_id_sub):
        r"""Sets the change_ticket_id_sub of this CocTicketDetailInfoResponseDataSubTickets.

        变更子单单号。

        :param change_ticket_id_sub: The change_ticket_id_sub of this CocTicketDetailInfoResponseDataSubTickets.
        :type change_ticket_id_sub: str
        """
        self._change_ticket_id_sub = change_ticket_id_sub

    @property
    def whether_to_change(self):
        r"""Gets the whether_to_change of this CocTicketDetailInfoResponseDataSubTickets.

        是否需要变更。

        :return: The whether_to_change of this CocTicketDetailInfoResponseDataSubTickets.
        :rtype: bool
        """
        return self._whether_to_change

    @whether_to_change.setter
    def whether_to_change(self, whether_to_change):
        r"""Sets the whether_to_change of this CocTicketDetailInfoResponseDataSubTickets.

        是否需要变更。

        :param whether_to_change: The whether_to_change of this CocTicketDetailInfoResponseDataSubTickets.
        :type whether_to_change: bool
        """
        self._whether_to_change = whether_to_change

    @property
    def is_deleted(self):
        r"""Gets the is_deleted of this CocTicketDetailInfoResponseDataSubTickets.

        是否已删除。

        :return: The is_deleted of this CocTicketDetailInfoResponseDataSubTickets.
        :rtype: bool
        """
        return self._is_deleted

    @is_deleted.setter
    def is_deleted(self, is_deleted):
        r"""Sets the is_deleted of this CocTicketDetailInfoResponseDataSubTickets.

        是否已删除。

        :param is_deleted: The is_deleted of this CocTicketDetailInfoResponseDataSubTickets.
        :type is_deleted: bool
        """
        self._is_deleted = is_deleted

    @property
    def id(self):
        r"""Gets the id of this CocTicketDetailInfoResponseDataSubTickets.

        变更工单ID

        :return: The id of this CocTicketDetailInfoResponseDataSubTickets.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CocTicketDetailInfoResponseDataSubTickets.

        变更工单ID

        :param id: The id of this CocTicketDetailInfoResponseDataSubTickets.
        :type id: str
        """
        self._id = id

    @property
    def main_ticket_id(self):
        r"""Gets the main_ticket_id of this CocTicketDetailInfoResponseDataSubTickets.

        变更工单主键ID。

        :return: The main_ticket_id of this CocTicketDetailInfoResponseDataSubTickets.
        :rtype: str
        """
        return self._main_ticket_id

    @main_ticket_id.setter
    def main_ticket_id(self, main_ticket_id):
        r"""Sets the main_ticket_id of this CocTicketDetailInfoResponseDataSubTickets.

        变更工单主键ID。

        :param main_ticket_id: The main_ticket_id of this CocTicketDetailInfoResponseDataSubTickets.
        :type main_ticket_id: str
        """
        self._main_ticket_id = main_ticket_id

    @property
    def parent_ticket_id(self):
        r"""Gets the parent_ticket_id of this CocTicketDetailInfoResponseDataSubTickets.

        父级工单ID。

        :return: The parent_ticket_id of this CocTicketDetailInfoResponseDataSubTickets.
        :rtype: str
        """
        return self._parent_ticket_id

    @parent_ticket_id.setter
    def parent_ticket_id(self, parent_ticket_id):
        r"""Sets the parent_ticket_id of this CocTicketDetailInfoResponseDataSubTickets.

        父级工单ID。

        :param parent_ticket_id: The parent_ticket_id of this CocTicketDetailInfoResponseDataSubTickets.
        :type parent_ticket_id: str
        """
        self._parent_ticket_id = parent_ticket_id

    @property
    def ticket_id(self):
        r"""Gets the ticket_id of this CocTicketDetailInfoResponseDataSubTickets.

        问题单ID。

        :return: The ticket_id of this CocTicketDetailInfoResponseDataSubTickets.
        :rtype: str
        """
        return self._ticket_id

    @ticket_id.setter
    def ticket_id(self, ticket_id):
        r"""Sets the ticket_id of this CocTicketDetailInfoResponseDataSubTickets.

        问题单ID。

        :param ticket_id: The ticket_id of this CocTicketDetailInfoResponseDataSubTickets.
        :type ticket_id: str
        """
        self._ticket_id = ticket_id

    @property
    def real_ticket_id(self):
        r"""Gets the real_ticket_id of this CocTicketDetailInfoResponseDataSubTickets.

        问题单单号。

        :return: The real_ticket_id of this CocTicketDetailInfoResponseDataSubTickets.
        :rtype: str
        """
        return self._real_ticket_id

    @real_ticket_id.setter
    def real_ticket_id(self, real_ticket_id):
        r"""Sets the real_ticket_id of this CocTicketDetailInfoResponseDataSubTickets.

        问题单单号。

        :param real_ticket_id: The real_ticket_id of this CocTicketDetailInfoResponseDataSubTickets.
        :type real_ticket_id: str
        """
        self._real_ticket_id = real_ticket_id

    @property
    def ticket_path(self):
        r"""Gets the ticket_path of this CocTicketDetailInfoResponseDataSubTickets.

        工单路径。

        :return: The ticket_path of this CocTicketDetailInfoResponseDataSubTickets.
        :rtype: str
        """
        return self._ticket_path

    @ticket_path.setter
    def ticket_path(self, ticket_path):
        r"""Sets the ticket_path of this CocTicketDetailInfoResponseDataSubTickets.

        工单路径。

        :param ticket_path: The ticket_path of this CocTicketDetailInfoResponseDataSubTickets.
        :type ticket_path: str
        """
        self._ticket_path = ticket_path

    @property
    def target_value(self):
        r"""Gets the target_value of this CocTicketDetailInfoResponseDataSubTickets.

        region信息。

        :return: The target_value of this CocTicketDetailInfoResponseDataSubTickets.
        :rtype: str
        """
        return self._target_value

    @target_value.setter
    def target_value(self, target_value):
        r"""Sets the target_value of this CocTicketDetailInfoResponseDataSubTickets.

        region信息。

        :param target_value: The target_value of this CocTicketDetailInfoResponseDataSubTickets.
        :type target_value: str
        """
        self._target_value = target_value

    @property
    def target_type(self):
        r"""Gets the target_type of this CocTicketDetailInfoResponseDataSubTickets.

        子单类型。

        :return: The target_type of this CocTicketDetailInfoResponseDataSubTickets.
        :rtype: str
        """
        return self._target_type

    @target_type.setter
    def target_type(self, target_type):
        r"""Sets the target_type of this CocTicketDetailInfoResponseDataSubTickets.

        子单类型。

        :param target_type: The target_type of this CocTicketDetailInfoResponseDataSubTickets.
        :type target_type: str
        """
        self._target_type = target_type

    @property
    def create_time(self):
        r"""Gets the create_time of this CocTicketDetailInfoResponseDataSubTickets.

        创建时间。

        :return: The create_time of this CocTicketDetailInfoResponseDataSubTickets.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this CocTicketDetailInfoResponseDataSubTickets.

        创建时间。

        :param create_time: The create_time of this CocTicketDetailInfoResponseDataSubTickets.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this CocTicketDetailInfoResponseDataSubTickets.

        更新时间。

        :return: The update_time of this CocTicketDetailInfoResponseDataSubTickets.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this CocTicketDetailInfoResponseDataSubTickets.

        更新时间。

        :param update_time: The update_time of this CocTicketDetailInfoResponseDataSubTickets.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def creator(self):
        r"""Gets the creator of this CocTicketDetailInfoResponseDataSubTickets.

        创单人。

        :return: The creator of this CocTicketDetailInfoResponseDataSubTickets.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this CocTicketDetailInfoResponseDataSubTickets.

        创单人。

        :param creator: The creator of this CocTicketDetailInfoResponseDataSubTickets.
        :type creator: str
        """
        self._creator = creator

    @property
    def operator(self):
        r"""Gets the operator of this CocTicketDetailInfoResponseDataSubTickets.

        操作人。

        :return: The operator of this CocTicketDetailInfoResponseDataSubTickets.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        r"""Sets the operator of this CocTicketDetailInfoResponseDataSubTickets.

        操作人。

        :param operator: The operator of this CocTicketDetailInfoResponseDataSubTickets.
        :type operator: str
        """
        self._operator = operator

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
        if not isinstance(other, CocTicketDetailInfoResponseDataSubTickets):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
