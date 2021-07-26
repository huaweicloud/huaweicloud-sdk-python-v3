# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckJobResp:


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
        'error_msg': 'str',
        'success': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'error_code': 'error_code',
        'error_msg': 'error_msg',
        'success': 'success'
    }

    def __init__(self, id=None, status=None, error_code=None, error_msg=None, success=None):
        """CheckJobResp - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._status = None
        self._error_code = None
        self._error_msg = None
        self._success = None
        self.discriminator = None

        self.id = id
        self.status = status
        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg
        if success is not None:
            self.success = success

    @property
    def id(self):
        """Gets the id of this CheckJobResp.

        任务id。

        :return: The id of this CheckJobResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CheckJobResp.

        任务id。

        :param id: The id of this CheckJobResp.
        :type: str
        """
        self._id = id

    @property
    def status(self):
        """Gets the status of this CheckJobResp.

        测试结果

        :return: The status of this CheckJobResp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CheckJobResp.

        测试结果

        :param status: The status of this CheckJobResp.
        :type: str
        """
        self._status = status

    @property
    def error_code(self):
        """Gets the error_code of this CheckJobResp.

        错误码。

        :return: The error_code of this CheckJobResp.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this CheckJobResp.

        错误码。

        :param error_code: The error_code of this CheckJobResp.
        :type: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        """Gets the error_msg of this CheckJobResp.

        错误信息。

        :return: The error_msg of this CheckJobResp.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this CheckJobResp.

        错误信息。

        :param error_msg: The error_msg of this CheckJobResp.
        :type: str
        """
        self._error_msg = error_msg

    @property
    def success(self):
        """Gets the success of this CheckJobResp.

        是否成功

        :return: The success of this CheckJobResp.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this CheckJobResp.

        是否成功

        :param success: The success of this CheckJobResp.
        :type: bool
        """
        self._success = success

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
        import simplejson as json
        return json.dumps(sanitize_for_serialization(self))

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CheckJobResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
