# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StatusFlowDirectToVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'parent_name': 'str',
        'parent_type': 'str',
        'status_id': 'str',
        'name': 'str',
        'status_type': 'str',
        'enabled': 'bool',
        'parent_id': 'str'
    }

    attribute_map = {
        'parent_name': 'parent_name',
        'parent_type': 'parent_type',
        'status_id': 'status_id',
        'name': 'name',
        'status_type': 'status_type',
        'enabled': 'enabled',
        'parent_id': 'parent_id'
    }

    def __init__(self, parent_name=None, parent_type=None, status_id=None, name=None, status_type=None, enabled=None, parent_id=None):
        r"""StatusFlowDirectToVo

        The model defined in huaweicloud sdk

        :param parent_name:  父状态的名称
        :type parent_name: str
        :param parent_type: 父状态的类型
        :type parent_type: str
        :param status_id: 状态id
        :type status_id: str
        :param name: 状态名称
        :type name: str
        :param status_type: 状态类型
        :type status_type: str
        :param enabled: 是否已开启状态流转， true： 开启, false 没开启
        :type enabled: bool
        :param parent_id: 父状态的uuid
        :type parent_id: str
        """
        
        

        self._parent_name = None
        self._parent_type = None
        self._status_id = None
        self._name = None
        self._status_type = None
        self._enabled = None
        self._parent_id = None
        self.discriminator = None

        if parent_name is not None:
            self.parent_name = parent_name
        if parent_type is not None:
            self.parent_type = parent_type
        if status_id is not None:
            self.status_id = status_id
        if name is not None:
            self.name = name
        if status_type is not None:
            self.status_type = status_type
        if enabled is not None:
            self.enabled = enabled
        if parent_id is not None:
            self.parent_id = parent_id

    @property
    def parent_name(self):
        r"""Gets the parent_name of this StatusFlowDirectToVo.

         父状态的名称

        :return: The parent_name of this StatusFlowDirectToVo.
        :rtype: str
        """
        return self._parent_name

    @parent_name.setter
    def parent_name(self, parent_name):
        r"""Sets the parent_name of this StatusFlowDirectToVo.

         父状态的名称

        :param parent_name: The parent_name of this StatusFlowDirectToVo.
        :type parent_name: str
        """
        self._parent_name = parent_name

    @property
    def parent_type(self):
        r"""Gets the parent_type of this StatusFlowDirectToVo.

        父状态的类型

        :return: The parent_type of this StatusFlowDirectToVo.
        :rtype: str
        """
        return self._parent_type

    @parent_type.setter
    def parent_type(self, parent_type):
        r"""Sets the parent_type of this StatusFlowDirectToVo.

        父状态的类型

        :param parent_type: The parent_type of this StatusFlowDirectToVo.
        :type parent_type: str
        """
        self._parent_type = parent_type

    @property
    def status_id(self):
        r"""Gets the status_id of this StatusFlowDirectToVo.

        状态id

        :return: The status_id of this StatusFlowDirectToVo.
        :rtype: str
        """
        return self._status_id

    @status_id.setter
    def status_id(self, status_id):
        r"""Sets the status_id of this StatusFlowDirectToVo.

        状态id

        :param status_id: The status_id of this StatusFlowDirectToVo.
        :type status_id: str
        """
        self._status_id = status_id

    @property
    def name(self):
        r"""Gets the name of this StatusFlowDirectToVo.

        状态名称

        :return: The name of this StatusFlowDirectToVo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this StatusFlowDirectToVo.

        状态名称

        :param name: The name of this StatusFlowDirectToVo.
        :type name: str
        """
        self._name = name

    @property
    def status_type(self):
        r"""Gets the status_type of this StatusFlowDirectToVo.

        状态类型

        :return: The status_type of this StatusFlowDirectToVo.
        :rtype: str
        """
        return self._status_type

    @status_type.setter
    def status_type(self, status_type):
        r"""Sets the status_type of this StatusFlowDirectToVo.

        状态类型

        :param status_type: The status_type of this StatusFlowDirectToVo.
        :type status_type: str
        """
        self._status_type = status_type

    @property
    def enabled(self):
        r"""Gets the enabled of this StatusFlowDirectToVo.

        是否已开启状态流转， true： 开启, false 没开启

        :return: The enabled of this StatusFlowDirectToVo.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this StatusFlowDirectToVo.

        是否已开启状态流转， true： 开启, false 没开启

        :param enabled: The enabled of this StatusFlowDirectToVo.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def parent_id(self):
        r"""Gets the parent_id of this StatusFlowDirectToVo.

        父状态的uuid

        :return: The parent_id of this StatusFlowDirectToVo.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        r"""Sets the parent_id of this StatusFlowDirectToVo.

        父状态的uuid

        :param parent_id: The parent_id of this StatusFlowDirectToVo.
        :type parent_id: str
        """
        self._parent_id = parent_id

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
        if not isinstance(other, StatusFlowDirectToVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
