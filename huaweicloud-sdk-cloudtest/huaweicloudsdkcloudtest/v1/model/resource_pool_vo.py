# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourcePoolVo:

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
        'selected': 'str',
        'active_state': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'selected': 'selected',
        'active_state': 'active_state'
    }

    def __init__(self, id=None, name=None, type=None, selected=None, active_state=None):
        """ResourcePoolVo

        The model defined in huaweicloud sdk

        :param id: 资源池ID
        :type id: str
        :param name: 资源池名称
        :type name: str
        :param type: 资源池类型（VM/DOCKER）
        :type type: str
        :param selected: 是否选中
        :type selected: str
        :param active_state: 资源池状态
        :type active_state: str
        """
        
        

        self._id = None
        self._name = None
        self._type = None
        self._selected = None
        self._active_state = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if selected is not None:
            self.selected = selected
        if active_state is not None:
            self.active_state = active_state

    @property
    def id(self):
        """Gets the id of this ResourcePoolVo.

        资源池ID

        :return: The id of this ResourcePoolVo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ResourcePoolVo.

        资源池ID

        :param id: The id of this ResourcePoolVo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ResourcePoolVo.

        资源池名称

        :return: The name of this ResourcePoolVo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ResourcePoolVo.

        资源池名称

        :param name: The name of this ResourcePoolVo.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this ResourcePoolVo.

        资源池类型（VM/DOCKER）

        :return: The type of this ResourcePoolVo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ResourcePoolVo.

        资源池类型（VM/DOCKER）

        :param type: The type of this ResourcePoolVo.
        :type type: str
        """
        self._type = type

    @property
    def selected(self):
        """Gets the selected of this ResourcePoolVo.

        是否选中

        :return: The selected of this ResourcePoolVo.
        :rtype: str
        """
        return self._selected

    @selected.setter
    def selected(self, selected):
        """Sets the selected of this ResourcePoolVo.

        是否选中

        :param selected: The selected of this ResourcePoolVo.
        :type selected: str
        """
        self._selected = selected

    @property
    def active_state(self):
        """Gets the active_state of this ResourcePoolVo.

        资源池状态

        :return: The active_state of this ResourcePoolVo.
        :rtype: str
        """
        return self._active_state

    @active_state.setter
    def active_state(self, active_state):
        """Sets the active_state of this ResourcePoolVo.

        资源池状态

        :param active_state: The active_state of this ResourcePoolVo.
        :type active_state: str
        """
        self._active_state = active_state

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
        if not isinstance(other, ResourcePoolVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
