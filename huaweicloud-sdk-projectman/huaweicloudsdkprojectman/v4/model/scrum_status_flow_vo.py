# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScrumStatusFlowVo:

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
        'status_id': 'int',
        'direct_to': 'list[ScrumStatusFlowDirectToVo]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status_id': 'status_id',
        'direct_to': 'direct_to'
    }

    def __init__(self, id=None, name=None, status_id=None, direct_to=None):
        """ScrumStatusFlowVo

        The model defined in huaweicloud sdk

        :param id: 流转数据的uuid
        :type id: str
        :param name: 状态名称
        :type name: str
        :param status_id: 状态id
        :type status_id: int
        :param direct_to: 流转到的数据
        :type direct_to: list[:class:`huaweicloudsdkprojectman.v4.ScrumStatusFlowDirectToVo`]
        """
        
        

        self._id = None
        self._name = None
        self._status_id = None
        self._direct_to = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if status_id is not None:
            self.status_id = status_id
        if direct_to is not None:
            self.direct_to = direct_to

    @property
    def id(self):
        """Gets the id of this ScrumStatusFlowVo.

        流转数据的uuid

        :return: The id of this ScrumStatusFlowVo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ScrumStatusFlowVo.

        流转数据的uuid

        :param id: The id of this ScrumStatusFlowVo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ScrumStatusFlowVo.

        状态名称

        :return: The name of this ScrumStatusFlowVo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ScrumStatusFlowVo.

        状态名称

        :param name: The name of this ScrumStatusFlowVo.
        :type name: str
        """
        self._name = name

    @property
    def status_id(self):
        """Gets the status_id of this ScrumStatusFlowVo.

        状态id

        :return: The status_id of this ScrumStatusFlowVo.
        :rtype: int
        """
        return self._status_id

    @status_id.setter
    def status_id(self, status_id):
        """Sets the status_id of this ScrumStatusFlowVo.

        状态id

        :param status_id: The status_id of this ScrumStatusFlowVo.
        :type status_id: int
        """
        self._status_id = status_id

    @property
    def direct_to(self):
        """Gets the direct_to of this ScrumStatusFlowVo.

        流转到的数据

        :return: The direct_to of this ScrumStatusFlowVo.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.ScrumStatusFlowDirectToVo`]
        """
        return self._direct_to

    @direct_to.setter
    def direct_to(self, direct_to):
        """Sets the direct_to of this ScrumStatusFlowVo.

        流转到的数据

        :param direct_to: The direct_to of this ScrumStatusFlowVo.
        :type direct_to: list[:class:`huaweicloudsdkprojectman.v4.ScrumStatusFlowDirectToVo`]
        """
        self._direct_to = direct_to

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
        if not isinstance(other, ScrumStatusFlowVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
