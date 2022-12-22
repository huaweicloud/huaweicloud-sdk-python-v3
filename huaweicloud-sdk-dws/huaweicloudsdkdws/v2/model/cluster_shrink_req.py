# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterShrinkReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'shrink_number': 'int',
        'online': 'bool',
        'type': 'str',
        'retry': 'bool',
        'force_backup': 'bool',
        'need_agency': 'bool'
    }

    attribute_map = {
        'shrink_number': 'shrink_number',
        'online': 'online',
        'type': 'type',
        'retry': 'retry',
        'force_backup': 'force_backup',
        'need_agency': 'need_agency'
    }

    def __init__(self, shrink_number=None, online=None, type=None, retry=None, force_backup=None, need_agency=None):
        """ClusterShrinkReq

        The model defined in huaweicloud sdk

        :param shrink_number: 缩容数
        :type shrink_number: int
        :param online: 在线
        :type online: bool
        :param type: 数据库类型
        :type type: str
        :param retry: 重试
        :type retry: bool
        :param force_backup: 执行备份
        :type force_backup: bool
        :param need_agency: 是否需要委托
        :type need_agency: bool
        """
        
        

        self._shrink_number = None
        self._online = None
        self._type = None
        self._retry = None
        self._force_backup = None
        self._need_agency = None
        self.discriminator = None

        self.shrink_number = shrink_number
        self.online = online
        self.type = type
        if retry is not None:
            self.retry = retry
        self.force_backup = force_backup
        self.need_agency = need_agency

    @property
    def shrink_number(self):
        """Gets the shrink_number of this ClusterShrinkReq.

        缩容数

        :return: The shrink_number of this ClusterShrinkReq.
        :rtype: int
        """
        return self._shrink_number

    @shrink_number.setter
    def shrink_number(self, shrink_number):
        """Sets the shrink_number of this ClusterShrinkReq.

        缩容数

        :param shrink_number: The shrink_number of this ClusterShrinkReq.
        :type shrink_number: int
        """
        self._shrink_number = shrink_number

    @property
    def online(self):
        """Gets the online of this ClusterShrinkReq.

        在线

        :return: The online of this ClusterShrinkReq.
        :rtype: bool
        """
        return self._online

    @online.setter
    def online(self, online):
        """Sets the online of this ClusterShrinkReq.

        在线

        :param online: The online of this ClusterShrinkReq.
        :type online: bool
        """
        self._online = online

    @property
    def type(self):
        """Gets the type of this ClusterShrinkReq.

        数据库类型

        :return: The type of this ClusterShrinkReq.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ClusterShrinkReq.

        数据库类型

        :param type: The type of this ClusterShrinkReq.
        :type type: str
        """
        self._type = type

    @property
    def retry(self):
        """Gets the retry of this ClusterShrinkReq.

        重试

        :return: The retry of this ClusterShrinkReq.
        :rtype: bool
        """
        return self._retry

    @retry.setter
    def retry(self, retry):
        """Sets the retry of this ClusterShrinkReq.

        重试

        :param retry: The retry of this ClusterShrinkReq.
        :type retry: bool
        """
        self._retry = retry

    @property
    def force_backup(self):
        """Gets the force_backup of this ClusterShrinkReq.

        执行备份

        :return: The force_backup of this ClusterShrinkReq.
        :rtype: bool
        """
        return self._force_backup

    @force_backup.setter
    def force_backup(self, force_backup):
        """Sets the force_backup of this ClusterShrinkReq.

        执行备份

        :param force_backup: The force_backup of this ClusterShrinkReq.
        :type force_backup: bool
        """
        self._force_backup = force_backup

    @property
    def need_agency(self):
        """Gets the need_agency of this ClusterShrinkReq.

        是否需要委托

        :return: The need_agency of this ClusterShrinkReq.
        :rtype: bool
        """
        return self._need_agency

    @need_agency.setter
    def need_agency(self, need_agency):
        """Sets the need_agency of this ClusterShrinkReq.

        是否需要委托

        :param need_agency: The need_agency of this ClusterShrinkReq.
        :type need_agency: bool
        """
        self._need_agency = need_agency

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
        if not isinstance(other, ClusterShrinkReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
