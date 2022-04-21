# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateJobResp:

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
        'status': 'str',
        'create_time': 'str',
        'error_code': 'str',
        'error_msg': 'str',
        'child_ids': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'create_time': 'create_time',
        'error_code': 'error_code',
        'error_msg': 'error_msg',
        'child_ids': 'child_ids'
    }

    def __init__(self, id=None, name=None, status=None, create_time=None, error_code=None, error_msg=None, child_ids=None):
        """CreateJobResp

        The model defined in huaweicloud sdk

        :param id: 任务ID
        :type id: str
        :param name: 任务名称
        :type name: str
        :param status: 任务状态
        :type status: str
        :param create_time: 创建时间，时间戳
        :type create_time: str
        :param error_code: 错误码
        :type error_code: str
        :param error_msg: 错误信息
        :type error_msg: str
        :param child_ids: 子任务ID，有子任务时返回该字段。
        :type child_ids: list[str]
        """
        
        

        self._id = None
        self._name = None
        self._status = None
        self._create_time = None
        self._error_code = None
        self._error_msg = None
        self._child_ids = None
        self.discriminator = None

        self.id = id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if create_time is not None:
            self.create_time = create_time
        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg
        if child_ids is not None:
            self.child_ids = child_ids

    @property
    def id(self):
        """Gets the id of this CreateJobResp.

        任务ID

        :return: The id of this CreateJobResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateJobResp.

        任务ID

        :param id: The id of this CreateJobResp.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this CreateJobResp.

        任务名称

        :return: The name of this CreateJobResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateJobResp.

        任务名称

        :param name: The name of this CreateJobResp.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this CreateJobResp.

        任务状态

        :return: The status of this CreateJobResp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CreateJobResp.

        任务状态

        :param status: The status of this CreateJobResp.
        :type status: str
        """
        self._status = status

    @property
    def create_time(self):
        """Gets the create_time of this CreateJobResp.

        创建时间，时间戳

        :return: The create_time of this CreateJobResp.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this CreateJobResp.

        创建时间，时间戳

        :param create_time: The create_time of this CreateJobResp.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def error_code(self):
        """Gets the error_code of this CreateJobResp.

        错误码

        :return: The error_code of this CreateJobResp.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this CreateJobResp.

        错误码

        :param error_code: The error_code of this CreateJobResp.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        """Gets the error_msg of this CreateJobResp.

        错误信息

        :return: The error_msg of this CreateJobResp.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this CreateJobResp.

        错误信息

        :param error_msg: The error_msg of this CreateJobResp.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def child_ids(self):
        """Gets the child_ids of this CreateJobResp.

        子任务ID，有子任务时返回该字段。

        :return: The child_ids of this CreateJobResp.
        :rtype: list[str]
        """
        return self._child_ids

    @child_ids.setter
    def child_ids(self, child_ids):
        """Sets the child_ids of this CreateJobResp.

        子任务ID，有子任务时返回该字段。

        :param child_ids: The child_ids of this CreateJobResp.
        :type child_ids: list[str]
        """
        self._child_ids = child_ids

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
        if not isinstance(other, CreateJobResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
