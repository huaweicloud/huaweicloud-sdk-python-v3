# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApiAclInfoWithBindNum:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'acl_name': 'str',
        'acl_type': 'str',
        'acl_value': 'str',
        'bind_num': 'int',
        'entity_type': 'str',
        'id': 'str',
        'update_time': 'datetime'
    }

    attribute_map = {
        'acl_name': 'acl_name',
        'acl_type': 'acl_type',
        'acl_value': 'acl_value',
        'bind_num': 'bind_num',
        'entity_type': 'entity_type',
        'id': 'id',
        'update_time': 'update_time'
    }

    def __init__(self, acl_name=None, acl_type=None, acl_value=None, bind_num=None, entity_type=None, id=None, update_time=None):
        """ApiAclInfoWithBindNum

        The model defined in huaweicloud sdk

        :param acl_name: ACL策略名称
        :type acl_name: str
        :param acl_type: 类型 - PERMIT（白名单类型） - DENY（黑名单类型）
        :type acl_type: str
        :param acl_value: ACL策略的值
        :type acl_value: str
        :param bind_num: 绑定的API数量
        :type bind_num: int
        :param entity_type: 对象类型 - IP - DOMAIN
        :type entity_type: str
        :param id: ACL策略编号
        :type id: str
        :param update_time: 更新时间
        :type update_time: datetime
        """
        
        

        self._acl_name = None
        self._acl_type = None
        self._acl_value = None
        self._bind_num = None
        self._entity_type = None
        self._id = None
        self._update_time = None
        self.discriminator = None

        if acl_name is not None:
            self.acl_name = acl_name
        if acl_type is not None:
            self.acl_type = acl_type
        if acl_value is not None:
            self.acl_value = acl_value
        if bind_num is not None:
            self.bind_num = bind_num
        if entity_type is not None:
            self.entity_type = entity_type
        if id is not None:
            self.id = id
        if update_time is not None:
            self.update_time = update_time

    @property
    def acl_name(self):
        """Gets the acl_name of this ApiAclInfoWithBindNum.

        ACL策略名称

        :return: The acl_name of this ApiAclInfoWithBindNum.
        :rtype: str
        """
        return self._acl_name

    @acl_name.setter
    def acl_name(self, acl_name):
        """Sets the acl_name of this ApiAclInfoWithBindNum.

        ACL策略名称

        :param acl_name: The acl_name of this ApiAclInfoWithBindNum.
        :type acl_name: str
        """
        self._acl_name = acl_name

    @property
    def acl_type(self):
        """Gets the acl_type of this ApiAclInfoWithBindNum.

        类型 - PERMIT（白名单类型） - DENY（黑名单类型）

        :return: The acl_type of this ApiAclInfoWithBindNum.
        :rtype: str
        """
        return self._acl_type

    @acl_type.setter
    def acl_type(self, acl_type):
        """Sets the acl_type of this ApiAclInfoWithBindNum.

        类型 - PERMIT（白名单类型） - DENY（黑名单类型）

        :param acl_type: The acl_type of this ApiAclInfoWithBindNum.
        :type acl_type: str
        """
        self._acl_type = acl_type

    @property
    def acl_value(self):
        """Gets the acl_value of this ApiAclInfoWithBindNum.

        ACL策略的值

        :return: The acl_value of this ApiAclInfoWithBindNum.
        :rtype: str
        """
        return self._acl_value

    @acl_value.setter
    def acl_value(self, acl_value):
        """Sets the acl_value of this ApiAclInfoWithBindNum.

        ACL策略的值

        :param acl_value: The acl_value of this ApiAclInfoWithBindNum.
        :type acl_value: str
        """
        self._acl_value = acl_value

    @property
    def bind_num(self):
        """Gets the bind_num of this ApiAclInfoWithBindNum.

        绑定的API数量

        :return: The bind_num of this ApiAclInfoWithBindNum.
        :rtype: int
        """
        return self._bind_num

    @bind_num.setter
    def bind_num(self, bind_num):
        """Sets the bind_num of this ApiAclInfoWithBindNum.

        绑定的API数量

        :param bind_num: The bind_num of this ApiAclInfoWithBindNum.
        :type bind_num: int
        """
        self._bind_num = bind_num

    @property
    def entity_type(self):
        """Gets the entity_type of this ApiAclInfoWithBindNum.

        对象类型 - IP - DOMAIN

        :return: The entity_type of this ApiAclInfoWithBindNum.
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this ApiAclInfoWithBindNum.

        对象类型 - IP - DOMAIN

        :param entity_type: The entity_type of this ApiAclInfoWithBindNum.
        :type entity_type: str
        """
        self._entity_type = entity_type

    @property
    def id(self):
        """Gets the id of this ApiAclInfoWithBindNum.

        ACL策略编号

        :return: The id of this ApiAclInfoWithBindNum.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApiAclInfoWithBindNum.

        ACL策略编号

        :param id: The id of this ApiAclInfoWithBindNum.
        :type id: str
        """
        self._id = id

    @property
    def update_time(self):
        """Gets the update_time of this ApiAclInfoWithBindNum.

        更新时间

        :return: The update_time of this ApiAclInfoWithBindNum.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ApiAclInfoWithBindNum.

        更新时间

        :param update_time: The update_time of this ApiAclInfoWithBindNum.
        :type update_time: datetime
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
        if not isinstance(other, ApiAclInfoWithBindNum):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
