# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteDdmDatabaseResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'database_name': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'database_name': 'database_name'
    }

    def __init__(self, job_id=None, database_name=None):
        r"""DeleteDdmDatabaseResponse

        The model defined in huaweicloud sdk

        :param job_id: 工作流id。
        :type job_id: str
        :param database_name: 逻辑库名
        :type database_name: str
        """
        
        super(DeleteDdmDatabaseResponse, self).__init__()

        self._job_id = None
        self._database_name = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if database_name is not None:
            self.database_name = database_name

    @property
    def job_id(self):
        r"""Gets the job_id of this DeleteDdmDatabaseResponse.

        工作流id。

        :return: The job_id of this DeleteDdmDatabaseResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this DeleteDdmDatabaseResponse.

        工作流id。

        :param job_id: The job_id of this DeleteDdmDatabaseResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def database_name(self):
        r"""Gets the database_name of this DeleteDdmDatabaseResponse.

        逻辑库名

        :return: The database_name of this DeleteDdmDatabaseResponse.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this DeleteDdmDatabaseResponse.

        逻辑库名

        :param database_name: The database_name of this DeleteDdmDatabaseResponse.
        :type database_name: str
        """
        self._database_name = database_name

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
        if not isinstance(other, DeleteDdmDatabaseResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
