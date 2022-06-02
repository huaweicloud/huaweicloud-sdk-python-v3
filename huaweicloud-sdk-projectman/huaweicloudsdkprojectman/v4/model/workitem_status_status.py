# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkitemStatusStatus:

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
        'description': 'str',
        'parent_status_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'description': 'description',
        'parent_status_id': 'parent_status_id'
    }

    def __init__(self, id=None, name=None, type=None, description=None, parent_status_id=None):
        """WorkitemStatusStatus

        The model defined in huaweicloud sdk

        :param id: 工作项的状态id
        :type id: str
        :param name: 状态名称
        :type name: str
        :param type: 工作项状态的类型， BACKLOG( \&quot;初始化\&quot;), READY(\&quot;待启动\&quot;), IN_PROGRESS(\&quot;进行中\&quot;), COMPLETE(\&quot;已完成\&quot;), DONE(\&quot;已结束\&quot;),
        :type type: str
        :param description: 工作项状态的描述
        :type description: str
        :param parent_status_id: 工作项状态的父状态id
        :type parent_status_id: str
        """
        
        

        self._id = None
        self._name = None
        self._type = None
        self._description = None
        self._parent_status_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if description is not None:
            self.description = description
        if parent_status_id is not None:
            self.parent_status_id = parent_status_id

    @property
    def id(self):
        """Gets the id of this WorkitemStatusStatus.

        工作项的状态id

        :return: The id of this WorkitemStatusStatus.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WorkitemStatusStatus.

        工作项的状态id

        :param id: The id of this WorkitemStatusStatus.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this WorkitemStatusStatus.

        状态名称

        :return: The name of this WorkitemStatusStatus.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WorkitemStatusStatus.

        状态名称

        :param name: The name of this WorkitemStatusStatus.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this WorkitemStatusStatus.

        工作项状态的类型， BACKLOG( \"初始化\"), READY(\"待启动\"), IN_PROGRESS(\"进行中\"), COMPLETE(\"已完成\"), DONE(\"已结束\"),

        :return: The type of this WorkitemStatusStatus.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this WorkitemStatusStatus.

        工作项状态的类型， BACKLOG( \"初始化\"), READY(\"待启动\"), IN_PROGRESS(\"进行中\"), COMPLETE(\"已完成\"), DONE(\"已结束\"),

        :param type: The type of this WorkitemStatusStatus.
        :type type: str
        """
        self._type = type

    @property
    def description(self):
        """Gets the description of this WorkitemStatusStatus.

        工作项状态的描述

        :return: The description of this WorkitemStatusStatus.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this WorkitemStatusStatus.

        工作项状态的描述

        :param description: The description of this WorkitemStatusStatus.
        :type description: str
        """
        self._description = description

    @property
    def parent_status_id(self):
        """Gets the parent_status_id of this WorkitemStatusStatus.

        工作项状态的父状态id

        :return: The parent_status_id of this WorkitemStatusStatus.
        :rtype: str
        """
        return self._parent_status_id

    @parent_status_id.setter
    def parent_status_id(self, parent_status_id):
        """Sets the parent_status_id of this WorkitemStatusStatus.

        工作项状态的父状态id

        :param parent_status_id: The parent_status_id of this WorkitemStatusStatus.
        :type parent_status_id: str
        """
        self._parent_status_id = parent_status_id

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
        if not isinstance(other, WorkitemStatusStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
