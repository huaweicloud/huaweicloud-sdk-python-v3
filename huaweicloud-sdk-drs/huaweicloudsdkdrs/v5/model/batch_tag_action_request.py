# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchTagActionRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_type': 'str',
        'job_id': 'str',
        'x_language': 'str',
        'body': 'BatchDealResourceTagReq'
    }

    attribute_map = {
        'resource_type': 'resource_type',
        'job_id': 'job_id',
        'x_language': 'X-Language',
        'body': 'body'
    }

    def __init__(self, resource_type=None, job_id=None, x_language=None, body=None):
        """BatchTagActionRequest

        The model defined in huaweicloud sdk

        :param resource_type: 资源类型。 - migration：实时迁移 - sync：实时同步 - cloudDataGuard：实时灾备 - subscription：数据订阅 - backupMigration：备份迁移 - replay：仿真回放
        :type resource_type: str
        :param job_id: 任务ID。
        :type job_id: str
        :param x_language: 请求语言类型。
        :type x_language: str
        :param body: Body of the BatchTagActionRequest
        :type body: :class:`huaweicloudsdkdrs.v5.BatchDealResourceTagReq`
        """
        
        

        self._resource_type = None
        self._job_id = None
        self._x_language = None
        self._body = None
        self.discriminator = None

        self.resource_type = resource_type
        self.job_id = job_id
        if x_language is not None:
            self.x_language = x_language
        if body is not None:
            self.body = body

    @property
    def resource_type(self):
        """Gets the resource_type of this BatchTagActionRequest.

        资源类型。 - migration：实时迁移 - sync：实时同步 - cloudDataGuard：实时灾备 - subscription：数据订阅 - backupMigration：备份迁移 - replay：仿真回放

        :return: The resource_type of this BatchTagActionRequest.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this BatchTagActionRequest.

        资源类型。 - migration：实时迁移 - sync：实时同步 - cloudDataGuard：实时灾备 - subscription：数据订阅 - backupMigration：备份迁移 - replay：仿真回放

        :param resource_type: The resource_type of this BatchTagActionRequest.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def job_id(self):
        """Gets the job_id of this BatchTagActionRequest.

        任务ID。

        :return: The job_id of this BatchTagActionRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this BatchTagActionRequest.

        任务ID。

        :param job_id: The job_id of this BatchTagActionRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def x_language(self):
        """Gets the x_language of this BatchTagActionRequest.

        请求语言类型。

        :return: The x_language of this BatchTagActionRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this BatchTagActionRequest.

        请求语言类型。

        :param x_language: The x_language of this BatchTagActionRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def body(self):
        """Gets the body of this BatchTagActionRequest.

        :return: The body of this BatchTagActionRequest.
        :rtype: :class:`huaweicloudsdkdrs.v5.BatchDealResourceTagReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this BatchTagActionRequest.

        :param body: The body of this BatchTagActionRequest.
        :type body: :class:`huaweicloudsdkdrs.v5.BatchDealResourceTagReq`
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
        if not isinstance(other, BatchTagActionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
