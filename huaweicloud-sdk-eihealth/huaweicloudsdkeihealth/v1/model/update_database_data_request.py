# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDatabaseDataRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'eihealth_project_id': 'str',
        'database_id': 'str',
        'row_num': 'int',
        'body': 'RowDataReq'
    }

    attribute_map = {
        'eihealth_project_id': 'eihealth_project_id',
        'database_id': 'database_id',
        'row_num': 'row_num',
        'body': 'body'
    }

    def __init__(self, eihealth_project_id=None, database_id=None, row_num=None, body=None):
        """UpdateDatabaseDataRequest

        The model defined in huaweicloud sdk

        :param eihealth_project_id: 医疗智能体平台项目ID，您可以在EIHealth平台单击所需的项目名称，进入项目设置页面查看。
        :type eihealth_project_id: str
        :param database_id: 数据库实例id
        :type database_id: str
        :param row_num: 数据行号，即_row_num值
        :type row_num: int
        :param body: Body of the UpdateDatabaseDataRequest
        :type body: :class:`huaweicloudsdkeihealth.v1.RowDataReq`
        """
        
        

        self._eihealth_project_id = None
        self._database_id = None
        self._row_num = None
        self._body = None
        self.discriminator = None

        self.eihealth_project_id = eihealth_project_id
        self.database_id = database_id
        self.row_num = row_num
        if body is not None:
            self.body = body

    @property
    def eihealth_project_id(self):
        """Gets the eihealth_project_id of this UpdateDatabaseDataRequest.

        医疗智能体平台项目ID，您可以在EIHealth平台单击所需的项目名称，进入项目设置页面查看。

        :return: The eihealth_project_id of this UpdateDatabaseDataRequest.
        :rtype: str
        """
        return self._eihealth_project_id

    @eihealth_project_id.setter
    def eihealth_project_id(self, eihealth_project_id):
        """Sets the eihealth_project_id of this UpdateDatabaseDataRequest.

        医疗智能体平台项目ID，您可以在EIHealth平台单击所需的项目名称，进入项目设置页面查看。

        :param eihealth_project_id: The eihealth_project_id of this UpdateDatabaseDataRequest.
        :type eihealth_project_id: str
        """
        self._eihealth_project_id = eihealth_project_id

    @property
    def database_id(self):
        """Gets the database_id of this UpdateDatabaseDataRequest.

        数据库实例id

        :return: The database_id of this UpdateDatabaseDataRequest.
        :rtype: str
        """
        return self._database_id

    @database_id.setter
    def database_id(self, database_id):
        """Sets the database_id of this UpdateDatabaseDataRequest.

        数据库实例id

        :param database_id: The database_id of this UpdateDatabaseDataRequest.
        :type database_id: str
        """
        self._database_id = database_id

    @property
    def row_num(self):
        """Gets the row_num of this UpdateDatabaseDataRequest.

        数据行号，即_row_num值

        :return: The row_num of this UpdateDatabaseDataRequest.
        :rtype: int
        """
        return self._row_num

    @row_num.setter
    def row_num(self, row_num):
        """Sets the row_num of this UpdateDatabaseDataRequest.

        数据行号，即_row_num值

        :param row_num: The row_num of this UpdateDatabaseDataRequest.
        :type row_num: int
        """
        self._row_num = row_num

    @property
    def body(self):
        """Gets the body of this UpdateDatabaseDataRequest.

        :return: The body of this UpdateDatabaseDataRequest.
        :rtype: :class:`huaweicloudsdkeihealth.v1.RowDataReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateDatabaseDataRequest.

        :param body: The body of this UpdateDatabaseDataRequest.
        :type body: :class:`huaweicloudsdkeihealth.v1.RowDataReq`
        """
        self._body = body

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
        if not isinstance(other, UpdateDatabaseDataRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
