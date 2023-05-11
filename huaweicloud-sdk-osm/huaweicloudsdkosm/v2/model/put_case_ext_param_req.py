# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PutCaseExtParamReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_id': 'str',
        'message_id': 'str',
        'extends_map': 'dict(str, object)'
    }

    attribute_map = {
        'group_id': 'group_id',
        'message_id': 'message_id',
        'extends_map': 'extends_map'
    }

    def __init__(self, group_id=None, message_id=None, extends_map=None):
        """PutCaseExtParamReq

        The model defined in huaweicloud sdk

        :param group_id: 组id
        :type group_id: str
        :param message_id: 消息id
        :type message_id: str
        :param extends_map: 扩展参数
        :type extends_map: dict(str, object)
        """
        
        

        self._group_id = None
        self._message_id = None
        self._extends_map = None
        self.discriminator = None

        if group_id is not None:
            self.group_id = group_id
        if message_id is not None:
            self.message_id = message_id
        if extends_map is not None:
            self.extends_map = extends_map

    @property
    def group_id(self):
        """Gets the group_id of this PutCaseExtParamReq.

        组id

        :return: The group_id of this PutCaseExtParamReq.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this PutCaseExtParamReq.

        组id

        :param group_id: The group_id of this PutCaseExtParamReq.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def message_id(self):
        """Gets the message_id of this PutCaseExtParamReq.

        消息id

        :return: The message_id of this PutCaseExtParamReq.
        :rtype: str
        """
        return self._message_id

    @message_id.setter
    def message_id(self, message_id):
        """Sets the message_id of this PutCaseExtParamReq.

        消息id

        :param message_id: The message_id of this PutCaseExtParamReq.
        :type message_id: str
        """
        self._message_id = message_id

    @property
    def extends_map(self):
        """Gets the extends_map of this PutCaseExtParamReq.

        扩展参数

        :return: The extends_map of this PutCaseExtParamReq.
        :rtype: dict(str, object)
        """
        return self._extends_map

    @extends_map.setter
    def extends_map(self, extends_map):
        """Sets the extends_map of this PutCaseExtParamReq.

        扩展参数

        :param extends_map: The extends_map of this PutCaseExtParamReq.
        :type extends_map: dict(str, object)
        """
        self._extends_map = extends_map

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
        if not isinstance(other, PutCaseExtParamReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
