# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ActionBaseResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'error_code': 'str',
        'error_msg': 'str',
        'id': 'str',
        'name': 'str',
        'status': 'str'
    }

    attribute_map = {
        'error_code': 'error_code',
        'error_msg': 'error_msg',
        'id': 'id',
        'name': 'name',
        'status': 'status'
    }

    def __init__(self, error_code=None, error_msg=None, id=None, name=None, status=None):
        """ActionBaseResp

        The model defined in huaweicloud sdk

        :param error_code: 错误码。
        :type error_code: str
        :param error_msg: 错误描述。
        :type error_msg: str
        :param id: 任务ID。
        :type id: str
        :param name: 任务名称。
        :type name: str
        :param status: 操作结果。
        :type status: str
        """
        
        

        self._error_code = None
        self._error_msg = None
        self._id = None
        self._name = None
        self._status = None
        self.discriminator = None

        self.error_code = error_code
        self.error_msg = error_msg
        self.id = id
        self.name = name
        self.status = status

    @property
    def error_code(self):
        """Gets the error_code of this ActionBaseResp.

        错误码。

        :return: The error_code of this ActionBaseResp.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this ActionBaseResp.

        错误码。

        :param error_code: The error_code of this ActionBaseResp.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        """Gets the error_msg of this ActionBaseResp.

        错误描述。

        :return: The error_msg of this ActionBaseResp.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this ActionBaseResp.

        错误描述。

        :param error_msg: The error_msg of this ActionBaseResp.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def id(self):
        """Gets the id of this ActionBaseResp.

        任务ID。

        :return: The id of this ActionBaseResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ActionBaseResp.

        任务ID。

        :param id: The id of this ActionBaseResp.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ActionBaseResp.

        任务名称。

        :return: The name of this ActionBaseResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ActionBaseResp.

        任务名称。

        :param name: The name of this ActionBaseResp.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this ActionBaseResp.

        操作结果。

        :return: The status of this ActionBaseResp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ActionBaseResp.

        操作结果。

        :param status: The status of this ActionBaseResp.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, ActionBaseResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
