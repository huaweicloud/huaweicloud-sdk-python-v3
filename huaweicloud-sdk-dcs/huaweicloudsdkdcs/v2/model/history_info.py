# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HistoryInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'history_id': 'str',
        'type': 'str',
        'created_at': 'str',
        'status': 'str'
    }

    attribute_map = {
        'history_id': 'history_id',
        'type': 'type',
        'created_at': 'created_at',
        'status': 'status'
    }

    def __init__(self, history_id=None, type=None, created_at=None, status=None):
        r"""HistoryInfo

        The model defined in huaweicloud sdk

        :param history_id: 修改记录ID
        :type history_id: str
        :param type: 修改类型
        :type type: str
        :param created_at: 修改时间
        :type created_at: str
        :param status: 修改状态
        :type status: str
        """
        
        

        self._history_id = None
        self._type = None
        self._created_at = None
        self._status = None
        self.discriminator = None

        if history_id is not None:
            self.history_id = history_id
        if type is not None:
            self.type = type
        if created_at is not None:
            self.created_at = created_at
        if status is not None:
            self.status = status

    @property
    def history_id(self):
        r"""Gets the history_id of this HistoryInfo.

        修改记录ID

        :return: The history_id of this HistoryInfo.
        :rtype: str
        """
        return self._history_id

    @history_id.setter
    def history_id(self, history_id):
        r"""Sets the history_id of this HistoryInfo.

        修改记录ID

        :param history_id: The history_id of this HistoryInfo.
        :type history_id: str
        """
        self._history_id = history_id

    @property
    def type(self):
        r"""Gets the type of this HistoryInfo.

        修改类型

        :return: The type of this HistoryInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this HistoryInfo.

        修改类型

        :param type: The type of this HistoryInfo.
        :type type: str
        """
        self._type = type

    @property
    def created_at(self):
        r"""Gets the created_at of this HistoryInfo.

        修改时间

        :return: The created_at of this HistoryInfo.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this HistoryInfo.

        修改时间

        :param created_at: The created_at of this HistoryInfo.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def status(self):
        r"""Gets the status of this HistoryInfo.

        修改状态

        :return: The status of this HistoryInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this HistoryInfo.

        修改状态

        :param status: The status of this HistoryInfo.
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
        if not isinstance(other, HistoryInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
