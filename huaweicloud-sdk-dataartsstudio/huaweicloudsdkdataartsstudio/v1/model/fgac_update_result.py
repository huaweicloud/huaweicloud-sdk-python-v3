# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FgacUpdateResult:

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
        'status': 'bool',
        'error_msg': 'str'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'error_msg': 'error_msg'
    }

    def __init__(self, id=None, status=None, error_msg=None):
        """FgacUpdateResult

        The model defined in huaweicloud sdk

        :param id: 数据连接id
        :type id: str
        :param status: 是否更新成功,true表示更新成功,false表示更新失败。
        :type status: bool
        :param error_msg: 细粒度认证更新错误信息
        :type error_msg: str
        """
        
        

        self._id = None
        self._status = None
        self._error_msg = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if error_msg is not None:
            self.error_msg = error_msg

    @property
    def id(self):
        """Gets the id of this FgacUpdateResult.

        数据连接id

        :return: The id of this FgacUpdateResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FgacUpdateResult.

        数据连接id

        :param id: The id of this FgacUpdateResult.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        """Gets the status of this FgacUpdateResult.

        是否更新成功,true表示更新成功,false表示更新失败。

        :return: The status of this FgacUpdateResult.
        :rtype: bool
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this FgacUpdateResult.

        是否更新成功,true表示更新成功,false表示更新失败。

        :param status: The status of this FgacUpdateResult.
        :type status: bool
        """
        self._status = status

    @property
    def error_msg(self):
        """Gets the error_msg of this FgacUpdateResult.

        细粒度认证更新错误信息

        :return: The error_msg of this FgacUpdateResult.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this FgacUpdateResult.

        细粒度认证更新错误信息

        :param error_msg: The error_msg of this FgacUpdateResult.
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
        if not isinstance(other, FgacUpdateResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
