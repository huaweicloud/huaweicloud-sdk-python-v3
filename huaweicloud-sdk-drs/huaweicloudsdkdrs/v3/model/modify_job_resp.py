# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyJobResp:

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
        'status': 'str',
        'error_code': 'str',
        'error_msg': 'str'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'error_code': 'error_code',
        'error_msg': 'error_msg'
    }

    def __init__(self, id=None, status=None, error_code=None, error_msg=None):
        """ModifyJobResp

        The model defined in huaweicloud sdk

        :param id: 任务ID
        :type id: str
        :param status: 状态。 - success 成功 - failed 失败
        :type status: str
        :param error_code: 错误码
        :type error_code: str
        :param error_msg: 错误信息
        :type error_msg: str
        """
        
        

        self._id = None
        self._status = None
        self._error_code = None
        self._error_msg = None
        self.discriminator = None

        self.id = id
        self.status = status
        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg

    @property
    def id(self):
        """Gets the id of this ModifyJobResp.

        任务ID

        :return: The id of this ModifyJobResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ModifyJobResp.

        任务ID

        :param id: The id of this ModifyJobResp.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        """Gets the status of this ModifyJobResp.

        状态。 - success 成功 - failed 失败

        :return: The status of this ModifyJobResp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ModifyJobResp.

        状态。 - success 成功 - failed 失败

        :param status: The status of this ModifyJobResp.
        :type status: str
        """
        self._status = status

    @property
    def error_code(self):
        """Gets the error_code of this ModifyJobResp.

        错误码

        :return: The error_code of this ModifyJobResp.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this ModifyJobResp.

        错误码

        :param error_code: The error_code of this ModifyJobResp.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        """Gets the error_msg of this ModifyJobResp.

        错误信息

        :return: The error_msg of this ModifyJobResp.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this ModifyJobResp.

        错误信息

        :param error_msg: The error_msg of this ModifyJobResp.
        :type error_msg: str
        """
        self._error_msg = error_msg

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
        if not isinstance(other, ModifyJobResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
