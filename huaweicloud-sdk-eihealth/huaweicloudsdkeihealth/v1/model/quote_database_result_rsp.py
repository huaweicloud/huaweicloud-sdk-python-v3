# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QuoteDatabaseResultRsp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source_project_id': 'str',
        'source_database_id': 'str',
        'destination_database_id': 'str',
        'destination_database_name': 'str',
        'failed_reason': 'str',
        'status': 'str'
    }

    attribute_map = {
        'source_project_id': 'source_project_id',
        'source_database_id': 'source_database_id',
        'destination_database_id': 'destination_database_id',
        'destination_database_name': 'destination_database_name',
        'failed_reason': 'failed_reason',
        'status': 'status'
    }

    def __init__(self, source_project_id=None, source_database_id=None, destination_database_id=None, destination_database_name=None, failed_reason=None, status=None):
        """QuoteDatabaseResultRsp

        The model defined in huaweicloud sdk

        :param source_project_id: 源项目id
        :type source_project_id: str
        :param source_database_id: 源数据库id
        :type source_database_id: str
        :param destination_database_id: 引用到项目后的数据库id
        :type destination_database_id: str
        :param destination_database_name: 引用到项目后的数据库名称
        :type destination_database_name: str
        :param failed_reason: 失败原因
        :type failed_reason: str
        :param status: 导入结果
        :type status: str
        """
        
        

        self._source_project_id = None
        self._source_database_id = None
        self._destination_database_id = None
        self._destination_database_name = None
        self._failed_reason = None
        self._status = None
        self.discriminator = None

        if source_project_id is not None:
            self.source_project_id = source_project_id
        if source_database_id is not None:
            self.source_database_id = source_database_id
        if destination_database_id is not None:
            self.destination_database_id = destination_database_id
        if destination_database_name is not None:
            self.destination_database_name = destination_database_name
        if failed_reason is not None:
            self.failed_reason = failed_reason
        if status is not None:
            self.status = status

    @property
    def source_project_id(self):
        """Gets the source_project_id of this QuoteDatabaseResultRsp.

        源项目id

        :return: The source_project_id of this QuoteDatabaseResultRsp.
        :rtype: str
        """
        return self._source_project_id

    @source_project_id.setter
    def source_project_id(self, source_project_id):
        """Sets the source_project_id of this QuoteDatabaseResultRsp.

        源项目id

        :param source_project_id: The source_project_id of this QuoteDatabaseResultRsp.
        :type source_project_id: str
        """
        self._source_project_id = source_project_id

    @property
    def source_database_id(self):
        """Gets the source_database_id of this QuoteDatabaseResultRsp.

        源数据库id

        :return: The source_database_id of this QuoteDatabaseResultRsp.
        :rtype: str
        """
        return self._source_database_id

    @source_database_id.setter
    def source_database_id(self, source_database_id):
        """Sets the source_database_id of this QuoteDatabaseResultRsp.

        源数据库id

        :param source_database_id: The source_database_id of this QuoteDatabaseResultRsp.
        :type source_database_id: str
        """
        self._source_database_id = source_database_id

    @property
    def destination_database_id(self):
        """Gets the destination_database_id of this QuoteDatabaseResultRsp.

        引用到项目后的数据库id

        :return: The destination_database_id of this QuoteDatabaseResultRsp.
        :rtype: str
        """
        return self._destination_database_id

    @destination_database_id.setter
    def destination_database_id(self, destination_database_id):
        """Sets the destination_database_id of this QuoteDatabaseResultRsp.

        引用到项目后的数据库id

        :param destination_database_id: The destination_database_id of this QuoteDatabaseResultRsp.
        :type destination_database_id: str
        """
        self._destination_database_id = destination_database_id

    @property
    def destination_database_name(self):
        """Gets the destination_database_name of this QuoteDatabaseResultRsp.

        引用到项目后的数据库名称

        :return: The destination_database_name of this QuoteDatabaseResultRsp.
        :rtype: str
        """
        return self._destination_database_name

    @destination_database_name.setter
    def destination_database_name(self, destination_database_name):
        """Sets the destination_database_name of this QuoteDatabaseResultRsp.

        引用到项目后的数据库名称

        :param destination_database_name: The destination_database_name of this QuoteDatabaseResultRsp.
        :type destination_database_name: str
        """
        self._destination_database_name = destination_database_name

    @property
    def failed_reason(self):
        """Gets the failed_reason of this QuoteDatabaseResultRsp.

        失败原因

        :return: The failed_reason of this QuoteDatabaseResultRsp.
        :rtype: str
        """
        return self._failed_reason

    @failed_reason.setter
    def failed_reason(self, failed_reason):
        """Sets the failed_reason of this QuoteDatabaseResultRsp.

        失败原因

        :param failed_reason: The failed_reason of this QuoteDatabaseResultRsp.
        :type failed_reason: str
        """
        self._failed_reason = failed_reason

    @property
    def status(self):
        """Gets the status of this QuoteDatabaseResultRsp.

        导入结果

        :return: The status of this QuoteDatabaseResultRsp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this QuoteDatabaseResultRsp.

        导入结果

        :param status: The status of this QuoteDatabaseResultRsp.
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
        if not isinstance(other, QuoteDatabaseResultRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
