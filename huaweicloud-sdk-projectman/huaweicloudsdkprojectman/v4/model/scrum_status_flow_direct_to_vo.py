# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScrumStatusFlowDirectToVo:

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
        'status_id': 'int',
        'name': 'str',
        'enabled': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'status_id': 'status_id',
        'name': 'name',
        'enabled': 'enabled'
    }

    def __init__(self, id=None, status_id=None, name=None, enabled=None):
        """ScrumStatusFlowDirectToVo

        The model defined in huaweicloud sdk

        :param id: 流转数据的uuid
        :type id: str
        :param status_id: 状态id
        :type status_id: int
        :param name: 状态名
        :type name: str
        :param enabled: 是否开启流转
        :type enabled: bool
        """
        
        

        self._id = None
        self._status_id = None
        self._name = None
        self._enabled = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if status_id is not None:
            self.status_id = status_id
        if name is not None:
            self.name = name
        if enabled is not None:
            self.enabled = enabled

    @property
    def id(self):
        """Gets the id of this ScrumStatusFlowDirectToVo.

        流转数据的uuid

        :return: The id of this ScrumStatusFlowDirectToVo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ScrumStatusFlowDirectToVo.

        流转数据的uuid

        :param id: The id of this ScrumStatusFlowDirectToVo.
        :type id: str
        """
        self._id = id

    @property
    def status_id(self):
        """Gets the status_id of this ScrumStatusFlowDirectToVo.

        状态id

        :return: The status_id of this ScrumStatusFlowDirectToVo.
        :rtype: int
        """
        return self._status_id

    @status_id.setter
    def status_id(self, status_id):
        """Sets the status_id of this ScrumStatusFlowDirectToVo.

        状态id

        :param status_id: The status_id of this ScrumStatusFlowDirectToVo.
        :type status_id: int
        """
        self._status_id = status_id

    @property
    def name(self):
        """Gets the name of this ScrumStatusFlowDirectToVo.

        状态名

        :return: The name of this ScrumStatusFlowDirectToVo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ScrumStatusFlowDirectToVo.

        状态名

        :param name: The name of this ScrumStatusFlowDirectToVo.
        :type name: str
        """
        self._name = name

    @property
    def enabled(self):
        """Gets the enabled of this ScrumStatusFlowDirectToVo.

        是否开启流转

        :return: The enabled of this ScrumStatusFlowDirectToVo.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this ScrumStatusFlowDirectToVo.

        是否开启流转

        :param enabled: The enabled of this ScrumStatusFlowDirectToVo.
        :type enabled: bool
        """
        self._enabled = enabled

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
        if not isinstance(other, ScrumStatusFlowDirectToVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
