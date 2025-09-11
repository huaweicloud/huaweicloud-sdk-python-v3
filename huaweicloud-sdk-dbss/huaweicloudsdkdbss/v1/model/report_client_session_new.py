# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReportClientSessionNew:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'db_id': 'str',
        'db_ip': 'str',
        'db_name': 'str',
        'session_num': 'int'
    }

    attribute_map = {
        'db_id': 'db_id',
        'db_ip': 'db_ip',
        'db_name': 'db_name',
        'session_num': 'session_num'
    }

    def __init__(self, db_id=None, db_ip=None, db_name=None, session_num=None):
        r"""ReportClientSessionNew

        The model defined in huaweicloud sdk

        :param db_id: 数据库ID
        :type db_id: str
        :param db_ip: 数据库IP
        :type db_ip: str
        :param db_name: 数据库名称
        :type db_name: str
        :param session_num: SESSION数量
        :type session_num: int
        """
        
        

        self._db_id = None
        self._db_ip = None
        self._db_name = None
        self._session_num = None
        self.discriminator = None

        if db_id is not None:
            self.db_id = db_id
        if db_ip is not None:
            self.db_ip = db_ip
        if db_name is not None:
            self.db_name = db_name
        if session_num is not None:
            self.session_num = session_num

    @property
    def db_id(self):
        r"""Gets the db_id of this ReportClientSessionNew.

        数据库ID

        :return: The db_id of this ReportClientSessionNew.
        :rtype: str
        """
        return self._db_id

    @db_id.setter
    def db_id(self, db_id):
        r"""Sets the db_id of this ReportClientSessionNew.

        数据库ID

        :param db_id: The db_id of this ReportClientSessionNew.
        :type db_id: str
        """
        self._db_id = db_id

    @property
    def db_ip(self):
        r"""Gets the db_ip of this ReportClientSessionNew.

        数据库IP

        :return: The db_ip of this ReportClientSessionNew.
        :rtype: str
        """
        return self._db_ip

    @db_ip.setter
    def db_ip(self, db_ip):
        r"""Sets the db_ip of this ReportClientSessionNew.

        数据库IP

        :param db_ip: The db_ip of this ReportClientSessionNew.
        :type db_ip: str
        """
        self._db_ip = db_ip

    @property
    def db_name(self):
        r"""Gets the db_name of this ReportClientSessionNew.

        数据库名称

        :return: The db_name of this ReportClientSessionNew.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        r"""Sets the db_name of this ReportClientSessionNew.

        数据库名称

        :param db_name: The db_name of this ReportClientSessionNew.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def session_num(self):
        r"""Gets the session_num of this ReportClientSessionNew.

        SESSION数量

        :return: The session_num of this ReportClientSessionNew.
        :rtype: int
        """
        return self._session_num

    @session_num.setter
    def session_num(self, session_num):
        r"""Sets the session_num of this ReportClientSessionNew.

        SESSION数量

        :param session_num: The session_num of this ReportClientSessionNew.
        :type session_num: int
        """
        self._session_num = session_num

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
        if not isinstance(other, ReportClientSessionNew):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
