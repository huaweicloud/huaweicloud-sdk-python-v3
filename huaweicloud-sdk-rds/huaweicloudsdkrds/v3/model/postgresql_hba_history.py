# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PostgresqlHbaHistory:

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
        'time': 'datetime',
        'fail_reason': 'str',
        'before_confs': 'list[PostgresqlHbaConf]',
        'after_confs': 'list[PostgresqlHbaConf]'
    }

    attribute_map = {
        'status': 'status',
        'time': 'time',
        'fail_reason': 'fail_reason',
        'before_confs': 'before_confs',
        'after_confs': 'after_confs'
    }

    def __init__(self, status=None, time=None, fail_reason=None, before_confs=None, after_confs=None):
        """PostgresqlHbaHistory

        The model defined in huaweicloud sdk

        :param status: 修改结果，    success：已生效     failed：未生效     setting：设置中\&quot;,
        :type status: str
        :param time: 修改时间
        :type time: datetime
        :param fail_reason: 修改失败原因
        :type fail_reason: str
        :param before_confs: 修改之前的值
        :type before_confs: list[:class:`huaweicloudsdkrds.v3.PostgresqlHbaConf`]
        :param after_confs: 修改之后的值
        :type after_confs: list[:class:`huaweicloudsdkrds.v3.PostgresqlHbaConf`]
        """
        
        

        self._status = None
        self._time = None
        self._fail_reason = None
        self._before_confs = None
        self._after_confs = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if time is not None:
            self.time = time
        if fail_reason is not None:
            self.fail_reason = fail_reason
        if before_confs is not None:
            self.before_confs = before_confs
        if after_confs is not None:
            self.after_confs = after_confs

    @property
    def status(self):
        """Gets the status of this PostgresqlHbaHistory.

        修改结果，    success：已生效     failed：未生效     setting：设置中\",

        :return: The status of this PostgresqlHbaHistory.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PostgresqlHbaHistory.

        修改结果，    success：已生效     failed：未生效     setting：设置中\",

        :param status: The status of this PostgresqlHbaHistory.
        :type status: str
        """
        self._status = status

    @property
    def time(self):
        """Gets the time of this PostgresqlHbaHistory.

        修改时间

        :return: The time of this PostgresqlHbaHistory.
        :rtype: datetime
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this PostgresqlHbaHistory.

        修改时间

        :param time: The time of this PostgresqlHbaHistory.
        :type time: datetime
        """
        self._time = time

    @property
    def fail_reason(self):
        """Gets the fail_reason of this PostgresqlHbaHistory.

        修改失败原因

        :return: The fail_reason of this PostgresqlHbaHistory.
        :rtype: str
        """
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, fail_reason):
        """Sets the fail_reason of this PostgresqlHbaHistory.

        修改失败原因

        :param fail_reason: The fail_reason of this PostgresqlHbaHistory.
        :type fail_reason: str
        """
        self._fail_reason = fail_reason

    @property
    def before_confs(self):
        """Gets the before_confs of this PostgresqlHbaHistory.

        修改之前的值

        :return: The before_confs of this PostgresqlHbaHistory.
        :rtype: list[:class:`huaweicloudsdkrds.v3.PostgresqlHbaConf`]
        """
        return self._before_confs

    @before_confs.setter
    def before_confs(self, before_confs):
        """Sets the before_confs of this PostgresqlHbaHistory.

        修改之前的值

        :param before_confs: The before_confs of this PostgresqlHbaHistory.
        :type before_confs: list[:class:`huaweicloudsdkrds.v3.PostgresqlHbaConf`]
        """
        self._before_confs = before_confs

    @property
    def after_confs(self):
        """Gets the after_confs of this PostgresqlHbaHistory.

        修改之后的值

        :return: The after_confs of this PostgresqlHbaHistory.
        :rtype: list[:class:`huaweicloudsdkrds.v3.PostgresqlHbaConf`]
        """
        return self._after_confs

    @after_confs.setter
    def after_confs(self, after_confs):
        """Sets the after_confs of this PostgresqlHbaHistory.

        修改之后的值

        :param after_confs: The after_confs of this PostgresqlHbaHistory.
        :type after_confs: list[:class:`huaweicloudsdkrds.v3.PostgresqlHbaConf`]
        """
        self._after_confs = after_confs

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
        if not isinstance(other, PostgresqlHbaHistory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
