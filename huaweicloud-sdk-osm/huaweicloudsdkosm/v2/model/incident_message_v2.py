# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IncidentMessageV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'int',
        'replier': 'str',
        'content': 'str',
        'message_id': 'str',
        'replier_name': 'str',
        'create_time': 'datetime',
        'is_first_message': 'int',
        'accessory_list': 'list[SimpleAccessoryV2]'
    }

    attribute_map = {
        'type': 'type',
        'replier': 'replier',
        'content': 'content',
        'message_id': 'message_id',
        'replier_name': 'replier_name',
        'create_time': 'create_time',
        'is_first_message': 'is_first_message',
        'accessory_list': 'accessory_list'
    }

    def __init__(self, type=None, replier=None, content=None, message_id=None, replier_name=None, create_time=None, is_first_message=None, accessory_list=None):
        """IncidentMessageV2

        The model defined in huaweicloud sdk

        :param type: 类型，0客户留言 1华为工程师留言
        :type type: int
        :param replier: 回复人ID
        :type replier: str
        :param content: 留言内容
        :type content: str
        :param message_id: 留言id
        :type message_id: str
        :param replier_name: 回复人名称
        :type replier_name: str
        :param create_time: 创建时间
        :type create_time: datetime
        :param is_first_message: 是否是第一条留言
        :type is_first_message: int
        :param accessory_list: 附件列表
        :type accessory_list: list[:class:`huaweicloudsdkosm.v2.SimpleAccessoryV2`]
        """
        
        

        self._type = None
        self._replier = None
        self._content = None
        self._message_id = None
        self._replier_name = None
        self._create_time = None
        self._is_first_message = None
        self._accessory_list = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if replier is not None:
            self.replier = replier
        if content is not None:
            self.content = content
        if message_id is not None:
            self.message_id = message_id
        if replier_name is not None:
            self.replier_name = replier_name
        if create_time is not None:
            self.create_time = create_time
        if is_first_message is not None:
            self.is_first_message = is_first_message
        if accessory_list is not None:
            self.accessory_list = accessory_list

    @property
    def type(self):
        """Gets the type of this IncidentMessageV2.

        类型，0客户留言 1华为工程师留言

        :return: The type of this IncidentMessageV2.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IncidentMessageV2.

        类型，0客户留言 1华为工程师留言

        :param type: The type of this IncidentMessageV2.
        :type type: int
        """
        self._type = type

    @property
    def replier(self):
        """Gets the replier of this IncidentMessageV2.

        回复人ID

        :return: The replier of this IncidentMessageV2.
        :rtype: str
        """
        return self._replier

    @replier.setter
    def replier(self, replier):
        """Sets the replier of this IncidentMessageV2.

        回复人ID

        :param replier: The replier of this IncidentMessageV2.
        :type replier: str
        """
        self._replier = replier

    @property
    def content(self):
        """Gets the content of this IncidentMessageV2.

        留言内容

        :return: The content of this IncidentMessageV2.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this IncidentMessageV2.

        留言内容

        :param content: The content of this IncidentMessageV2.
        :type content: str
        """
        self._content = content

    @property
    def message_id(self):
        """Gets the message_id of this IncidentMessageV2.

        留言id

        :return: The message_id of this IncidentMessageV2.
        :rtype: str
        """
        return self._message_id

    @message_id.setter
    def message_id(self, message_id):
        """Sets the message_id of this IncidentMessageV2.

        留言id

        :param message_id: The message_id of this IncidentMessageV2.
        :type message_id: str
        """
        self._message_id = message_id

    @property
    def replier_name(self):
        """Gets the replier_name of this IncidentMessageV2.

        回复人名称

        :return: The replier_name of this IncidentMessageV2.
        :rtype: str
        """
        return self._replier_name

    @replier_name.setter
    def replier_name(self, replier_name):
        """Sets the replier_name of this IncidentMessageV2.

        回复人名称

        :param replier_name: The replier_name of this IncidentMessageV2.
        :type replier_name: str
        """
        self._replier_name = replier_name

    @property
    def create_time(self):
        """Gets the create_time of this IncidentMessageV2.

        创建时间

        :return: The create_time of this IncidentMessageV2.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this IncidentMessageV2.

        创建时间

        :param create_time: The create_time of this IncidentMessageV2.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def is_first_message(self):
        """Gets the is_first_message of this IncidentMessageV2.

        是否是第一条留言

        :return: The is_first_message of this IncidentMessageV2.
        :rtype: int
        """
        return self._is_first_message

    @is_first_message.setter
    def is_first_message(self, is_first_message):
        """Sets the is_first_message of this IncidentMessageV2.

        是否是第一条留言

        :param is_first_message: The is_first_message of this IncidentMessageV2.
        :type is_first_message: int
        """
        self._is_first_message = is_first_message

    @property
    def accessory_list(self):
        """Gets the accessory_list of this IncidentMessageV2.

        附件列表

        :return: The accessory_list of this IncidentMessageV2.
        :rtype: list[:class:`huaweicloudsdkosm.v2.SimpleAccessoryV2`]
        """
        return self._accessory_list

    @accessory_list.setter
    def accessory_list(self, accessory_list):
        """Sets the accessory_list of this IncidentMessageV2.

        附件列表

        :param accessory_list: The accessory_list of this IncidentMessageV2.
        :type accessory_list: list[:class:`huaweicloudsdkosm.v2.SimpleAccessoryV2`]
        """
        self._accessory_list = accessory_list

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
        if not isinstance(other, IncidentMessageV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
