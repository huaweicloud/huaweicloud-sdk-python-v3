# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApiMoveParaDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'target_pid': 'str',
        'apis': 'list[str]'
    }

    attribute_map = {
        'target_pid': 'target_pid',
        'apis': 'apis'
    }

    def __init__(self, target_pid=None, apis=None):
        """ApiMoveParaDTO

        The model defined in huaweicloud sdk

        :param target_pid: 父目录编号
        :type target_pid: str
        :param apis: 需要移动的目录
        :type apis: list[str]
        """
        
        

        self._target_pid = None
        self._apis = None
        self.discriminator = None

        if target_pid is not None:
            self.target_pid = target_pid
        if apis is not None:
            self.apis = apis

    @property
    def target_pid(self):
        """Gets the target_pid of this ApiMoveParaDTO.

        父目录编号

        :return: The target_pid of this ApiMoveParaDTO.
        :rtype: str
        """
        return self._target_pid

    @target_pid.setter
    def target_pid(self, target_pid):
        """Sets the target_pid of this ApiMoveParaDTO.

        父目录编号

        :param target_pid: The target_pid of this ApiMoveParaDTO.
        :type target_pid: str
        """
        self._target_pid = target_pid

    @property
    def apis(self):
        """Gets the apis of this ApiMoveParaDTO.

        需要移动的目录

        :return: The apis of this ApiMoveParaDTO.
        :rtype: list[str]
        """
        return self._apis

    @apis.setter
    def apis(self, apis):
        """Sets the apis of this ApiMoveParaDTO.

        需要移动的目录

        :param apis: The apis of this ApiMoveParaDTO.
        :type apis: list[str]
        """
        self._apis = apis

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
        if not isinstance(other, ApiMoveParaDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
