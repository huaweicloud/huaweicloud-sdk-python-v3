# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AvailableQueueInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'name': 'str',
        'uuid': 'str',
        'err_msg': 'str',
        'update_time': 'int'
    }

    attribute_map = {
        'status': 'status',
        'name': 'name',
        'uuid': 'uuid',
        'err_msg': 'err_msg',
        'update_time': 'update_time'
    }

    def __init__(self, status=None, name=None, uuid=None, err_msg=None, update_time=None):
        r"""AvailableQueueInfo

        The model defined in huaweicloud sdk

        :param status: 执行请求是否成功。“true”表示请求执行成功。
        :type status: str
        :param name: 队列名称。
        :type name: str
        :param uuid: uuid。
        :type uuid: str
        :param err_msg: 状态为失败时的详细报错信息。
        :type err_msg: str
        :param update_time: 作业更新时间, 毫秒数。
        :type update_time: int
        """
        
        

        self._status = None
        self._name = None
        self._uuid = None
        self._err_msg = None
        self._update_time = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if name is not None:
            self.name = name
        if uuid is not None:
            self.uuid = uuid
        if err_msg is not None:
            self.err_msg = err_msg
        if update_time is not None:
            self.update_time = update_time

    @property
    def status(self):
        r"""Gets the status of this AvailableQueueInfo.

        执行请求是否成功。“true”表示请求执行成功。

        :return: The status of this AvailableQueueInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this AvailableQueueInfo.

        执行请求是否成功。“true”表示请求执行成功。

        :param status: The status of this AvailableQueueInfo.
        :type status: str
        """
        self._status = status

    @property
    def name(self):
        r"""Gets the name of this AvailableQueueInfo.

        队列名称。

        :return: The name of this AvailableQueueInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AvailableQueueInfo.

        队列名称。

        :param name: The name of this AvailableQueueInfo.
        :type name: str
        """
        self._name = name

    @property
    def uuid(self):
        r"""Gets the uuid of this AvailableQueueInfo.

        uuid。

        :return: The uuid of this AvailableQueueInfo.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        r"""Sets the uuid of this AvailableQueueInfo.

        uuid。

        :param uuid: The uuid of this AvailableQueueInfo.
        :type uuid: str
        """
        self._uuid = uuid

    @property
    def err_msg(self):
        r"""Gets the err_msg of this AvailableQueueInfo.

        状态为失败时的详细报错信息。

        :return: The err_msg of this AvailableQueueInfo.
        :rtype: str
        """
        return self._err_msg

    @err_msg.setter
    def err_msg(self, err_msg):
        r"""Sets the err_msg of this AvailableQueueInfo.

        状态为失败时的详细报错信息。

        :param err_msg: The err_msg of this AvailableQueueInfo.
        :type err_msg: str
        """
        self._err_msg = err_msg

    @property
    def update_time(self):
        r"""Gets the update_time of this AvailableQueueInfo.

        作业更新时间, 毫秒数。

        :return: The update_time of this AvailableQueueInfo.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this AvailableQueueInfo.

        作业更新时间, 毫秒数。

        :param update_time: The update_time of this AvailableQueueInfo.
        :type update_time: int
        """
        self._update_time = update_time

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
        if not isinstance(other, AvailableQueueInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
