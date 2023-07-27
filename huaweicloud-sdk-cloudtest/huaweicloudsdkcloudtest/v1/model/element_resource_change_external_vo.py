# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ElementResourceChangeExternalVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tracker_name': 'str',
        'value': 'str',
        'key': 'str',
        'object_value': 'object',
        'object_key': 'object',
        'tracker_names': 'object',
        'board_info': 'list[object]'
    }

    attribute_map = {
        'tracker_name': 'tracker_name',
        'value': 'value',
        'key': 'key',
        'object_value': 'object_value',
        'object_key': 'object_key',
        'tracker_names': 'tracker_names',
        'board_info': 'board_info'
    }

    def __init__(self, tracker_name=None, value=None, key=None, object_value=None, object_key=None, tracker_names=None, board_info=None):
        """ElementResourceChangeExternalVo

        The model defined in huaweicloud sdk

        :param tracker_name: 工作项类型
        :type tracker_name: str
        :param value: 值
        :type value: str
        :param key: key
        :type key: str
        :param object_value: 对象值
        :type object_value: object
        :param object_key: 对象key
        :type object_key: object
        :param tracker_names: 缺陷类型
        :type tracker_names: object
        :param board_info: 归属看板信息，用例关联工作项信息使用
        :type board_info: list[object]
        """
        
        

        self._tracker_name = None
        self._value = None
        self._key = None
        self._object_value = None
        self._object_key = None
        self._tracker_names = None
        self._board_info = None
        self.discriminator = None

        if tracker_name is not None:
            self.tracker_name = tracker_name
        if value is not None:
            self.value = value
        if key is not None:
            self.key = key
        if object_value is not None:
            self.object_value = object_value
        if object_key is not None:
            self.object_key = object_key
        if tracker_names is not None:
            self.tracker_names = tracker_names
        if board_info is not None:
            self.board_info = board_info

    @property
    def tracker_name(self):
        """Gets the tracker_name of this ElementResourceChangeExternalVo.

        工作项类型

        :return: The tracker_name of this ElementResourceChangeExternalVo.
        :rtype: str
        """
        return self._tracker_name

    @tracker_name.setter
    def tracker_name(self, tracker_name):
        """Sets the tracker_name of this ElementResourceChangeExternalVo.

        工作项类型

        :param tracker_name: The tracker_name of this ElementResourceChangeExternalVo.
        :type tracker_name: str
        """
        self._tracker_name = tracker_name

    @property
    def value(self):
        """Gets the value of this ElementResourceChangeExternalVo.

        值

        :return: The value of this ElementResourceChangeExternalVo.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ElementResourceChangeExternalVo.

        值

        :param value: The value of this ElementResourceChangeExternalVo.
        :type value: str
        """
        self._value = value

    @property
    def key(self):
        """Gets the key of this ElementResourceChangeExternalVo.

        key

        :return: The key of this ElementResourceChangeExternalVo.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this ElementResourceChangeExternalVo.

        key

        :param key: The key of this ElementResourceChangeExternalVo.
        :type key: str
        """
        self._key = key

    @property
    def object_value(self):
        """Gets the object_value of this ElementResourceChangeExternalVo.

        对象值

        :return: The object_value of this ElementResourceChangeExternalVo.
        :rtype: object
        """
        return self._object_value

    @object_value.setter
    def object_value(self, object_value):
        """Sets the object_value of this ElementResourceChangeExternalVo.

        对象值

        :param object_value: The object_value of this ElementResourceChangeExternalVo.
        :type object_value: object
        """
        self._object_value = object_value

    @property
    def object_key(self):
        """Gets the object_key of this ElementResourceChangeExternalVo.

        对象key

        :return: The object_key of this ElementResourceChangeExternalVo.
        :rtype: object
        """
        return self._object_key

    @object_key.setter
    def object_key(self, object_key):
        """Sets the object_key of this ElementResourceChangeExternalVo.

        对象key

        :param object_key: The object_key of this ElementResourceChangeExternalVo.
        :type object_key: object
        """
        self._object_key = object_key

    @property
    def tracker_names(self):
        """Gets the tracker_names of this ElementResourceChangeExternalVo.

        缺陷类型

        :return: The tracker_names of this ElementResourceChangeExternalVo.
        :rtype: object
        """
        return self._tracker_names

    @tracker_names.setter
    def tracker_names(self, tracker_names):
        """Sets the tracker_names of this ElementResourceChangeExternalVo.

        缺陷类型

        :param tracker_names: The tracker_names of this ElementResourceChangeExternalVo.
        :type tracker_names: object
        """
        self._tracker_names = tracker_names

    @property
    def board_info(self):
        """Gets the board_info of this ElementResourceChangeExternalVo.

        归属看板信息，用例关联工作项信息使用

        :return: The board_info of this ElementResourceChangeExternalVo.
        :rtype: list[object]
        """
        return self._board_info

    @board_info.setter
    def board_info(self, board_info):
        """Sets the board_info of this ElementResourceChangeExternalVo.

        归属看板信息，用例关联工作项信息使用

        :param board_info: The board_info of this ElementResourceChangeExternalVo.
        :type board_info: list[object]
        """
        self._board_info = board_info

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
        if not isinstance(other, ElementResourceChangeExternalVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
