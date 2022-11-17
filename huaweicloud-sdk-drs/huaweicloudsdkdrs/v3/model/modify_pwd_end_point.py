# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyPwdEndPoint:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'db_password': 'str',
        'end_point_type': 'str',
        'job_id': 'str',
        'kerberos': 'KerberosVO'
    }

    attribute_map = {
        'db_password': 'db_password',
        'end_point_type': 'end_point_type',
        'job_id': 'job_id',
        'kerberos': 'kerberos'
    }

    def __init__(self, db_password=None, end_point_type=None, job_id=None, kerberos=None):
        """ModifyPwdEndPoint

        The model defined in huaweicloud sdk

        :param db_password: 数据库密码
        :type db_password: str
        :param end_point_type: 类型，so：源库；ta：目标库。
        :type end_point_type: str
        :param job_id: 任务id
        :type job_id: str
        :param kerberos: 
        :type kerberos: :class:`huaweicloudsdkdrs.v3.KerberosVO`
        """
        
        

        self._db_password = None
        self._end_point_type = None
        self._job_id = None
        self._kerberos = None
        self.discriminator = None

        self.db_password = db_password
        self.end_point_type = end_point_type
        self.job_id = job_id
        if kerberos is not None:
            self.kerberos = kerberos

    @property
    def db_password(self):
        """Gets the db_password of this ModifyPwdEndPoint.

        数据库密码

        :return: The db_password of this ModifyPwdEndPoint.
        :rtype: str
        """
        return self._db_password

    @db_password.setter
    def db_password(self, db_password):
        """Sets the db_password of this ModifyPwdEndPoint.

        数据库密码

        :param db_password: The db_password of this ModifyPwdEndPoint.
        :type db_password: str
        """
        self._db_password = db_password

    @property
    def end_point_type(self):
        """Gets the end_point_type of this ModifyPwdEndPoint.

        类型，so：源库；ta：目标库。

        :return: The end_point_type of this ModifyPwdEndPoint.
        :rtype: str
        """
        return self._end_point_type

    @end_point_type.setter
    def end_point_type(self, end_point_type):
        """Sets the end_point_type of this ModifyPwdEndPoint.

        类型，so：源库；ta：目标库。

        :param end_point_type: The end_point_type of this ModifyPwdEndPoint.
        :type end_point_type: str
        """
        self._end_point_type = end_point_type

    @property
    def job_id(self):
        """Gets the job_id of this ModifyPwdEndPoint.

        任务id

        :return: The job_id of this ModifyPwdEndPoint.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ModifyPwdEndPoint.

        任务id

        :param job_id: The job_id of this ModifyPwdEndPoint.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def kerberos(self):
        """Gets the kerberos of this ModifyPwdEndPoint.

        :return: The kerberos of this ModifyPwdEndPoint.
        :rtype: :class:`huaweicloudsdkdrs.v3.KerberosVO`
        """
        return self._kerberos

    @kerberos.setter
    def kerberos(self, kerberos):
        """Sets the kerberos of this ModifyPwdEndPoint.

        :param kerberos: The kerberos of this ModifyPwdEndPoint.
        :type kerberos: :class:`huaweicloudsdkdrs.v3.KerberosVO`
        """
        self._kerberos = kerberos

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
        if not isinstance(other, ModifyPwdEndPoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
