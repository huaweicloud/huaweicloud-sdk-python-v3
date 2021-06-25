# coding: utf-8

import pprint
import re

import six





class QueryMessageInfoV2:


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
        'replier_type': 'int',
        'replier': 'str',
        'content': 'str',
        'create_time': 'datetime',
        'replier_name': 'str',
        'is_first_message': 'int',
        'iam_user_type': 'int',
        'accessory_list': 'list[SimpleAccessoryV2]'
    }

    attribute_map = {
        'type': 'type',
        'replier_type': 'replier_type',
        'replier': 'replier',
        'content': 'content',
        'create_time': 'create_time',
        'replier_name': 'replier_name',
        'is_first_message': 'is_first_message',
        'iam_user_type': 'iam_user_type',
        'accessory_list': 'accessory_list'
    }

    def __init__(self, type=None, replier_type=None, replier=None, content=None, create_time=None, replier_name=None, is_first_message=None, iam_user_type=None, accessory_list=None):
        """QueryMessageInfoV2 - a model defined in huaweicloud sdk"""
        
        

        self._type = None
        self._replier_type = None
        self._replier = None
        self._content = None
        self._create_time = None
        self._replier_name = None
        self._is_first_message = None
        self._iam_user_type = None
        self._accessory_list = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if replier_type is not None:
            self.replier_type = replier_type
        if replier is not None:
            self.replier = replier
        if content is not None:
            self.content = content
        if create_time is not None:
            self.create_time = create_time
        if replier_name is not None:
            self.replier_name = replier_name
        if is_first_message is not None:
            self.is_first_message = is_first_message
        if iam_user_type is not None:
            self.iam_user_type = iam_user_type
        if accessory_list is not None:
            self.accessory_list = accessory_list

    @property
    def type(self):
        """Gets the type of this QueryMessageInfoV2.

        类型，0客户留言 1华为工程师留言

        :return: The type of this QueryMessageInfoV2.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this QueryMessageInfoV2.

        类型，0客户留言 1华为工程师留言

        :param type: The type of this QueryMessageInfoV2.
        :type: int
        """
        self._type = type

    @property
    def replier_type(self):
        """Gets the replier_type of this QueryMessageInfoV2.

        回复人类型，0客户留言 1华为工程师留言 2第三方留言

        :return: The replier_type of this QueryMessageInfoV2.
        :rtype: int
        """
        return self._replier_type

    @replier_type.setter
    def replier_type(self, replier_type):
        """Sets the replier_type of this QueryMessageInfoV2.

        回复人类型，0客户留言 1华为工程师留言 2第三方留言

        :param replier_type: The replier_type of this QueryMessageInfoV2.
        :type: int
        """
        self._replier_type = replier_type

    @property
    def replier(self):
        """Gets the replier of this QueryMessageInfoV2.

        回复人id

        :return: The replier of this QueryMessageInfoV2.
        :rtype: str
        """
        return self._replier

    @replier.setter
    def replier(self, replier):
        """Sets the replier of this QueryMessageInfoV2.

        回复人id

        :param replier: The replier of this QueryMessageInfoV2.
        :type: str
        """
        self._replier = replier

    @property
    def content(self):
        """Gets the content of this QueryMessageInfoV2.

        留言内容

        :return: The content of this QueryMessageInfoV2.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this QueryMessageInfoV2.

        留言内容

        :param content: The content of this QueryMessageInfoV2.
        :type: str
        """
        self._content = content

    @property
    def create_time(self):
        """Gets the create_time of this QueryMessageInfoV2.

        创建时间

        :return: The create_time of this QueryMessageInfoV2.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this QueryMessageInfoV2.

        创建时间

        :param create_time: The create_time of this QueryMessageInfoV2.
        :type: datetime
        """
        self._create_time = create_time

    @property
    def replier_name(self):
        """Gets the replier_name of this QueryMessageInfoV2.

        回复人名称

        :return: The replier_name of this QueryMessageInfoV2.
        :rtype: str
        """
        return self._replier_name

    @replier_name.setter
    def replier_name(self, replier_name):
        """Sets the replier_name of this QueryMessageInfoV2.

        回复人名称

        :param replier_name: The replier_name of this QueryMessageInfoV2.
        :type: str
        """
        self._replier_name = replier_name

    @property
    def is_first_message(self):
        """Gets the is_first_message of this QueryMessageInfoV2.

        是否是第一条留言

        :return: The is_first_message of this QueryMessageInfoV2.
        :rtype: int
        """
        return self._is_first_message

    @is_first_message.setter
    def is_first_message(self, is_first_message):
        """Sets the is_first_message of this QueryMessageInfoV2.

        是否是第一条留言

        :param is_first_message: The is_first_message of this QueryMessageInfoV2.
        :type: int
        """
        self._is_first_message = is_first_message

    @property
    def iam_user_type(self):
        """Gets the iam_user_type of this QueryMessageInfoV2.

        子用户类型

        :return: The iam_user_type of this QueryMessageInfoV2.
        :rtype: int
        """
        return self._iam_user_type

    @iam_user_type.setter
    def iam_user_type(self, iam_user_type):
        """Sets the iam_user_type of this QueryMessageInfoV2.

        子用户类型

        :param iam_user_type: The iam_user_type of this QueryMessageInfoV2.
        :type: int
        """
        self._iam_user_type = iam_user_type

    @property
    def accessory_list(self):
        """Gets the accessory_list of this QueryMessageInfoV2.

        附件列表

        :return: The accessory_list of this QueryMessageInfoV2.
        :rtype: list[SimpleAccessoryV2]
        """
        return self._accessory_list

    @accessory_list.setter
    def accessory_list(self, accessory_list):
        """Sets the accessory_list of this QueryMessageInfoV2.

        附件列表

        :param accessory_list: The accessory_list of this QueryMessageInfoV2.
        :type: list[SimpleAccessoryV2]
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, QueryMessageInfoV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other